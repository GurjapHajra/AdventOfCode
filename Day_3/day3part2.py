def get_values():
  lst = []
  with open('Day_3\input.txt', 'r') as file:
    for line in file:
      lst.append(line.strip())
  return lst

