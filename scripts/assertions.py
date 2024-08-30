import requests

BASE_URL = "http://localhost:8000"

def assert_login():
    response = requests.get(f"{BASE_URL}/login/testuser")
    #проверка ответа 200
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
      #проверка в ответе правильного токена
    assert response.json()["token"] == "Token_testuser", f"Unexpected token: {response.json()['token']}"

def assert_add_booking():
    response = requests.post(f"{BASE_URL}/booking/add", json={"service_name": "massage"})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
  
    assert "message" in response.json(), "Response does not contain 'message' key"

def assert_checkout():
    response = requests.post(f"{BASE_URL}/checkout", json={"order_id": 1234})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    #проверка наличия ключа "message"
    assert "message" in response.json(), "Response does not contain 'message' key"

#проверки
if __name__ == "__main__":
    assert_login()
    print("Login test passed")

    assert_add_booking()
    print("Add booking test passed")

    assert_checkout()
    print("Checkout test passed")
