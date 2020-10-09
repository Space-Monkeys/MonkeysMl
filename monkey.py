import numpy as np
import sklearn.neural_network

class Model:
    def __init__(self):
        self.model = sklearn.neural_network.MLPClassifier(
                activation='logistic',
                max_iter=100,
                hidden_layer_sizes=(2,),
                solver='lbfgs')
    def train(self):
        inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
        expected_output = np.array([0,0,0,1])
        self.model.fit(inputs, expected_output)

    def test(self):
        print(self.model.predict([[0,1],[0,0],[1,0],[1,1]]))

    def predict(self, n):
        result = self.model.predict([[0,1],n,[1,0],[1,1]])
        return result[1]