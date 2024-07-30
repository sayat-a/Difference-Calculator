import pytest
from gendiff.gen_diff import generate_diff


@pytest.mark.parametrize(
    "file1_path, file2_path, result_path, formatter",
    [
        (
            'tests/fixtures/nested_file1.json',
            'tests/fixtures/nested_file2.json',
            'tests/fixtures/diff_json.txt', 'stylish'
        ),
        (
            'tests/fixtures/nested_yml_file1.yaml',
            'tests/fixtures/nested_yml_file2.yaml',
            'tests/fixtures/diff_json.txt', 'stylish'
        ),
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'tests/fixtures/expected_result_flat_json.txt',
            'stylish'
        ),
        (
            'tests/fixtures/plain_yml_file1.yaml',
            'tests/fixtures/plain_yml_file2.yaml',
            'tests/fixtures/expected_result_flat_json.txt',
            'stylish'
        ),
        (
            'tests/fixtures/nested_file1.json',
            'tests/fixtures/nested_file2.json',
            'tests/fixtures/expected_result_plain_format.txt',
            'plain'
        )
    ]
)
def test_generate_diff(file1_path, file2_path, result_path, formatter):
    with open(result_path, 'r', encoding='utf-8') as file:
        expected_result = file.read()
    assert generate_diff(
        file1_path, file2_path, formatter=formatter
    ) == expected_result
