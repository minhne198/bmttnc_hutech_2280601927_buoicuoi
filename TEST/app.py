from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/open_gui/<cipher>", methods=["POST"])
def open_gui(cipher):
    try:
        # Định nghĩa các file GUI
        gui_files = {
            "caesar": "caesar_cipher.py",
            "vigenere": "vigenere_cipher.py",
            "railfence": "railfence_cipher.py",
            "playfair": "playfair_cipher.py"
        }
        if cipher in gui_files:
            # Tạo đường dẫn tuyệt đối đến file GUI trong thư mục TEST
            base_dir = os.path.dirname(os.path.abspath(__file__))  # Thư mục chứa app.py
            gui_path = os.path.join(base_dir, gui_files[cipher])
            if not os.path.exists(gui_path):
                return {"error": f"File {gui_files[cipher]} not found"}, 404
            # Chạy file Python GUI
            subprocess.Popen(["python", gui_path])
            return {"status": "success"}, 200
        else:
            return {"error": "Invalid cipher"}, 400
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)