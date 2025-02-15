import os
import json
import csv
import pickle


def calc_dir_size(path: str) -> int:
    total_size = 0
    for path, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size


def directory_info(directory: str, filename: str='directory_info') -> None:
    results = []
    for dir_path, dir_names, file_names in os.walk(directory):
        for dir_name in dir_names:
            dir_info = {
                'path': os.path.join(dir_path, dir_name),
                'type': 'directory',
                'size': calc_dir_size(os.path.join(dir_path, dir_name))
            }
            results.append(dir_info)
        for file_name in file_names:
            file_info = {
                'path': os.path.join(dir_path, file_name),
                'type': 'file',
                'size': os.path.getsize(os.path.join(dir_path, file_name))
            }
            results.append(file_info)
    save_to_pickle(results, filename)
    save_to_json(results, filename)
    save_to_csv(results, filename)


def save_to_json(data, filename: str) -> None:
    with open(filename + '.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


def save_to_csv(data, filename: str) -> None:
    with open(filename + '.csv', 'w', encoding='utf-8', newline='') as csv_file:
        field_names = ['path', 'type', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def save_to_pickle(data, filename: str) -> None:
    with open(filename + '.pkl', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
