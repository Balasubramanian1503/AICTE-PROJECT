from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('encrypt.html')  # Default page is encryption

@app.route('/encrypt_page')
def encrypt_page():
    return render_template('encrypt.html')

@app.route('/decrypt_page')
def decrypt_page():
    return render_template('decrypt.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['image']
    message = request.form['message']
    password = request.form['password']
    
    if file:
        img_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(img_path)
        
        img = cv2.imread(img_path)
        d = {chr(i): i for i in range(256)}

        # Store message length in the first pixel
        msg_length = len(message)
        img[0, 0, 0] = msg_length

        n, m, z = 1, 0, 0  # Start from second pixel
        for char in message:
            img[n, m, z] = d[char]
            n += 1
            m += 1
            z = (z + 1) % 3
        
        enc_img_path = os.path.join(UPLOAD_FOLDER, "encrypted.png")
        cv2.imwrite(enc_img_path, img)
        
        return send_file(enc_img_path, as_attachment=True)
    
    return "Error in encryption"

@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.files['image']
    user_password = request.form['user_password']
    
    if file:
        img_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(img_path)
        
        img = cv2.imread(img_path)
        c = {i: chr(i) for i in range(256)}

        # Read message length from the first pixel
        msg_length = img[0, 0, 0]

        message = ""
        n, m, z = 1, 0, 0  # Start from second pixel
        for _ in range(msg_length):
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        
        return f"Decrypted Message: {message}"
    
    return "Error in decryption"

if __name__ == "__main__":
    app.run(debug=True)
