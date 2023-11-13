"""
This module contains a FastAPI application that generates QR codes from a given secret.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_generate_qrcode_base64():
    """Test the generation of QR code with base64 encoding."""
    response = client.get("/generate_qrcode_base64/HelloWorld")
    assert response.status_code == 200
    assert "qrcode_base64" in response.json()


def test_generate_qrcode_base64_empty():
    """Test the generation of QR code with base64 encoding with empty input."""
    response = client.get("/generate_qrcode_base64/")
    assert response.status_code == 404


def test_generate_qrcode_base64_special_characters():
    """Test the generation of QR code with base64 encoding with special characters."""
    special_characters = "!@#$%^&*()_+"
    response = client.get(f"/generate_qrcode_base64/{special_characters}")
    assert response.status_code == 200
    assert "qrcode_base64" in response.json()
