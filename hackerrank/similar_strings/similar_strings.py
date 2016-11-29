from sys import stdin 

def define_similar_string(ori, next, len):
  for i in range(len):
   for j in range(len -1):
     if j == 0:
       continue
     
     print('i=' + str(i), 'j=' + str(j))

argument = stdin.readline().split(' ')

#print(argument)
s_length = int(argument[0])
q_length = int(argument[1])

S = stdin.readline()
point_list = []

for i in range(q_length):
  Q = stdin.readline().split(' ')
  li = int(Q[0])
  ri = int(Q[1])
  #print(li, ri)
  point_list.append((li, ri))
	
#print(point_list)
define_similar_string(point_list, point_list, s_length)


