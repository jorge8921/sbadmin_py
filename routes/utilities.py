# routes/utilities.py
from flask import Blueprint, render_template, request, jsonify

utilities_bp = Blueprint('utilities', __name__)

@utilities_bp.route('/utilities/colors')
def colors():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('utilities/colors.html')
        return jsonify({'title': 'Colors', 'content': html})
    return render_template('layout/base.html')

@utilities_bp.route('/utilities/borders')
def borders():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('utilities/borders.html')
        return jsonify({'title': 'Borders', 'content': html})
    return render_template('layout/base.html')

@utilities_bp.route('/utilities/animations')
def animations():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('utilities/animations.html')
        return jsonify({'title': 'Animations', 'content': html})
    return render_template('layout/base.html')

@utilities_bp.route('/utilities/other')
def other():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('utilities/other.html')
        return jsonify({'title': 'Other', 'content': html})
    return render_template('layout/base.html')
