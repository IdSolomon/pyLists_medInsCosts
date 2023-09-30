# Below are ten names in a list belonging to some members of the X-Men.
# Included, is a list of their medical insurance costs.

names = [
    "Cyclops", 
    "Storm", 
    "Jubilee", 
    "Beast", 
    "Phoenix", 
    "Sunfire", 
    "Ice_Man", 
    "Shadowcat", 
    "Polaris", 
    "Colossus"
]
insuranceCosts = [
    13262.0, 
    4816.0, 
    6839.0, 
    5054.0,
    14724.0, 
    5360.0, 
    7640.0, 
    6072.0, 
    2750.0, 
    12064.0
]

# Appending another X-Man into the lists --

names.append("Emma_Frost")
insuranceCosts.append(8320.0)
print(names)
print(insuranceCosts)

# OUTPUT: ['Cyclops', 'Storm', 'Jubilee', 'Beast', 'Phoenix', 'Sunfire', 'Ice_Man', 'Shadowcat', 'Polaris', 'Colossus', 'Emma_Frost']
# OUTPUT: [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0, 8320.0]

# Using the zip() function to combine insuranceCosts and names into a new variable --

medicalRecords = list(zip(insuranceCosts, names))
print(medicalRecords)

# OUTPUT: [(13262.0, 'Cyclops'), (4816.0, 'Storm'), (6839.0, 'Jubilee'), (5054.0, 'Beast'), (14724.0, 'Phoenix'), (5360.0, 'Sunfire'), (7640.0, 'Ice_Man'), 
# (6072.0, 'Shadowcat'), (2750.0, 'Polaris'), (12064.0, 'Colossus'), (8320.0, 'Emma_Frost')]

# Using the len() function to see how many medical records I'm dealing with --

num_medicalRecords = len(medicalRecords)
print("There are " + str(num_medicalRecords) + " medical records stored.")

# OUTPUT: There are 11 medical records stored.

# Selecting the first medical record --

first_medicalRecord = medicalRecords[0]
print("Here is the first medical record: " + str(first_medicalRecord))

# OUTPUT: Here is the first medical record: (13262.0, 'Cyclops')

# Sorting through the medical records from lowest to highest --

medicalRecords.sort()
print("Here are the medical records sorted by insurance cost: " + str(medicalRecords))

# OUTPUT: Here are the medical records sorted by insurance cost: [(2750.0, 'Polaris'), (4816.0, 'Storm'), (5054.0, 'Beast'), 
# (5360.0, 'Sunfire'), (6072.0, 'Shadowcat'), (6839.0, 'Jubilee'), (7640.0, 'Ice_Man'), (8320.0, 'Emma_Frost'), (12064.0, 'Colossus'), (13262.0, 'Cyclops'), (14724.0, 'Phoenix')]

# Slicing the medical records to find the three cheapest insurance costs --

cheapThree = medicalRecords[:3]
print("Here are the three cheapest insurance costs in the medical records: " + str(cheapThree))

# OUTPUT: Here are the three cheapest insurance costs in the medical records: [(2750.0, 'Polaris'), (4816.0, 'Storm'), (5054.0, 'Beast')]

# Slicing the medical records list once more to find the three most expensive insurance costs --

expensiveThree = medicalRecords[-3:]
print("Here are the three most expensive insurance costs in the medical records: " + str(expensiveThree))

# OUTPUT: Here are the three most expensive insurance costs in the medical records: [(12064.0, 'Colossus'), (13262.0, 'Cyclops'), (14724.0, 'Phoenix')]