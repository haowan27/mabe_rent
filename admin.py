from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
import controller.login

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/rent"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

app.register_blueprint(controller.login.bp)


class RentCustomer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(128))
    avatar_url = db.Column(db.String(512))
    wx_open_id = db.Column(db.String(256))
    wx_session_key = db.Column(db.String(256))


class RentHouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_customer = db.Column(db.Integer)
    area_size = db.Column(db.Integer)
    price = db.Column(db.Integer)
    province_code = db.Column(db.Integer)
    check_status = db.Column(db.Integer)
    house_type = db.Column(db.String(256))
    title = db.Column(db.String(128))
    location = db.Column(db.Text)
    photo_list = db.Column(db.Text)
    content = db.Column(db.Text)


class RentRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_customer = db.Column(db.Integer)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)


class RentExpect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_customer = db.Column(db.Integer)
    house_type = db.Column(db.String(256))
    price = db.Column(db.Integer)
    province_code = db.Column(db.Integer)
    location = db.Column(db.Text)
    Title = db.Column(db.String(128))
    Content = db.Column(db.Text)


##实测 这一步完成之后会添加一个名为admin的蓝图，具体没研究，当黑盒用
admin = Admin(
    app,
    name="RentAdmin",
    template_mode="bootstrap3",
    index_view=AdminIndexView(url="/", template="admin/home.html"),
)

admin.add_view(ModelView(RentExpect, db.session))
admin.add_view(ModelView(RentCustomer, db.session))
admin.add_view(ModelView(RentHouse, db.session))
admin.add_view(ModelView(RentRequest, db.session))

# def initTable():
#     with app.app_context():
#         inspector = db.inspect(db.engine)
#         if not inspector.has_table("rent_expect"):
#             db.create_all()


if __name__ == "__main__":
    # initTable()
    app.run(debug=True)
