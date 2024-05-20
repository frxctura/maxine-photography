import os
import re

def rename_images(directory):
    extensions = ['.jpg', '.jpeg', '.png', '.gif']
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    image_files = [f for f in files if any(f.lower().endswith(ext) for ext in extensions)]
    
    pattern = re.compile(r'^image\d+\.\w+$', re.IGNORECASE)

    existing_numbers = []
    for f in image_files:
        if pattern.match(f):
            existing_numbers.append(int(re.search(r'\d+', f).group()))

    max_number = max(existing_numbers) if existing_numbers else 0

    for i, filename in enumerate(image_files, start=max_number + 1):
        if pattern.match(filename):
            continue 
        ext = os.path.splitext(filename)[1]
        new_filename = f'image{i}{ext}'
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_filename)
        os.rename(src, dst)
        print(f'Renamed {src} to {dst}')

image_directory = './photos'  
rename_images(image_directory)
