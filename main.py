import uuid

from pathlib import Path
from datetime import datetime
from collections import Counter

def seperate_date_time(timestamp):
    try:
        dt = datetime.fromtimestamp(timestamp)
    except ValueError:
        print('incorrect timestamp')

        return None

    return dt.strftime('%Y %m %d %H %M %S').split()


def count_extensions(folder):
    counter = Counter()

    for path in Path(folder).rglob("*"):
        if path.is_file():
            suffix = path.suffix or path.name
            counter[suffix] += 1

    return counter

def do_counters_have_same_elements(counter1, counter2):
    all_keys = set(counter1.keys()) | set(counter2.keys())

    return all(counter1.get(key, 0) == counter2.get(key, 0) for key in all_keys)

def main():
    source_path = Path('../Downloads/1_photos')
    source_counter = count_extensions(source_path)

    mov_files = source_path.glob('*.[mM][oO][vV]')
    jpg_files = source_path.glob('*.[jJ][pP][gG]')
    png_files = source_path.glob('*.[pP][nN][gG]')

    files = list(mov_files) + list(jpg_files) + list(png_files)

    target_path = Path('../Downloads/1_photos_organized')

    for file in files:
        year, month, *_ = seperate_date_time(file.stat().st_birthtime)

        target_folder = target_path / str(year) / str(month)
        target_folder.mkdir(parents=True, exist_ok=True)

        new_file = target_folder / file.name

        if new_file.exists():
            new_file = target_folder / f'{file.stem}_{uuid.uuid4()}{file.suffix}'

        file.rename(new_file)

        # print(f'{file} -> {new_file}')

    target_counter = count_extensions(target_path)

    if do_counters_have_same_elements(source_counter, target_counter):
        print('Organized successfully', sum(source_counter.values()), sum(target_counter.values()))
    else:
        print('Organized UNsuccessfully', sum(source_counter.values()), sum(target_counter.values()))

if __name__ == '__main__':
    main()
