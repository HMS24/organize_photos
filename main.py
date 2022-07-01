from pathlib import Path
from configparser import ConfigParser

from files import rename

parser = ConfigParser()
parser.read('config.conf')

PHOTOS_FOLDER = parser.get('folder_path', 'photos')
ORGANIZED_PHOTOS_FOLDER = parser.get('folder_path', 'organized_photos')


def move_file_from_source_to_target_by_pattern(source, target, file_pattern):
    source_path = Path(source)
    target_path = Path(target)
    paths = source_path.glob(file_pattern)

    for path in paths:
        rename(path, target_path)


def main():
    move_file_from_source_to_target_by_pattern(
        PHOTOS_FOLDER, ORGANIZED_PHOTOS_FOLDER, '*.JPG')


if __name__ == '__main__':
    main()
