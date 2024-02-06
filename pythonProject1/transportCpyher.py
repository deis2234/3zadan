import tkinter as tk
from tkinter import messagebox

def encrypt(text, key):
    encrypted_text = [''] * key
    for col in range(key):
        position = col
        while position < len(text):
            encrypted_text[col] += text[position]
            position += key
    return ''.join(encrypted_text)

def visualize_encrypt(text, key):
    encrypted_text = [''] * key
    table = [['' for _ in range(len(text))] for _ in range(key)]
    for col in range(key):
        position = col
        while position < len(text):
            encrypted_text[col] += text[position]
            table[col][position] = text[position]
            position += key
    return ''.join(encrypted_text), table

def on_encrypt():
    text = entry_text.get()
    key = int(entry_key.get())
    if key <= 0:
        messagebox.showerror("Error", "Ключ должен быть целым положительным числом.")
        return
    encrypted_text, table = visualize_encrypt(text, key)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Зашифрованный текст: " + encrypted_text)


    table_text.delete(1.0, tk.END)
    for row in table:
        table_text.insert(tk.END, ' '.join(row) + '\n')


root = tk.Tk()
root.title("Шифр Перестановки")


label_text = tk.Label(root, text="Введите текст:")
label_text.grid(row=0, column=0, padx=5, pady=5)

entry_text = tk.Entry(root)
entry_text.grid(row=0, column=1, padx=5, pady=5)

label_key = tk.Label(root, text="Введите ключ:")
label_key.grid(row=1, column=0, padx=5, pady=5)

entry_key = tk.Entry(root)
entry_key.grid(row=1, column=1, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Зашифровать", command=on_encrypt)
encrypt_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

result_text = tk.Text(root, height=5, width=40)
result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# виджет для визуализации
table_text = tk.Text(root, height=24, width=40)
table_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()
