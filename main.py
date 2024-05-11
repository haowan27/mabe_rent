from flask import Flask
from controller import admin
import yaml

app = Flask(__name__)
app.register_blueprint(admin.bp)


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
    app.run()
else:
    load_config()
