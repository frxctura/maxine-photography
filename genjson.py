import os
import json

def generate_images_json(directory):
    extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                image_files.append('/photos/' + os.path.relpath(os.path.join(root, file), directory))
    
    image_files.sort()
    
    with open('images.json', 'w') as json_file:
        json.dump({'images': image_files}, json_file)

image_directory = './photos' 
generate_images_json(image_directory)
