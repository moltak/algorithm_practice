# https://www.hackerrank.com/challenges/30-binary-numbers

class MaxCount:
  def __init__(self):
    self.count = 0
    self.max = 0

  def count_plus(self):
    self.count = self.count + 1

  def count_zero_and_save(self):
    if self.count > self.max:
      self.max = self.count
    self.count = 0

def convert_to_binary(n, list):
  if n == 0:
    list.reverse()
    return list

  list.append(n % 2)
  #print(n, list)
  return convert_to_binary(int(n / 2), list)


def test_for_binary():
  assert [1, 1, 1] == convert_to_binary(7, [])
  assert [1, 0, 1, 1] == convert_to_binary(11, [])
  assert [1, 0, 0, 1] == convert_to_binary(9, [])

#test_for_binary()

def count_consecutive_binary(count, head, tail):
  if head == 1:
    count.count_plus()
  else:
    count.count_zero_and_save()

  if len(tail) == 0:
    count.count_zero_and_save()
    return count
  else:
    return count_consecutive_binary(count, tail[0], tail[1:len(tail)])

def main():
  count = MaxCount()
  binary = convert_to_binary(int(input()), [])
  count = count_consecutive_binary(count, binary[0], binary[1:len(binary)])
  print(count.max)


def test_count_consecutive_binary():
  binary = [1, 1, 0, 0]
  count = count_consecutive_binary(MaxCount(), binary[0], binary[1:len(binary)])
  assert 2 == count.max

  binary = [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0]
  count = count_consecutive_binary(MaxCount(), binary[0], binary[1:len(binary)])
  assert 4 == count.max

  binary = convert_to_binary(7, [])
  assert [1, 1, 1] == binary
  count = count_consecutive_binary(MaxCount(), binary[0], binary[1:len(binary)])
  assert 3 == count.max

  binary = [1, 1, 1, 1]
  count = count_consecutive_binary(MaxCount(), binary[0], binary[1:len(binary)])
  assert 4 == count.max
  

#test_count_consecutive_binary()

if __name__ == '__main__':
  main()
