import os
import shutil
from lib.launcher.scaffold import write_to_file, scaffold, descaffold
from tests.unit import TEMP_DIR_PATH
import pytest
from config.settings import app_paths


@pytest.fixture(scope="session", autouse=True)
def temp_dir():
    # Will be executed before the first test
    if not os.path.isdir(TEMP_DIR_PATH):
        os.mkdir(TEMP_DIR_PATH)
    yield TEMP_DIR_PATH
    # Will be executed after the last test
    shutil.rmtree(TEMP_DIR_PATH)


@pytest.fixture(scope="session", autouse=True)
def scaffold_init():
    test_name = "test_scaffold"
    scaffold(test_name)
    yield test_name
    descaffold(test_name)


def test_write_to_file(temp_dir):
    print(temp_dir)
    assert os.path.isdir(temp_dir)
    filename = f"{temp_dir}/write_test.txt"
    content = "Hello, World!"
    write_to_file(filename, content)
    assert os.path.isfile(filename)
    with open(filename, "r") as f:
        assert f.read() == content


def test_scaffold_model(scaffold_init):
    model_path = f"{app_paths['models']}/{scaffold_init}.py"
    assert os.path.isfile(model_path)
    # todo add test cases for content of generated files


def test_scaffold_repo(scaffold_init):
    repo_path = f"{app_paths['repos']}/{scaffold_init}_repository.py"
    assert os.path.isfile(repo_path)
    # todo add test cases for content of generated files


def test_scaffold_service(scaffold_init):
    service_path = f"{app_paths['services']}/{scaffold_init}_service.py"
    assert os.path.isfile(service_path)
    # todo add test cases for content of generated files


def test_scaffold_controller(scaffold_init):
    controller_path = f"{app_paths['controllers']}/{scaffold_init}_controller.py"
    assert os.path.isfile(controller_path)
    # todo add test cases for content of generated files


def test_scaffold_api(scaffold_init):
    api_path = f"{app_paths['api']}/{scaffold_init}_api.py"
    assert os.path.isfile(api_path)
    # todo add test cases for content of generated files
