from gendiff.gen_diff import generate_diff


def test_generate_diff_json():
    file_path = 'tests/fixtures/diff_json.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        expected_result = file.read()
    file1_path = 'tests/fixtures/nested_file1.json'
    file2_path = 'tests/fixtures/nested_file2.json'
    assert generate_diff(file1_path, file2_path) == expected_result


def test_generate_diff_yaml():
    file_path = 'tests/fixtures/diff_json.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        expected_result = file.read()
    file1_path = 'tests/fixtures/nested_yml_file1.yaml'
    file2_path = 'tests/fixtures/nested_yml_file2.yaml'
    assert generate_diff(file1_path, file2_path) == expected_result


def test_generate_diff():
    file_path = 'tests/fixtures/expected_result_flat_json.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        expected_result = file.read()
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'
    assert generate_diff(file1_path, file2_path) == expected_result


def test_generate_diff_json_plain():
    file_path = 'tests/fixtures/expected_result_plain_format.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        expected_result = file.read()
    file1_path = 'tests/fixtures/nested_file1.json'
    file2_path = 'tests/fixtures/nested_file2.json'
    result = generate_diff(file1_path, file2_path, formatter='plain')
    assert result == expected_result
