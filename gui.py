import pygame

import board

# board display settings
BOARD_START_X = 50
BOARD_START_Y = 50

TILE_WIDTH = 64
TILE_HEIGHT = 64

PIECE_WIDTH = 56
PIECE_HEIGHT = 56

PIECE_X_OFFSET = 5
PIECE_Y_OFFSET = 5

TEXT_START_X = BOARD_START_X + (8*TILE_WIDTH) + 50
TEXT_START_Y = BOARD_START_Y
TEXT_Y_OFFSET = 32

# tile type constants
TILE_WHITE = 0
TILE_BLACK = 1
TILE_KING_IN_CHECK = 2
TILE_MOVE = 3
TILE_PIECE_HIGHLIGHT = 4
TILE_TARGET = 5

# piece type constants
WHITE_KING = 0
WHITE_QUEEN = 1
WHITE_ROOK = 2
WHITE_KNIGHT = 3
WHITE_BISHOP = 4
WHITE_PAWN = 5
BLACK_KING = 6
BLACK_QUEEN = 7
BLACK_ROOK = 8
BLACK_KNIGHT = 9
BLACK_BISHOP = 10
BLACK_PAWN = 11

# string to int conversion dictionary
CHESS_PIECE_TO_INT = {"K": WHITE_KING,
                      "Q": WHITE_QUEEN,
                      "R": WHITE_ROOK,
                      "N": WHITE_KNIGHT,
                      "B": WHITE_BISHOP,
                      "P": WHITE_PAWN,
                      "k": BLACK_KING,
                      "q": BLACK_QUEEN,
                      "r": BLACK_ROOK,
                      "n": BLACK_KNIGHT,
                      "b": BLACK_BISHOP,
                      "p": BLACK_PAWN}


# display the board in PyGame
class GUI:
    def __init__(self, win):

        # set up the PyGame window
        self.win = win

        # set up the PyGame font
        self.font = pygame.font.SysFont("Arial", 24)

        # create a list of all images corresponding to their constant value
        self.img_list = []
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/king_white.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/queen_white.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/rook_white.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/knight_white.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/bishop_white.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/pawn_white.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/king_black.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/queen_black.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/rook_black.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/knight_black.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/bishop_black.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())
        self.img_list.append(pygame.transform.scale(pygame.image.load("chess_images/pawn_black.png"),
                                                    (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha())

        # create a list of all tiles corresponding to their constant value
        self.tile_list = []
        self.tile_list.append(pygame.transform.scale(pygame.image.load("chess_images/tile_white.png"),
                                                     (TILE_WIDTH, TILE_HEIGHT)).convert_alpha())
        self.tile_list.append(pygame.transform.scale(pygame.image.load("chess_images/tile_black.png"),
                                                     (TILE_WIDTH, TILE_HEIGHT)).convert_alpha())
        self.tile_list.append(pygame.transform.scale(pygame.image.load("chess_images/tile_king_in_check.png"),
                                                     (TILE_WIDTH, TILE_HEIGHT)).convert_alpha())
        self.tile_list.append(pygame.transform.scale(pygame.image.load("chess_images/tile_move.png"),
                                                     (TILE_WIDTH, TILE_HEIGHT)).convert_alpha())
        self.tile_list.append(pygame.transform.scale(pygame.image.load("chess_images/tile_piece_highlight.png"),
                                                     (TILE_WIDTH, TILE_HEIGHT)).convert_alpha())
        self.tile_list.append(pygame.transform.scale(pygame.image.load("chess_images/tile_target.png"),
                                                     (TILE_WIDTH, TILE_HEIGHT)).convert_alpha())

    # refresh the displayed board to show the new board
    def display_board(self, board_to_show: board.Board, white_time, black_time, game_state, engine_info):

        # fill in the background to be blank
        self.win.fill((255, 255, 255))

        # draw each tile on the screen
        for row in range(8):
            for col in range(8):
                tile_type = 0
                if not (row + col) % 2 == 0:
                    tile_type = 1
                self.win.blit(self.tile_list[tile_type],
                              (BOARD_START_X + (col * TILE_WIDTH),
                               BOARD_START_Y + (row * TILE_HEIGHT)))

        # draw each piece on the screen
        for row in range(8):
            for col in range(8):
                piece_on_sq = board_to_show.get_piece_type_on_sq(row * 8 + col)
                if piece_on_sq is not None:
                    piece_type = CHESS_PIECE_TO_INT[piece_on_sq.symbol()]
                    self.win.blit(self.img_list[piece_type],
                                  (BOARD_START_X + (col * TILE_WIDTH) + PIECE_X_OFFSET,
                                   BOARD_START_Y + (row * TILE_HEIGHT) + PIECE_Y_OFFSET))

        # display the time for each side
        white_img = self.font.render(f'White time remaining: {white_time}', False, (0, 0, 0)).convert_alpha()
        black_img = self.font.render(f'Black time remaining: {black_time}', False, (0, 0, 0)).convert_alpha()
        self.win.blit(white_img, (TEXT_START_X, TEXT_START_Y + (TEXT_Y_OFFSET * 0)))
        self.win.blit(black_img, (TEXT_START_X, TEXT_START_Y + (TEXT_Y_OFFSET * 1)))

        # display the game state
        state_img = self.font.render(f'Game State: {game_state}', False, (0, 0, 0)).convert_alpha()
        self.win.blit(state_img, (TEXT_START_X, TEXT_START_Y + (TEXT_Y_OFFSET * 2)))

        # display engine info
        engine_img = self.font.render(f'{engine_info}', False, (0, 0, 0)).convert_alpha()
        self.win.blit(engine_img, (TEXT_START_X, TEXT_START_Y + (TEXT_Y_OFFSET * 3)))

        # finally refresh the screen
        pygame.display.update()
