from flask import Flask
from routes import todo_bp
from login import login_bp

app = Flask(__name__)
app.secret_key = "luyiguo"
app.register_blueprint(todo_bp)
app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(port=9999,debug=True)