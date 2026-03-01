# Student API (Flask)

This API manages student records using Flask + SQLAlchemy with a SQLite database (`data.db`).

- Base URL: `http://localhost:24655`
- Content-Type for write operations: `application/json`

## Student Object

```json
{
  "roll": 1,
  "name": "John Doe",
  "father_name": "Richard Doe",
  "mother_name": "Jane Doe",
  "gender": "M",
  "email": "john@example.com",
  "phone": "9876543210"
}
```

### Field Types

- `roll`: integer (primary key)
- `name`: string
- `father_name`: string
- `mother_name`: string
- `gender`: string (1 character)
- `email`: string
- `phone`: string (10 characters)

## Endpoints

### 1) Health Check

- Method: `GET`
- Path: `/`
- Request Body: none

Success Response (`200`):

```json
{
  "status": "success"
}
```

---

### 2) Add Student

- Method: `POST`
- Path: `/add`
- Request Body: required (all fields)

Request Payload:

```json
{
  "roll": 1,
  "name": "John Doe",
  "father_name": "Richard Doe",
  "mother_name": "Jane Doe",
  "gender": "M",
  "email": "john@example.com",
  "phone": "9876543210"
}
```

Success Response (`200`):

```json
{
  "status": "success"
}
```

Notes:
- The code expects all keys to exist in the request JSON.
- `roll` must be unique.

---

### 3) Get Student by Roll

- Method: `GET`
- Path: `/student/<roll>`
- Path Parameter:
  - `roll`: student roll number
- Request Body: none

Success Response (`200`):

```json
{
  "status": "success",
  "data": {
    "roll": 1,
    "name": "John Doe",
    "father_name": "Richard Doe",
    "mother_name": "Jane Doe",
    "gender": "M",
    "email": "john@example.com",
    "phone": "9876543210"
  }
}
```

Error Response (`404`):

```json
{
  "status": "error",
  "message": "Student not found"
}
```

---

### 4) Delete Student by Roll

- Method: `DELETE`
- Path: `/student/<roll>`
- Path Parameter:
  - `roll`: student roll number
- Request Body: none

Success Response (`200`):

```json
{
  "status": "success"
}
```

Error Response (`404`):

```json
{
  "status": "error",
  "message": "Student not found"
}
```

---

### 5) Replace Student (Full Update)

- Method: `PUT`
- Path: `/student/<roll>`
- Path Parameter:
  - `roll`: student roll number
- Request Body: required (all updateable fields)

Request Payload:

```json
{
  "name": "John Doe",
  "father_name": "Richard Doe",
  "mother_name": "Jane Doe",
  "gender": "M",
  "email": "john@example.com",
  "phone": "9876543210"
}
```

Success Response (`200`):

```json
{
  "status": "success"
}
```

Error Response (`404`):

```json
{
  "status": "error",
  "message": "Student not found"
}
```

Notes:
- `roll` in the URL identifies the student and is not updated in this endpoint.
- The code expects all listed keys to exist in the request JSON.

---

### 6) Update Student (Partial Update)

- Method: `PATCH`
- Path: `/student/<roll>`
- Path Parameter:
  - `roll`: student roll number
- Request Body: required (any subset of fields)

Allowed Payload Fields:

```json
{
  "name": "Optional",
  "father_name": "Optional",
  "mother_name": "Optional",
  "gender": "Optional",
  "email": "Optional",
  "phone": "Optional"
}
```

Success Response (`200`):

```json
{
  "status": "success"
}
```

Error Response (`404`):

```json
{
  "status": "error",
  "message": "Student not found"
}
```

## Run the App

```bash
pip install -r requirements.txt
python app.py
```

App starts on:

- `http://localhost:24655`

## Database

- SQLite DB URI: `sqlite:///data.db`
- Tables are created automatically on startup (`db.create_all()`).
