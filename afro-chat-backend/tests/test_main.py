from fastapi import FastAPI
from fastapi.testclient import TestClient
import unittest
import pytest
import asyncio

app = FastAPI()


@app.get("/")
async def read_main():
    await asyncio.sleep(10)
    return {"msg": "Hello World"}


client = TestClient(app=app)



 # test normal functions

def test_hi():
    assert 1 == 1
    print("HI")

def test_hi2():
    assert 1 == 1
    print("HI")

# use this for async testing
@pytest.mark.anyio
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


class MainTest(unittest.TestCase):
    def test_check(self):
        self.assertEqual(201, 201)

    def test_check2(self):
        self.assertEqual(201, 201)


if __name__ == "__main__":
    unittest.main()

