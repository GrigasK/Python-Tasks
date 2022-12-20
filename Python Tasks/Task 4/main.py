# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

limit = 100000000

class Movie():
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
    
    def wasExpensive(self):
        if self.budget > limit:
            return True
        else:
            return False


movie1=Movie('Avatar', 'Cameron', 100000000000000)
movie2=Movie('Rambo', 'Spielber', 5000000)
movie3=Movie('Titanic', 'Cameron', 10000000000)
movie4=Movie('Brother bear', 'Me', 100000)

print(movie1.wasExpensive())
print(movie2.wasExpensive())
print(movie3.wasExpensive())
print(movie4.wasExpensive())
