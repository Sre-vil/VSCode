from flask import Flask, request, Response
import string, secrets

app = Flask(__name__)
sessions = {}

def create_session():
    global sessions
    alphabet = string.ascii_letters + string.digits + "!#$%&'*+-.^_`|~"
    new = ''.join(secrets.choice(alphabet) for i in range(64))
    # sessions[new] = {'have':True}
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
        print(sessions)
        return f'You have session.<br> Your session info : {session_id}'
    else:
        session_value = create_session()
        rsp = set_response(session_value)
        return rsp

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)