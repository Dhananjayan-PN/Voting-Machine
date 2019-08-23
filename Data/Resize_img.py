from PIL import Image
file = 'Pics/MAHIKA SURI.png'
im = Image.open(file)
imResize = im.resize((int(195),int(215)), Image.ANTIALIAS)
imResize.save(file, 'PNG', quality=100)

