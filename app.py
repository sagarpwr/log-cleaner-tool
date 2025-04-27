from flask import Flask, render_template, request
import re
import json

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
        raw_log = request.form["log"]
        cleaned_log = clean_log_text(raw_log)
        cleaned_output = extract_key_value_pairs(cleaned_log)
        result = json.dumps(cleaned_output, indent=2)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
