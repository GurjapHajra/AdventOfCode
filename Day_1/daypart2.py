numbers = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}
ind = [1]
def letter5(inp: str, direction: bool):
    word = ''
    # right to left
    if(direction):
        index_word = 999999999999
        for num in numbers.keys():
            if num in inp:
                index = inp.find(num)
                if (index < index_word):
                    index_word = index
                    word = num
        index_num = -1
        for i in range(0, len(inp)):
            if inp[i].isnumeric():
                index_num = i
                break
        if (index_num == -1 and word != ''):
            return numbers[word]
        elif (index_num != -1 and word == ''):
            return int(inp[index_num])
        elif(index_word<index_num):
            return numbers[word]
        else:
            return int(inp[index_num])
    # left to right
    else:
        index_word = -1
        for num in numbers.keys():
            if num in inp:
                index = inp.rfind(num)
                if (index > index_word):
                    index_word = index
                    word = num
        index_num = -1
        for i in range(len(inp)-1, -1,-1):
            if inp[i].isnumeric():
                index_num = i
                break
        if (index_num == -1 and word != ''):
            return numbers[word]
        elif (index_num != -1 and word == ''):
            return int(inp[index_num])
        elif(index_word>index_num):
            return numbers[word]
        else:
            return int(inp[index_num])

def get_values():
  lst = []
  with open('Day_1\input.txt', 'r') as file:
    for line in file:
      lst.append(line.strip())
  return lst

def get2num(val: str):
    print(str(ind[0]),str(letter5(val,True))+str(letter5(val,False)))
    ind[0] = ind[0] + 1
    return int("".join([str(letter5(val,True)),str(letter5(val,False))]))

sum = 0

for val in get_values():
  sum = sum + get2num(val)

print('answer: ',sum)

print('custom: ',get2num('six'))