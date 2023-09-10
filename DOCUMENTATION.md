
# Project Documentation

This document provides detailed information on how to use the REST API for the "Person" resource. Please refer to this documentation for setup instructions, request/response formats, sample API usage, and any known limitations or assumptions made during development.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Request/Response Formats](#requestresponse-formats)
- [Sample API Usage](#sample-api-usage)
- [Known Limitations and Assumptions](#known-limitations-and-assumptions)

---

## Setup Instructions

Follow these steps to set up and run the API locally:

1. **Clone the Repository:**
   ```python
   import os
   import requests

   # Replace with your repository URL
   repository_url = "https://github.com/prmpsmart/hgnx_backend.git"
   repository_directory = "hgnx_backend"

   os.system(f"git clone {repository_url}")
   os.chdir(repository_directory)
   ```

2. **Install Dependencies:**
   ```python
   # Install Python dependencies
   import subprocess

   subprocess.run(["pip", "install", "-r", "requirements.txt"])
   ```

3. **Run the API:**
   ```python
   # Run the API using Uvicorn
   subprocess.run(["uvicorn", "main:app"])
   ```

4. The API will be available locally at `http://127.0.0.1:8000`.

---

## API Endpoints

The API provides the following endpoints for CRUD operations on the "Person" resource:

- **Create a Person**:
  - **POST /api/**
  - Add a new person to the database.

- **Read a Person**:
  - **GET /api/{name}**
  - Retrieve details of a person by name.

- **Update a Person**:
  - **PUT /api/{name}**
  - Modify details of an existing person by name.

- **Delete a Person**:
  - **DELETE /api/{name}**
  - Remove a person from the database by name.

---

## Request/Response Formats

### Create a Person (POST /api/)

**Request Format:**
```python
import requests

api_url = "http://127.0.0.1:8000/api/"

data = {
    "name": "Miracle Apata",
    "age": "24"
}

response = requests.post(api_url, json=data)
print(response.json())
```

**Response Format (Success - 200):**
```json
{
    "name": "Miracle Apata",
    "age": "24"
}
```

**Response Format (Conflict - 409):**
```json
{
    "detail": "Person with 'Miracle Apata' already exists"
}
```

### Read a Person (GET /api/{name})

**Request Format:**
```python
import requests

api_url = "http://127.0.0.1:8000/api/Miracle%20Apata"

response = requests.get(api_url)
print(response.json())
```

**Response Format (Success- 200):**
```json
{
    "name": "Miracle Apata",
    "age": "24"
}
```

**Response Format (Not Found - 404):**
```json
{
    "detail": "Person with 'Miracle Apata' not found"
}
```

### Update a Person (PUT /api/{name})

**Request Format:**
```python
import requests

api_url = "http://127.0.0.1:8000/api/Miracle%20Apata"

data = {
    "age": "35"
}

response = requests.put(api_url, json=data)
print(response.json())
```

**Response Format (Success - 200):**
```json
{
    "name": "Miracle Apata",
    "age": 35
}
```

**Response Format (Not Found - 404):**
```json
{
  "detail": "Person with 'Miracle Apata' not found"
}
```

### Delete a Person (DELETE /api/{name})

**Request Format:**
```python
import requests

api_url = "http://127.0.0.1:8000/api/Miracle%20Apata"

response = requests.delete(api_url)
print(response.json())
```

**Response Format (Not Found - 404):**
```json
{
  "detail": "Person with 'Miracle Apata' not found"
}
```

---

## Sample API Usage

Here are some sample API usage scenarios with Python code examples:

1. **Create a Person:**
   ```python
   import requests

   api_url = "http://127.0.0.1:8000/api/"

   data = {
       "name": "Alice Johnson",
       "age": "25"
   }

   response = requests.post(api_url, json=data)
   print(response.json())
   ```

2. **Read a Person:**
   ```python
   import requests

   api_url = "http://127.0.0.1:8000/api/Alice%20Johnson"

   response = requests.get(api_url)
   print(response.json())
   ```

3. **Update a Person:**
   ```python
   import requests

   api_url = "http://127.0.0.1:8000/api/Alice%20Johnson"

   data = {
       "age": "26"
   }

   response = requests.put(api_url, json=data)
   print(response.json())
   ```

4. **Delete a Person:**
   ```python
   import requests

   api_url = "http://127.0.0.1:8000/api/Alice%20Johnson"

   response = requests.delete(api_url)
   print(response.json())
   ```

---

## Known Limitations and Assumptions

- This API uses a Python built-in database (sqlite3) for demonstration purposes.
- Input validation is handled by FastAPI in this task. Implement more robust validation and error handling in a production-ready application.
- Authentication and authorization mechanisms are not implemented here. Ensure secure access to your API in a real-world scenario.
- This documentation assumes that you have successfully set up the API locally.
