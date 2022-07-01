from collections import Counter
from pathlib import Path

from utils import get_split_datetime
from mapping import DUPLICATE


def _walk_directory_tree(top, callback):
    """遞迴走訪資料夾"""

    for path in Path(top).iterdir():
        if path.is_dir():
            _walk_directory_tree(path, callback)
        elif path.is_file():
            callback(path)
        else:
            print(f'Skipping {path}')


def generate_filename_extension_counter(folder):
    """計算資料夾裡各種副檔名的數量"""

    counter = Counter()

    def counting(path):
        # 可能會有隱藏檔
        suffix = path.suffix or path.stem
        counter[suffix] = counter.get(suffix, 0) + 1

    _walk_directory_tree(folder, counting)
    return counter


def _rename(path, new_path):
    """改名並移動檔案至新資料夾"""

    (year, month, day, *_) = get_split_datetime(path.stat().st_birthtime)

    folder = new_path.joinpath(year, f'{month}-{day}')
    folder.mkdir(parents=True, exist_ok=True)

    new_path = folder.joinpath(f'{path.stem}{path.suffix}')

    if new_path.exists():
        new_path = folder.joinpath(f'{path.stem}_{DUPLICATE}{path.suffix}')

    path.rename(new_path)

def move_by_file_pattern(source, target, file_pattern):
    """移動特定檔案"""

    source_path = Path(source)
    target_path = Path(target)
    paths = source_path.glob(file_pattern)

    for path in paths:
        _rename(path, target_path)
