from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__, template_folder="../templates")
app.config["SECRET_KEY"] = "your_secret_key"


# 创建登录表单
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# 定义路由
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)

        # 在这里处理登录逻辑，这里只是简单的重定向到首页
        return redirect(url_for("index"))
    return render_template("static/login.html", form=form)


@app.route("/")
def index():
    return str(app.template_folder)


if __name__ == "__main__":
    app.run(debug=True)
