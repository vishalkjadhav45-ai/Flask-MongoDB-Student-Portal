# Flask & MongoDB Student Submission Portal

A lightweight web application built using **Python Flask** and **MongoDB** that allows users to submit student information through a web form and store the submitted records in a MongoDB database.

The project demonstrates backend development, database integration, REST-style JSON data handling, and containerized database deployment using Docker.

## Overview

The application provides a simple interface where users can enter their details and submit them through a form. Flask processes the request, validates the submitted fields, and stores the information in MongoDB using PyMongo.

It also exposes a JSON API endpoint that reads and returns data from a local JSON file.

## Key Features

- **Student Submission Form:** Accepts name, email, and message from users.
- **MongoDB Integration:** Stores submitted records in a MongoDB collection using PyMongo.
- **Form Validation:** Checks that all required fields are provided.
- **Success Page:** Redirects users to a confirmation page after successful submission.
- **Error Handling:** Displays an error message when submission or database insertion fails.
- **JSON API:** Provides data from a local JSON file through the `/api` endpoint.
- **Docker Support:** Includes Docker configuration for containerizing the application and supporting database deployment.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Flask | Web application framework |
| MongoDB | NoSQL database |
| PyMongo | Python-MongoDB connectivity |
| HTML | Frontend structure |
| CSS | Frontend styling |
| Docker | Containerization |
| Linux / Amazon EC2 | Development and deployment environment |

## Application Architecture

```text
                  User / Browser
                        |
                        v
                Flask Web Application
                        |
             +----------+----------+
             |          |          |
             v          v          v
          Home Page   Form       /api
                      Submit       |
                        |           v
                        v        data.json
                  Form Validation
                        |
                        v
                     PyMongo
                        |
                        v
                     MongoDB
                   (Docker)
                        |
                        v
                Submission Stored
                        |
                        v
                  Success Page
```

## Project Structure

```text
Flask-MongoDB-Student-Portal/
│
├── templates/
│   ├── index.html
│   └── success.html
│
├── app.py
├── data.json
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

### File Description

| File / Directory | Description |
|---|---|
| `app.py` | Main Flask application and backend routes |
| `templates/` | HTML templates for the web interface |
| `index.html` | Student submission form |
| `success.html` | Submission confirmation page |
| `data.json` | JSON data served through the API |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Instructions to build the Flask application image |
| `.dockerignore` | Excludes unnecessary files from Docker build context |
| `.gitignore` | Excludes environment files and unnecessary files from Git |

## Application Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Displays the student submission form |
| `/submit` | POST | Processes form data and inserts it into MongoDB |
| `/success` | GET | Displays the successful submission page |
| `/api` | GET | Returns JSON data from `data.json` |

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vishalkjadhav45-ai/Flask-MongoDB-Student-Portal.git

cd Flask-MongoDB-Student-Portal
```

### 2. Create a Python Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
MONGO_URI=mongodb://127.0.0.1:27017
DB_NAME=FlaskDB
COLLECTION_NAME=submissions
```

Update `MONGO_URI` according to your MongoDB deployment and network configuration.

**Important:** Keep `.env` private. Never commit database credentials or other secrets to GitHub.

### 5. Start MongoDB Using Docker

Create a persistent Docker volume:

```bash
docker volume create mongodb_data
```

Run the MongoDB container:

```bash
docker run -d \
  --name mongodb \
  -p 127.0.0.1:27017:27017 \
  -v mongodb_data:/data/db \
  mongo:7
```

Verify the container:

```bash
docker ps
```

### 6. Run the Flask Application

```bash
python app.py
```

Open the application in your browser:

```text
http://YOUR_SERVER_PUBLIC_IP:5000
```

For local testing, use:

```text
http://127.0.0.1:5000
```

Ensure the Flask server is configured to listen on the appropriate network interface and that the required firewall or security group rules are in place.

## Docker Image Build

The repository also includes a Dockerfile for building the Flask application image.

Build the image:

```bash
docker build -t flask-mongodb-app:v1 .
```

Verify the image:

```bash
docker images
```

When running Flask inside a container, configure `MONGO_URI` to use a MongoDB address reachable from that container. `127.0.0.1` inside a container refers to the container itself, not a separate MongoDB container.

## API Testing

The application provides a JSON endpoint:

```text
GET /api
```

Open the following URL in a browser:

```text
http://YOUR_SERVER_PUBLIC_IP:5000/api
```

The endpoint reads the contents of `data.json` and returns the data as a JSON response.

## Database Details

| Configuration | Value |
|---|---|
| Database | `FlaskDB` |
| Collection | `submissions` |
| Database Engine | MongoDB |
| Python Driver | PyMongo |
| Container Image | `mongo:7` |
| Persistent Volume | `mongodb_data` |

Submitted records contain the following fields:

- `name`
- `email`
- `message`

## Security & Best Practices

- Environment variables are used to store database configuration.
- `.env` is excluded from version control.
- `.gitignore` prevents unnecessary files and virtual environments from being committed.
- `.dockerignore` keeps unnecessary files out of Docker build context.
- MongoDB is bound to localhost in the example Docker deployment rather than exposed publicly.
- Database credentials should never be hardcoded into source code.

## Learning Outcomes

Through this project, the following practical concepts were implemented:

- Building a backend web application using Python Flask.
- Handling HTTP GET and POST requests.
- Processing and validating HTML form submissions.
- Connecting Python applications with MongoDB.
- Performing database insert operations using PyMongo.
- Creating and consuming a JSON API endpoint.
- Running MongoDB inside a Docker container.
- Managing application dependencies and environment variables.
- Preparing and maintaining a GitHub project repository.

## Author

**Vishal Jadhav**

DevOps & Cloud Computing Enthusiast

GitHub: [vishalkjadhav45-ai](https://github.com/vishalkjadhav45-ai)

Project Repository: [Flask-MongoDB-Student-Portal](https://github.com/vishalkjadhav45-ai/Flask-MongoDB-Student-Portal)

---

*Built as a hands-on learning project to explore Flask backend development, MongoDB integration, and Docker-based deployment.*
