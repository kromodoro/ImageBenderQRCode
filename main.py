import time
from datetime import date
from PIL import ImageFont, ImageDraw, Image
import qrcode


v = 30
h = 1000
coord_data = (h+230,v)
data = date.today().strftime('%d/%m/%Y')

# QRCODE
qr  = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=5,
	border=2,
)


with open(r'textos.txt', 'r') as f:

	textos = f.read()
	
	imagem = Image.open(r'5w2h-off.jpg')
	imagem.save(f'5w2h.jpg')
	imagem = Image.open(r'5w2h.jpg')

	desenho = ImageDraw.Draw(imagem)
	caminho_fonte = r"font/impact.ttf"
	font = ImageFont.truetype(caminho_fonte, 24)
	rgb_preto = (255,255,255)
	
	nc = 30
	for texto in textos.split('\n'):
		coord_qrcode = (h+150,v+60)
		print(texto)
		if texto.find("http") != -1:
			nc = 230
			qr.add_data(texto)
			qr.make(fit=True)
			img = qr.make_image(fill_color="black", back_color="white")
			img.save(f'teste2.png')

			img1 = imagem
			img2 = Image.open(r'teste2.png')

			img1.paste(img2, coord_qrcode)
			img1.save(f'5w2h.jpg')
		else:
			coord_texto = (h+80,v+nc)
			desenho.text(coord_texto, texto, font=font, fill=rgb_preto)

	desenho.text(coord_data, data, font=font, fill=rgb_preto)
	imagem.save(f"/home/kromodoro/Imagens/Wallpapers/5w2h.jpg")








