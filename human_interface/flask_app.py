import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from flask import Flask, request, render_template_string
from ai_writer.writer import spin_content
from ai_writer.reviewer import review_content

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>AI Book Editor</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow-lg border-0">
            <div class="card-header bg-primary text-white">
                <h4 class="mb-0">📘 AI-Powered Book Editor</h4>
            </div>
            <div class="card-body">
                <form method="POST">
                    <div class="mb-3">
                        <label for="content" class="form-label">Chapter Content</label>
                        <textarea name="content" class="form-control" id="content" rows="12" placeholder="Paste your chapter content here...">{{ content }}</textarea>
                    </div>
                    <div class="d-flex justify-content-between">
                        <button type="submit" name="action" value="Spin" class="btn btn-success px-4">✍️ Spin</button>
                        <button type="submit" name="action" value="Review" class="btn btn-info px-4">🔍 Review</button>
                    </div>
                </form>
                {% if result %}
                    <hr>
                    <h5 class="mt-4">📝 AI Output</h5>
                    <pre class="bg-dark text-white p-3 rounded">{{ result }}</pre>
                {% endif %}
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    content = ""
    if request.method == 'POST':
        content = request.form['content']
        action = request.form['action']
        if action == 'Spin':
            result = spin_content(content)
        elif action == 'Review':
            result = review_content(content)
    return render_template_string(HTML_TEMPLATE, result=result, content=content)

if __name__ == '__main__':
    app.run(debug=True)

