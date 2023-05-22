# create a small opening book for the engines to play varied games
# the book creates a list of uci moves to get to each starting position
opening_book = []

# blank match (engine play anything)
move_sequence = []
opening_book.append(move_sequence)

# e4 Game
move_sequence = ["e2e4"]
opening_book.append(move_sequence)

# d4 Game
move_sequence = ["d2d4"]
opening_book.append(move_sequence)

# c4 Game
move_sequence = ["c2c4"]
opening_book.append(move_sequence)

# e4 c5 Sicilian
move_sequence = ["e2e4", "c7c5"]
opening_book.append(move_sequence)

# e5 e5 Nf3 Nc6 Bb5 Ruy-Lopez
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1b5"]
opening_book.append(move_sequence)

# e5 e5 Nf3 Nc6 Bc4 Italian Game
move_sequence = ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4"]
opening_book.append(move_sequence)

# d4 d5 c4 Queen's Gambit
move_sequence = ["d2d4", "d7d5", "c2c4"]
opening_book.append(move_sequence)

# d4 d5 c4 e6 Queen's Gambit Declined
move_sequence = ["d2d4", "d7d5", "c2c4", "e7e6"]
opening_book.append(move_sequence)

# e4 c6 Caro-Kann Defence
move_sequence = ["e2e4", "c7c6"]
opening_book.append(move_sequence)

# e4 e6 French Defence
move_sequence = ["e2e4", "e7e6"]
opening_book.append(move_sequence)

# e4 e5 f4 King's Gambit
move_sequence = ["e2e4", "e7e5", "f2f4"]
opening_book.append(move_sequence)

# Nf3 d5 c4 Reti Opening
move_sequence = ["g1f3", "d7d5", "c2c4"]
opening_book.append(move_sequence)
