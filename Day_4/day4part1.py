def get_values():
  lst = []
  with open('Day_4\input.txt', 'r') as file:
    for line in file:
      lst.append(line.strip())
  return lst

all_cards = []

for line in get_values():
  all_cards.append(line[9:])

winning_cards = []
my_cards = []

for line in all_cards:
  winning_cards.append([x for x in line[0:31].split(" ") if (x != '')])

for line in all_cards:
  my_cards.append([x for x in line[33:].split(" ") if (x != '')])

res = 0

for i in range(len(winning_cards)):
  points = 0
  for card in my_cards[i]:
    if card in winning_cards[i]:
      if points == 0:
        points = 1
      else:
        points = points * 2
  res = res + points

print(res)