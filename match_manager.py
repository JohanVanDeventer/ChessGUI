import sys
from datetime import datetime
import time

import engine
import board
import gui
import opening_book


# manages a match (multiple games) between two engines on a chess board
class MatchManager:
    def __init__(self,
                 engine_1_path, engine_2_path,
                 starting_time, increment,
                 win):

        # set up the engine paths
        self.engine_1_path = engine_1_path
        self.engine_2_path = engine_2_path

        # set up the time management variables
        self.starting_time = starting_time
        self.increment = increment

        # set up the gui used to display the board
        self.gui = gui.GUI(win)

        # set up the match counters
        self.engine_1_wins = 0
        self.engine_2_wins = 0
        self.draws = 0
        self.games_finished = 0

    # start the match and continue with each game until the end
    def start_match(self):

        # loop over each new position in the opening book
        for opening_sequence in opening_book.opening_book:

            # we play each engine from both white and black in each position
            for engine_1_side in range(2):
                engine_1_is_white = True
                if engine_1_side == 1:
                    engine_1_is_white = False

                sys.stdout.write("********** Stating New Game **********\n")
                print(f"Opening Sequence: {opening_sequence}")
                if engine_1_is_white:
                    sys.stdout.write("Engine 1 is white. Engine 2 is black.")
                else:
                    sys.stdout.write("Engine 2 is white. Engine 1 is black.")

                self.start_game(opening_sequence, engine_1_is_white)

        # when the match is over, save the results if at least 1 game was played
        if self.games_finished > 0:
            match_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = f'{match_time}: Engine 1 won {self.engine_1_wins} times. Engine 2 won {self.engine_2_wins} times. ' \
                     f'There were {self.draws} draws. Time ms: {self.starting_time}. Increment ms: {self.increment}.\n'

            with open('results.txt', 'a') as file:
                # Write the text to the file
                file.write(result)

    # start a new game between the engines
    def start_game(self, opening_sequence, engine_1_is_white):

        # ----------------------------- START ENGINES -------------------------------
        # start each engine from fresh
        engine_1 = engine.Engine(self.engine_1_path)
        engine_2 = engine.Engine(self.engine_2_path)
        sys.stdout.write(" Started Engines. \n")

        try:

            # ----------------------------- BOARD VARIABLES -------------------------------
            # set up a new board with the starting position
            game_board = board.Board(fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

            # ----------------------------- GAME VARIABLES -------------------------------
            white_time = self.starting_time
            black_time = self.starting_time

            white_inc = self.increment
            black_inc = self.increment

            is_white_turn = True

            # ----------------------------- POSITION COMMAND SETUP -------------------------------
            # list of commands to send on each "position" command
            position_command = f"position startpos moves"

            # append the moves from the opening book to the position command
            # also switch the side to play on every move added
            # also play the move on the game board
            for move in opening_sequence:
                position_command += f" {move}"
                is_white_turn = not is_white_turn
                game_board.play_move(move)

            # ----------------------------- UCI -------------------------------
            # send the "uci" command to both engines, and receive "uciok"
            engine_1.send_input("uci\n")
            _ = engine_1.receive_output()  # the id of the engine is not used
            _ = engine_1.receive_output()  # the id of the author is not used
            engine_1_output = engine_1.receive_output()  # the id of the engine is not used
            engine_1_ok = False
            if engine_1_output == "uciok":
                engine_1_ok = True
            if not engine_1_ok:
                print("Engine 1 did not respond to uci. Aborting the game.")
                return
            sys.stdout.write("Engine 1 uciok. ")

            engine_2.send_input("uci\n")
            _ = engine_2.receive_output()  # the id of the engine is not used
            _ = engine_2.receive_output()  # the id of the author is not used
            engine_2_output = engine_2.receive_output()  # the id of the engine is not used
            engine_2_ok = False
            if engine_2_output == "uciok":
                engine_2_ok = True
            if not engine_2_ok:
                print("Engine 2 did not respond to uci. Aborting the game.")
                return
            sys.stdout.write("Engine 2 uciok. ")

            # ----------------------------- UCI NEW GAME -------------------------------
            # send ucinewgame command and check whether is ready
            engine_1.send_input("ucinewgame\n", is_flush=False)
            engine_1.send_input("isready\n")
            engine_1_output = engine_1.receive_output()
            engine_1_ok = False
            if engine_1_output == "readyok":
                engine_1_ok = True
            if not engine_1_ok:
                print("Engine 1 did not respond to ucinewgame and isready. Aborting the game.")
                return
            sys.stdout.write("Engine 1 readyok. ")

            engine_2.send_input("ucinewgame\n", is_flush=False)
            engine_2.send_input("isready\n")
            engine_2_output = engine_2.receive_output()
            engine_2_ok = False
            if engine_2_output == "readyok":
                engine_2_ok = True
            if not engine_2_ok:
                print("Engine 2 did not respond to ucinewgame and isready. Aborting the game.")
                return
            sys.stdout.write("Engine 2 readyok.\n")

            # ----------------------------- LAST BEFORE LOOP -------------------------------
            self.gui.display_board(game_board, white_time, black_time, board.STATE_ONGOING, engine_1_is_white,
                                   self.engine_1_wins, self.engine_2_wins, self.draws)

            # ----------------------------- PLAY LOOP -------------------------------
            # now that the engines are ready, start the loop
            while True:

                # set up the go command to send to the engine
                go_command = f"go wtime {white_time} btime {black_time} winc {white_inc} binc {black_inc}"

                # get the next best move
                start_time = time.perf_counter()
                if is_white_turn:
                    if engine_1_is_white:
                        engine_1.send_input(f"{position_command}\n")
                        engine_1.send_input(f"{go_command}\n")
                        best_move_output = engine_1.receive_output()
                    else:
                        engine_2.send_input(f"{position_command}\n")
                        engine_2.send_input(f"{go_command}\n")
                        best_move_output = engine_2.receive_output()
                else:
                    if engine_1_is_white:
                        engine_2.send_input(f"{position_command}\n")
                        engine_2.send_input(f"{go_command}\n")
                        best_move_output = engine_2.receive_output()
                    else:
                        engine_1.send_input(f"{position_command}\n")
                        engine_1.send_input(f"{go_command}\n")
                        best_move_output = engine_1.receive_output()

                # deduct time taken for the search
                end_time = time.perf_counter()
                elapsed_ms = int((end_time - start_time) * 1000)
                if is_white_turn:
                    white_time -= elapsed_ms
                    white_time += white_inc
                else:
                    black_time -= elapsed_ms
                    black_time += black_inc

                # check for time fails
                if white_time <= 0:
                    print("Game over. White lost on time")
                    if engine_1_is_white:
                        self.engine_2_wins += 1
                    else:
                        self.engine_1_wins += 1
                    self.games_finished += 1
                    return

                if black_time <= 0:
                    print("Game over. Black lost on time")
                    if engine_1_is_white:
                        self.engine_1_wins += 1
                    else:
                        self.engine_2_wins += 1
                    self.games_finished += 1
                    return

                # clean the next best move to one uci move, example: "bestmove e7e8q"
                best_move_uci = best_move_output.strip()
                if len(best_move_uci) == 13:  # normal move
                    best_move_uci = best_move_uci[9:13]
                else:  # promotion move
                    best_move_uci = best_move_uci[9:14]

                # append the move to the position command for the next turn
                position_command += f' {best_move_uci}'
                # print(f"Best move {best_move_uci}")

                # play the move on the board
                game_board.play_move(best_move_uci)

                # check the game state, and stop the loop if the game is not ongoing
                game_state = game_board.get_game_state()

                # update the gui
                self.gui.display_board(game_board, white_time, black_time, game_state, engine_1_is_white,
                                       self.engine_1_wins, self.engine_2_wins, self.draws)

                # end the game loop if the game is over
                if not game_state == board.STATE_ONGOING:
                    sys.stdout.write("Game over. ")
                    if game_state == board.STATE_WHITE_WIN:
                        sys.stdout.write("White Wins!\n")
                        if engine_1_is_white:
                            self.engine_1_wins += 1
                        else:
                            self.engine_2_wins += 1
                    elif game_state == board.STATE_BLACK_WIN:
                        sys.stdout.write("Black Wins!\n")
                        if engine_1_is_white:
                            self.engine_2_wins += 1
                        else:
                            self.engine_1_wins += 1
                    else:
                        sys.stdout.write("Draw.\n")
                        self.draws += 1

                    self.games_finished += 1
                    return

                # finally, change the side to move
                is_white_turn = not is_white_turn

        finally:
            engine_1.close()
            engine_2.close()