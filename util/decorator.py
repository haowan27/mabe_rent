from functools import wraps
from flask import session, redirect, url_for


# 自定义装饰器，用于验证用户登录状态
def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        # 检查 session 中是否存在用户名
        if "username" not in session:
            # 如果用户未登录，则重定向到登录页面
            return redirect(url_for("login"))
        # 如果用户已登录，则调用原始的视图函数
        return view(*args, **kwargs)

    return wrapped_view
