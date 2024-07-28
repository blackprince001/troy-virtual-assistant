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

[Documentation Markdown](troy-api-documentation.md)

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
