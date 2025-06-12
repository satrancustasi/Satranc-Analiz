import chess.pgn

def analyze_pgn(filepath):
    with open(filepath) as f:
        game = chess.pgn.read_game(f)
        board = game.board()
        moves = []
        for move in game.mainline_moves():
            moves.append(board.san(move))
            board.push(move)
        return moves
