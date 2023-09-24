from bakery import assert_equal

import shrek

# TESTS FOR GENERATE SWAP
print("testing generate swap")

generateCount = 0
generateSampleSize = 100000 # there's probably a more statistically appropriate number but the test is O(n) anyway so whatever
generatedMin = 999_999_999_999_999
generatedMax = 0

sampleTime = 10

while generateCount < generateSampleSize:
    
    newSubject = shrek.generateSwap(sampleTime)

    if (newSubject < generatedMin):
        generatedMin = newSubject
    if (newSubject > generatedMax):
        generatedMax = newSubject

    generateCount += 1

print("")

print("generateSwap does not produce a value less than 0")
assert_equal(generatedMin >= 0, True)
print("")

print("Test: generateSwap does not produce a value greater than max")
assert_equal(generatedMax <= sampleTime, True)
print("")

print("Test: generateSwap should include the max")
assert_equal(generatedMax == sampleTime, True)
print("")

# TESTS FOR GENERATE SWAP