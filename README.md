# TROY Virtual Teaching Assistant

TROY is a web-based virtual teaching assistant that facilitates interactive learning for students in specific courses. It leverages natural language processing to provide personalized responses to student queries, enhance learning experiences, and support academic interactions.

## Features

- User Authentication and Management
- Course Selection and Navigation
- Interactive Chatbot for Learning
- Interaction History Management
- Lecturer Dashboard
- Administrative Controls

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up your .env file with necessary configurations
6. Initialize the database: `alembic upgrade head`
7. Run the application: `uvicorn app.main:app --reload`

## API Documentation

# TROY Virtual Teaching Assistant API Documentation

## Introduction

The TROY Virtual Teaching Assistant is a web-based platform that facilitates interactive learning for students in specific courses. This API documentation outlines how students, lecturers, and administrators can interact with the system.

## Base URL

All API requests should be prefixed with: `https://domain_name/api`

## Authentication

All API endpoints (except registration and login) require authentication using JWT tokens. Include the token in the Authorization header:

```
Authorization: Bearer <your_access_token>
```

## User Roles

1. Student
2. Lecturer
3. Administrator

## Endpoints

### 1. Authentication

#### Register a new user

- **POST** `/register`
- **Body**:

  ```json
  {
    "username": "string",
    "email": "user@example.com",
    "password": "string",
    "role": "student" | "lecturer"
  }
  ```

- **Response**: User object with JWT token

#### Login

- **POST** `/token`
- **Body**:

  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

- **Response**: JWT access token

### 2. User Management (Admin only)

#### Get all users

- **GET** `/users`
- **Response**: List of user objects

#### Get user by ID

- **GET** `/users/{user_id}`
- **Response**: User object

#### Update user

- **PUT** `/users/{user_id}`
- **Body**: User update object
- **Response**: Updated user object

#### Delete user

- **DELETE** `/users/{user_id}`
- **Response**: Deleted user object

### 3. Course Management

#### Create a new course (Lecturers only)

- **POST** `/courses`
- **Body**:

  ```json
  {
    "name": "string",
    "description": "string"
  }
  ```

- **Response**: Course object

#### Get all courses

- **GET** `/courses`
- **Response**: List of course objects

#### Get course by ID

- **GET** `/courses/{course_id}`
- **Response**: Course object with enrollment information

#### Update course (Lecturer who created the course only)

- **PUT** `/courses/{course_id}`
- **Body**: Course update object
- **Response**: Updated course object

#### Delete course (Lecturer who created the course only)

- **DELETE** `/courses/{course_id}`
- **Response**: Deleted course object

#### Enroll in a course (Students only)

- **POST** `/courses/{course_id}/enroll`
- **Response**: Updated course object with enrollment information

#### Unenroll from a course (Students only)

- **POST** `/courses/{course_id}/unenroll`
- **Response**: Updated course object with enrollment information

### 4. Chat Interaction

#### Create a new chat message

- **POST** `/chat`
- **Body**:

  ```json
  {
    "message": "string",
    "course_id": integer
  }
  ```

- **Response**: Chat message object with AI response

#### Get chat messages for a course

- **GET** `/chat/{course_id}`
- **Query Parameters**:
  - `skip`: integer (default: 0)
  - `limit`: integer (default: 100)
- **Response**: List of chat message objects

#### Get a specific chat message

- **GET** `/chat/message/{message_id}`
- **Response**: Chat message object

## Usage Scenarios

### For Students

1. Register for an account using the `/register` endpoint.
2. Log in using the `/token` endpoint to receive a JWT token.
3. View available courses using the GET `/courses` endpoint.
4. Enroll in a course using the POST `/courses/{course_id}/enroll` endpoint.
5. Interact with the AI teaching assistant by sending messages using the POST `/chat` endpoint.
6. View chat history for a course using the GET `/chat/{course_id}` endpoint.

### For Lecturers

1. Register for an account as a lecturer using the `/register` endpoint.
2. Log in using the `/token` endpoint to receive a JWT token.
3. Create new courses using the POST `/courses` endpoint.
4. Update or delete their courses using the PUT or DELETE `/courses/{course_id}` endpoints.
5. View chat interactions of students in their courses using the GET `/chat/{course_id}` endpoint.

### For Administrators

1. Log in using the `/token` endpoint (admin accounts are typically pre-created).
2. Manage user accounts using the various `/users` endpoints.
3. View all courses and their enrollments using the GET `/courses` and GET `/courses/{course_id}` endpoints.
4. Monitor system usage and interactions across all courses.

## Error Handling

The API uses conventional HTTP response codes to indicate the success or failure of requests. Codes in the 2xx range indicate success, codes in the 4xx range indicate an error that failed given the information provided, and codes in the 5xx range indicate an error with the server.

Common error codes:

- 400 Bad Request: The request was unacceptable, often due to missing a required parameter.
- 401 Unauthorized: No valid API key provided.
- 403 Forbidden: The API key doesn't have permissions to perform the request.
- 404 Not Found: The requested resource doesn't exist.
- 429 Too Many Requests: Too many requests hit the API too quickly.
- 500, 502, 503, 504 Server Errors: Something went wrong on the server side.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
