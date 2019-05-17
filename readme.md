

# Python-Flask-AAD

This solution demonstrates deploying a Python 3.7 Flask application to a Linux Azure App Service, with Azure Active Directory authentication.

For initial setup, run the following code in the directory where you cloned the repo:

```
# Create Python Environment in root
py -3.7 -m venv venv

# Activate virtual env
venv\Scripts\activate

# Update Pip
python -m pip install --upgrade pip

# Install Flask and Flask-Dance
pip install -r requirements.txt

# Run for local testing
set FLASK_APP=app.py & set FLASK_DEBUG=1 & set OAUTHLIB_INSECURE_TRANSPORT=1 & python -m flask run
```