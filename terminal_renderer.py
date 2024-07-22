import argparse
from image_processing import image_to_ascii, print_colored_image
from video_processing import video_to_ascii, video_to_colored_ascii

def main():
    parser = argparse.ArgumentParser(description="Render images and videos in the terminal.")
    parser.add_argument('file', type=str, help='Image or video file path')
    parser.add_argument('--ascii', action='store_true', help='Render as ASCII art')
    parser.add_argument('--color', action='store_true', help='Render with colors')
    parser.add_argument('--output', type=str, help='File to save the output')
    args = parser.parse_args()

    if args.ascii:
        if args.file.endswith(('.png', '.jpg', '.jpeg')):
            ascii_image = image_to_ascii(args.file,args.output)
            print(ascii_image)
        elif args.file.endswith(('.mp4', '.avi')):
            video_to_ascii(args.file)
        else:
            print("ASCII mode supports only images or videos.")
    elif args.color:
        if args.file.endswith(('.png', '.jpg', '.jpeg')):
            print_colored_image(args.file,args.output)
        elif args.file.endswith(('.mp4', '.avi')):
            video_to_colored_ascii(args.file)
        else:
            print("Color mode supports only images or videos.")
    else:
        if args.file.endswith(('.mp4', '.avi')):
                video_to_colored_ascii(args.file)
        elif args.file.endswith(('.png', '.jpg', '.jpeg')):
            print_colored_image(args.file)
        else:
            print("Unsupported file type.")

if __name__ == "__main__":
    main()
