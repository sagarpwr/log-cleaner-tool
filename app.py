import os
from flask import Flask, render_template, request
import re
import json



app = Flask(__name__)


app = Flask(__name__)

def clean_log_text(raw_log):
    # Step 1: Cleaning
    cleaned = raw_log.replace('“', '"').replace('”', '"').replace('’', "'")
    cleaned = cleaned.replace("{[\\n]”|", "").replace("[\\n]”|", "")
    cleaned = cleaned.replace("\\n", "").replace("\n", "").replace("{", "").replace("}", "")
    cleaned = re.sub(r'\s+', ' ', cleaned)  # replace multiple spaces/newlines into single space
    return cleaned

def extract_key_value_pairs(cleaned_log):
    # Step 2: Extract key-value pairs
    extracted = {}

    matches = re.findall(r'"\s*(\w+)"\s*:\s*"([^"]+)"', cleaned_log)

    for key, value in matches:
        extracted[key.strip()] = value.strip()

    return {"body": extracted}


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        log_data = request.form.get("log")
        # Process log_data here (you can clean the logs here)
        result = log_data  # Modify this as needed to clean the log
    return render_template("index.html", result=result)

if __name__ == "__main__":
    # Use the environment variable PORT for the port, or default to 5000 locally
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 for local development
    app.run(host="0.0.0.0", port=port)  # Bind to all available interfaces
