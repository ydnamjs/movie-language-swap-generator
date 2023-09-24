import shrek

# CONSTANTS
MOVIE_SECONDS = 90 * 60 # duration of the movie in seconds
NUM_SWAPS = 5 # number of times to swap to a different language
SWAP_MIN_SECONDS = 30 # minimum number of seconds before reverting back to english
SWAP_MAX_SECONDS = 90 # maximum number of seconds before reverting back to english

# MAIN
def main():
    
    shrek.printTimes(shrek.generateSwaps(NUM_SWAPS, MOVIE_SECONDS, SWAP_MIN_SECONDS, SWAP_MAX_SECONDS))

main()