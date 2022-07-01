from configparser import ConfigParser

from files import move_by_file_pattern
from mapping import FILE_PATTERN

parser = ConfigParser()
parser.read('config.conf')

SOURCE_FOLDER = parser.get('folder_path', 'source_folder')
TARGET_FOLDER = parser.get('folder_path', 'target_folder')


def main():
    move_by_file_pattern(SOURCE_FOLDER, TARGET_FOLDER, FILE_PATTERN['MOV'])


if __name__ == '__main__':
    main()
