# train_model.py
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generate some sample data
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to a file
import joblib
joblib.dump(model, 'trained_model.pkl')
