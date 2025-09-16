from flask import Flask, request, render_template_string
import qrcode
import io
import base64

app = Flask(__name__)

# HTML template (kept inside app.py for simplicity)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>QR Code Generator</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h2>QR Code Generator</h2>
    <form method="post">
        <input type="text" name="url" placeholder="Enter your link" style="width:300px; padding:5px;">
        <button type="submit">Generate QR Code</button>
    </form>
    {% if qr_code %}
        <h3>Here is your QR Code:</h3>
        <img src="data:image/png;base64,{{ qr_code }}" alt="QR Code">
    {% endif %}
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
            # Encode image as base64 string
            qr_code = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return render_template_string(HTML_PAGE, qr_code=qr_code)

if __name__ == "__main__":
    # Use host="0.0.0.0" for Render
    app.run(host="0.0.0.0", port=5000)
