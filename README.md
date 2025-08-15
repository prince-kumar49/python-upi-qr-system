# 💸 UPI Payment QR Generator

A simple desktop app made with Python, Tkinter, and qrcode that generates UPI payment QR codes.
Just enter your UPI ID, Name, optional Amount, and Note → and instantly get a QR code that can be scanned with Google Pay, PhonePe, Paytm, BHIM, etc.

### 🔧 Features
- Accepts dynamic input: Name, UPI ID, Amount, Note
- Generates QR code for UPI payment
- Saves and displays QR using `qrcode` and `Pillow`
- Supports all major UPI apps

###🖥️ How It Works
Open the app.
Enter:
1.UPI ID (required)
2.Name (required)
3.Amount (optional)
4.Note (optional)
Click Generate QR.
A QR code is displayed that anyone can scan to pay.

### 📦 Built With
- Python(main language)
- tkinter
- qrcode
- PIL (Pillow)

### 🚀 How to Run
1. Install dependencies:
```bash
pip install qrcode pillow

