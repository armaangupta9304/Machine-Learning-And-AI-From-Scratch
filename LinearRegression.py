import numpy as np

class LinearRegression:
    def __init__(self, input_shapes, lr=0.1):

        # At the time of initialization we will ask the user for the shape of the input user will be given
        self.input_shapes = input_shapes

        # Since their can be a lot of dimensions involved we gonna use numpy matrices and at first we will initialize them randomly
        self.m = np.random.randn(input_shapes) 

        # Coef value since there formula is something like y = sum(m * x) + b we dont need much bias values we just need one of them
        self.b = np.random.randn(1)

        # we might need a learning rate value at the time of adjusting the slope and coef so why not take it here only
        self.lr = lr

    def predict(self, x):

        # The formula to calculate y is { y = sum(m * x) + b }
        output = sum(self.m * x) + self.b

        return output

    

