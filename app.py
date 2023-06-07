import qrcode

def create_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="black")
    img.save(filename)

# Örnek kullanım
website_url = "https://github.com/burakkozturk"
filename = "qr_code.png"
create_qr_code(website_url, filename)
print(f"{filename} adlı QR kod oluşturuldu.")
