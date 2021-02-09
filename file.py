

from PIL import Image
import requests
from io import BytesIO
import cloudinary.uploader

cloudinary.config(
    cloud_name = "dgjvthpnh",
    api_key = "875298853688417",
    api_secret = "0nkrKbN5bPew17Ntax3BzzMzCXo"
)


url='https://res.cloudinary.com/dgjvthpnh/image/upload/v1611870513/rriqhcazxzexr5ake5sc.png'


import io
response = requests.get(url)
image_bytes = io.BytesIO(response.content)
img = Image.open(image_bytes)
# Create a buffer to hold the bytes
buf = BytesIO()

# Save the image as jpeg to the buffer
img.save(buf, 'png'or'jpeg'or'jpg')

# Rewind the buffer's file pointer
buf.seek(0)

# Read the bytes from the buffer
image_bytes = buf.read()

# Close the buffer
buf.close()
print(img,image_bytes)
cloudinary.uploader.upload(image_bytes)