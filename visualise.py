# Description: Visualise the answer sheet template on an image

import cv2
import json

COLOR = (0, 0, 255)

def is_within_image(image, x, y):
    return 0 <= x < image.shape[1] and 0 <= y < image.shape[0]

def draw_bubbles(image_path, template_path):
    # Load the template
    with open(template_path, 'r') as file:
        template = json.load(file)
    
    # Load the image
    image = cv2.imread(image_path)
    
    # Iterate through each section
    for section in template["sections"]:
        for item in section["items"]:
            for bubble in item["bubbles"]:
                shape = bubble["shape"]
                
                # Draw Circle
                if shape == "circle":
                    center = tuple(bubble["center"])
                    radius = bubble["radius"]
                    if is_within_image(image, center[0], center[1]):
                        cv2.circle(image, center, radius, COLOR, -1)
                    else:
                        print(f"Warning: Circle with center {center} is out of image boundaries.")
                
                # Draw Rectangle
                elif shape == "rectangle":
                    top_left = tuple(bubble["top_left"])
                    bottom_right = tuple(bubble["bottom_right"])
                    if is_within_image(image, top_left[0], top_left[1]) and is_within_image(image, bottom_right[0], bottom_right[1]):
                        cv2.rectangle(image, top_left, bottom_right, COLOR, -1)
                    else:
                        print(f"Warning: Rectangle with top left {top_left} and bottom right {bottom_right} is out of image boundaries.")
                
                # Draw Ellipse
                elif shape == "ellipse":
                    center = tuple(bubble["center"])
                    axes = tuple(bubble["axes"])
                    angle = bubble["angle"]
                    if is_within_image(image, center[0], center[1]):
                        cv2.ellipse(image, center, axes, angle, 0, 360, COLOR, -1)
                    else:
                        print(f"Warning: Ellipse with center {center} is out of image boundaries.")
                else:
                    print(f"Warning: Unknown shape '{shape}'.")

    # Show the result
    cv2.imshow('Answer Sheet Visualization', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
draw_bubbles("example.png", "template.json")