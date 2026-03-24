from flask import Flask, request, render_template, send_file, redirect, url_for
import qrcode
import io

app = Flask(__name__)

qr_bytes = None
qr_generated_flag = False


def generate_qr_bytes(url: str):
    qr = qrcode.make(url)

    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)

    return img_io.getvalue()   

@app.route('/')
def home():
    return render_template('index.html', qr_generated=qr_generated_flag)


@app.route('/generate', methods=['POST'])
def generate_qr():
    global qr_bytes, qr_generated_flag

    url = request.form.get('url')

    if not url:
        return "URL is required", 400

    qr_bytes = generate_qr_bytes(url)
    qr_generated_flag = True

    return redirect(url_for('home'))


@app.route('/qr-image')
def qr_image():
    global qr_bytes

    if qr_bytes is None:
        return "No QR generated", 404

    return send_file(
        io.BytesIO(qr_bytes),
        mimetype='image/png'
    )


@app.route('/download')
def download_qr():
    global qr_bytes

    if qr_bytes is None:
        return "No QR generated", 404

    return send_file(
        io.BytesIO(qr_bytes),
        mimetype='image/png',
        as_attachment=True,
        download_name="qr_code.png"
    )


@app.route('/reset')
def reset():
    global qr_bytes, qr_generated_flag
    qr_bytes = None
    qr_generated_flag = False
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
