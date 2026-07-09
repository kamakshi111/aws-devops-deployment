from app import app

client = app.test_client()


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "AWS DevOps Assignment"
    assert data["status"] == "Running Successfully"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "Healthy"


def test_get_employees():
    response = client.get("/employees")

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) >= 2


def test_add_employee():
    response = client.post(
        "/employees",
        json={
            "name": "Aman",
            "role": "Cloud Engineer"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["name"] == "Aman"
    assert data["role"] == "Cloud Engineer"


def test_delete_employee():
    response = client.delete("/employees/3")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "Employee deleted"