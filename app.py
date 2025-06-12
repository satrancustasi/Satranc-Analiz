from flask import Flask, render_template, request
import os
from analysis import analyze_pgn

UPLOAD_FOLDER = 'uploads'
ENGINE_PATH = '/data/data/com.termux/files/home/stockfish/stockfish'  # kendi stockfish yoluna göre ayarla

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    moves = None
    if request.method == 'POST':
        file = request.files['pgn_file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            moves = analyze_pgn(filepath, engine_path=ENGINE_PATH)
    return render_template('index.html', moves=moves)

if __name__ == '__main__':
    app.run(debug=True)
