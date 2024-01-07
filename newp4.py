import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Read the dataset
data = pd.read_csv(r"C:\Users\shash\Downloads\Lab3data.csv")

# One-hot encode categorical variables
data = pd.get_dummies(data, columns=['Outlook', 'Temperature', 'Humidity', 'Wind'])

# Features and target variable
X = data.drop('PlayTennis', axis=1)
y = data['PlayTennis']

# Build the decision tree model
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

# Display the decision tree
tree_rules = export_text(model, feature_names=list(X.columns))
print("Decision Tree:")
print(tree_rules)

# Classify a new sample
def classify_sample(instance):
    instance = instance.split(',')
    instance_dict = {}
    for i, column in enumerate(X.columns):
        if i < len(instance):
            instance_dict[column] = instance[i]
        else:
            instance_dict[column] = 0  # If the value is missing, assume 0 for simplicity
    instance_df = pd.DataFrame(instance_dict, index=[0])
    instance_df = pd.get_dummies(instance_df)
    
    # Align the columns of instance_df with X to ensure consistency
    instance_df = instance_df.reindex(columns=X.columns, fill_value=0)
    
    prediction = model.predict(instance_df)
    return prediction[0]

# Take user input for the test instance
user_input = input("Enter a test instance (comma-separated values): ")
output_class = classify_sample(user_input)
print(f"User Input: {user_input}")
print(f"Output Class: {output_class}")