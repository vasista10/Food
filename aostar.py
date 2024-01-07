import csv
file = open(r"C:\Users\shash\Downloads\Lab1data_new.csv") # Read CSV data
data = list(csv.reader(file)) # Convert into list format
length = len(data[0]) - 1 # -1 because we don't need the target variable
h = ['0'] * length # Initial hypothesis
print("Initial Hypothesis:", h)
print('Data:')
for i in data:
    print(i)
col = data.pop(0) # Removing the column names
for i in range(len(data)):
    if data[i][length] == 'yes': # Considering only the positive examples
        for j in range(len(data[i]) - 1): # Not considering the target variable
            if h[j] == '0':
                h[j] = data[i][j] # If 0 then copy the data
            if h[j] != data[i][j]: # If not equal to the previous hypothesis,then put '?'
                h[j] = '?'
print("Final Hypothesis (Most Specific):", h)