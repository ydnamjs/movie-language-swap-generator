import math
import random

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

#TODO This really ought to return a list of pairs rather than just every 2 elements being a pair
def generateSwaps(numSwaps: int, movieSeconds: int, swapTimeMin: int, swapTimeMax: int):

    times = []

    while times.__len__() // 2 < numSwaps:

        newSwapTime = generateSwap(movieSeconds)
        newEnglishReturn = generateEnglishReturn(newSwapTime, swapTimeMin, swapTimeMax)

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

def printTimes(times, originalLanguage: str, swapLanguages):

    isReturnToEnglish = False

    for i in times:

        if (isReturnToEnglish):
            printTime(i, originalLanguage)
            isReturnToEnglish = False
            print("")
        else:
            printTime(i, swapLanguages[random.randint(0, swapLanguages.__len__() - 1)])
            isReturnToEnglish = True