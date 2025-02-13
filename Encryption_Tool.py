from Crypto.Random import get_random_bytes

KEY = get_random_bytes(32)


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import tkinter as tk
from tkinter import filedialog, messagebox

key = get_random_bytes(32)

def pad(data):
    """"pad the data to be a multiple of 16 bytes (AES block size)."""
    return data + b"\0" * (16 - len(data) % 16)


def encrypt_file(filename):
    """"Encrypts a file using AES-256 CBC mode."""
    with open(filename, "rb") as file:
        plaintext = file.read()


    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext))

    with open(filename + ".enc", "wb") as file:
        file.write(iv + ciphertext)

    messagebox.showinfo("success", f"File Encrypted: {filename}.enc")


def decrypt_file(filename):
    """Decrypts an AES-256 encrypted file."""
    with open(filename, "rb") as file:
        iv = file.read(16)
        ciphertext = file.read()

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext).rstrip(b"\0")

    original_filename = filename.replace(".enc", "")
    with open(original_filename, "wb") as file:
        file.write(plaintext)


    messagebox.showinfo("success", f"File Decrypted: {original_filename}")


def select_file(action):
    """"open file dialog and perform encryption or decryption."""
    filename = filedialog.askopenfilename()
    if not filename:
        return
    if action == "encrypt":
        encrypt_file(filename)
    elif action == "decrypt":
        decrypt_file(filename)


root = tk.Tk()
root.title("AES-256 file Encryption tool")
root.geometry("300x200")


tk.Button(root, text="Encrypt file", command=lambda: select_file("encrypt")).pack(pady=10)
tk.Button(root, text="Decrypt file", command=lambda: select_file("decrypt")).pack(pady=10)

root.mainloop()