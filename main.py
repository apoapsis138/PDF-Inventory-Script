from pathlib import Path
import sys
from datetime import datetime
import csv

def path_check():
    path = Path("c:\\Users\\nonli\\OneDrive\\Books\\")
    if path.exists():
        print(f"{path} is a valid path")
    else:
        print("Not a valid path, exiting")
        sys.exit()
    if not path.is_dir():
        print("Path is a file, exiting")
        sys.exit()
    print(f"Using {path} as root for file inventory")
    return path

def read_dir(path):
    files_list = [files for files in Path(path).rglob('*') if files.is_file()]
    results = []
    for file in files_list:
        try:
            result = {
                "file_name": Path(file).name,
                "file_type": Path(file).suffix,
                "parent": str(Path(file).parent),
                "size": Path.stat(file).st_size,
                "modified_date": datetime.fromtimestamp(Path.stat(file).st_mtime).strftime("%Y-%m-%d"),
                "last_accessed": datetime.fromtimestamp(Path.stat(file).st_atime).strftime("%Y-%m-%d")
            }
            results.append(result)
        except Exception as e:
            print(f"Something went wrong: {e}")
        return results

def create_csv(results):
    output = "directory.csv"
    if not results:
        print("No files found, nothing to write")
        return
    headers = results[0].keys()

    with open(output, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=headers)

        writer.writeheader()
        writer.writerows(results)

def main():
    path = path_check()        
    results = read_dir(path)
    create_csv(results)

if __name__ == "__main__":
    main()
