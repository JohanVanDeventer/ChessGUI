import chess

STATE_ONGOING = "Game Ongoing"
STATE_WHITE_WIN = "White Wins!"
STATE_BLACK_WIN = "Black Wins!"
STATE_STALEMATE = "Draw: Stalemate"
STATE_3_FOLD_REPETITION = "Draw: 3 Fold Repetition"
STATE_50_MOVE_DRAW = "Draw: 50 Move Rule"
STATE_INSUFFICIENT_MATERIAL = "Draw: Insufficient Material"


# create a new board to play moves on
class Board:
    def __init__(self, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.board = chess.Board(fen)

    def play_move(self, uci_move):
        move = chess.Move.from_uci(uci_move)
        self.board.push(move)

    def undo(self):
        self.board.pop()

    def get_piece_type_on_sq(self, sq):
        return self.board.piece_at(sq)

    def get_game_state(self):

        if self.board.is_game_over(claim_draw=True):

            if self.board.is_checkmate():
                if self.board.turn:
                    return STATE_BLACK_WIN
                else:
                    return STATE_WHITE_WIN

            if self.board.can_claim_threefold_repetition():
                return STATE_3_FOLD_REPETITION

            if self.board.is_stalemate():
                return STATE_STALEMATE

            if self.board.is_insufficient_material():
                return STATE_INSUFFICIENT_MATERIAL

            if self.board.is_fifty_moves():
                return STATE_50_MOVE_DRAW

        return STATE_ONGOING
