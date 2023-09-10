import requests

base_url = "http://localhost:8000"
base_url = "https://hgnxbackend-prmpsmart.b4a.run"
name = "Miracle Apata"
age = '24'


# Function to print the response nicely
def print_response(response: requests.Response):
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}\n")


# Test Create (POST) operation
def test_create_person():
    endpoint = "/api/"
    data = {"name": name, "age": age}
    response = requests.post(base_url + endpoint, json=data)
    print("Testing Create (POST) operation:")
    print_response(response)


# Test Read (GET) operation
def test_read_person(name: str):
    endpoint = f"/api/{name}"
    response = requests.get(base_url + endpoint)
    print(f"Testing Read (GET) operation for {name}:")
    print_response(response)


# Test Update (PUT) operation
def test_update_person(name: str, new_age: int):
    endpoint = f"/api/{name}"
    data = {"age": new_age}
    response = requests.put(base_url + endpoint, json=data)
    print(f"Testing Update (PUT) operation for {name}:")
    print_response(response)


# Test Delete (DELETE) operation
def test_delete_person(name: str):
    endpoint = f"/api/{name}"
    response = requests.delete(base_url + endpoint)
    print(f"Testing Delete (DELETE) operation for {name}:")
    print_response(response)


if __name__ == "__main__":
    # Test Create operation
    test_create_person()

    # Test Read operation
    test_read_person(name)

    # Test Update operation
    test_update_person(name, '56')

    # Test Read operation after update
    test_read_person(name)

    # Test Delete operation
    test_delete_person(name)

    # Test Read operation after delete
    test_read_person(name)