import os
import json
from PIL import Image

def generate_thumbnails_and_json(image_directory, thumbnail_directory, json_file_path):
    extensions = ['.jpg', '.jpeg', '.png', '.gif']
    images_data = []
    
    if not os.path.exists(thumbnail_directory):
        os.makedirs(thumbnail_directory)

    for root, _, files in os.walk(image_directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                full_image_path = os.path.join(root, file)
                thumbnail_image_path = os.path.join(thumbnail_directory, file)
                
                with Image.open(full_image_path) as img:
                    img.thumbnail((512, 512))  
                    img.save(thumbnail_image_path)
                
                full_image_url = '/photos/' + os.path.relpath(full_image_path, image_directory)
                thumbnail_image_url = '/thumbnails/' + os.path.relpath(thumbnail_image_path, thumbnail_directory)
                
                images_data.append({
                    'thumbnail': thumbnail_image_url,
                    'fullSize': full_image_url
                })

    images_data.sort(key=lambda x: x['fullSize']) 
    with open(json_file_path, 'w') as json_file:
        json.dump({'images': images_data}, json_file, indent=2)

image_directory = './photos'
thumbnail_directory = './thumbnails'
json_file_path = 'images.json'

generate_thumbnails_and_json(image_directory, thumbnail_directory, json_file_path)
