import solve

def test_first():
  arg = []
  arg.append((1, 3))
  arg.append([3])
  
  result = solve.kSums(arg)

  assert result[0] == 1


def test_second():
  arg = []
  arg.append((5, 2))
  arg.append((4, 10, 14, 20, 26))

  result = solve.kSums(arg)

  assert result[0] == 2
  assert result[1] == 8
  assert result[2] == 12
  assert result[3] == 18
  assert result[4] == 24


