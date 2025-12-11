https://flask.palletsprojects.com/en/stable/

Step 1: Install Python
Check version: python --version

Step 2: Create a Virtual Environment(use cmd command)

python3 -m venv .venv
source .venv/Scripts/activate


Step 3: 
Install Flask:
pip install Flask

Check installation:
pip show flask

Step 4: Create a Simple Flask App
app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! 🚀"

if __name__ == '__main__':
    app.run(debug=True)

#If have not install flask, then use this code.
Run it: (use cmd command)
python3 -m venv .venv
source .venv/Scripts/activate
pip install Flask
python app.py


#If have install flask, then use this code.
source .venv/Scripts/activate
python app.py

