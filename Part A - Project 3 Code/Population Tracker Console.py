start_pop = int(input("Starting number of organisms: "))
growth_rate = int(input("The average daily population increase (as a percentage): ").strip().replace('%', ''))
days = int(input("Number of days the organisms will be left to multiply: "))
new_growth_rate = (growth_rate / 100) + 1

print("Day Approximation\t Population")
for i in range(1, (days + 1)):
    new_growth = (start_pop * new_growth_rate) - start_pop
    start_pop += new_growth
    rounded_pop = round(start_pop, 5)
    print(f"{i}\t                 {rounded_pop}")
