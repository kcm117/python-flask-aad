

```
# Create Python Environment in root
py -3.7 -m venv venv

# Activate virtual env
venv\Scripts\activate

# Update Pip
python -m pip install --upgrade pip

# Install Flask and Flask-Dance
pip install -r requirements.txt


# For Local Testing
set FLASK_APP=app.py & set FLASK_DEBUG=1 & set OAUTHLIB_INSECURE_TRANSPORT=1 & python -m flask run

```