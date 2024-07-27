import pytest
import json
from gendiff.gen_diff import generate_diff


@pytest.fixture
def json_file1(tmp_path):
    content = {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    }
    file_path = tmp_path / "file1.json"
    with open(file_path, "w") as file:
        json.dump(content, file)
    return file_path


@pytest.fixture
def json_file2(tmp_path):
    content = {
        "common": {
            "follow": False,
            "setting1": "Value 1",
            "setting3": None,
            "setting4": "blah blah",
            "setting5": {
                "key5": "value5"
            },
            "setting6": {
                "key": "value",
                "ops": "vops",
                "doge": {
                    "wow": "so much"
                }
            }
        },
        "group1": {
            "foo": "bar",
            "baz": "bars",
            "nest": "str"
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
    file_path = tmp_path / "file2.json"
    with open(file_path, "w") as file:
        json.dump(content, file)
    return file_path


@pytest.fixture
def yaml_file1(tmp_path):
    content = """
common:
  setting1: "Value 1"
  setting2: 200
  setting3: true
  setting6:
    key: "value"
    doge:
      wow: ""
group1:
  baz: "bas"
  foo: "bar"
  nest:
    key: "value"
group2:
  abc: 12345
  deep:
    id: 45
"""
    file_path = tmp_path / "file1.yaml"
    with open(file_path, "w") as file:
        file.write(content)
    return file_path


@pytest.fixture
def yaml_file2(tmp_path):
    content = """
common:
  follow: false
  setting1: "Value 1"
  setting3: null
  setting4: "blah blah"
  setting5:
    key5: "value5"
  setting6:
    key: "value"
    ops: "vops"
    doge:
      wow: "so much"
group1:
  foo: "bar"
  baz: "bars"
  nest: "str"
group3:
  deep:
    id:
      number: 45
  fee: 100500
"""
    file_path = tmp_path / "file2.yaml"
    with open(file_path, "w") as file:
        file.write(content)
    return file_path


def test_generate_diff_json(json_file1, json_file2):
    expected_result = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    assert generate_diff(json_file1, json_file2) == expected_result


def test_generate_diff_yaml(yaml_file1, yaml_file2):
    expected_result = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    assert generate_diff(yaml_file1, yaml_file2) == expected_result


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
