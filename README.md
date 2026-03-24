

# 📌 QRGen Pro — Flask QR Code Generator

QRGen Pro is a modern, lightweight web application built with **Flask** that allows users to generate, preview, download, and reset QR codes instantly from any URL.

It is designed with a **clean UI + production-safe backend architecture** (no global variables, session-based storage, and reliable file download handling).

---

## 🚀 Features

* ⚡ Instant QR code generation from URLs
* 🖼️ Live QR preview in browser
* 📥 Download QR code as PNG file
* 🔄 Reset and generate new QR codes easily
* 🔐 Session-based secure storage (no global variables)
* 🌐 Fully responsive and modern UI
* 🧠 Production-safe Flask architecture

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **QR Generator:** `qrcode` (Pillow-based)
* **Frontend:** HTML5, CSS3 (Jinja2 templates)
* **Data Handling:** Flask Sessions
* **Image Processing:** `io.BytesIO`, `base64`

---

## 📁 Project Structure

```plaintext
QRGen-Pro/
│── app.py
│── templates/
│     └── index.html
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/qrgen-pro.git
cd qrgen-pro
```

---

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install flask qrcode[pil]
```

---

### 4. Run the application

```bash
python app.py
```

---

### 5. Open in browser

```plaintext
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. User enters a URL in the input field
2. Flask generates a QR code using `qrcode` library
3. Image is converted into binary and stored in session (base64 format)
4. QR is displayed instantly in the frontend
5. User can download QR using `/download` route
6. Reset clears session and allows new generation

---

## 📌 API Routes

| Route       | Method | Description               |
| ----------- | ------ | ------------------------- |
| `/`         | GET    | Home page UI              |
| `/generate` | POST   | Generates QR code         |
| `/download` | GET    | Downloads QR image (PNG)  |
| `/reset`    | GET    | Clears current QR session |

---

## 🎨 UI Highlights

* Minimal and modern card-based design
* Responsive layout (mobile-friendly)
* Clean buttons for download and reset
* Smooth user experience with instant feedback

---

## ⚠️ Important Notes

* QR code is stored per session (not shared between users)
* No database is used (lightweight architecture)
* Restarting server clears session data
* Designed for simplicity + deployment readiness

---

## 🚀 Future Improvements

* 🎨 Custom QR styles (colors, gradients, logos)
* 📊 QR history dashboard
* 🔗 API endpoint for external apps
* ☁️ Deployment on Render / Railway / AWS
* 📱 Mobile PWA version
* 🔍 Support for WiFi, Text, Email QR types

---

## 📦 requirements.txt

```txt
flask
qrcode[pil]
```

---

## 👨‍💻 Author

Built with ❤️ using Flask
Simple. Fast. Reliable QR Generator.

---

## 📄 License

This project is open-source and free to use.

---

