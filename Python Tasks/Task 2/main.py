# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]


# 1. age reiksmes sudedame i atskira masyva amzius ir atliekame 
# matematinius veiksmus:sumuojame ir daliname is masyvo ilgio, gauname amziaus vidurki

def getUserAverageAge(list):
  amzius = [x["age"] for x in list]
  print(sum(amzius)/len(amzius))
getUserAverageAge(users)

# 2. age reiksmes sudedame i atskira masyva vardai ir ji sortiname

def getUsersNames(list):
  vardai = [x["name"] for x in list]
  vardai.sort()
  print(vardai)
getUsersNames(users)





