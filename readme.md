

```
# Create Python Environment in root
py -3.7 -m venv venv

# Activate virtual env
venv\Scripts\activate

# Install Flask and Flask-Dance
pip install Flask Flask-Dance

set FLASK_APP=app.py & set FLASK_DEBUG=1 & python -m flask run

```