import pytest

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["project"] == "AquaPredict AI"


def test_water_shortage():
    response = client.post(
        "/assess",
        json={
            "region": "Region_A",
            "water_supply_mld": 80,
            "water_demand_mld": 95,
        },
    )

    assert response.status_code == 200

    result = response.json()
    assert result["water_deficit_mld"] == 15
    assert result["assessment"] == "Potential shortage"
    assert result["is_machine_learning_prediction"] is False


def test_supply_exceeds_demand():
    response = client.post(
        "/assess",
        json={
            "region": "Region_B",
            "water_supply_mld": 120,
            "water_demand_mld": 100,
        },
    )

    assert response.status_code == 200

    result = response.json()
    assert result["water_deficit_mld"] == -20
    assert result["assessment"] == "Estimated supply exceeds demand"


def test_supply_equals_demand():
    response = client.post(
        "/assess",
        json={
            "region": "Region_C",
            "water_supply_mld": 100,
            "water_demand_mld": 100,
        },
    )

    assert response.status_code == 200
    assert response.json()["water_deficit_mld"] == 0
    assert response.json()["assessment"] == "Estimated supply equals demand"


def test_negative_supply_is_rejected():
    response = client.post(
        "/assess",
        json={
            "region": "Region_A",
            "water_supply_mld": -10,
            "water_demand_mld": 100,
        },
    )

    assert response.status_code == 422


def test_negative_demand_is_rejected():
    response = client.post(
        "/assess",
        json={
            "region": "Region_A",
            "water_supply_mld": 100,
            "water_demand_mld": -10,
        },
    )

    assert response.status_code == 422


def test_empty_region_is_rejected():
    response = client.post(
        "/assess",
        json={
            "region": "",
            "water_supply_mld": 100,
            "water_demand_mld": 120,
        },
    )

    assert response.status_code == 422
