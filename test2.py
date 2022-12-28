from PIL import Image
from PIL import ImageDraw


from PIL import Image

img = Image.open("E:\\Entreprenuership\\PycharmProjects\\Fx_barcode_generator_v1.1\\Generated Barcodes\\Kids\\891722100001.png")

right = 10
left = 10
top = 10
bottom = 10

width, height = img.size

new_width = width + right + left
new_height = height + top + bottom

result = Image.new(img.mode, (new_width, new_height), (255, 255, 255))

result.paste(img, (left, top))

result.save('E:\\Entreprenuership\\PycharmProjects\\Fx_barcode_generator_v1.1\\Generated Barcodes\\Kids\\891722100001.png')
img = Image.open("E:\\Entreprenuership\\PycharmProjects\\Fx_barcode_generator_v1.1\\Generated Barcodes\\Kids\\891722100001.png")
I1 = ImageDraw.Draw(img)
I1.text((150, 35), "PSPN-891-722-100-002-1", fill=(0, 0, 0))

img.save("E:\\Entreprenuership\\PycharmProjects\\Fx_barcode_generator_v1.1\\Generated Barcodes\\Kids\\891722100001.png")
print("Barcode padded with the required info.")