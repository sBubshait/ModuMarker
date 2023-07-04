import cv2
import json
import numpy as np

def is_inside_circle(x, y, center, radius):
    # Check if point (x, y) is inside the circle with given center and radius
    return (x - center[0]) ** 2 + (y - center[1]) ** 2 < radius ** 2


def is_inside_rectangle(x, y, top_left, bottom_right):
    # Check if point (x, y) is inside the rectangle with given top-left and bottom-right corners
    return top_left[0] <= x <= bottom_right[0] and top_left[1] <= y <= bottom_right[1]


def is_inside_ellipse(x, y, center, axes, angle):
    # Check if point (x, y) is inside the ellipse with given center, axes, and angle
    angle_rad = np.deg2rad(angle)
    xr = (x - center[0]) * np.cos(angle_rad) + (y - center[1]) * np.sin(angle_rad)
    yr = -(x - center[0]) * np.sin(angle_rad) + (y - center[1]) * np.cos(angle_rad)
    return (xr / axes[0]) ** 2 + (yr / axes[1]) ** 2 < 1

def calculate_white_pixels_ratio(thresh, bubble, shape):
    # Calculate the ratio of white pixels within a given shape
    total_pixels = 0
    white_pixels = 0

    # Circle shape
    if shape == 'circle':
        center = bubble['center']
        radius = bubble['radius']
        for x in range(center[0] - radius, center[0] + radius):
            for y in range(center[1] - radius, center[1] + radius):
                if is_inside_circle(x, y, center, radius):
                    total_pixels += 1
                    if thresh[y, x] == 255:
                        white_pixels += 1

    # Rectangle shape
    elif shape == 'rectangle':
        top_left = bubble['top_left']
        bottom_right = bubble['bottom_right']
        for x in range(top_left[0], bottom_right[0]):
            for y in range(top_left[1], bottom_right[1]):
                if is_inside_rectangle(x, y, top_left, bottom_right):
                    total_pixels += 1
                    if thresh[y, x] == 255:
                        white_pixels += 1

    # Ellipse shape
    elif shape == 'ellipse':
        center = bubble['center']
        axes = bubble['axes']
        angle = bubble['angle']
        for x in range(center[0] - axes[0], center[0] + axes[0]):
            for y in range(center[1] - axes[1], center[1] + axes[1]):
                if is_inside_ellipse(x, y, center, axes, angle):
                    total_pixels += 1
                    if thresh[y, x] == 255:
                        white_pixels += 1

    return (white_pixels / total_pixels) * 100 if total_pixels > 0 else 0


def process_answer_sheet(image_path, template_path):
    """
    Process an answer sheet image to determine the selected options for each section item.
    
    :param image_path: The path to the image file.
    :param template_path: The path to the template JSON file.
    :return: A dictionary containing the selected options for each section.
    """
    try:
        # Load the template
        with open(template_path, 'r') as file:
            template = json.load(file)

        # Read the image in grayscale
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print("Error: Unable to read image")
            return

        # Convert to binary. NB: 128 is considered the threshold, may want to change this.
        _, thresh = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)


        responses = {}

        # Loop through each section and item
        for section in template["sections"]:
            selected_options_in_section = []  
            for item in section["items"]:
                selected_options_in_item = []  
                for option, bubble in zip(item["options"], item["bubbles"]):
                    shape = bubble["shape"]
                    ratio = calculate_white_pixels_ratio(thresh, bubble, shape)
                    if ratio >= template["threshold"]:
                        selected_options_in_item.append(option)

                selected_options_in_section.append(selected_options_in_item)

            responses[section["name"]] = selected_options_in_section

        return responses

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    responses = process_answer_sheet("example.png", "example.json")
    print(responses)