from flask import Flask, request, Response, redirect, url_for, render_template
import string, secrets

app = Flask(__name__)
sessions = {}
rsp = ''

def create_session():
    global sessions
    alphabet = string.ascii_letters + string.digits + "!#$%&'*+-.^_`|~"
    new = ''.join(secrets.choice(alphabet) for i in range(64))
    sessions = {new:'have'}
    return new

def set_response(session_value):
    response = Response(f"Your session : {session_value}")    
    response.set_cookie('sessionID', session_value)
    return response
    
@app.route('/')    
def check_session():
    session_id = request.cookies.get('sessionID')
    if session_id and session_id in sessions:
        return redirect(url_for("login"))
    else:
        session_value = create_session()
        rsp = set_response(session_value)
        rsp.headers['Location'] = url_for('login')
        return rsp, 302

@app.route('/login')
def login():
    return render_template('login.html')
            
@app.route('/login_confirm', methods=['POST'])    
def login_confirm():
    session_id = request.cookies.get('sessionID')
    id = request.form['id']
    pw = request.form['pw']
    if id == 'admin' and pw == 'admin' and session_id in sessions:
        return render_template('success.html', session_value=session_id)
    else:
        return '''
        <script>
            alert("로그인 실패");
            window.location.href = "{}";
        </script>
        '''.format(url_for('login'))

@app.route('/logout')
def logout():
    session_id = request.cookies.get("sessionID")
    if session_id and session_id in sessions:
        del sessions[session_id]
        rsp = redirect(url_for('check_session'))
        rsp.set_cookie('sessionID','', expires=0)
        return rsp
    

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)