# FastAPI Based Full Stack Application

## Overview

This project is a simple full-stack application built using FastAPI. It allows users to select an animal and view its image, as well as upload files to the server. The application serves static files (HTML, CSS, JS) and handles file uploads.

## Features

- Select an animal (Cat, Dog, Elephant) to view its image.
- Upload files to the server.
- Display uploaded file information (name, size, type).

## Project Structure
fullstack-fastapi-basic/
│
├── main.py # Main application file
├── pyproject.toml # Project dependencies and metadata
└── static/ # Directory for static files
├── index.html # Main HTML file
├── script.js # JavaScript for handling user interactions
└── styles.css # CSS styles

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd fullstack-fastapi-basic
   ```

2. Create a virtual environment:
   
   ```bash
   uv sync
   uv .venc/bin/activate
   ```

## Running the Application

To run the application, execute the following command:

uvicorn main:app --host 0.0.0.0 --port 8000

You can then access the application in your web browser at `http://localhost:8000`.

## Usage

1. **Select an Animal**: Choose an animal from the radio buttons to view its image.
2. **Upload a File**: Select a file using the file input and click the "Upload" button. The file information will be displayed after a successful upload.

## Dependencies

- FastAPI: `0.115.3`
- Uvicorn: `0.32.0`
- Python Multipart: `0.0.12`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.