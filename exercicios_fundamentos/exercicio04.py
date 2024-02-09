import qrcode

#Documentação: https://github.com/lincolnloop/python-qrcode

imagem = qrcode.make("https://ge.globo.com/")
imagem.save("qrcode.png")

## com imagem

from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://ge.globo.com/")

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="logo.png"
)

imagem.save("qrcode_logo.png")

redes_sociais={
"Youtube":"https://www.youtube.com/",
"Instagram":"https://www.instagram.com/"
}

for redes_sociais , url  in redes_sociais.items():
    qr = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)

    imagem = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path="logo.png"
    )
    imagem.save("logo"+redes_sociais+".png")
