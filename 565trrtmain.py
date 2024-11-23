from flask import Flask, render_template_string
import random
import string

app = Flask(__name__)

length = 12  # Длина пароля

@app.route("/")
def index():
    return '<a href="/generate_password">Генератор паролей<a/>'

@app.route("/generate_password/")
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
 
app.run(debug=True)
