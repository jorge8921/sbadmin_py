# routes/general.py
from flask import Blueprint, render_template, request, jsonify, url_for

general_bp = Blueprint('general', __name__)

@general_bp.route('/charts')
def charts():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('/charts.html')
        return jsonify({'title': 'Charts', 'content': html})
    return render_template('charts.html')

@general_bp.route('/tables')
def tables():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('/tables.html')
        return jsonify({'title': 'Tables', 'content': html})
    return render_template('tables.html')