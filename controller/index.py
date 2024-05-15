from flask import Blueprint, redirect, url_for


bp = Blueprint("Index", __name__)


@bp.route("/", methods=["GET"])
def Redir():
    return redirect(url_for("admin.Home"))
