SECURE THE DATA TO PREVENT HACKERS:
 REQUIRED TOOL:
Backend: Flask (Python), OpenCV
Frontend: HTML, CSS
Libraries Used: Flask, NumPy, OpenCV

image-encryption-flask
 1) static
    i) uploads (Stores uploaded & encrypted images)
    ii)styles.css (CSS for styling)
 2) templates
    i)encrypt.html (Encryption Page)
    ii)decrypt.html (Decryption Page)
 3) app.py (Main Flask application)
 4) README.md (Project Documentation)
 5) requirements.txt (Dependencies List)
 6) .gitignore (Files to exclude from Git)

-> Install Dependencies
pip install -r requirements.txt

-> Run the Flask App
python app.py

Usage Guide

=> Encryption (Hiding Message in Image)


1️) Open http://127.0.0.1:5000/encrypt_page

2️) Upload an image

3️) Enter your secret message

4️) Set a passcode

5️) Click "Encrypt & Download" to save the encrypted image


=> Decryption (Extracting Message)


1️) Open http://127.0.0.1:5000/decrypt_page

2️) Upload the encrypted image

3️) Enter the correct passcode

4️) Click "Decrypt" to reveal the hidden message



