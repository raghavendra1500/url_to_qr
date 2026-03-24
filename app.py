from flask import Flask, request, render_template, send_file, redirect, url_for
import qrcode
import io

app = Flask(__name__)

qr_img = None
qr_generated_flag = False

@app.route('/')
def home():
    return render_template('index.html', qr_generated=qr_generated_flag)

@app.route('/generate', methods=['POST'])
def generate_qr():
    global qr_img, qr_generated_flag

    url = request.form['url']
    qr = qrcode.make(url)

    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)

    qr_img = img_io
    qr_generated_flag = True

    return redirect(url_for('home'))  # 🔥 important

@app.route('/qr-image')
def qr_image():
    global qr_img
    if qr_img:
        qr_img.seek(0)
        return send_file(qr_img, mimetype='image/png')
    return "No QR generated"

@app.route('/download')
def download_qr():
    global qr_img
    if qr_img:
        qr_img.seek(0)
        return send_file(qr_img, mimetype='image/png', as_attachment=True, download_name="qr_code.png")
    return "No QR generated"

@app.route('/reset')
def reset():
    global qr_generated_flag
    qr_generated_flag = False
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
