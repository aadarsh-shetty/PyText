from PIL import Image
from rich.console import Console
from file_utility import write_to_file,append_to_file

def resize_image(image, max_width=200):
    aspect_ratio = image.height / image.width
    new_width = min(max_width, image.width)
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def image_to_ascii(image_path, output_path,width=200, char_set=" .:-=+*#%@"):
    image = Image.open(image_path)
    image = resize_image(image, width)
    image = image.convert("L")

    pixels = image.getdata()
    ascii_str = ''.join([char_set[pixel * len(char_set) // 256] for pixel in pixels])
    ascii_str = '\n'.join([ascii_str[i:i + width] for i in range(0, len(ascii_str), width)])
    if output_path:
        write_to_file(output_path,ascii_str);
    return ascii_str

def print_colored_image(image,output_path):
    if isinstance(image, str):
        image = Image.open(image)
    image = resize_image(image, 200)
    image = image.convert("RGB")
    console = Console()
    if output_path:
        write_to_file(output_path, "");


    for y in range(image.height):
        line = []
        if output_path:
            append_to_file(output_path, "\n")
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            line.append(f"[rgb({r},{g},{b})]█[/]")
            if output_path:
                append_to_file(output_path, f"\033[38;2;{r};{g};{b}m█\033[0m")
        console.print("".join(line))
