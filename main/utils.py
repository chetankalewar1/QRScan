# Import QRCode from pyqrcode
import pyqrcode
import pandas as pd


# QR is generated for each code.
def get_qr_for_each_record(filename):
    df = pd.read_excel(filename)
    data = df.to_dict("records")
    # print(data)
    for k in data:
        # String which represents the QR code
        s = f"http://127.0.0.1/{k['Code128']}"

        # Generate QR code
        url = pyqrcode.create(s)

        # Create and save the png file naming "myqr.png"
        url.png(f"../qrs_images/{k['Code128']}.png", scale=6)


# get_qr_for_each_record(filename="/home/chetan/Desktop/test_for_2nd_source/Test.xlsm")
