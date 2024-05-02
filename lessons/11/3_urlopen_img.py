from urllib.request import urlopen
from PIL import Image

with urlopen('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7nf28zz8umcnOlywWAPSUJ8yLpArlMJoxVeDWmhG3fQ&s') as f:
    Image.open(f).show()