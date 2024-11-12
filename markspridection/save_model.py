import pickle
from sklearn.linear_model import LinearRegression

# Example data for training (MST 1 and MST 2 marks, and 3rd MST marks)
X_train = [[10, 20], [15, 30], [20, 40], [25, 50]]  # Replace with actual data
y_train = [25, 30, 35, 40]  # Replace with actual 3rd MST marks

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model to a file
with open('marksmodel.pickle', 'wb') as f:
    pickle.dump(model, f)

print("Model has been trained and saved successfully!")
