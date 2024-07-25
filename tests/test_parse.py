from gendiff.parse import load_file, define_extension
import json


def test_define_extension():
    file_path = 'tests/fixtures/file1.json'
    assert define_extension(file_path) == 'json'


def test_load_file():
    file_path = 'tests/fixtures/file1.json'
    expected_result = json.load(file_path)
    assert load_file(file_path) == expected_result
