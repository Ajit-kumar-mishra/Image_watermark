from PIL import Image, ImageDraw, ImageFont

# Create an Image Object from an Image
im = Image.open('input_image.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "hello earth"

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# Calculate the new x, y coordinates for the text
x = 30  # Adjust this value to move the text horizontally
y = height - textheight - 40  # Adjust this value to move the text vertically

# Draw watermark at the specified position with black color
draw.text((x, y), text, font=font, fill=(0, 0, 0, 255))
im.show()

# Save watermarked image
im.save('input_image_with_custom_position.jpg')
