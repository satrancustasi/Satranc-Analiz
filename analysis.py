import chess.pgn
import chess.engine

def analyze_pgn(filepath, engine_path=None):
    with open(filepath) as f:
        game = chess.pgn.read_game(f)
    
    board = game.board()
    moves = []

    engine = None
    if engine_path:
        engine = chess.engine.SimpleEngine.popen_uci(engine_path)

    for move in game.mainline_moves():
        san_move = board.san(move)  # önce SAN formatını al
        board.push(move)            # sonra hamleyi uygula
        move_info = {'move': san_move}

        if engine:
            info = engine.analyse(board, chess.engine.Limit(time=0.1))
            move_info['eval'] = info['score'].white().score(mate_score=10000)
        moves.append(move_info)

    if engine:
        engine.quit()

    return moves
