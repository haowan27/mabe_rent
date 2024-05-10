from flask import Blueprint, jsonify

todo_bp = Blueprint("todo", __name__)


@todo_bp.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify("hello")


@todo_bp.route("/api/todos", methods=["POST"])
def create_todo():
    return jsonify("create_todo")


def mod_name():
    return __name__
