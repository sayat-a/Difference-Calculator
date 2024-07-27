import json
from gendiff.gen_diff import generate_diff


def test_format_json():
    file1_path = 'tests/fixtures/nested_file1.json'
    file2_path = 'tests/fixtures/nested_file2.json'
    expected_result_python = {
        "common": {
            "status": "nested",
            "children": {
                "follow": {
                    "status": "added",
                    "value": False
                },
                "setting1": {
                    "status": "unchanged",
                    "value": "Value 1"
                },
                "setting2": {
                    "status": "removed",
                    "value": 200
                },
                "setting3": {
                    "status": "changed",
                    "old_value": True,
                    "new_value": None
                },
                "setting4": {
                    "status": "added",
                    "value": "blah blah"
                },
                "setting5": {
                    "status": "added",
                    "value": {
                        "key5": "value5"
                    }
                },
                "setting6": {
                    "status": "nested",
                    "children": {
                        "doge": {
                            "status": "nested",
                            "children": {
                                "wow": {
                                    "status": "changed",
                                    "old_value": "",
                                    "new_value": "so much"
                                }
                            }
                        },
                        "key": {
                            "status": "unchanged",
                            "value": "value"
                        },
                        "ops": {
                            "status": "added",
                            "value": "vops"
                        }
                    }
                }
            }
        },
        "group1": {
            "status": "nested",
            "children": {
                "baz": {
                    "status": "changed",
                    "old_value": "bas",
                    "new_value": "bars"
                },
                "foo": {
                    "status": "unchanged",
                    "value": "bar"
                },
                "nest": {
                    "status": "changed",
                    "old_value": {
                        "key": "value"
                    },
                    "new_value": "str"
                }
            }
        },
        "group2": {
            "status": "removed",
            "value": {
                "abc": 12345,
                "deep": {
                    "id": 45
                }
            }
        },
        "group3": {
            "status": "added",
            "value": {
                "deep": {
                    "id": {
                        "number": 45
                    }
                },
                "fee": 100500
            }
        }
    }
    result = generate_diff(file1_path, file2_path, formatter='json')
    expected_result_json = json.dumps(expected_result_python, indent=4)
    assert result == expected_result_json
