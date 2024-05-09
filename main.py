import uuid

from pathlib import Path
from datetime import datetime
from collections import defaultdict
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

def count_file_extensions_in_directory(path):
    counter = defaultdict(int)

    for file in path.rglob('*'):
        if file.is_file():
            counter[file.suffix] += 1

    return counter


def counters_have_identical_elements(counter1, counter2):
    all_keys = set(counter1.keys()) | set(counter2.keys())

    return all(counter1.get(key, 0) == counter2.get(key, 0) for key in all_keys)


def organize_photos_by_month(source_dir, target_dir):
   for file_path in source_dir.rglob('*'):
        if file_path.is_dir():
            continue

        creation_date = datetime.fromtimestamp(file_path.stat().st_birthtime)

        target_folder = target_dir / str(creation_date.year)
        target_folder.mkdir(parents=True, exist_ok=True)

        new_file_path = target_folder / file_path.name

        if new_file_path.exists():
            new_file_path = target_folder / f'{file_path.stem}_{uuid.uuid4()}{file_path.suffix}'

        file_path.rename(new_file_path)


def main():
    source_dir = Path(config['path']['source_path'])
    target_dir = Path(config['path']['target_path'])

    source_file_extensions_counter = count_file_extensions_in_directory(source_dir)

    organize_photos_by_month(source_dir, target_dir)

    target_file_extensions_counter = count_file_extensions_in_directory(target_dir)

    if counters_have_identical_elements(source_file_extensions_counter, target_file_extensions_counter):
        print('Photos organized successfully', sum(source_file_extensions_counter.values()), sum(target_file_extensions_counter.values()))
    else:
        print('Photos organized unsuccessfully', sum(source_file_extensions_counter.values()), sum(target_file_extensions_counter.values()))


if __name__ == '__main__':
    main()
