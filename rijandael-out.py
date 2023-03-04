import tkinter as tk
import subprocess

def encrypt_file():
    input_file = input_file_entry.get()
    password = subprocess.check_output(['openssl', 'rand', '-base64', '16']).strip().decode('utf-8')
    subprocess.run(['ccrypt', '-e', '-K', password, input_file])
    output_message = f"File \"{input_file}\".cpt encrypted with password \"{password}\"."
    output_label.config(text=output_message)
    save_output(output_message)

def save_output(output_message):
    with open("output.txt", "a") as f:
        f.write(output_message + "\n")

root = tk.Tk()
root.title("File Encryption")

input_file_label = tk.Label(root, text="Enter input file name:")
input_file_entry = tk.Entry(root)
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_file)
output_label = tk.Label(root, text="")

input_file_label.pack()
input_file_entry.pack()
encrypt_button.pack()
output_label.pack()

root.mainloop()

