import uuid

from pathlib import Path
from datetime import datetime
from collections import defaultdict
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

def count_extensions(path):
    counter = defaultdict(int)

    for file in path.rglob('*'):
        if file.is_file():
            counter[file.suffix] += 1

    return counter


def do_counters_have_same_elements(counter1, counter2):
    all_keys = set(counter1.keys()) | set(counter2.keys())

    return all(counter1.get(key, 0) == counter2.get(key, 0) for key in all_keys)


def organize_photos(source_path, target_path):
    for path in source_path.rglob('*'):
        if path.is_dir():
            continue

        birthtime = datetime.fromtimestamp(path.stat().st_birthtime)
        year, month = birthtime.year, birthtime.month

        target_folder = target_path / str(year) / str(month)
        target_folder.mkdir(parents=True, exist_ok=True)

        new_path = target_folder / path.name

        if new_path.exists():
            new_path = target_folder / f'{path.stem}_{uuid.uuid4()}{path.suffix}'

        path.rename(new_path)


def main():
    source_path = Path(config['path']['source_path'])
    target_path = Path(config['path']['target_path'])

    source_file_extensions_counter = count_extensions(source_path)

    organize_photos(source_path, target_path)

    target_file_extensions_counter = count_extensions(target_path)

    if do_counters_have_same_elements(source_file_extensions_counter, target_file_extensions_counter):
        print('Photos organized successfully', sum(source_file_extensions_counter.values()), sum(target_file_extensions_counter.values()))
    else:
        print('Photos organized unsuccessfully', sum(source_file_extensions_counter.values()), sum(target_file_extensions_counter.values()))


if __name__ == '__main__':
    main()
