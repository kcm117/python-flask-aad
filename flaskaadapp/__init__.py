from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
import os

# http://flask.pocoo.org/snippets/35/
# http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/#proxy-setups

app = Flask(__name__)

# App Proxy
app.wsgi_app = ProxyFix(app.wsgi_app)

# App Secret
app.secret_key = 'SUPER_SECRET_KEY'

# App Config
app.config['AZURE_OAUTH_CLIENT_ID'] = os.environ['AAD_CLIENTID']
app.config['AZURE_OAUTH_CLIENT_SECRET'] = os.environ['AAD_CLIENTSECRET']
app.config['PREFERRED_URL_SCHEME'] = 'https'