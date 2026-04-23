import os
import time
import uuid

import pytest
import requests

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
TOKEN = os.getenv("YANDEX_DISK_TOKEN")


@pytest.fixture
def headers():
    if not TOKEN:
        pytest.skip("Нет токена. Добавьте YANDEX_DISK_TOKEN в переменные окружения или .env")
    return {"Authorization": f"OAuth {TOKEN}"}


@pytest.fixture
def folder_name():
    return f"pytest_folder_{int(time.time())}_{uuid.uuid4().hex[:8]}"



def test_create_folder_success(headers, folder_name):
    create_response = requests.put(
        BASE_URL,
        headers=headers,
        params={"path": folder_name},
        timeout=10,
    )

    assert create_response.status_code in (201, 409)

    check_response = requests.get(
        BASE_URL,
        headers=headers,
        params={"path": folder_name},
        timeout=10,
    )

    assert check_response.status_code == 200
    assert check_response.json()["name"] == folder_name
    assert check_response.json()["type"] == "dir"



def test_create_folder_without_token():
    response = requests.put(
        BASE_URL,
        params={"path": "folder_without_token"},
        timeout=10,
    )

    assert response.status_code == 401



def test_create_folder_with_invalid_token():
    response = requests.put(
        BASE_URL,
        headers={"Authorization": "OAuth invalid_token"},
        params={"path": "folder_with_invalid_token"},
        timeout=10,
    )

    assert response.status_code == 401



def test_create_existing_folder_returns_conflict(headers, folder_name):
    first_response = requests.put(
        BASE_URL,
        headers=headers,
        params={"path": folder_name},
        timeout=10,
    )
    assert first_response.status_code == 201

    second_response = requests.put(
        BASE_URL,
        headers=headers,
        params={"path": folder_name},
        timeout=10,
    )

    assert second_response.status_code == 409