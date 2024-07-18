import pytest
import json
from gendiff.gen_diff import generate_diff

result1 = {
	- follow: False
	host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
  }


def test_generate_diff():
	file1 = 'tests/fixtures/file1.json'
	file2 = 'tests/fixtures/file2.json'
	assert generate_diff(file1, file2) == result1

