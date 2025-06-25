import random
import os


def find_file(cur_path, file_names):
    all_paths = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if i_elem in file_names:
            all_paths.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_names)
            if result:
                all_paths.extend(result)

    return all_paths


def check_file_inside(path_to_file):
    file = open(path_to_file, "r", encoding="utf8")
    for line in file:
        print(line, end='')
    file.close()


all_paths = find_file(
    "..",
    (
        "task 5.3.2.py",
        "task 3.4.3.py",
        "task 9.2.2.py",
    ),
)
check_file_inside(random.choice(all_paths))