import pytest
import json

from src.jsonsaver import JsonSaver


TEST_FILE = "test_data.json"


@pytest.fixture
def json_saver():
    return JsonSaver(TEST_FILE)


def test_file_property(json_saver):
    assert json_saver.file == TEST_FILE


def test_file_setter(json_saver):
    new_filename = "new_test_data.json"
    json_saver.file = new_filename
    assert json_saver.file == new_filename


def test_str_method(tmp_path):
    test_data = [
        {"job_name": "Engineer", "salary": 50000},
        {"job_name": "Manager", "salary": 60000}
    ]
    test_file = tmp_path / "test_data.json"
    with open(test_file, 'w', encoding='utf-8') as f:
        for item in test_data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')

    json_saver = JsonSaver(str(test_file))
    assert str(json_saver) == str(test_data)