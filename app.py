from flask import Flask, request, render_template, send_file, redirect, url_for, session
import qrcode
import io
import base64

app = Flask(__name__)
app.secret_key = "qrgen-secret"


def create_qr(url: str):
    qr = qrcode.make(url)

    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer.read()


def to_base64(image_bytes):
    return base64.b64encode(image_bytes).decode("utf-8")


@app.route('/')
def home():
    qr_image = session.get("qr_image")
    return render_template("index.html", qr_image=qr_image)


@app.route('/generate', methods=['POST'])
def generate():
    url = request.form.get("url")

    if not url:
        return redirect(url_for("home"))

    image_bytes = create_qr(url)

    session["qr_image"] = to_base64(image_bytes)

    return redirect(url_for("home"))


@app.route('/download')
def download():
    qr_image = session.get("qr_image")

    if not qr_image:
        return "No QR generated", 404

    image_bytes = base64.b64decode(qr_image)

    return send_file(
        io.BytesIO(image_bytes),
        mimetype='image/png',
        as_attachment=True,
        download_name="qr_code.png"
    )


@app.route('/reset')
def reset():
    session.pop("qr_image", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
