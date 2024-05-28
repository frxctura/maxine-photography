import os
import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_next_available_number(existing_numbers):
    num = 1
    while num in existing_numbers:
        num += 1
    return num

def rename_files(directory):
    pattern = re.compile(r'image(\d+)\.jpg')
    existing_numbers = set()
    other_files = []
    
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            existing_numbers.add(number)
        else:
            other_files.append(filename)

    existing_numbers = sorted(existing_numbers)

    for filename in other_files:
        old_path = os.path.join(directory, filename)
        new_number = get_next_available_number(existing_numbers)
        new_filename = f'image{new_number}.jpg'
        new_path = os.path.join(directory, new_filename)
        
        try:
            os.rename(old_path, new_path)
            existing_numbers.append(new_number)
            existing_numbers = sorted(existing_numbers)
            logging.info(f'Renamed {old_path} to {new_path}')
        except Exception as e:
            logging.error(f'Error renaming {old_path} to {new_path}: {e}')

def main():
    directory = './photos'
    if not os.path.exists(directory):
        logging.error(f'Directory {directory} does not exist.')
        return

    rename_files(directory)

if __name__ == '__main__':
    main()
