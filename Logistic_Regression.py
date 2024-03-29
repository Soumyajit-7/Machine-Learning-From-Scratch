import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class LogisticRegression():
    def __init__(self,L=0.001,epochs=10000):
        self.L = L
        self.epochs = epochs
        self.w = None
        self.b = None


    def fit(self,X, y):

        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0
        for i in range(self.epochs):
            if i % 50 == 0:
                print(f'Epoch: {i} / {self.epochs}')
            linear_pred  = np.dot(X, self.w) + self.b
            predictions = sigmoid(linear_pred)

            dw = (1/n_samples) * np.dot(X.T, (predictions - y))
            db = (1/n_samples) * np.sum(predictions - y)

            self.w = self.w - self.L * dw
            self.b = self.b - self.L * db



    def predict(self, X):
        linear_pred = np.dot(X, self.w) + self.b
        y_pred = sigmoid(linear_pred)
        class_pred = [0 if y<= 0.5 else 1 for y in y_pred]
        return class_pred
