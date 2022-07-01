from configparser import ConfigParser
from files import move_by_file_pattern

parser = ConfigParser()
parser.read('config.conf')

PHOTOS_FOLDER = parser.get('folder_path', 'photos')
ORGANIZED_PHOTOS_FOLDER = parser.get('folder_path', 'organized_photos')


def main():
    move_by_file_pattern(
        PHOTOS_FOLDER, ORGANIZED_PHOTOS_FOLDER, '*.JPG')


if __name__ == '__main__':
    main()
