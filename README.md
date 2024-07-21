
# Intelligent Health Record (IHR)

Welcome to the IHR repository! IHR is an AI-powered healthcare documentation platform designed to reduce physician burnout by automating the generation of patient history and clinical notes from doctor-patient conversations.

## Project Overview

IHR aims to alleviate physician burnout by leveraging AI to handle tedious documentation tasks, allowing physicians to focus on patient care. Features include automated documentation, drug-drug interaction alerts, and differential diagnosis support.

## Features

- **Automated Documentation:** AI transcribes and structures doctor-patient conversations into detailed clinical notes.
- **Drug-Drug Interaction Alerts:** Real-time alerts for potential adverse interactions between medications.
- **Differential Diagnosis Support:** AI-driven suggestions based on patient history and symptoms.
- **Patient History Extraction:** Integration of data from both scanned and digital records.
- **User-Friendly Interface:** Simplified and intuitive UI.

## Project Structure

```
/backend/
    app.py
    routes.py
    requirements.txt

/frontend/
    index.html
    styles.css
    scripts.js

/database/
    app.db

/static/
    css/
    js/
    images/

/templates/
    layout.html
    index.html

README.md
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Flask
- SQLite3
- Langchain or Langflow

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/IHR.git
   cd IHR
   ```

2. **Set up a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r backend/requirements.txt
   ```

4. **Set up the database:**
   ```sh
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Run the application:**
   ```sh
   flask run
   ```

6. **Open your browser:**
   ```
   http://127.0.0.1:5000/
   ```

## Challenges

- **Compute Resources:** Significant computational power required for AI models.
- **Integration:** Incorporating existing records seamlessly.
- **Data Privacy:** Ensuring patient data security.

## Contributing

1. **Fork the repository**
2. **Create a new branch:**
   ```sh
   git checkout -b feature-branch
   ```
3. **Make changes and commit:**
   ```sh
   git commit -m "Description of changes"
   ```
4. **Push to the branch:**
   ```sh
   git push origin feature-branch
   ```
5. **Create a Pull Request**

## License

A2SV Hackathon.

