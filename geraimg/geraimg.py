import argparse
import base64
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def geraimg(text, size, background_color, foreground_color):
    buffered = BytesIO()

    img = Image.new('RGB', size=size, color=background_color)
    font = ImageFont.truetype('Helvetica', 30)

    draw = ImageDraw.Draw(img)

    for idx,t in enumerate(text):
        y = 30 * idx + 10
        draw.text(xy=(10,y),
                  text=t, 
                  fill=foreground_color,
                  font=font)

    # Improve output quality? https://stackoverflow.com/a/19303889
    img.save(fp=buffered,
             format="JPEG",
             subsampling=0,
             quality=100)

    return buffered

def write_file(data, timestamped):
    raise Exception("Not implemented. Use `-b64` to output as base64 and then `| base64 --decode > file.jpeg`")

if __name__ == "__main__":
    print(f"Install with `poetry install`.")


def cli():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--format", choices=['jpeg'], default="jpeg", help="Output format")
    parser.add_argument("-t", "--text", action="append", type=str, help="Text, repeat to include multiple lines.")

    parser.add_argument("-b64", "--base64", action="store_true", help="Return base64-encoded image.")
    parser.add_argument("-o", "--output", default="output", help="Output file.")

    parser.add_argument("-bg", "--background", default="#FFFFFF", help="Background color.")
    parser.add_argument("-fg", "--foreground", default="#000000", help="Foreground color.")

    args = parser.parse_args()

    background_color = hex_to_rgb(args.background)
    foreground_color = hex_to_rgb(args.foreground)
    output_filename = f"{args.output}.{args.format}"

    lines = len(args.text)

    img_buffered = geraimg(text=args.text,
                           size=(400,60 * lines),
                           background_color=background_color,
                           foreground_color=foreground_color)

    if args.base64:
        print(base64.b64encode(img_buffered.getvalue()).decode("utf-8"))
    
    with open(output_filename, 'wb') as f:
        f.write(img_buffered.getvalue())
