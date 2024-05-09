from flask import Flask
import yaml

app = Flask(__name__)

def load_config():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    app.config.update(config)

if __name__ == '__main__':
    load_config()
    app.run()