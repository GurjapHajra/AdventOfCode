def get_values():
  lst = []
  with open('Day_1\input.txt', 'r') as file:
    for line in file:
      lst.append(line.strip())
  return lst

def getNums(str: str):
  num1 = ''
  num2 = ''
  for i in range(0, len(str)):
    print(str[i])
    if str[i].isnumeric():
      num1 = (str[i])
      break
  for i in range(len(str)-1, -1,-1):
    print(str[i])
    if str[i].isnumeric():
      num2 = str[i]
      break
  print('together: ',int("".join([num1,num2])))
  return int("".join([num1,num2]))


sum = 0

for val in get_values():
  sum = sum + getNums(val)

print('answer: ',sum)