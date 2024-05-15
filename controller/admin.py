from flask import Blueprint, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from util.decorator import login_required

bp = Blueprint(
    "admin", __name__, url_prefix="/admin", template_folder="../templates/static"
)
identity = {"username": "admin", "password": "admin"}


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


@bp.route("/hello", methods=["GET"])
@login_required
def Hello():
    return str(bp.template_folder)


@bp.route("/login", methods=["GET", "POST"])
def Login():
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template("login.html", form=form)
    if not (
        form.username.data == identity["username"]
        and form.password.data == identity["username"]
    ):
        return render_template("login.html", error="账号或密码错误", form=form)
    session["username"] = form.username.data
    return redirect(url_for("admin.index"))


@bp.route("/home", methods=["GET"])
def Home():
    return render_template("home.html")


@bp.route("/about", methods=["GET"])
def About():
    return render_template("about.html")
