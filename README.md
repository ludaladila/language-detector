# Language Detector

This project is a web application for detecting languages using a Flask-based backend and a dynamic front-end interface. The application utilizes `googletrans` for language detection and provides a user-friendly interface for real-time language detection. Users can input text to detect its language, view the detection history, and interact with features like light/dark mode themes.

## Live Demo

Access the live application deployed on Render: [language-detector](https://language-detector-eg92.onrender.com)

## Project Structure

```
language-detector/
├── .vscode/                     # VSCode settings (if present)
├── static/
│   └── css/
│       └── style.css            # Stylesheet for the front-end
├── templates/
│   └── index.html               # HTML template for the front-end
├── venv/                        # Virtual environment (not included, listed in .gitignore)
├── .gitignore                   # Git ignore file
├── app.py                       # Flask backend application
├── requirements.txt             # Python dependencies
```

## Setup and Installation (Local)

1. Clone the repository:
    ```bash
    git clone https://github.com/ludaladila/language-detector.git
    cd language-detector
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Access the application in your browser at `http://localhost:10000/` (or the specified port).

## Features

- **Language Detection**: Enter any text to detect the language using the `googletrans` library.
- **History Tracking**: View the history of detected languages and clear it as needed.
- **Theme Toggle**: Switch between light and dark mode themes.
- **Responsive UI**: Built with responsive design in mind using Tailwind CSS.


## File Descriptions

- **app.py**: Main Flask backend that handles routing, language detection, and session management.
- **index.html**: Front-end template with an input area for detecting languages and displaying results.
- **style.css**: Custom styles for the front-end, including theme support and UI elements.

## Usage

1. Navigate to the home page.
2. Enter the text you want to detect in the text area.
3. Click the "Detect Language" button to get the detected language and its confidence level.
4. View and manage the detection history.
5. Toggle between light and dark themes for a personalized UI experience.