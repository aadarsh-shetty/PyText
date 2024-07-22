import cv2
import numpy as np
from PIL import Image
from rich.console import Console
from rich.text import Text
from image_processing import print_colored_image

def resize_frame(frame, max_width=80):
    height, width = frame.shape[:2]
    aspect_ratio = height / width
    new_width = min(max_width, width)
    new_height = int(aspect_ratio * new_width)
    return cv2.resize(frame, (new_width, new_height))

def frame_to_pil_image(frame):
    return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

def video_to_ascii(video_path, width=80, char_set=" .:-=+*#%@"):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file.")
        return

    num_chars = len(char_set)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_frame = resize_frame(gray_frame, width)

        # Convert pixel values to integers in range [0, 255] and then map to characters
        pixel_values = resized_frame.astype(float)  # Convert to float to avoid overflow
        pixel_indices = np.clip((pixel_values * num_chars / 256).astype(int), 0, num_chars - 1)
        ascii_frame = ''.join([char_set[index] for index in pixel_indices.flatten()])
        ascii_frame = '\n'.join([ascii_frame[i:i + width] for i in range(0, len(ascii_frame), width)])

        print("\033c", end="")  # Clear screen
        print(ascii_frame)

    cap.release()

def video_to_colored_ascii(video_path, width=80):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resized_frame = resize_frame(frame_rgb, width)

        # Convert frame to PIL image
        pil_image = frame_to_pil_image(resized_frame)

        # Use print_colored_image to display the frame
        print("\033c", end="")  # Clear screen
        print_colored_image(pil_image)

    cap.release()
