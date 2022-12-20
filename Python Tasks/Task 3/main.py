# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

# atspausdina naują masyvą/list su žodyno/dict raktų reikšmėmis(nespausdinant pačių raktų). du metodai

def showObjectKeys(list):
  print(list.values())
showObjectKeys(audi)

masyvas = []
def showObjectKeys2(list):
 for x in list.values(): 
  masyvas.append(x)
showObjectKeys2(audi)
print(masyvas)

print(list(audi.values()))
