def get_values():
  lst = []
  with open('Day_1\input.txt', 'r') as file:
    for line in file:
      lst.append(line.strip())
  return lst

def ans():
  return 0

for val in get_values():
  sum = sum + ans(val)

print('answer: ',sum)