from flask import Flask, render_template
from routes import register_routes

app = Flask(__name__, template_folder='template')
register_routes(app)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/other/error-404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)