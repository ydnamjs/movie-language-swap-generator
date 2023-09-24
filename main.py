import shrek

# CONSTANTS
MOVIE_SECONDS = 90 * 60 # duration of the movie in seconds
DEFAULT_LANGUAGE = "English"

NUM_SWAPS = 5 # number of times to swap to a different language
SWAP_MIN_SECONDS = 30 # minimum number of seconds before reverting back to english
SWAP_MAX_SECONDS = 90 # maximum number of seconds before reverting back to english
SWAP_LANGUAGES = ["Spanish", "French", "Test"] # pool of languages that can be swapped to

# MAIN
def main():

    shrek.printTimes(shrek.generateSwaps(NUM_SWAPS, MOVIE_SECONDS, SWAP_MIN_SECONDS, SWAP_MAX_SECONDS), DEFAULT_LANGUAGE, SWAP_LANGUAGES)

main()