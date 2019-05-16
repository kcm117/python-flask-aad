# set FLASK_APP=app.py & set FLASK_DEBUG=1 & python -m flask run
from flaskaadapp import app
from flaskaadapp.forms import Form1
from flask import redirect, url_for, render_template, request
from flask_dance.contrib.azure import make_azure_blueprint, azure
import os

blueprint = make_azure_blueprint(
    client_id=os.environ['AAD_CLIENTID'],
    client_secret=os.environ['AAD_CLIENTSECRET'],
    tenant='microsoft.onmicrosoft.com',
    redirect_to='form1'
)
app.register_blueprint(blueprint, url_prefix="/login")

# https://flask-dance.readthedocs.io/en/latest/providers.html#module-flask_dance.contrib.azure
# https://flask-dance.readthedocs.io/en/v1.2.0/quickstarts/azure.html

@app.route("/")
def home():
    if not azure.authorized:
        return redirect(url_for("azure.login",_scheme="https",_external=True))
    resp = azure.get("/v1.0/me")
    assert resp.ok

    display_text = resp.json()
    # return "You are {mail} on Azure AD".format(mail=resp.json()["userPrincipalName"])
    return render_template('home.html', data=display_text, azure=azure)

@app.route("/form1")
def form1():
    if not azure.authorized:
        return redirect(url_for("azure.login",_scheme="https",_external=True))
    resp = azure.get("/v1.0/me")
    assert resp.ok
    
    form = Form1()
    
    return render_template('form1.html', form=form,azure=azure)
