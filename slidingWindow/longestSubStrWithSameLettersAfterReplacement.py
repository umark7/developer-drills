
# may 31 20
def length_of_longest_substring(str, k):
  # init vars
  windowStart = 0
  maxLen = 0
  allowence = 0
  # our char dict
  d = {}

  # window is range [windowStart, windowEnd]
  for windowEnd in range(len(str)):
    # example 'e' in the
    rightChar = str[windowEnd]
    if rightChar not in d:
      d[rightChar] = 0
    d[rightChar] +=1

    # tracks the most freq letter count at each window
    allowence = max(allowence, d[rightChar])

    if windowEnd - windowStart + 1 - allowence > k:
      oldestChar = str[windowStart]
      d[oldestChar] -=1
      if d[oldestChar] == 0:
        del d[oldestChar]
      windowStart +=1

    maxLen = max(maxLen, windowEnd - windowStart +1)

  return maxLen



# may 27 20
def length_of_longest_substring(str, k):
  """
  - NOTES + Plan
  - allowed to replace 1,2,3, K charcters
  - we can use sling window approcah to find largest contiguous substr
  - to extend that we need to chk when the length of subtr increres by K
  - if k = 0 max is 1 is k is 1 max is 2

  """

  windowIndex, maxCount, d = 0,0,{}
  maxLen = 0

  for endIndex in range(len(str)):
    leftChar = str[endIndex]
    if leftChar not in d:
      d[leftChar] = 0
    d[leftChar] +=1
    maxCount = max(maxCount, d[leftChar])

    if endIndex - windowIndex + 1 - maxCount > k:
      rightChr = str[windowIndex]
      d[rightChr]-=1
      windowIndex +=1

    maxLen = max(maxLen,  endIndex - windowIndex + 1)



  return maxLen


# 5.19  WORKS
def length_of_longest_substring(str, k):
  # TODO: Write your code here
  windowStart, limit, maxLen, d = 0, 0,0, {}

  for windowEnd in range(len(str)):
    rightChar = str[windowEnd]
    if rightChar not in d:
      d[rightChar] = 0
    d[rightChar] +=1
    limit = max(limit, d[rightChar])

    if windowEnd - windowStart + 1 - limit > k:
      leftChar = str[windowStart]
      d[leftChar] -=1
      windowStart +=1
    maxLen = max(maxLen, windowEnd - windowStart + 1 )



  return maxLen

# 5.19 DN WORK
def length_of_longest_substring(str, k):
  # TODO: Write your code here
  windowStart, limit, maxLen, d = 0, 0,0, {}

  for windowEnd in range(len(str)):
    rightChar = str[windowEnd]
    if rightChar not in d:
      d[rightChar] = 0
    d[rightChar] +=1

    # to catch when were replacing two-k more same letters
    if len(d) > k:
      limit +=1

    # while len(d) - k > k or limit > k:
    while limit > k :
      leftChar = str[windowStart]
      d[leftChar]-=1
      if d[leftChar] == 0:
        del d[leftChar]
      print(k, str, windowStart, windowEnd, limit)
      windowStart +=1
      limit -=1

    maxLen = max(maxLen, windowEnd - windowStart + 1)
