# User Profile Card Generator

A clean, responsive Flask web application that accepts user details via an HTTP `POST` form and dynamically renders a formatted profile card.

## Features
- **POST Request Processing:** Validates and sanitizes form inputs (`name`, `role`, `bio`, `image_url`) on the Python backend.
- **Smart Avatar Fallback:** Automatically generates a monogram avatar if no image URL is provided or if an external image fails to load.
- **Responsive UI:** Modern two-column layout with real-time card rendering.

## Tech Stack
- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3, Jinja2 Templates

## How to Run Locally
```bash
pip install flask
python app.py