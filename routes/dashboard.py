# routes/dashboard.py
from flask import Blueprint, render_template, request, jsonify, url_for

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/dashboard_content.html')
        scripts = [
            url_for('static', filename='vendor/chart.js/Chart.min.js'),
            url_for('static', filename='js/demo/chart-area-demo.js'),
            url_for('static', filename='js/demo/chart-pie-demo.js')
        ]
        return jsonify({
            'title': 'Dashboard',
            'content': html,
            'scripts': scripts
        })
    else:
        return render_template('dashboard.html')