from gendiff.gen_diff import generate_diff


def test_generate_diff():
    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'
    assert generate_diff(file1_path, file2_path) == expected_result
