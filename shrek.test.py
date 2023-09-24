from bakery import assert_equal

import shrek

# TESTS FOR GENERATE SWAP
print("-----testing generateSwap")

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

# TESTS FOR GENERATE ENGLISH RETURN
print("-----testing generateEnglishReturn")

generateCount = 0
generateSampleSize = 100000 # there's probably a more statistically appropriate number but the test is O(n) anyway so whatever
generatedMin = 999_999_999_999_999
generatedMax = 0

sampleTime = 10
sampleMin = 4
sampleMax = 8

while generateCount < generateSampleSize:
    
    newSubject = shrek.generateEnglishReturn(sampleTime, 4, 8)

    if (newSubject < generatedMin):
        generatedMin = newSubject
    if (newSubject > generatedMax):
        generatedMax = newSubject

    generateCount += 1

print("")

print("generateEnglishReturn does not produce a value less than the original + the min")
assert_equal(generatedMin >= sampleTime + sampleMin, True)
print("")

print("generateEnglishReturn does not produce a value greater than the original + the max")
assert_equal(generatedMax <= sampleTime + sampleMax, True)
print("")

print("generateEnglishReturn should be able to generate the maximum value")
assert_equal(generatedMax == sampleTime + sampleMax, True)
print("")

# TESTS FOR IS BETWEEN
print("-----testing isBetween")

print("isBetween works for a general in between case")
assert_equal(shrek.isBetween(1, 4, 2), True)
print("")

print("isBetween works when the checked number is above the max")
assert_equal(shrek.isBetween(4, 8, 9), False)
print("")

print("isBetween works when the checked number is below the max")
assert_equal(shrek.isBetween(3, 5, 2), False)
print("")

print("isBetween works for when the number is equal to the lower parameter")
assert_equal(shrek.isBetween(1, 4, 1), True)
print("")

print("isBetween works for when the number is equal to the upper parameter")
assert_equal(shrek.isBetween(1, 4, 4), True)
print("")