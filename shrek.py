import math
import random

# CONSTANTS
MOVIE_SECONDS = 90 * 60 # duration of the movie in seconds
NUM_SWAPS = 5 # number of times to swap to a different language
SWAP_MIN_SECONDS = 30 # minimum number of seconds before reverting back to english
SWAP_MAX_SECONDS = 90 # maximum number of seconds before reverting back to english
SWAP_LANGUAGES = ["Spanish", "French", "Test"] # pool of languages that can be swapped to

# HELPER FUNCTIONS
def generateSwap() -> int:

    return random.randrange(1, MOVIE_SECONDS)

def generateEnglishReturn(swapTime: int) -> int:

    return swapTime + random.randrange(SWAP_MIN_SECONDS, SWAP_MAX_SECONDS)

def secondsToTime(seconds: int):
    
    time_hours = math.floor((seconds / 60) / 60)

    seconds = seconds - (time_hours * 60 * 60)

    time_minutes = math.floor((seconds / 60))

    seconds = seconds - (time_minutes * 60)

    return [time_hours, time_minutes, seconds]

def checkCollision(currentSwaps, newSwap) -> bool:
    
    for i in range(0, (currentSwaps.__len__() - 1 ) / 2):

        if 


def generateSwaps():

    times = []

    for i in range(0, NUM_SWAPS):

        newSwapTime = generateSwap()

        times.append(secondsToTime(newSwapTime))
        times.append(secondsToTime(generateEnglishReturn(newSwapTime)))

    return times

def printTime(time, newLanguage: str):

    hours = time[0]
    minutes = time[1]
    seconds = time[2]

    print(
    ("0" + hours.__str__() if hours < 10 else hours.__str__()) + ":" +
    ("0" + minutes.__str__() if minutes < 10 else minutes.__str__()) + ":" +
    ("0" + seconds.__str__() if seconds < 10 else seconds.__str__()) + 
    " -> Switch to " + newLanguage)

def printTimes(times):

    isReturnToEnglish = False

    for i in times:

        if (isReturnToEnglish):
            printTime(i, "English")
            isReturnToEnglish = False
            print("")
        else:
            printTime(i, SWAP_LANGUAGES[random.randint(0, SWAP_LANGUAGES.__len__() - 1)])
            isReturnToEnglish = True

# MAIN
def main():
    
    printTimes(generateSwaps())

main()