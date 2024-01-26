zero_misses = """
  +---+
      |
      |
      |
    ====="""


one_misses = """
  +---+
  O   |
      |
      |
    ====="""

two_misses = """
  +---+
  O   |
  |   |
      |
    ====="""

three_misses = """
  +---+
  O   |
 /|   |
      |
    ====="""

four_misses = """
  +---+
  O   |
 /|\  |
      |
    ====="""

five_misses = """
  +---+
  O   |
 /|\  |
 /    |
    ====="""

game_over = """
  +---+
  O   |
 /|\  |
 / \  |
    ====="""

HANGMAN_PICS = [
    zero_misses,
    one_misses,
    two_misses,
    three_misses,
    four_misses,
    five_misses,
    game_over,
]
