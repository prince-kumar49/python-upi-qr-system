import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    upi_id = upi_entry.get().strip()
    name = name_entry.get().strip()
    amount = amount_entry.get().strip()
    note = note_entry.get().strip()

    if not upi_id or not name:
        messagebox.showerror("Error", "UPI ID and Name are required!")
        return

    upi_url = f"upi://pay?pa={upi_id}&pn={name}&cu=INR"
    if amount:
        upi_url += f"&am={amount}"
    if note:
        upi_url += f"&tn={note}"

    qr = qrcode.make(upi_url)
    qr.save("upi_qr.png")

    img = Image.open("upi_qr.png").resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # keep reference so it doesn’t get garbage collected

#  Create the Tkinter root window first
root = tk.Tk()
root.title("UPI QR Code Generator")

# Input fields
tk.Label(root, text="UPI ID:").grid(row=0, column=0, sticky="e")
upi_entry = tk.Entry(root, width=30)
upi_entry.grid(row=0, column=1)

tk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=1, column=1)

tk.Label(root, text="Amount (optional):").grid(row=2, column=0, sticky="e")
amount_entry = tk.Entry(root, width=30)
amount_entry.grid(row=2, column=1)

tk.Label(root, text="Note (optional):").grid(row=3, column=0, sticky="e")
note_entry = tk.Entry(root, width=30)
note_entry.grid(row=3, column=1)

tk.Button(root, text="Generate QR", command=generate_qr).grid(row=4, columnspan=2, pady=10)

# QR Code display area
qr_label = tk.Label(root)
qr_label.grid(row=5, columnspan=2)

#  Start Tkinter main loop
root.mainloop()
