import uuid
import requests
from api import YougileApi

BASE_URL = "https://ru.yougile.com"
TOKEN = ""  # Наставник, вставь сюда токен из Yougile

api = YougileApi(BASE_URL, TOKEN)


def delete_project(project_id):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.delete(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers=headers
    )
    return response.json(), response.status_code


def test_create_project_success():
    """Позитивный тест: успешное создание проекта"""
    project_name = f"Test Project {uuid.uuid4().hex[:8]}"

    response_data, status_code = api.create_project(project_name)

    assert status_code == 201
    assert "id" in response_data

    project_id = response_data["id"]
    delete_project(project_id)


def test_update_project_success():
    """Позитивный тест: успешное изменение проекта"""
    original_name = f"Original {uuid.uuid4().hex[:8]}"
    create_data, _ = api.create_project(original_name)
    project_id = create_data["id"]

    new_name = f"Updated {uuid.uuid4().hex[:8]}"
    update_data, status_code = api.update_project(project_id, new_name)

    assert status_code == 200

    get_data, get_status = api.get_project(project_id)
    assert get_status == 200
    assert get_data["id"] == project_id

    delete_project(project_id)


def test_get_project_success():
    """Позитивный тест: успешное получение проекта по ID"""
    project_name = f"Test Get Project {uuid.uuid4().hex[:8]}"
    create_data, _ = api.create_project(project_name)
    project_id = create_data["id"]

    response_data, status_code = api.get_project(project_id)

    assert status_code == 200
    assert response_data["id"] == project_id

    delete_project(project_id)


def test_create_project_without_title():
    """Негативный тест: создание без названия"""
    response_data, status_code = api.create_project("")

    assert status_code in [400, 422]
    assert "error" in response_data or "message" in response_data


def test_update_nonexistent_project():
    """Негативный тест: изменение несуществующего проекта"""
    fake_id = "test_123_test"
    response_data, status_code = api.update_project(fake_id, "New Title")

    assert status_code in [404, 400]
    assert "error" in response_data or "message" in response_data


def test_get_nonexistent_project():
    """Негативный тест: получение несуществующего проекта"""
    fake_id = "test_123_test"
    response_data, status_code = api.get_project(fake_id)

    assert status_code in [404, 400]
    assert "error" in response_data or "message" in response_data
