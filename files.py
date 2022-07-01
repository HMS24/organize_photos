from collections import Counter
from pathlib import Path


# 將計數邏輯獨立抽出為 callback
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
