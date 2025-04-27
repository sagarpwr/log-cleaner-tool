# Log Cleaner Tool 🔧

## 🚀 Overview
The **Log Cleaner Tool** is designed to clean and normalize raw log data by **automatically removing unnecessary metadata**. It saves time by eliminating the need to manually filter out irrelevant information using tools like Postman. This is a Flask-based tool that provides a user-friendly web interface to process your log data efficiently.

### 🎯 Problem Statement
When working with log data in the office, raw logs often contain unnecessary metadata that makes processing difficult. To clean this data, users would traditionally use tools like **Postman**, manually finding and pasting the data into the tool to get key-value pairs. This is **time-consuming** and **error-prone**.

With this tool, **all of that is automated**!

### ✨ Key Features
- **Metadata Removal**: Automatically filters out irrelevant data from logs.
- **Key-Value Pair Extraction**: Converts raw logs into structured JSON format.
- **No More Postman**: Say goodbye to manually pasting and cleaning data.
- **Fast & Efficient**: Save hours of work and reduce human error.

### 🔧 Requirements

Before running the tool, make sure to install the necessary dependencies.

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/log-cleaner-tool.git
    cd log-cleaner-tool
    ```

2. Create a virtual environment (optional, but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### 🚀 How to Run the Tool

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

3. You will see the web interface where you can paste your raw log data and choose the **strip direction** (left, right, or both).

4. After submitting the form, the tool will clean the log data and return the extracted key-value pairs.

### 🛠️ Running with Docker (Optional)

You can also run this tool using Docker for easier deployment.

1. Build the Docker image:
    ```bash
    docker build -t log-cleaner-tool .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 log-cleaner-tool
    ```

3. Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

### 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💻 Code Snippets

### `app.py` (Main Flask Application)
```python
from flask import Flask, render_template, request
import re
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        result = clean_logs(text)
    return render_template("index.html", result=result)

def clean_logs(raw_logs):
    # Extract key-value pairs using regex
    pattern = r'"(\w+)":\s*"([^"]+)"'
    matches = re.findall(pattern, raw_logs)
    cleaned_data = {key: value for key, value in matches}
    return json.dumps({"body": cleaned_data}, indent=2)

if __name__ == "__main__":
    app.run(debug=True)
