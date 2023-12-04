def get_values():
  lst = []
  with open('Day_3\input.txt', 'r') as file:
    for line in file:
      lst.append(line.strip())
  return lst

def returnRemove(x:int, y:int):
  if (not engine[x][y].isnumeric()):
    return 0
  ind = y
  start = y
  end = y
  while (ind+1 < len(engine[x])) and engine[x][ind+1].isnumeric():
    ind = ind+1
  end = ind
  ind = y
  while (ind-1 >= 0) and  engine[x][ind-1].isnumeric():
    ind = ind - 1
  start = ind
  num = "".join(engine[x][start:end+1])

  for i in range(end-start+1):
    engine[x][start+i] = '.'
  return int(num)

engine:list[list[str]] = []

for line in get_values():
  eng = [*line]
  engine.append(eng)

res = 0

for i in range(len(engine)):
  for j in range(len(engine[i])):
    adds = []
    if not (engine[i][j].isalpha() or engine[i][j].isnumeric() or engine[i][j] == '.'):

      if(i>0 and j>0 and engine[i-1][j-1].isnumeric()):
        adds.append(returnRemove(i-1,j-1))

      if(i>0 and engine[i-1][j].isnumeric()):
        adds.append(returnRemove(i-1,j))

      if(i>0 and j<(len(engine[i])-1) and engine[i-1][j+1].isnumeric()):
        adds.append(returnRemove(i-1,j+1))
        
      if(j>0 and engine[i][j-1].isnumeric()):
        adds.append(returnRemove(i,j-1))
        
      if(j<(len(engine[i])-1) and engine[i][j+1].isnumeric()):
        adds.append(returnRemove(i,j+1))
        
      if(i<(len(engine)-1) and j>0 and engine[i+1][j-1].isnumeric()):
        adds.append(returnRemove(i+1,j-1))
        
      if(i<(len(engine)-1) and engine[i+1][j].isnumeric()):
        adds.append(returnRemove(i+1,j))
        
      if(i<(len(engine)-1) and j<(len(engine[i])-1) and engine[i+1][j+1].isnumeric()):
        adds.append(returnRemove(i+1,j+1))
      
      res = res + sum(adds)
    else:
      if(engine[i][j] != '.'):
        print(engine[i][j],end='')
  print('')
for i in engine:
  print(''.join(i))
print("result: ",res)