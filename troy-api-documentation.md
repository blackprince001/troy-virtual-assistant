# TROY Virtual Teaching Assistant API Documentation

## Introduction

This document provides an overview and usage instructions for the TROY Virtual Teaching Assistant API. The API allows users to interact with various features of the virtual teaching assistant, including user management, course management, chat functionality, and feedback systems.

## Base URL

The base URL for all API endpoints is not specified in the provided OpenAPI document. You should replace `{base_url}` with the actual base URL of your API in all the examples below.

## Authentication

Most endpoints require authentication using OAuth2 Password Bearer tokens. To authenticate, you need to obtain an access token using the `/api/token` endpoint.

### Obtaining an Access Token

**Endpoint:** `POST {base_url}/api/token`

**Request Body (form-data):**

- `username`: Your username
- `password`: Your password

**Example Request:**

```
curl -X POST "{base_url}/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=your_username&password=your_password"
```

**Example Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Use this access token in the `Authorization` header for other API requests that require authentication.

## User Management

### Register a New User

**Endpoint:** `POST {base_url}/api/register`

**Request Body:**

```json
{
  "username": "new_user",
  "email": "user@example.com",
  "password": "secure_password",
  "role": "student"
}
```

**Example Request:**

```
curl -X POST "{base_url}/api/register" \
     -H "Content-Type: application/json" \
     -d '{"username": "new_user", "email": "user@example.com", "password": "secure_password", "role": "student"}'
```

### Get All Users

**Endpoint:** `GET {base_url}/api/users/`

**Query Parameters:**

- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

**Example Request:**

```
curl -X GET "{base_url}/api/users/?skip=0&limit=10" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Get User by ID

**Endpoint:** `GET {base_url}/api/users/{user_id}`

**Example Request:**

```
curl -X GET "{base_url}/api/users/1" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Update User

**Endpoint:** `PUT {base_url}/api/users/{user_id}`

**Request Body:**

```json
{
  "username": "updated_username",
  "email": "updated_email@example.com",
  "password": "new_password",
  "role": "lecturer"
}
```

**Example Request:**

```
curl -X PUT "{base_url}/api/users/1" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"username": "updated_username", "email": "updated_email@example.com", "password": "new_password", "role": "lecturer"}'
```

### Delete User

**Endpoint:** `DELETE {base_url}/api/users/{user_id}`

**Example Request:**

```
curl -X DELETE "{base_url}/api/users/1" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Get Current User

**Endpoint:** `GET {base_url}/api/users/me`

**Example Request:**

```
curl -X GET "{base_url}/api/users/me" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Course Management

### Create a Course

**Endpoint:** `POST {base_url}/api/courses/`

**Request Body:**

```json
{
  "name": "Introduction to Computer Science",
  "description": "A beginner-friendly course covering the basics of computer science."
}
```

**Example Request:**

```
curl -X POST "{base_url}/api/courses/" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "Introduction to Computer Science", "description": "A beginner-friendly course covering the basics of computer science."}'
```

### Get All Courses

**Endpoint:** `GET {base_url}/api/courses/`

**Query Parameters:**

- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

**Example Request:**

```
curl -X GET "{base_url}/api/courses/?skip=0&limit=10" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Get Course by ID

**Endpoint:** `GET {base_url}/api/courses/{course_id}`

**Example Request:**

```
curl -X GET "{base_url}/api/courses/1" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Update Course

**Endpoint:** `PUT {base_url}/api/courses/{course_id}`

**Request Body:**

```json
{
  "name": "Updated Course Name",
  "description": "Updated course description."
}
```

**Example Request:**

```
curl -X PUT "{base_url}/api/courses/1" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "Updated Course Name", "description": "Updated course description."}'
```

### Delete Course

**Endpoint:** `DELETE {base_url}/api/courses/{course_id}`

**Example Request:**

```
curl -X DELETE "{base_url}/api/courses/1" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Enroll in a Course

**Endpoint:** `POST {base_url}/api/courses/{course_id}/enroll`

**Example Request:**

```
curl -X POST "{base_url}/api/courses/1/enroll" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Unenroll from a Course

**Endpoint:** `POST {base_url}/api/courses/{course_id}/unenroll`

**Example Request:**

```
curl -X POST "{base_url}/api/courses/1/unenroll" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Chat Functionality

### Create a Chat Message

**Endpoint:** `POST {base_url}/api/chat/`

**Request Body:**

```json
{
  "message": "What are the main topics covered in this course?",
  "course_id": 1
}
```

**Example Request:**

```
curl -X POST "{base_url}/api/chat/" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"message": "What are the main topics covered in this course?", "course_id": 1}'
```

### Get Chat Messages for a Course

**Endpoint:** `GET {base_url}/api/chat/{course_id}`

**Query Parameters:**

- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

**Example Request:**

```
curl -X GET "{base_url}/api/chat/1?skip=0&limit=20" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Get Specific Chat Message

**Endpoint:** `GET {base_url}/api/chat/message/{message_id}`

**Example Request:**

```
curl -X GET "{base_url}/api/chat/message/1" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Feedback System

### Create Feedback

**Endpoint:** `POST {base_url}/api/feedback/`

**Request Body:**

```json
{
  "content": "The response was very helpful and clear.",
  "rating": 5,
  "chat_message_id": 1
}
```

**Example Request:**

```
curl -X POST "{base_url}/api/feedback/" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"content": "The response was very helpful and clear.", "rating": 5, "chat_message_id": 1}'
```

### Get Feedback for a Chat Message

**Endpoint:** `GET {base_url}/api/feedback/{chat_message_id}`

**Example Request:**

```
curl -X GET "{base_url}/api/feedback/1" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Admin Functions

### Create an Admin User

**Endpoint:** `POST {base_url}/api/admin/`

**Request Body:**

```json
{
  "username": "admin_user",
  "email": "admin@example.com",
  "password": "secure_admin_password",
  "role": "admin",
  "is_admin": true
}
```

**Example Request:**

```
curl -X POST "{base_url}/api/admin/" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"username": "admin_user", "email": "admin@example.com", "password": "secure_admin_password", "role": "admin", "is_admin": true}'
```

### Get All Admin Users

**Endpoint:** `GET {base_url}/api/admin/`

**Query Parameters:**

- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

**Example Request:**

```
curl -X GET "{base_url}/api/admin/?skip=0&limit=10" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of requests. In case of validation errors or other issues, the API will return a JSON response with details about the error.

Example error response:

```json
{
  "detail": [
    {
      "loc": ["body", "username"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

Make sure to handle these errors appropriately in your client application.
