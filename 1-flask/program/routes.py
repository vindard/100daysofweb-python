from program import app

@app.route('/')
@app.route('/index')
def index():
    return "Hellow Pythonistas"

