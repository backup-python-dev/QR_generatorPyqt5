from urllib.parse import urlparse
import qrcode

from PIL import Image

def Is_URL(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False



def Genrar_qrcode(url):
    qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="#2F4466")
    img.save("url.png")
    img = Image.open("url.png")
    new_img = img.resize((300,300))
    new_img.save('url.png','png')


