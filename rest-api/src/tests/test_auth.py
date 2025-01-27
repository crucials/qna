import uuid

import pytest
from flask.testing import FlaskClient

from flask_app import create_flask_app


@pytest.fixture(name="app")
def app_fixture():
    return create_flask_app()


@pytest.fixture(name="client")
def client_fixture(app):
    return app.test_client()


@pytest.fixture(name="runner")
def runner_fixture(app):
    return app.test_cli_runner()


account_name = "test_account_" + str(uuid.uuid4())[:7].replace("-", "_")
token = None


def test_sign_up(client: FlaskClient):
    response = client.post(
        "/auth/sign-up", json={"name": account_name, "password": "123456"}
    )

    assert response.json and response.json.get("data") is not None

    response_data = response.json.get("data")
    assert "token" in response_data and "account" in response_data


def test_log_in(client: FlaskClient):
    global token

    response = client.post(
        "/auth/log-in", json={"name": account_name, "password": "123456"}
    )

    assert response.json and response.json.get("data") is not None

    response_data = response.json.get("data")
    assert "token" in response_data and "account" in response_data

    token = response_data["token"]


def test_account_deletion(client: FlaskClient):
    assert token is not None

    response = client.delete(
        "/current-account", headers={"Authorization": "Bearer " + token}
    )

    assert response.status_code == 200
