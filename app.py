# set FLASK_APP=app.py & set FLASK_DEBUG=1 & python -m flask run
from flaskaadapp import app
from flaskaadapp.forms import Form1
from flask import redirect, url_for, render_template, request, flash
from flask_dance.contrib.azure import make_azure_blueprint, azure
import os

blueprint = make_azure_blueprint(
    tenant= os.environ['AAD_TENANT'] # Store your tenant name in an environment variable called "AAD_TENANT", e.g value: 'microsoft.onmicrosoft.com'
)
app.register_blueprint(blueprint, url_prefix="/login")

# https://flask-dance.readthedocs.io/en/latest/providers.html#module-flask_dance.contrib.azure
# https://flask-dance.readthedocs.io/en/v1.2.0/quickstarts/azure.html

@app.route('/')
def home():
    if not azure.authorized:
        return redirect(url_for("azure.login"))
    resp = azure.get("/v1.0/me")
    assert resp.ok

    display_text = resp.json()
    # return "You are {mail} on Azure AD".format(mail=resp.json()["userPrincipalName"])
    return render_template('home.html', data=display_text, azure=azure)

@app.route('/form1', methods=['GET','POST'])
def form1():
    if not azure.authorized:
        return redirect(url_for("azure.login"))
    resp = azure.get("/v1.0/me")
    assert resp.ok
    
    form = Form1()
    
    if form.validate_on_submit():   
        parameter1 = form.parameter1.data
        parameter2 = form.parameter2.data

        flash("Thanks for filling out the form!")
        print(parameter1,parameter2)

        return render_template('form1.html', form=form,azure=azure)

    return render_template('form1.html', form=form,azure=azure)
