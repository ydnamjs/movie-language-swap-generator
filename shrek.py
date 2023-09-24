import math
import random

# CONSTANTS
MOVIE_SECONDS = 90 * 60 # duration of the movie in seconds
NUM_SWAPS = 5 # number of times to swap to a different language
SWAP_MIN_SECONDS = 30 # minimum number of seconds before reverting back to english
SWAP_MAX_SECONDS = 90 # maximum number of seconds before reverting back to english
SWAP_LANGUAGES = ["Spanish", "French", "Test"] # pool of languages that can be swapped to

# HELPER FUNCTIONS
def generateSwap(time: int) -> int:

    return random.randrange(1, time + 1)

def generateEnglishReturn(swapTime: int, minSeconds: int, maxSeconds: int) -> int:

    return swapTime + random.randrange(minSeconds, maxSeconds + 1)

def isBetween(start: int, end: int, toCheck: int) -> bool:

    return (toCheck >= start) and (toCheck <= end)

def hasCollision(currentSwaps, newSwap: int) -> bool:
    
    for i in range(0, (currentSwaps.__len__()) // 2):

        if isBetween(currentSwaps[i*2], currentSwaps[i*2 + 1], newSwap):
            print("was true")
            return True

        
    return False

def secondsToTime(seconds: int):
    
    time_hours = math.floor((seconds / 60) / 60)

    seconds = seconds - (time_hours * 60 * 60)

    time_minutes = math.floor((seconds / 60))

    seconds = seconds - (time_minutes * 60)

    return [time_hours, time_minutes, seconds]

def generateSwaps():

    times = []

    while times.__len__() < NUM_SWAPS:

        newSwapTime = generateSwap(MOVIE_SECONDS)
        newEnglishReturn = generateEnglishReturn(newSwapTime, SWAP_MIN_SECONDS, SWAP_MAX_SECONDS)

        if not (hasCollision(times, newSwapTime) or hasCollision(times, newEnglishReturn)):
            times.append(newSwapTime)
            times.append(newEnglishReturn)

    timesConverted = []

    for i in times:
        timesConverted.append(secondsToTime(i))

    return timesConverted

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