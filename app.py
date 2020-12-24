# Developer: Abdullah Rehmat
# Import Modules Here
import os
import time
import webview
import os.path
import multiprocessing
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from flask_mde import Mde, MdeField
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired, DataRequired, Length
from flask import Flask, request, render_template, flash, session, url_for


app = Flask(__name__)
load_dotenv()
mde = Mde(app)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY")

windowTitle = os.environ.get("WINDOW_TITLE")
fileDirPath = os.environ.get("FILE_DIRECTORY")


def error_flasher(form):
    for field, message_list in form.errors.items():
        for message in message_list:
            flash(form[field].label.text + ': ' + message, 'error')
    print(message, message_list)


def fileHandler(form):
    savePath = os.path.join(fileDirPath, form.title.data)
    f = open(savePath, "w+")
    f.write(form.editor.data)
    f.close()


def contentLoader(form):
    savePath = os.path.join(fileDirPath, form.title.data)
    fileName = savePath
    f = open(fileName, "r")
    return f.read()


def startFlaskServer():
    app.run(debug=True)


def startWebview():
    webview.create_window(windowTitle, 'http://localhost:5000')
    webview.start()


class MdeForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])

    editor = MdeField(
        validators=[
            #InputRequired("Input required"),
            Length(min=0, max=30000)
        ]
    )
    submit = SubmitField()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MdeForm()

    if form.validate_on_submit() and form.editor.data == "":
        form.editor.data = contentLoader(form)

    elif form.validate_on_submit() and form.editor.data != "":
        session['editor'] = request.form['editor']
        fileHandler(form)
        form.title.data = ""
        form.editor.data = ""

    return render_template("index.html", form=form, windowTitle=windowTitle)


if __name__ == "__main__":

    p1 = multiprocessing.Process(target=startFlaskServer)
    p2 = multiprocessing.Process(target=startWebview)

    p1.start()
    time.sleep(2)
    p2.start()
    p2.join()
    p1.terminate()
