from flask import Blueprint,session,request,redirect,url_for

login_bp = Blueprint("login",__name__)

@login_bp.route('/')
def indexPage():
    if 'username' in session:
        return f'Logged in as {session["username"]}<br><a href="/logout">Logout</a>'
    return 'You are not logged in<br><a href="/login">Login</a>'

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('login.indexPage'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@login_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.indexPage'))