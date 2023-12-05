def get_values():
  lst = []
  with open('Day_5\input.txt', 'r') as file:
    for line in file:
      lst.append(line.strip())
  return lst

inp = []

for line in get_values():
   inp.append(line)

seeds = [int(x) for x in inp[0][6:].strip().split(" ")]

seed_to_soil:list[int] = []
soil_to_fert:list[int] = []
fert_to_wate:list[int] = []
wate_to_ligh:list[int] = []
ligh_to_temp:list[int] = []
temp_to_humi:list[int] = []
humi_to_loci:list[int] = []

for i in range (3,15):
  seed_to_soil.append([int(x) for x in inp[i].split(" ")])

for i in range (17,46):
  soil_to_fert.append([int(x) for x in inp[i].split(" ")])

for i in range (48,65):
  fert_to_wate.append([int(x) for x in inp[i].split(" ")])

for i in range (67,85):
  wate_to_ligh.append([int(x) for x in inp[i].split(" ")])

for i in range (87,121):
  ligh_to_temp.append([int(x) for x in inp[i].split(" ")])

for i in range (123,158):
  temp_to_humi.append([int(x) for x in inp[i].split(" ")])

for i in range (160,172):
  humi_to_loci.append([int(x) for x in inp[i].split(" ")])

def seedToSoil(seed: int):
  for mapin in seed_to_soil:
    if (seed > mapin[1]) and (seed < (mapin[1] + mapin[2])):
      diff = seed - mapin[1]
      return mapin[0] + diff
  return seed

def soilToFert(seed: int):
  for mapin in soil_to_fert:
    if (seed > mapin[1]) and (seed < (mapin[1] + mapin[2])):
      diff = seed - mapin[1]
      return mapin[0] + diff
  return seed

def fertToWate(seed: int):
  for mapin in fert_to_wate:
    if (seed > mapin[1]) and (seed < (mapin[1] + mapin[2])):
      diff = seed - mapin[1]
      return mapin[0] + diff
  return seed

def wateToLigh(seed: int):
  for mapin in wate_to_ligh:
    if (seed > mapin[1]) and (seed < (mapin[1] + mapin[2])):
      diff = seed - mapin[1]
      return mapin[0] + diff
  return seed

def lighToTemp(seed: int):
  for mapin in ligh_to_temp:
    if (seed > mapin[1]) and (seed < (mapin[1] + mapin[2])):
      diff = seed - mapin[1]
      return mapin[0] + diff
  return seed

def tempToHumi(seed: int):
  for mapin in temp_to_humi:
    if (seed > mapin[1]) and (seed < (mapin[1] + mapin[2])):
      diff = seed - mapin[1]
      return mapin[0] + diff
  return seed

def humiToLoci(seed: int):
  for mapin in humi_to_loci:
    if (seed > mapin[1]) and (seed < (mapin[1] + mapin[2])):
      diff = seed - mapin[1]
      return mapin[0] + diff
  return seed

def seedToLoci(seed: int):
  return humiToLoci(tempToHumi(lighToTemp(wateToLigh(fertToWate(soilToFert(seedToSoil(seed)))))))

res = []

dic = {}

for seed in range(0,len(seeds),2):
  for x in range(seeds[seed],seeds[seed]+seeds[seed+1]):
    if(x in dic):
      print("i like hashmap")
      res.append(dic.get(x))
    else:
      y = seedToLoci(x)
      dic.update({x:y})
      res.append(y)
  print("progress: ", seed+1,'/',20)

print(min(res))
