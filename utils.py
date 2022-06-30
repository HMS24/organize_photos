from pathlib import Path


# 將計數邏輯獨立抽出為 callback    
def walk_directory_tree(top, callback):
    """遞迴走訪資料夾"""

    for path in Path(top).iterdir():
        if path.is_dir():
            walk_directory_tree(path, callback)
        elif path.is_file():
            callback(path)
        else:
            print(f'Skipping {path}')