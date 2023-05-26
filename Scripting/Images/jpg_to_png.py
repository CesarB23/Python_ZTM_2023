from PIL import Image
import sys,os

if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])

for file in os.listdir(sys.argv[1]):
    img = Image.open(f"{sys.argv[1]}{file}")
    clean_file, format = os.path.splitext(file)
    try:
        img.save(f"{sys.argv[2]}{clean_file}.png","png")
        print(f"{clean_file} converted from {format} to .png")
    except OSError:
        print("Cannot convert file {file} to png")
