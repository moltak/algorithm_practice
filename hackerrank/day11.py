#https://www.hackerrank.com/challenges/30-2d-arrays


def createHourGlass(arr):
  newArr = []
  
  for i in range(4):
    for j in range(4):
      innerArr = []
      firstLine = i * 6 + j

      innerArr.append(arr[firstLine + 0])
      innerArr.append(arr[firstLine + 1])
      innerArr.append(arr[firstLine + 2])

      secondLine = firstLine + 6
      innerArr.append(0)
      innerArr.append(arr[secondLine + 1])
      innerArr.append(0)

      thirdLine = secondLine + 6
      innerArr.append(arr[thirdLine + 0])
      innerArr.append(arr[thirdLine + 1])
      innerArr.append(arr[thirdLine + 2])
      newArr.append(innerArr)
  return newArr


def findMaximumSum(arr):
  maximumDic = {'max':sum(arr[0])}
  for i in arr:
    if maximumDic.get('max') < sum(i):
      maximumDic['max'] = sum(i)
      maximumDic['value'] = i
      print(sum(i))
  return maximumDic


def calc(arr):
  hourGlass = createHourGlass(arr)
  maximumSum = findMaximumSum(hourGlass)
  print(maximumSum.get('max'))


def testCalc():
  arr = [1, 1, 1, 0, 0, 0,
         0, 1, 0, 0, 0, 0,
	 1, 1, 1, 0, 0, 0,
	 0, 0, 2, 4, 4, 0,
	 0, 0, 0, 2, 0, 0,
	 0, 0, 1, 2, 4, 0];
  calc(arr)
  
  assert 36 == len(arr)

  arr = createHourGlass(arr)
  assert 16 == len(arr)
  assert 7 == sum(arr[0])
  assert 19 == sum(arr[14])
  result = findMaximumSum(arr)
  assert 19 == result.get('max')
  assert [2, 4, 4, 0, 2, 0, 1, 2, 4] == result.get('value')

def main():
  arr = []
  for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.extend(arr_t)
  print(arr) 
  calc(arr)

if __name__ == '__main__':
  main()
  #testCalc()
