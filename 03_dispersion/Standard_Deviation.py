#Step 1 → Find center of data         → Mean = 50
#Step 2 → How far is each value       → [-10, -5, 0, 5, 10]
#Step 3 → Make all positive           → [100, 25, 0, 25, 100]
#Step 4 → Average of those            → Variance = 50
#Step 5 → Undo the squaring           → Std Dev = 7.07

import math as mth 
data = [40, 45, 50, 55, 60]

# Step 1 - Mean

mean = sum(data)/len(data)

# Step 2 - Differences

diff =[]

for value in data:
    diff.append(value-mean)
print(diff)


# Step 3 - Square
square=[]
for differences in diff:
    square.append(differences**2)

# Step 4 - Variance
variance = sum(square) / len(square)
print("Variance:", variance)

# Step 5 - Std Deviation
std_dev = mth.sqrt(variance)
print("Std Dev:", round(std_dev, 2))
    
    