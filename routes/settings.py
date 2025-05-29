# routes/settings.py
from flask import Blueprint, render_template, request, jsonify, url_for

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/settings/profile')
def profile():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/settings/profile_content.html')
        return jsonify({'title': 'Profile', 'content': html, 'scripts': []})
    return render_template('settings/profile.html')

@settings_bp.route('/settings/profile/billing')
def billing():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/settings/billing_content.html')
        return jsonify({'title': 'Billing', 'content': html, 'scripts': []})
    return render_template('settings/billing.html')

@settings_bp.route('/settings/profile/security')
def security():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/settings/security_content.html')
        return jsonify({'title': 'Security', 'content': html, 'scripts': []})
    return render_template('settings/security.html')

@settings_bp.route('/settings/profile/notifications')
def notifications():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/settings/notifications_content.html')
        scripts = [
            "https://cdnjs.cloudflare.com/ajax/libs/feather-icons/4.29.0/feather.min.js",
            url_for('static', filename='css/styles.css')
        ]
        return jsonify({'title': 'Notifications', 'content': html, 'scripts': scripts})
    return render_template('settings/notifications.html')


@settings_bp.route('/settings/profile/activity_log')
def activity_log():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/settings/activity_log_content.html')
        scripts = [

        ]
        return jsonify({'title': 'Activity Log', 'content': html, 'scripts': scripts})
    return render_template('settings/activity-log.html')

@settings_bp.route('/settings/settings')
def settings():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/settings/settings_content.html')
        scripts = [

        ]
        return jsonify({'title': 'Activity Log', 'content': html, 'scripts': scripts})
    return render_template('settings/settings.html')