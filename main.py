import CreateImage
import sys

if len(sys.argv) > 2:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
else:
    arg1 = input("Type quote text: ")
    arg2 = input("Type author name: ")

if __name__ == '__main__':
    # construct base image
    baseImg = CreateImage.construct_image(1400, 600, 20, 20)

    # write quote and author text
    baseImg = CreateImage.draw_text(baseImg, (70, 55), (1330, 450), 'Ubuntu-BI.ttf', 300, '"' + arg1 + '"')
    baseImg = CreateImage.draw_text(baseImg, (900, 440), (1380, 500), 'Ubuntu-L.ttf', 50, "~" + arg2)

    baseImg.convert('RGB').save('output_text.png')
    exit()
