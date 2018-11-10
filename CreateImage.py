from PIL import Image, ImageDraw, ImageFont
import random

# define colours that will be used in this image
maincolor = random.randint(0, 12) * 30
textcolor = maincolor


def construct_image(w=300, h=300, borderW=10, borderH=10):
    img = Image.new('HSV', (w, h), color=(maincolor, 150, 90))

    # draw rect over this new image
    rect = ImageDraw.Draw(img, 'HSV')
    rect.rectangle([(borderW, borderH), (w-borderW, h-borderH)], (maincolor, 255, 20))

    return img


def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word,
            # add the line to the lines array
            lines.append(line)
    return lines


def draw_text(imgbuffer, topLeft=(10, 10), bottomRight=(20, 20), fontPath='Ubuntu-L.ttf', fontsize=20, text="test"):
    # open the background file
    img = imgbuffer

    # size() returns a tuple of (width, height)
    textbox_width = (bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1])

    # create the ImageFont instance
    font_file_path = fontPath
    font = ImageFont.truetype(font_file_path, size=fontsize, encoding="unic")

    rect = ImageDraw.Draw(img, 'HSV')

    line_height = font.getsize('hg')[1]
    # get shorter lines
    lines = text_wrap(text, font, textbox_width[0])

    while len(lines) > ((bottomRight[1] - topLeft[1]) / line_height):
        fontsize = fontsize-5
        print("new font size: " + str(fontsize))

        # Reconstruct font
        font = ImageFont.truetype(font_file_path, size=fontsize, encoding="unic")
        line_height = font.getsize('hg')[1]
        lines = text_wrap(text, font, textbox_width[0])
        print("new line height : " + str(line_height))

    x = topLeft[0]
    y = topLeft[1]
    for line in lines:
        # draw the line on the image
        rect.text((x, y), line, fill=(textcolor, 150, 150), font=font)

        # update the y position so that we can use it for next line
        y = y + line_height

    # return image
    return img

