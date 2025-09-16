from flask import Flask, request, render_template_string, send_file, session, redirect, url_for
import qrcode
import io
import base64
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for session storage

# Professional UI with Bootstrap + Fixed Download

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Code Generator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea, #764ba2);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            position: relative;
        }
        .card {
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }
        .btn-custom {
            background-color: #667eea;
            color: white;
            font-weight: bold;
            transition: 0.3s;
        }
        .btn-custom:hover {
            background-color: #764ba2;
            color: #fff;
        }
        img {
            margin-top: 20px;
            border: 5px solid #fff;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        .developer-tag {
            position: fixed;
            bottom: 10px;
            right: 10px;
            font-size: 0.85rem;
            color: #fff;
            font-weight: bold;
            background: rgba(0,0,0,0.3);
            padding: 5px 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card p-4 text-center">
                    <h2 class="mb-4">✨ QR Code Generator ✨</h2>
                    <form method="post">
                        <div class="input-group mb-3">
                            <input type="text" name="url" class="form-control" placeholder="Enter your link" required>
                            <button class="btn btn-custom" type="submit">Generate</button>
                        </div>
                    </form>
                    {% if qr_code %}
                        <h5 class="mt-4">Here is your QR Code:</h5>
                        <img src="data:image/png;base64,{{ qr_code }}" alt="QR Code" class="img-fluid">
                        <div class="mt-3">
                            <a href="{{ url_for('download') }}" class="btn btn-success">⬇ Download QR Code</a>
                        </div>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
    <div class="developer-tag">Developed by Sai Chaitanya</div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    qr_code = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Generate QR Code
            img = qrcode.make(url)
            buffer = io.BytesIO()
            img.save(buffer, "PNG")
            buffer.seek(0)

            # Store original URL in session for download
            session["last_url"] = url

            # Encode image as base64 string for inline display
            qr_code = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render_template_string(HTML_PAGE, qr_code=qr_code)

@app.route("/download")
def download():
    url = session.get("last_url")
    if url:
        # Regenerate QR Code from stored URL
        img = qrcode.make(url)
        buffer = io.BytesIO()
        img.save(buffer, "PNG")
        buffer.seek(0)
        return send_file(buffer, mimetype="image/png", as_attachment=True, download_name="qrcode.png")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
