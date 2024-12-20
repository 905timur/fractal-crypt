# fractal-crypt

Mandelbrot Fractal Encryption (MFE)

Version 1.0

# Mandelbrot Fractal Encryption 🔐

An encryption method using the Mandelbrot set to create ciphertext by mapping characters to complex plane coordinates. Built with Python, featuring a GUI for encryption, decryption, and fractal visualization.

> ⚠️ **Note**: This is an experimental project for educational purposes. Not intended for production use or sensitive data encryption.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/905timur/fractal-crypt.git

# Install dependencies
pip install numpy matplotlib tkinter

# Run the application
python fractal-crypt.py
```

## 🛠️ Features

- Character-to-fractal point mapping encryption
- GUI interface for easy encryption/decryption
- Real-time Mandelbrot set visualization
- Position-dependent character encoding
- Complex number-based ciphertext generation

## 🔧 How It Works

1. **Encryption**:
   - Maps each character to a unique complex plane point
   - Applies Mandelbrot set iterations (z = z² + c)
   - Generates ciphertext from iteration count and final z-value

2. **Decryption**:
   - Reverse-maps ciphertext using stored parameters
   - Matches characters based on iteration behavior
   - Reconstructs original message

## 📊 Technical Details

```python
# Encryption Example
message = "Hello, World!"
key_point = (-0.5, 0)
ciphertext = encrypt_message(message, key_point, -2, 1, -1.5, 1.5, 500, 500, 100)
```

### Parameters
- Complex plane: x∈[-2,1], y∈[-1.5,1.5]
- Resolution: 500x500
- Max iterations: 100
- Default key: (-0.5, 0)

## 🖥️ GUI Interface

The application provides:
- Message input field
- Encryption/decryption buttons
- Ciphertext display
- Fractal visualization window

## 🔍 Dependencies

- Python 3.x
- NumPy
- Matplotlib
- Tkinter

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

[MIT License](LICENSE)

## 🔗 Contact

- Timur - [timur.gab@gmail.com]
- Project Link: [https://github.com/905timur/fractal-crypt]
