from flask import Flask
from controller import admin, index
from extention.admin import InitAdmin

import yaml

app = Flask(__name__)
app.register_blueprint(admin.bp)
app.register_blueprint(index.bp)


def load_config():
    with open("config.yml", "r") as file:
        config = yaml.safe_load(file)
    app.config.update(config)


def load_debug_config():
    with open("debug-config.yml", "r") as file:
        config = yaml.safe_load(file)
    app.config.update(config)


if __name__ == "__main__":
    load_config()
    InitAdmin(app)
    app.run()
else:
    load_config()
