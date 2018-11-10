from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (500, 500), color=(190, 190, 190))

fnt = ImageFont.truetype('Ubuntu-B.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10, 10), "Ubuntu", font=fnt, fill=(255, 255, 0))

img.save('pil_text_font.png')