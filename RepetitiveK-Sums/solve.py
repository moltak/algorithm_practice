def createFormula(K, list, i):
  formula = [0 for _ in range(K)]
  for i in range(K):
    formula[i] = list[0]

  formula[K - 1] = 0
  return formula


def calc(list, formula, permutation, i):
  if formula[0] == 0:
    list[0] = permutation / len(formula)
  else:
    list[i] = permutation - sum(formula)

  #print('permutation: {0}, i: {1}, sum: {2}'.format(permutation, i, sum(formula)))
  #print('formula: {0}'.format(formula))
 

def kSums(arg):
  N = arg[0][0]
  K = arg[0][1]
  permutation = arg[1]

  list = [0 for _ in range(N)]

  for i in range(N):
    formula = createFormula(K, list, i)
    calc(list, formula, permutation[i], i)
  
  return list


def printList(result):
  for i in result:
    print('%d ' % i, end="")
  print()


def main():
  tn = int(input())
  list = []

  for i in range(tn):
    nk = [int(i) for i in input().split(' ')]
    permutation = [int(i) for i in input().split(' ')]
    list.append((nk, permutation))

  for i in range(tn):
    printList(kSums(list[i]))

if __name__ == '__main__':
  main()
