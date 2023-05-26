# create a small opening book for the engines to play varied games
# the book creates a list of uci moves to get to each starting position
opening_book = []

# blank match (engine play anything)
move_sequence = []
move_sequence_name = "Engine Free To Play"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 Game
move_sequence = ["e2e4"]
move_sequence_name = "e4 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 c5 Sicilian
move_sequence = ["e2e4", "c7c5"]
move_sequence_name = "e4 c5 Sicilian"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 c5 c3 Alapin Sicilian
move_sequence = ["e2e4", "c7c5", "c2c3"]
move_sequence_name = "e4 c5 c3 Alapin Sicilian"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 c5 Nc3 Nc6 g3 Closed Sicilian
move_sequence = ["e2e4", "c7c5", "b1c3", "b8c6", "g2g3"]
move_sequence_name = "e4 c5 Nc3 Nc6 g3 Closed Sicilian"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 c5 Nf3 d6 d4 cxd4 Nxd4 Open Sicilian
move_sequence = ["e2e4", "c7c5", "g1f3", "d7d6", "d2d4", "c5d4", "f3d4"]
move_sequence_name = "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Open Sicilian"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 d5 Scandinavian
move_sequence = ["e2e4", "d7d5"]
move_sequence_name = "e4 d5 Scandinavian"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Game
move_sequence = ["e2e4", "e7e5"]
move_sequence_name = "e4 e5 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Bc4 Bishop's Opening
move_sequence = ["e2e4", "e7e5", "f1c4"]
move_sequence_name = "e4 e5 Bc4 Bishop's Opening"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 d4 exd4 c3 Danish Gambit
move_sequence = ["e2e4", "e7e5", "d2d4", "e5d4", "c2c3"]
move_sequence_name = "e4 e5 d4 exd4 c3 Danish Gambit"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Nf3 d6 Philidor's Defence
move_sequence = ["e2e4", "e7e5", "g1f3", "d7d6"]
move_sequence_name = "e4 e5 Nf3 d6 Philidor's Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Nf3 f5 Latvian Gambit
move_sequence = ["e2e4", "e7e5", "g1f3", "f7f5"]
move_sequence_name = "e4 e5 Nf3 f5 Latvian Gambit"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nf6 Petroff Defence
move_sequence = ["e2e4", "e7e5", "g1f3", "g8f6"]
move_sequence_name = "e4 e5 Nf3 Nf6 Petroff Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 d4 Scotch Game
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "d2d4"]
move_sequence_name = "e4 e5 Nf3 Nc6 d4 Scotch Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 Bb5 Ruy-Lopez
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1b5"]
move_sequence_name = "e4 e5 Nf3 Nc6 Bb5 Ruy-Lopez"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 Bc4 Italian Game
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4"]
move_sequence_name = "e4 e5 Nf3 Nc6 Bc4 Italian Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 Bc4 Bc5 Giuoco Piano
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4", "f8c5"]
move_sequence_name = "e4 e5 Nf3 Nc6 Bc4 Bc5 Giuoco Piano"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 Bc4 Bc5 b4 Evans Gambit
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4", "f8c5", "b2b4"]
move_sequence_name = "e4 e5 Nf3 Nc6 Bc4 Bc5 b4 Evans Gambit"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 Nf3 Nc6 Bc4 Nf6 Two Knights Defence
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4", "g8f6"]
move_sequence_name = "e4 e5 Nf3 Nc6 Bc4 Nf6 Two Knights Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 c6 Caro-Kann Defence
move_sequence = ["e2e4", "c7c6"]
move_sequence_name = "e4 c6 Caro-Kann Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e6 French Defence
move_sequence = ["e2e4", "e7e6"]
move_sequence_name = "e4 e6 French Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 d6 Pirc Defence Precursor
move_sequence = ["e2e4", "d7d6"]
move_sequence_name = "e4 d6 Pirc Defence Precursor"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 e5 f4 King's Gambit
move_sequence = ["e2e4", "e7e5", "f2f4"]
move_sequence_name = "e4 e5 f4 King's Gambit"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e4 Nf6 Alekhine's Defence
move_sequence = ["e2e4", "g8f6"]
move_sequence_name = "e4 Nf6 Alekhine's Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 Game
move_sequence = ["d2d4"]
move_sequence_name = "d4 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 c5 Old Benoni
move_sequence = ["d2d4", "c7c5"]
move_sequence_name = "d4 c5 Old Benoni"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 d5 Game
move_sequence = ["d2d4", "d7d5"]
move_sequence_name = "d4 d5 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 d5 f4 London System
move_sequence = ["d2d4", "d7d5", "c1f4"]
move_sequence_name = "d4 d5 f4 London System"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 d5 c4 Queen's Gambit
move_sequence = ["d2d4", "d7d5", "c2c4"]
move_sequence_name = "d4 d5 c4 Queen's Gambit"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 d5 c4 e6 Queen's Gambit Declined
move_sequence = ["d2d4", "d7d5", "c2c4", "e7e6"]
move_sequence_name = "d4 d5 c4 e6 Queen's Gambit Declined"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 d5 c4 dxc4 Queen's Gambit Accepted
move_sequence = ["d2d4", "d7d5", "c2c4", "d5c4"]
move_sequence_name = "d4 d5 c4 e6 Queen's Gambit Accepted"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 Nf6 Queen's Pawn Game
move_sequence = ["d2d4", "g8f6"]
move_sequence_name = " d4 Nf6 Queen's Pawn Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 Nf6 c4 e5 Budapest Gambit
move_sequence = ["d2d4", "g8f6", "c2c4", "e7e5"]
move_sequence_name = "d4 Nf6 c4 e5 Budapest Gambit"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 Nf6 c4 g6 King's Indian Defence
move_sequence = ["d2d4", "g8f6", "c2c4", "g7g6"]
move_sequence_name = "d4 Nf6 c4 g6 King's Indian Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 Nf6 c4 e6 Catalan or Nimzo-Indian Precursor
move_sequence = ["d2d4", "g8f6", "c2c4", "e7e6"]
move_sequence_name = "d4 Nf6 c4 e6 Catalan or Nimzo-Indian Precursor"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 Nf6 c4 e6 g3 Catalan
move_sequence = ["d2d4", "g8f6", "c2c4", "e7e6", "g2g3"]
move_sequence_name = "d4 Nf6 c4 e6 g3 Catalan"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 Nf6 c4 e6 Nc3 Bb4 Nimzo-Indian Defence
move_sequence = ["d2d4", "g8f6", "c2c4", "e7e6", "b1c3", "f8b4"]
move_sequence_name = "d4 Nf6 c4 e6 Nc3 Bb4 Nimzo-Indian Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 Nf6 c4 e6 Nf3 b6 Queen's Indian Defence
move_sequence = ["d2d4", "g8f6", "c2c4", "e7e6", "g1f3", "b7b6"]
move_sequence_name = "d4 Nf6 c4 e6 Nf3 b6 Queen's Indian Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 Nf6 c4 c5 d5 Benoni
move_sequence = ["d2d4", "g8f6", "c2c4", "c7c5", "d4d5"]
move_sequence_name = "d4 Nf6 c4 c5 d5 Benoni"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 Nf6 c4 c5 d5 b5 Benko Gambit
move_sequence = ["d2d4", "g8f6", "c2c4", "c7c5", "d4d5", "b7b5"]
move_sequence_name = "d4 Nf6 c4 c5 d5 b5 Benko Gambit"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 d5 c4 c6 Slav Defence
move_sequence = ["d2d4", "d7d5", "c2c4", "c7c6"]
move_sequence_name = "d4 d5 c4 c6 Slav Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d4 f5 Dutch Defence
move_sequence = ["d2d4", "f7f5"]
move_sequence_name = "d4 f5 Dutch Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# c4 English
move_sequence = ["c2c4"]
move_sequence_name = "c4 English"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# c4 d5 Anglo-Scandinavian Defence
move_sequence = ["c2c4", "d7d5"]
move_sequence_name = "c4 d5 Anglo-Scandinavian Defence"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# c4 c6 Caro-Kann in English
move_sequence = ["c2c4", "c7c6"]
move_sequence_name = "c4 c6 Caro-Kann in English"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# c4 e6 French Defence in English
move_sequence = ["c2c4", "e7e6"]
move_sequence_name = "c4 e6 French Defence in English"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# c4 c5 Symmetrical English
move_sequence = ["c2c4", "c7c5"]
move_sequence_name = "c4 c5 Symmetrical English"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# c4 e5 Reverse Sicilian
move_sequence = ["c2c4", "e7e5"]
move_sequence_name = "c4 e5 Reverse Sicilian"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# Nf3 Game
move_sequence = ["g1f3"]
move_sequence_name = "Nf3 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# Nf3 d5 c4 Reti Opening
move_sequence = ["g1f3", "d7d5", "c2c4"]
move_sequence_name = "Nf3 d5 c4 Reti Opening"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# Nc3 Game
move_sequence = ["b1c3"]
move_sequence_name = "Nc3 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# a4 Game
move_sequence = ["a2a4"]
move_sequence_name = "a4 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# b3 Game
move_sequence = ["b2b3"]
move_sequence_name = "b3 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# b4 Orangutan/Polish
move_sequence = ["b2b4"]
move_sequence_name = "b4 Orangutan/Polish"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# c3 Game
move_sequence = ["c2c3"]
move_sequence_name = "c3 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# d3 Game
move_sequence = ["d2d3"]
move_sequence_name = "d3 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# e3 Game
move_sequence = ["e2e3"]
move_sequence_name = "e3 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# f3 Game
move_sequence = ["f2f3"]
move_sequence_name = "f3 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# f4 Bird's Opening
move_sequence = ["f2f4"]
move_sequence_name = "f4 Bird's Opening"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)

# g3 Game
move_sequence = ["g2g3"]
move_sequence_name = "g3 Game"
move_tuple = (move_sequence, move_sequence_name)
opening_book.append(move_tuple)
