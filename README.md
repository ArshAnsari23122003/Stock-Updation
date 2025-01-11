QR Code Inventory Management System
This Python program is designed for inventory management using QR codes. It allows you to generate QR codes for products, scan QR codes to update stock levels, and save the updated stock information to a CSV file.

Requirements
To run this program, you will need to install the following Python libraries:

opencv-python (for accessing the camera and handling image processing)
pandas (for handling and manipulating the CSV file)
pyzbar (for decoding QR codes)
qrcode (for generating QR codes)

You can install these dependencies using pip:
pip install opencv-python pandas pyzbar qrcode


How it Works
Generate QR Codes:
You can generate QR codes for different products by specifying their names and stock quantities. The QR code will store the product name and stock, and each code will be saved as an image file.

Scan QR Codes:
Using a webcam or external camera, the program can scan QR codes in real-time.
When a QR code is scanned, the data (product name and stock) is extracted.

Update Stock in CSV:
After scanning a QR code, the stock information is updated in a CSV file (product_stock.csv). If the item already exists, its stock value will be updated (by adding the scanned stock). If the item does not exist, it will be added to the CSV.

Features
QR code generation for multiple products.
Real-time QR code scanning using the webcam.
CSV file to store product stock information.
Automatic stock update in the CSV file based on scanned QR codes.

Usage
1. Define Products and Stock
You can modify the product_list dictionary in the main() function to include any products and their initial stock quantities:
product_list = {
    "300 GSM Sheets": 500,
    "200 GSM Sheets": 300,
    "Wooden Stands": 150,
    "Metal Stands": 100,
    "Display Boards": 50
}

2. Generate QR Codes
The QR codes for the defined products will be automatically generated and saved as PNG files in the same directory with the filename format: <product_name>_qr.png.

3. Scan QR Code
Once the QR codes are generated, run the script. The program will access your camera to scan QR codes in real-time. When a QR code is detected, the product's stock will be updated accordingly.

To exit the scanning window, press the "q" key.

4. Update Stock in CSV
After scanning a QR code, the stock data will be updated in the product_stock.csv file. The CSV file will have two columns: Item and Stock.

File Structure
product_stock.csv: The file that stores product names and their stock levels.
<product_name>_qr.png: QR code images for each product.

Example
When you run the program, the following steps happen:
QR codes are generated for products.
The program accesses the camera to scan a QR code.
Upon scanning, the stock of the product is updated in the product_stock.csv file.

License
This project is licensed under the MIT License - see the LICENSE file for details.



