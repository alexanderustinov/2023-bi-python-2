import numpy as np
import PIL.Image

size = 300
dtype = np.uint8
# при X, Y от 0 до 255 Z~X**2+Y**2 довольно быстро переполняется
X = np.linspace(0, 16, size, dtype=dtype)
Y = X.copy()
Z = np.zeros([3], dtype=dtype)
X, Y, Z = np.meshgrid(X, Y, Z)
# print(X, Y)

img_data = (X**2+Y**2)
img_data[:,:,1] = np.zeros_like(img_data[:,:,1])
img_data[:,:,2] = np.zeros_like(img_data[:,:,2])
# slice_ = np.slice(1,2)
# X[slice_]
print(img_data[:,:,0], X[:,:,0])

# print(img_data)

img = PIL.Image.fromarray(img_data)
# img.show()
img.save('img.bmp')
img.save('img.png') # flac / loseless
img.save('img.jpg') # mp3 / lossy
