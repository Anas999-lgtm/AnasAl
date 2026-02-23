import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class SimpleNN:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

if __name__ == '__main__':
    # Sample data: hours studied vs. grades
    hours_studied = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
    grades = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    # Create the SimpleNN model
    nn = SimpleNN()
    nn.train(hours_studied, grades)

    # Predicting grades
    predicted_grades = nn.predict(hours_studied)

    # Plotting the results
    plt.scatter(hours_studied, grades, color='blue', label='Actual Grades')
    plt.plot(hours_studied, predicted_grades, color='red', label='Predicted Grades')
    plt.xlabel('Hours Studied')
    plt.ylabel('Grades')
    plt.title('Study Hours vs Grades')
    plt.legend()
    plt.show()