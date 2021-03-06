from predictor import Predictor
import numpy as np


class LinearRegressionMAP(Predictor):
    def __init__(self):
        self.weights = None

    def train(self, train_x, train_y, lambd):
        bias = np.ones((train_x.shape[0], 1))
        X = np.concatenate((train_x, bias), axis = 1)
        self.weights = np.linalg.inv(X.T.dot(X) + lambd*np.eye(X.shape[1])).dot(X.T).dot(train_y)
        

    def predict(self, test_x):
        bias = np.ones((test_x.shape[0], 1))
        X = np.concatenate((test_x, bias), axis = 1)
        return X.dot(self.weights)
        
    

