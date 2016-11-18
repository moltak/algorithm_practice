tn = int(input())

list = []

for i in range(tn):
  nk = [int(i) for i in input().split(' ')]
  permutation = [int(i) for i in input().split(' ')]
  list.append((nk, permutation))

#print(list)


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
 

def k_sums(arg):
  N = arg[0][0]
  K = arg[0][1]
  permutation = arg[1]

  list = [0 for _ in range(N)]

  for i in range(N):
    formula = createFormula(K, list, i)
    calc(list, formula, permutation[i], i)
  
  #print(str(list).replace('[', '').replace(']', '').replace('.0', '').replace(',', ''))
  for i in list:
    print('%d ' % i, end="")


for i in range(tn):
  k_sums(list[i])
