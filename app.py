from flask import Flask, render_template, request
import os
from analysis import analyze_pgn

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ENGINE_PATH = "/data/data/com.termux/files/home/stockfish-android-armv8"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['pgn']
        if file and file.filename.endswith('.pgn'):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            # analyze_pgn fonksiyonuna engine_path parametresi eklenmiş varsayımıyla
            analysis_result = analyze_pgn(filepath, engine_path=ENGINE_PATH)
            return render_template('index.html', result=analysis_result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
