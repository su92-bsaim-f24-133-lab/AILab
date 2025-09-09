movies = [
    ("Sunshine of the Spotless Mind", 2000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# Add all budgets
total = 0
for movie, budget in movies:
    total += budget

# Get average
average = total / len(movies)


print("Average budget:", average)


print("Big budget movies:")
for movie, budget in movies:
    if budget > average:
        print(movie, ":", budget)