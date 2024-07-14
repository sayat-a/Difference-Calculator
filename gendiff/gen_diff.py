import json


def generate_diff(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)
    with open(file2_path, 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    diff_lines = []
    for key in all_keys:
        if key in data1 and key not in data2:
            diff_lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            diff_lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff_lines.append(f"  - {key}: {data1[key]}")
            diff_lines.append(f"  + {key}: {data2[key]}")
        else:
            diff_lines.append(f"    {key}: {data1[key]}")
    result = "{\n" + "\n".join(diff_lines) + "\n}"
    return result
