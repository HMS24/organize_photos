from configparser import ConfigParser
from files import move_by_file_pattern

parser = ConfigParser()
parser.read('config.conf')

SOURCE_FOLDER = parser.get('folder_path', 'source_folder')
TARGET_FOLDER = parser.get('folder_path', 'target_folder')


def main():
    move_by_file_pattern(SOURCE_FOLDER, TARGET_FOLDER, '*.JPG')


if __name__ == '__main__':
    main()
