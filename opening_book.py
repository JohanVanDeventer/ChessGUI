# create an opening book for the engines to play varied games
# the book creates a list of uci moves to get to each starting position
# or contains a fen string from which the engines need to play on from
opening_book = []

# ------------------------------------- VARIOUS OPENINGS ------------------------------------

# blank match (engine play anything)
move_sequence = []
move_sequence_name = "Engine Free To Play"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 Game
move_sequence = ["e2e4"]
move_sequence_name = "e4 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 c5 Sicilian
move_sequence = ["e2e4", "c7c5"]
move_sequence_name = "e4 c5 Sicilian"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 c5 c3 Alapin Sicilian
move_sequence = ["e2e4", "c7c5", "c2c3"]
move_sequence_name = "e4 c5 c3 Alapin Sicilian"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 c5 Nc3 Nc6 g3 Closed Sicilian
move_sequence = ["e2e4", "c7c5", "b1c3", "b8c6", "g2g3"]
move_sequence_name = "e4 c5 Nc3 Nc6 g3 Closed Sicilian"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 c5 Nf3 d6 d4 cxd4 Nxd4 Open Sicilian
move_sequence = ["e2e4", "c7c5", "g1f3", "d7d6", "d2d4", "c5d4", "f3d4"]
move_sequence_name = "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Open Sicilian"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 d5 Scandinavian
move_sequence = ["e2e4", "d7d5"]
move_sequence_name = "e4 d5 Scandinavian"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Game
move_sequence = ["e2e4", "e7e5"]
move_sequence_name = "e4 e5 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Bc4 Bishop's Opening
move_sequence = ["e2e4", "e7e5", "f1c4"]
move_sequence_name = "e4 e5 Bc4 Bishop's Opening"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 d4 exd4 c3 Danish Gambit
move_sequence = ["e2e4", "e7e5", "d2d4", "e5d4", "c2c3"]
move_sequence_name = "e4 e5 d4 exd4 c3 Danish Gambit"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Nf3 d6 Philidor's Defence
move_sequence = ["e2e4", "e7e5", "g1f3", "d7d6"]
move_sequence_name = "e4 e5 Nf3 d6 Philidor's Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Nf3 f5 Latvian Gambit
move_sequence = ["e2e4", "e7e5", "g1f3", "f7f5"]
move_sequence_name = "e4 e5 Nf3 f5 Latvian Gambit"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nf6 Petroff Defence
move_sequence = ["e2e4", "e7e5", "g1f3", "g8f6"]
move_sequence_name = "e4 e5 Nf3 Nf6 Petroff Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 d4 Scotch Game
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "d2d4"]
move_sequence_name = "e4 e5 Nf3 Nc6 d4 Scotch Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 Bb5 Ruy-Lopez
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1b5"]
move_sequence_name = "e4 e5 Nf3 Nc6 Bb5 Ruy-Lopez"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 Bc4 Italian Game
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4"]
move_sequence_name = "e4 e5 Nf3 Nc6 Bc4 Italian Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 Bc4 Bc5 Giuoco Piano
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4", "f8c5"]
move_sequence_name = "e4 e5 Nf3 Nc6 Bc4 Bc5 Giuoco Piano"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 Bc4 Bc5 b4 Evans Gambit
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4", "f8c5", "b2b4"]
move_sequence_name = "e4 e5 Nf3 Nc6 Bc4 Bc5 b4 Evans Gambit"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 Bc4 Nf6 Two Knights Defence
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4", "g8f6"]
move_sequence_name = "e4 e5 Nf3 Nc6 Bc4 Nf6 Two Knights Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 c6 Caro-Kann Defence
move_sequence = ["e2e4", "c7c6"]
move_sequence_name = "e4 c6 Caro-Kann Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e6 French Defence
move_sequence = ["e2e4", "e7e6"]
move_sequence_name = "e4 e6 French Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 d6 Pirc Defence Precursor
move_sequence = ["e2e4", "d7d6"]
move_sequence_name = "e4 d6 Pirc Defence Precursor"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 e5 f4 King's Gambit
move_sequence = ["e2e4", "e7e5", "f2f4"]
move_sequence_name = "e4 e5 f4 King's Gambit"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e4 Nf6 Alekhine's Defence
move_sequence = ["e2e4", "g8f6"]
move_sequence_name = "e4 Nf6 Alekhine's Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 Game
move_sequence = ["d2d4"]
move_sequence_name = "d4 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 c5 Old Benoni
move_sequence = ["d2d4", "c7c5"]
move_sequence_name = "d4 c5 Old Benoni"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 d5 Game
move_sequence = ["d2d4", "d7d5"]
move_sequence_name = "d4 d5 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 d5 f4 London System
move_sequence = ["d2d4", "d7d5", "c1f4"]
move_sequence_name = "d4 d5 f4 London System"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 d5 c4 Queen's Gambit
move_sequence = ["d2d4", "d7d5", "c2c4"]
move_sequence_name = "d4 d5 c4 Queen's Gambit"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 d5 c4 e6 Queen's Gambit Declined
move_sequence = ["d2d4", "d7d5", "c2c4", "e7e6"]
move_sequence_name = "d4 d5 c4 e6 Queen's Gambit Declined"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 d5 c4 dxc4 Queen's Gambit Accepted
move_sequence = ["d2d4", "d7d5", "c2c4", "d5c4"]
move_sequence_name = "d4 d5 c4 e6 Queen's Gambit Accepted"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 Nf6 Queen's Pawn Game
move_sequence = ["d2d4", "g8f6"]
move_sequence_name = " d4 Nf6 Queen's Pawn Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 Nf6 c4 e5 Budapest Gambit
move_sequence = ["d2d4", "g8f6", "c2c4", "e7e5"]
move_sequence_name = "d4 Nf6 c4 e5 Budapest Gambit"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 Nf6 c4 g6 King's Indian Defence
move_sequence = ["d2d4", "g8f6", "c2c4", "g7g6"]
move_sequence_name = "d4 Nf6 c4 g6 King's Indian Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 Nf6 c4 e6 Catalan or Nimzo-Indian Precursor
move_sequence = ["d2d4", "g8f6", "c2c4", "e7e6"]
move_sequence_name = "d4 Nf6 c4 e6 Catalan or Nimzo-Indian Precursor"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 Nf6 c4 e6 g3 Catalan
move_sequence = ["d2d4", "g8f6", "c2c4", "e7e6", "g2g3"]
move_sequence_name = "d4 Nf6 c4 e6 g3 Catalan"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 Nf6 c4 e6 Nc3 Bb4 Nimzo-Indian Defence
move_sequence = ["d2d4", "g8f6", "c2c4", "e7e6", "b1c3", "f8b4"]
move_sequence_name = "d4 Nf6 c4 e6 Nc3 Bb4 Nimzo-Indian Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 Nf6 c4 e6 Nf3 b6 Queen's Indian Defence
move_sequence = ["d2d4", "g8f6", "c2c4", "e7e6", "g1f3", "b7b6"]
move_sequence_name = "d4 Nf6 c4 e6 Nf3 b6 Queen's Indian Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 Nf6 c4 c5 d5 Benoni
move_sequence = ["d2d4", "g8f6", "c2c4", "c7c5", "d4d5"]
move_sequence_name = "d4 Nf6 c4 c5 d5 Benoni"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 Nf6 c4 c5 d5 b5 Benko Gambit
move_sequence = ["d2d4", "g8f6", "c2c4", "c7c5", "d4d5", "b7b5"]
move_sequence_name = "d4 Nf6 c4 c5 d5 b5 Benko Gambit"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 d5 c4 c6 Slav Defence
move_sequence = ["d2d4", "d7d5", "c2c4", "c7c6"]
move_sequence_name = "d4 d5 c4 c6 Slav Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d4 f5 Dutch Defence
move_sequence = ["d2d4", "f7f5"]
move_sequence_name = "d4 f5 Dutch Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# c4 English
move_sequence = ["c2c4"]
move_sequence_name = "c4 English"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# c4 d5 Anglo-Scandinavian Defence
move_sequence = ["c2c4", "d7d5"]
move_sequence_name = "c4 d5 Anglo-Scandinavian Defence"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# c4 c6 Caro-Kann in English
move_sequence = ["c2c4", "c7c6"]
move_sequence_name = "c4 c6 Caro-Kann in English"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# c4 e6 French Defence in English
move_sequence = ["c2c4", "e7e6"]
move_sequence_name = "c4 e6 French Defence in English"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# c4 c5 Symmetrical English
move_sequence = ["c2c4", "c7c5"]
move_sequence_name = "c4 c5 Symmetrical English"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# c4 e5 Reverse Sicilian
move_sequence = ["c2c4", "e7e5"]
move_sequence_name = "c4 e5 Reverse Sicilian"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# Nf3 Game
move_sequence = ["g1f3"]
move_sequence_name = "Nf3 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# Nf3 d5 c4 Reti Opening
move_sequence = ["g1f3", "d7d5", "c2c4"]
move_sequence_name = "Nf3 d5 c4 Reti Opening"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# Nc3 Game
move_sequence = ["b1c3"]
move_sequence_name = "Nc3 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# a4 Game
move_sequence = ["a2a4"]
move_sequence_name = "a4 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# b3 Game
move_sequence = ["b2b3"]
move_sequence_name = "b3 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# b4 Orangutan/Polish
move_sequence = ["b2b4"]
move_sequence_name = "b4 Orangutan/Polish"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# c3 Game
move_sequence = ["c2c3"]
move_sequence_name = "c3 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# d3 Game
move_sequence = ["d2d3"]
move_sequence_name = "d3 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# e3 Game
move_sequence = ["e2e3"]
move_sequence_name = "e3 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# f3 Game
move_sequence = ["f2f3"]
move_sequence_name = "f3 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# f4 Bird's Opening
move_sequence = ["f2f4"]
move_sequence_name = "f4 Bird's Opening"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# g3 Game
move_sequence = ["g2g3"]
move_sequence_name = "g3 Game"
fen = "startpos"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# ------------------------------------- VARIOUS ENDGAMES ------------------------------------

# custom position
move_sequence = []
move_sequence_name = "White to play and win in endgame"
fen = "8/k7/3p4/p2P1p2/P2P1P2/8/8/K7 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "White to play and draw in endgame"
fen = "7K/8/k1P5/7p/8/8/8/8 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "White to play and win in difficult endgame"
fen = "8/5k1p/1p1pRp2/p2P4/P1P3Pp/1P4bP/6K1/8 w - - 0 49"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "King vs King and Rook"
fen = "8/8/4k3/8/8/8/8/2KR4 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "White to play and win in endgame"
fen = "4k3/8/8/8/8/8/3P4/3K4 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "Black to hold draw in endgame"
fen = "8/3k4/8/8/8/8/3P4/3K4 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "King, Bishop and Knight Checkmate"
fen = "8/3k4/8/8/8/2BNK3/8/8 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "King and Two Bishops Checkmate"
fen = "8/4k3/8/8/3K4/3BB3/8/8 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "K+Q vs K+P: Winning for White"
fen = "K7/2Q5/8/8/8/8/4p3/5k2 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "K+Q vs K+P: Black to hold draw"
fen = "8/2K5/8/4Q3/8/8/5p2/6k1 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "White to put Black in Zugzwang"
fen = "8/4kb1p/2p3pP/1pP1P1P1/1P3K2/1B6/8/8 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "Black to hold the draw"
fen = "8/2k1b3/2P5/3KP2B/8/8/8/8 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "Lucena 1: White to play and win"
fen = "4K3/4P1k1/8/8/8/8/r7/5R2 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "Lucena 2: White to play and win"
fen = "K7/P4k2/8/8/8/8/1r6/4R3 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "R vs BPP: White to hold the draw"
fen = "4R3/8/3b4/3k4/3pp3/8/4K3/8 w - - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# ------------------------------------- VARIOUS MIDDLE GAMES ------------------------------------

# custom position
move_sequence = []
move_sequence_name = "Kiwipete"
fen = "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "Poisoned Pawn: White to play to win"
fen = "2r1kr2/6p1/pp2Pn1p/3p1P1N/2pP3P/P4R2/1P4K1/5R2 w - - 0 37"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "Rook f3: White to play and win"
fen = "2rr2k1/2q1bpp1/p3p3/1pn1P3/3N1BQ1/1PP5/P5PP/3R1R1K w - - 0 23"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "Rook takes Knight for long term advantage"
fen = "r1b2r2/p5kp/1p1q1p2/4nP2/3p1N2/3B4/P2Q2PP/4RRK1 w - - 0 21"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)

# custom position
move_sequence = []
move_sequence_name = "Sacrifice material by white to win"
fen = "4rr1k/2q2pp1/p1NRp1b1/1pn1P3/5Q1P/2P1PB2/P7/5RK1 w - - 0 25"
move_tuple = (move_sequence, move_sequence_name, fen)
opening_book.append(move_tuple)