from sunshine import app

@app.route('/')
@app.route('/index')
def index():
    return "o shit waddupp!!!!"