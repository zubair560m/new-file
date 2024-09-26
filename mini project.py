movies =[
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
Additional_movies=int(input("Enter the number of additional movies: "))
for i in range(Additional_movies):
    name=input("Enter the movie name: ")
    budget=int(input("Enter the movie budget: "))
    movies.append((name,budget))
total_budget=sum(budget for _, budget in movies)
average_budget=total_budget/len(movies)
print("Total budget:", total_budget)
print("Average budget:", average_budget)
high_budget_movies=[]
for name, budget in movies:
    if budget > average_budget:
        difference=budget-average_budget
        high_budget_movies.append((name, difference))
        print(f"{name} has a budget that is {difference} above the average")
        
print("High budget movies:", high_budget_movies)
