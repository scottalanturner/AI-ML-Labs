from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a decision tree classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Save the model to a pickle file
joblib.dump(model, 'iris_model.pkl')
print("Model saved as iris_model.pkl")