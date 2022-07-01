from pathlib import Path
from configparser import ConfigParser

from files import rename

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
        rename(path, target_path)


def main():
    move(PHOTOS_FOLDER, ORGANIZED_PHOTOS_FOLDER, '*.JPG')


if __name__ == '__main__':
    main()
