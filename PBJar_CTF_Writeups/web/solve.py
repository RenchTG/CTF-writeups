min_limit = 133791015
max_limit = 133791027

halfway = int(((max_limit - min_limit) / 2) + min_limit)

print("Version can be: " + str(min_limit))
print("Version can't be: " + str(max_limit))
print("In the middle: " + str(halfway))