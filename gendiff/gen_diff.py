from gendiff import parse


def generate_diff(file1_path, file2_path):
    data1 = parse.load_file(file1_path)
    data2 = parse.load_file(file2_path)
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    diff_lines = []
    for key in all_keys:
        if key in data1 and key not in data2:
            diff_lines.append(f"  - {key}: {(str(data1[key])).lower()}")
        elif key not in data1 and key in data2:
            diff_lines.append(f"  + {key}: {(str(data2[key])).lower()}")
        elif data1[key] != data2[key]:
            diff_lines.append(f"  - {key}: {(str(data1[key])).lower()}")
            diff_lines.append(f"  + {key}: {(str(data2[key])).lower()}")
        else:
            diff_lines.append(f"    {key}: {(str(data1[key])).lower()}")
    result = "{\n" + "\n".join(diff_lines) + "\n}"
    return result
