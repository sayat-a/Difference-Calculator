from gendiff.parse import load_file, define_extension
import json
import yaml
import pytest


@pytest.mark.parametrize("file_path, expected_result", [
    ('tests/fixtures/file1.json', '.json'),
    ('tests/fixtures/plain_yml_file1.yaml', '.yaml')
])
def test_define_extension(file_path, expected_result):
    assert define_extension(file_path) == expected_result


@pytest.mark.parametrize("file_path, loader", [
    ('tests/fixtures/file1.json', json.load),
    ('tests/fixtures/plain_yml_file1.yaml', yaml.safe_load)
])
def test_load_file(file_path, loader):
    with open(file_path, 'r', encoding='utf-8') as file:
        expected_result = loader(file)
        assert load_file(file_path) == expected_result
