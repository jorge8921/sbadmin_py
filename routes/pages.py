# routes/pages.py
from flask import Blueprint, render_template, request, jsonify, url_for

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/login')
def login():
    return render_template('/pages/login.html')


@pages_bp.route('/forgot-password')
def forgot_password():
    return render_template('/pages/forgot-password.html')

@pages_bp.route('/register')
def register():
    return render_template('/pages/register.html')

@pages_bp.route('/error_404')
def error404():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/pages/other/404_content.html')
        return jsonify({'title': 'Error 404', 'content': html, 'scripts': []})
    return render_template('pages/other/error-404.html')

@pages_bp.route('/blank')
def blank():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/pages/other/blank_content.html')
        return jsonify({'title': 'Blank', 'content': html, 'scripts': []})
    return render_template('pages/other/blank.html')