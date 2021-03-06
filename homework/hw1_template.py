# Please do not use other libraries except for numpy
import numpy as np


class MyRidge:

    def __init__(self):
        self.intercept = 0
        self.coef = None

    def fit(self, X, y, coef_prior=None, lmbd=1.0):

        n, m = X.shape

        lmbd = lmbd * n

        if coef_prior == None:
            coef_prior = np.zeros(m)

        # Normalize X
        # [Question 1] Explain why in the comments (10 pt)
        x_mu = np.mean(X, axis=0)
        x_sigma = np.std(X, axis=0)
        X = (X - x_mu)/x_sigma # normalized X

        # Scale coef_prior based on the standard dev. of X
        # [Question 2] Explain Explain why in the comments (10 pt)
        coef_prior = coef_prior * x_sigma

        # [Question 3] Derive an equation for getting the coefficient (20 pt)
        intercept = np.mean(y)
        coef = ... # HERE, you should find the coef

        # Re-scale coef for the original X scale (not normalized)
        # [Question 4] Explain why in the comments (10 pt)
        self.intercept = intercept - np.sum(coef * x_mu / x_sigma)
        self.coef = coef / x_sigma

        return 0

    def get_coef(self):
        return self.intercept, self.coef


def test_myridge():

    # [Question 5] Import your Ridge class (5 pt)

    # [Question 6] Import a test dataset (5 pt)

    # [Question 7] Set coef_prior=None, and check if it gives the same results as 
    # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html
    # (20 pt)

    # [Question 8] Set coef_prior != None, and change lmbd from 0 to 1000
    # Describe how estimated coefficients change, and explain why in the comments. (20 pt)



if __name__ == "__main__":
    
    test_myridge()