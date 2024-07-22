from PIL import Image
from rich.console import Console

def resize_image(image, max_width=80):
    aspect_ratio = image.height / image.width
    new_width = min(max_width, image.width)
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def image_to_ascii(image_path, width=80, char_set=" .:-=+*#%@"):
    image = Image.open(image_path)
    image = resize_image(image, width)
    image = image.convert("L")

    pixels = image.getdata()
    ascii_str = ''.join([char_set[pixel * len(char_set) // 256] for pixel in pixels])
    ascii_str = '\n'.join([ascii_str[i:i + width] for i in range(0, len(ascii_str), width)])

    return ascii_str

def print_colored_image(image):
    if isinstance(image, str):
        image = Image.open(image)
    image = resize_image(image, 80)
    image = image.convert("RGB")
    console = Console()

    for y in range(image.height):
        line = []
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            line.append(f"[rgb({r},{g},{b})]█[/]")
        console.print("".join(line))
