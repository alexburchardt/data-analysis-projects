# 1. Declare and assign the variables here:
Name_of_the_space_shuttle = "Determination"
Shuttle_speed = 17500
Distance_to_Mars = 225000000
Distance_to_the_moon = 384400
Miles_per_kilometer = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(Name_of_the_space_shuttle))
print(type(Shuttle_speed))
print(type(Distance_to_Mars))
print(type(Distance_to_the_moon))
print(type(Miles_per_kilometer))

# Code your solution to exercises 3 and 4 here:
miles_to_Mars = Distance_to_Mars * Miles_per_kilometer
hours_to_Mars = miles_to_Mars/Shuttle_speed
days_to_Mars = hours_to_Mars/24

print(Name_of_the_space_shuttle,"will take",str(days_to_Mars),"days to reach Mars.")

# Code your solution to exercise 5 here
miles_to_moon = Distance_to_the_moon * Miles_per_kilometer
hours_to_moon = miles_to_moon/Shuttle_speed
days_to_moon = hours_to_moon/24

print(Name_of_the_space_shuttle, "will take", str(days_to_moon), "days to reach the moon.")