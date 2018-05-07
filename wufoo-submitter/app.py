from chalice import Chalice

app = Chalice(app_name='wufoo-submitter')

@app.route('/')
def index():
    return ''

