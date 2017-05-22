from math import sqrt
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
import numpy as np

def validate(real, pred, max_lags= 168, name = "Unnamed method"):
    print("----------------------------------")
    print("{0} validation summary".format(name))
    print("-----------------------------------")
    residuals = real - pred
    rmse_stat(residuals)
    residuals_stat(residuals, max_lags)

def rmse_stat(residuals):
    rmse =  sqrt(sum(residuals ** 2) / len(residuals) )
    print("RMSE = {0}".format(rmse))

def residuals_stat(residuals, max_lags):
    print("residuals sum = {0}".format(sum(residuals)))
    plot_acf(residuals, lags = max_lags)
    plt.show()
    bins = 25
    plt.hist(residuals, bins, alpha = 0.8)
    plt.title('residuals distribution')
    plt.show()
