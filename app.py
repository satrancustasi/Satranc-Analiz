from flask import Flask, render_template, request
import os
from analysis import analyze_pgn

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['pgn']
        if file and file.filename.endswith('.pgn'):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            analysis_result = analyze_pgn(filepath)
            return render_template('index.html', result=analysis_result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
