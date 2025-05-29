# routes/components.py
from flask import Blueprint, render_template, request, jsonify

components_bp = Blueprint('components', __name__)

@components_bp.route('/components/buttons')
def buttons():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/components/buttons_content.html')
        return jsonify({'title': 'Buttons', 'content': html, 'scripts': []})
    return render_template('components/buttons.html')

@components_bp.route('/components/cards')
def cards():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/components/cards_content.html')
        return jsonify({'title': 'Cards', 'content': html, 'scripts': []})
    return render_template('components/cards.html')

