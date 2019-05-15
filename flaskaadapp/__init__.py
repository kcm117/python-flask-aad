from flask import Flask

app = Flask(__name__)

app.secret_key = "SUPER_SECRET_KEY"