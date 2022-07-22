# import qrcode as qr
# Img=qr.make("https://github.com/MuskanVishwakarmaa?tab=repositories")
# Img.save("github.png")

#************************************************************2ND METHOD*****************************************************
import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10, border=4,)
qr.add_data("https://www.bing.com/images/search?q=Funny+Jokes&form=RESTAB&first=1&tsc=ImageHoverTitle")     
qr.make(fit=True)
img=qr.make_image(fill_color="cyan",back_color="pink")
img.save("certificate.png")   