from pathlib import Path
from datetime import datetime
from collections import Counter
from configparser import ConfigParser

from utils import walk_directory_tree
from mapping import DUPLICATE

parser = ConfigParser()
parser.read('config.conf')

IMAGES_FOLDER = parser.get('folder_path', 'images')
ORGANIZED_IMAGES_FOLDER = parser.get('folder_path', 'organized_images')
ARCHIVE_FOLDER = parser.get('folder_path', 'archive')


def generate_file_extension_counter_from(dir):
    """副檔名計數"""

    counter = Counter()

    def counting(path):
        # 可能會有隱藏檔
        suffix = path.suffix or path.stem
        counter[suffix] = counter.get(suffix, 0) + 1

    walk_directory_tree(dir, counting)
    return counter


def move(source, target, file_pattern):
    """"""

    source_path = Path(source)
    target_path = Path(target)
    paths = source_path.glob(file_pattern)

    for path in paths:
        last_mod_datetime = datetime.fromtimestamp(path.stat().st_birthtime)
        last_mod_year_str = str(last_mod_datetime.year)
        last_mod_date_str = last_mod_datetime.strftime('%m-%d')

        folder = target_path.joinpath(last_mod_year_str, last_mod_date_str)
        folder.mkdir(parents=True, exist_ok=True)

        new_path = folder.joinpath(f'{path.stem}{path.suffix}')

        if new_path.exists():
            new_path = folder.joinpath(f'{path.stem}_{DUPLICATE}{path.suffix}')

        path.rename(new_path)


def main():
    move(IMAGES_FOLDER, ORGANIZED_IMAGES_FOLDER, '.JPG')


if __name__ == '__main__':
    main()
