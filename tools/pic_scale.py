import glob
import os, sys
from PIL import Image # `pip install Pillow`

# python pic_scale.py <scale> <input_file> <output_path>
# Input file should be a text file like:
#  *.jpg
#  some_pic.png

def pic_scale(src_image: Image, scale):
  size_img = src_image.size
  return src_image.resize((int(size_img[0] * scale), int(size_img[1] * scale)))

scale       = float(sys.argv[-3])
input_file  = sys.argv[-2]
output_path = sys.argv[-1]

files_path_raw = []
with open(input_file) as file:
  files_path_raw = file.readlines()
# print(files_path_raw)

files_path = []
for file_raw in files_path_raw:
  files_path += glob.glob(file_raw)
# print(files_path)

if not os.path.exists(output_path):
  os.makedirs(output_path)

for file in files_path:
  file_basename = os.path.basename(file)
  src_image = Image.open(file)
  output_image = pic_scale(src_image, scale)
  output_image.save(output_path + '/' + file_basename)