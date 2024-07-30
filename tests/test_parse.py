from gendiff.parse import load_file, define_extension
import json
import yaml


def test_define_extension():
    file_path = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/plain_yml_file1.yaml'
    assert define_extension(file_path) == '.json'
    assert define_extension(file_path2) == '.yaml'


def test_load_file():
    file_path = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/plain_yml_file1.yaml'
    with open(file_path, 'r', encoding='utf-8') as file:
        expected_result = json.load(file)
        assert load_file(file_path) == expected_result
    with open(file_path2, 'r', encoding='utf-8') as file2:
        expected_result = yaml.safe_load(file2)
        assert load_file(file_path) == expected_result
