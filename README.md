# Flask Dynamic SPA Template

This repository provides a simple structure for building a Single Page Application (SPA) with Flask using HTML templates, Bootstrap, and JavaScript `fetch()` for dynamic content loading without full-page reloads.

## 🚀 Features

- Flask routing with AJAX and full-page support.
- Templates organized by sections: dashboard, components, utilities, settings, etc.
- Dynamic content loading using `fetch()` + JSON.
- Responsive design using Bootstrap (based on SB Admin 2 template).
- Modular HTML templates using `partials/` and `layout/` folders.
- Custom 404 error view.

## 🧱 Project Structure

templates/
├── layout/
│ └── base.html # Main layout file
├── partials/
│ ├── dashboard_content.html # Dashboard content (AJAX)
│ └── pages/
│ └── other/
│ └── 404_content.html # Partial for error 404 page
├── pages/
│ └── other/
│ └── error-404.html # Full error 404 page
├── utilities/
│ ├── colors.html
│ ├── borders.html
│ ├── animations.html
│ └── other.html
├── components/
│ ├── buttons.html
│ └── cards.html
├── settings/
│ ├── profile.html
│ ├── billing.html
│ ├── security.html
│ └── notifications.html
├── charts.html
├── dashboard.html
├── tables.html
└── welcome.html


## 📦 Dependencies

- Python 3.10+
- Flask
- Bootstrap 4/5
- jQuery (optional for Bootstrap plugins)
- Chart.js (for chart examples)
- Feather Icons (optional)

## 🔧 Running the App

1. Clone the repo:
# git clone https://github.com/jorge8921/sbadmin_py.git
# cd sbadmin_py


Create a virtual environment:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

Install dependencies:
pip install flask

Run the app:
python main.py
Visit http://127.0.0.1:5000

🔄 Dynamic Routing Logic
Each route checks if the request is made via AJAX (X-Requested-With: XMLHttpRequest). If so, it returns a JSON response with HTML content and optional scripts. Otherwise, it loads a full HTML layout.

Example:

@app.route('/dashboard')
def dashboard():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/dashboard_content.html')
        return jsonify({'title': 'Dashboard', 'content': html})
    else:
        return render_template('dashboard.html')
❌ Custom Error Pages
You can define custom error handlers in the main.py:

@app.errorhandler(404)
def not_found(e):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_template('partials/pages/other/404_content.html')
        return jsonify({'title': '404 Not Found', 'content': html}), 404
    return render_template('pages/other/error-404.html'), 404

📁 Modular Routes
You can move your routes into Blueprints for better structure (e.g., dashboard_bp, settings_bp, etc.), and register them in the main app.

📄 License
This project is open-source and free to use under the MIT License.
