from pathlib import Path
from configparser import ConfigParser

from mapping import DUPLICATE
from utils import get_split_datetime

parser = ConfigParser()
parser.read('config.conf')

PHOTOS_FOLDER = parser.get('folder_path', 'photos')
ORGANIZED_PHOTOS_FOLDER = parser.get('folder_path', 'organized_photos')
ARCHIVE_FOLDER = parser.get('folder_path', 'archive')


def move(source, target, file_pattern):
    source_path = Path(source)
    target_path = Path(target)
    paths = source_path.glob(file_pattern)

    for path in paths:
        (year, month, day, *_) = get_split_datetime(path.stat().st_birthtime)

        folder = target_path.joinpath(year, f'{month}-{day}')
        folder.mkdir(parents=True, exist_ok=True)

        new_path = folder.joinpath(f'{path.stem}{path.suffix}')

        if new_path.exists():
            new_path = folder.joinpath(f'{path.stem}_{DUPLICATE}{path.suffix}')

        path.rename(new_path)


def main():
    move(PHOTOS_FOLDER, ORGANIZED_PHOTOS_FOLDER, '*.JPG')


if __name__ == '__main__':
    main()
