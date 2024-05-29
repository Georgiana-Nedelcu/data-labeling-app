import pytest
import sys
import os
from httpx import AsyncClient

# Adaugă directorul rădăcină în sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

@pytest.mark.asyncio
async def test_create_project():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/projects/", json={"name": "Test Project", "description": "Test Description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Project"

@pytest.mark.asyncio
async def test_read_projects():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/projects/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
