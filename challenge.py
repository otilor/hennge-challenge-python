#Goal is to calculate the sum of given integers, excluding any negatives,

#That is 2, 3, 2, -1 becomes 17

numberOfTestCases = int(input("Enter the number of test cases "))
numberOfSpaceSeparatedInteger = int(input("Enter the number of space separated integer: "))

spaceSeparatedIntegers = list(map(int,input().split()))



def isNegative(number):
  if number < 0:
    return True
  return False


def convertIntegers(listOfIntegers):
  convertedIntegers = 0
  for i in range(len(listOfIntegers)):
    if not isNegative(listOfIntegers[i]):
      convertedIntegers += listOfIntegers[i] ** 2
  return convertedIntegers

print(convertIntegers(spaceSeparatedIntegers))
