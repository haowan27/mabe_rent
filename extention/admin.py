from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()


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


def InitAdmin(app):
    # 这一步完成之后会添加一个名为flask-admin的蓝图，具体没研究，当黑盒用
    flask_admin = Admin(
        app,
        name="RentAdmin",
        template_mode="bootstrap3",
        index_view=AdminIndexView(
            url="/extention/admin", template="admin/home.html", endpoint="flask-admin"
        ),
    )
    db = SQLAlchemy(app)
    flask_admin.add_view(ModelView(RentExpect, db.session))
    flask_admin.add_view(ModelView(RentCustomer, db.session))
    flask_admin.add_view(ModelView(RentHouse, db.session))
    flask_admin.add_view(ModelView(RentRequest, db.session))


# def initTable():
#     with app.app_context():
#         inspector = db.inspect(db.engine)
#         if not inspector.has_table("rent_expect"):
#             db.create_all()
