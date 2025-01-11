import cv2
import pandas as pd
from pyzbar.pyzbar import decode
import qrcode

# Step 2: Generate QR Codes for Multiple Products
def generate_qr_codes(product_list):
    for product, stock in product_list.items():
       
        data = f"{product},{stock}"  # Format: "ProductName,Stock"
        
        # Create the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        # Save the QR code image
        img = qr.make_image(fill='black', back_color='white')
        filename = f"{product.replace(' ', '_')}_qr.png"
        img.save(filename)
        print(f"QR Code Generated: {filename}")

# Step 3: Scan a QR Code Using the Camera
def scan_qr_code():
    cap = cv2.VideoCapture(0)  # 0 for default camera
    print("Scanning for QR code...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Decode QR codes in the frame
        decoded_objects = decode(frame)
        
        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")  # Get the QR code data
            print(f"QR Code Data: {qr_data}")
            cap.release()
            cv2.destroyAllWindows()
            return qr_data
        
        # Show the video stream with QR code scanning
        cv2.imshow("QR Code Scanner", frame)

        # Exit the loop if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return None

# Step 3: Update the Stock in the CSV File
def update_stock_in_csv(stock_file, qr_data):
    if qr_data is None:
        print("No QR code data found. Exiting.")
        return
    
    item, stock = qr_data.split(',')
    stock = int(stock)  # Ensure stock is an integer

    try:
        # Load the CSV file
        df = pd.read_csv(stock_file)
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame
        df = pd.DataFrame(columns=["Item", "Stock"])

    if item in df["Item"].values:
        # If the item exists, double the stock value from the QR code
        current_stock = df.loc[df["Item"] == item, "Stock"].values[0]
        new_stock = current_stock + (stock)
        df.loc[df["Item"] == item, "Stock"] = new_stock
        print(f"Stock for {item} updated to {new_stock}.")
    else:
        # Add the item if it doesn't exist
        new_row = pd.DataFrame({"Item": [item], "Stock": [stock]})
        df = pd.concat([df, new_row], ignore_index=True)
        print(f"{item} added with stock {stock}.")

    # Save the updated data back to the CSV file
    df.to_csv(stock_file, index=False)
    print("Stock data updated in the CSV file.")

# Step 4: Main Program for Multiple Products
def main():
    stock_file = "product_stock.csv"  
    
    # Step 1: Define the products and their initial stock
    product_list = {
        "300 GSM Sheets": 500,
        "200 GSM Sheets": 300,
        "Wooden Stands": 150,
        "Metal Stands": 100,
        "Display Boards": 50
    }
    
    # Step 2: Generate QR codes for the products
    generate_qr_codes(product_list)
    
    # Step 3: Scan a QR code from the camera
    qr_data = scan_qr_code()
    
    # Step 4: Update the stock in the CSV file
    update_stock_in_csv(stock_file, qr_data)

if __name__ == "__main__":
    main()
