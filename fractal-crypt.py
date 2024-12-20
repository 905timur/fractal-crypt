import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# Fractal and encryption functions
def generate_mandelbrot(width, height, max_iter, x_min, x_max, y_min, y_max):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    mandelbrot_set = np.zeros((height, width))
    
    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            z = 0
            for k in range(max_iter):
                z = z**2 + c
                if abs(z) > 2:
                    mandelbrot_set[i, j] = k
                    break
    return mandelbrot_set

def visualize_fractal(width, height, max_iter, x_min, x_max, y_min, y_max):
    mandelbrot_set = generate_mandelbrot(width, height, max_iter, x_min, x_max, y_min, y_max)
    plt.imshow(mandelbrot_set, cmap="hot", extent=(x_min, x_max, y_min, y_max))
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.show()

def encrypt_message(message, key_point, x_min, x_max, y_min, y_max, width, height, max_iter):
    key_x, key_y = key_point
    x_step = (x_max - x_min) / width
    y_step = (y_max - y_min) / height
    ciphertext = []

    for idx, char in enumerate(message):
        char_value = ord(char)
        # Create a unique key for each character based on its index in the message
        unique_x = key_x + (char_value * 0.1) + (idx * 0.001)
        unique_y = key_y + (char_value * 0.1) + (idx * 0.001)
        
        c = complex(unique_x, unique_y)

        z = 0
        iter_count = 0
        for k in range(max_iter):
            z = z**2 + c
            iter_count += 1
            if abs(z) > 2:
                break

        ciphertext.append((iter_count, z))

    return ciphertext

def decrypt_message(ciphertext, key_point, x_min, x_max, y_min, y_max, width, height, max_iter):
    key_x, key_y = key_point
    plaintext = ""

    for idx, encrypted_data in enumerate(ciphertext):
        target_iter_count, target_z = encrypted_data
        best_char = "?"
        min_combined_diff = float('inf')

        for char_value in range(256):
            unique_x = key_x + (char_value * 0.1) + (idx * 0.001)
            unique_y = key_y + (char_value * 0.1) + (idx * 0.001)

            c = complex(unique_x, unique_y)
            z = 0
            iter_count = 0
            for k in range(max_iter):
                z = z**2 + c
                iter_count += 1
                if abs(z) > 2:
                    break

            iter_diff = abs(iter_count - target_iter_count)
            z_diff = abs(z - target_z)
            combined_diff = iter_diff + (z_diff.real**2 + z_diff.imag**2)

            if combined_diff < min_combined_diff:
                min_combined_diff = combined_diff
                best_char = chr(char_value)

        plaintext += best_char

    return plaintext

# Tkinter GUI
class FractalEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fractal Encryption")

        # Encryption parameters
        self.x_min, self.x_max = -2, 1
        self.y_min, self.y_max = -1.5, 1.5
        self.width, self.height = 500, 500
        self.max_iter = 100
        self.key_point = (-0.5, 0)
        
        # Message input
        tk.Label(root, text="Message to Encrypt:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Encrypt Button
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_message)
        self.encrypt_button.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Ciphertext display
        tk.Label(root, text="Ciphertext:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.ciphertext_display = tk.Entry(root, width=50)
        self.ciphertext_display.grid(row=2, column=1, padx=10, pady=5)
        
        # Decrypt Button
        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_message)
        self.decrypt_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Decrypted message display
        tk.Label(root, text="Decrypted Message:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.decrypted_message_display = tk.Entry(root, width=50)
        self.decrypted_message_display.grid(row=4, column=1, padx=10, pady=5)
        
        # Visualize Fractal Button
        self.visualize_button = tk.Button(root, text="Visualize Fractal", command=self.visualize_fractal)
        self.visualize_button.grid(row=5, column=0, columnspan=2, pady=10)
    
    def encrypt_message(self):
        message = self.message_entry.get()
        if not message:
            messagebox.showerror("Error", "Please enter a message to encrypt.")
            return
        
        ciphertext = encrypt_message(message, self.key_point, self.x_min, self.x_max, self.y_min, self.y_max, self.width, self.height, self.max_iter)
        self.ciphertext_display.delete(0, tk.END)
        self.ciphertext_display.insert(0, ",".join(map(str, ciphertext)))
    
    def decrypt_message(self):
        ciphertext = self.ciphertext_display.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter ciphertext to decrypt.")
            return
        import ast
        try:
            ciphertext = ast.literal_eval(self.ciphertext_display.get())
        except (ValueError, SyntaxError):
            messagebox.showerror("Error", "Invalid ciphertext format.")
            return
        
        decrypted_message = decrypt_message(ciphertext, self.key_point, self.x_min, self.x_max, self.y_min, self.y_max, self.width, self.height, self.max_iter)
        self.decrypted_message_display.delete(0, tk.END)
        self.decrypted_message_display.insert(0, decrypted_message)
    
    def visualize_fractal(self):
        visualize_fractal(self.width, self.height, self.max_iter, self.x_min, self.x_max, self.y_min, self.y_max)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FractalEncryptionApp(root)
    root.mainloop()
