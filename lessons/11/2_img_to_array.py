from struct import unpack
import numpy as np
from PIL import Image

with open('img.bmp', 'rb') as f:
    byte_data = f.read()

img_data = byte_data[int('36', base=16):]
img_byte_size = len(img_data)
img_size = int((img_byte_size/3)**0.5)

img_array = np.array(unpack(f'<{img_byte_size}B', img_data), 
                     dtype=np.uint8).reshape((img_size, img_size, 3))
img_array = img_array[:,:,::-1]
print(img_array[:10,:10,:])
Image.fromarray(img_array,'RGB').show()
