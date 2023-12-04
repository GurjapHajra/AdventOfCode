def get_values():
  lst = []
  with open('Day_4\input.txt', 'r') as file:
    for line in file:
      lst.append(line.strip())
  return lst

all_cards = []

for line in get_values():
  all_cards.append(line[8:])

each_card = [1]*len(all_cards)

winning_cards = []
my_cards = []

for line in all_cards:
  winning_cards.append([x for x in line[0:31].split(" ") if (x != '')]) # 31

for line in all_cards:
  my_cards.append([x for x in line[33:].split(" ") if (x != '')]) # 33

for i in range(len(winning_cards)):
  points = 0
  for card in my_cards[i]:
    if card in winning_cards[i]:
        points = points + 1
  for j in range(i+1,i+points+1):
    each_card[j] = each_card[j] + each_card[i]

print(sum(each_card))