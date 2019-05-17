from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
import os

# http://flask.pocoo.org/snippets/35/
# http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/#proxy-setups
# https://docs.microsoft.com/en-us/azure/app-service/containers/how-to-configure-python#detect-https-session
# https://flask-dance.readthedocs.io/en/v1.2.0/proxies.html
# https://werkzeug.palletsprojects.com/en/0.15.x/middleware/proxy_fix/#module-werkzeug.middleware.proxy_fix

app = Flask(__name__)

# App Proxy
app.wsgi_app = ProxyFix(app.wsgi_app,x_for=1,x_proto=1,x_host=1,x_port=1,x_prefix=1) # Had to set these numbers to make auth work in Linux App Service!!!!

# App Secret
app.secret_key = 'SUPER_SECRET_KEY'

# App Config
app.config['AZURE_OAUTH_CLIENT_ID'] = os.environ['AAD_CLIENTID']
app.config['AZURE_OAUTH_CLIENT_SECRET'] = os.environ['AAD_CLIENTSECRET']
# app.config['PREFERRED_URL_SCHEME'] = 'https'