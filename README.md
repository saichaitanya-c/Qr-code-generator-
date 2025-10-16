

---

# 🌐 QR Code Generator Web App

A simple, elegant **QR Code Generator** web application built with **Flask**, **Python**, and **Bootstrap**, featuring a responsive UI and an option to download the generated QR codes. The app is fully deployable with **Gunicorn** for production environments.

---

## 🧩 Features

* Generate QR codes for any URL.
* Inline display of the QR code.
* Download QR code as a PNG image.
* Responsive design with **Bootstrap 5**.
* Session-based storage of the last generated QR code for download.
* Developer credit displayed on the page.

---

## ⚙️ Technologies Used

| Technology      | Purpose                               |
| --------------- | ------------------------------------- |
| **Python**      | Backend programming language          |
| **Flask**       | Web framework                         |
| **qrcode[pil]** | QR code generation                    |
| **Bootstrap 5** | Frontend styling & responsive design  |
| **Gunicorn**    | WSGI server for production deployment |
| **HTML/CSS**    | Frontend markup and styling           |

---

## 💡 Why `render_template_string` is used

In Flask, there are two main ways to render HTML:

1. **`render_template`** – renders HTML files stored in the `templates/` directory.
2. **`render_template_string`** – renders HTML directly from a Python string.

In this project, we use:

```python
render_template_string(HTML_PAGE, qr_code=qr_code)
```

**Reasons:**

* Allows embedding the full HTML directly inside `app.py` for a self-contained application.
* Facilitates passing Python variables (`qr_code`) to the HTML dynamically.
* Quick prototyping without creating separate template files.
* Keeps small projects simple and portable.

> **Note:** For larger projects, using `render_template` with external HTML files is recommended for better maintainability.

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/saichaitanya-c/Qr-code-generator.git
cd Qr-code-generator
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app locally**

```bash
python app.py
```

4. **Open in browser**

```
http://127.0.0.1:5000/
```

---

## 🖥 Usage

1. Enter the URL or text in the input box.
2. Click **Generate** to create the QR code.
3. View your QR code displayed on the page.
4. Click **⬇ Download QR Code** to save it as a PNG.

---

## 📁 Project Structure

```
FlaskQRCodeGenerator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile               # For Gunicorn deployment
└── README.md              # Project documentation
```

---

## 🏗 Deployment

This app can be deployed to any WSGI-compatible server. For example, using **Heroku**:

* **Procfile** specifies how to run the app:

```
web: gunicorn app:app
```

* **Gunicorn** serves the Flask app in production.

**Steps:**

```bash
git add .
git commit -m "Deploy QR Code Generator"
git push heroku main
```

---

## 🔑 Notes

* The QR code download works by storing the last generated URL in a **Flask session**.
* `render_template_string` is used to embed the HTML directly for simplicity.
* For production, you may separate HTML into templates for cleaner code.

---


**Sai Chaitanya**

🌐 LinkedIn: https://www.linkedin.com/in/sai-chaitanya-kancharana/

---

## 📜 License

MIT License – free to use, modify, and share.



