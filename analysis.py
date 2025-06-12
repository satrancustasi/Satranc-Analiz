import chess.pgn
import chess.engine

def analyze_pgn(filepath, engine_path, depth=15):
    results = []
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)

    with open(filepath) as f:
        game = chess.pgn.read_game(f)
        board = game.board()

        for move in game.mainline_moves():
            board.push(move)
            info = engine.analyse(board, chess.engine.Limit(depth=depth))
            score = info["score"].white()  # Beyaz perspektifinden skoru alıyoruz
            if score.is_mate():
                score_str = f"Mate in {score.mate()}"
            else:
                score_str = f"{score.score() / 100:.2f}"  # Centipawn'u puana çevir

            san_move = board.san(move)
            results.append((san_move, score_str))

    engine.quit()
    return results
