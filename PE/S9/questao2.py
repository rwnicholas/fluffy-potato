#!/usr/bin/python3

import numpy as np
from numpy.core.fromnumeric import mean
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

#### 2 Questão ####
data = pd.read_csv("data/record_data.csv")
y = data[['obs1', 'obs2', 'obs3']]
x = np.array(data['size']).reshape((-1,1))

Y = np.array(np.mean(y, axis=1)).reshape(8,1)

model = LinearRegression().fit(x, Y)

## 2.a Questão
def quest2aTest1():
    sm.qqplot((Y-model.predict(x)))
    plt.tight_layout()
    plt.savefig('fig2aTest1.png')
    plt.close()

def quest2aTest2():
    plt.xlabel("Record Size")
    plt.ylabel("Observations (mean)")

    print("\n## 2.a Questão")
    plt.scatter(x, Y, color='r')
    plt.savefig('fig2aTest2.png')

## 2.b Questão
def quest2b():
    print("\n## 2.b Questão")
    predicts = model.predict(x)
    plt.plot(x, predicts, color='k')
    plt.tight_layout()
    plt.savefig('fig2b.png')
    plt.close()

## 2.c Questão
def quest2c():
    print("\n## 2.c Questão")
    print("Porcentagem de variação:", model.score(x, Y))

## 2.d Questão
def quest2d():
    print("\n## 2.d Questão")
    print('Confiança de 90% para b0:', sm.OLS(Y, sm.add_constant(x)).fit().conf_int(0.1)[0])
    print('Confiança de 90% para b1:', sm.OLS(Y, sm.add_constant(x)).fit().conf_int(0.1)[1])

def quest2dTeste1():
    plt.title("Tendência do Espalhamento")
    plt.xlabel("ŷ")
    plt.ylabel("e")
    plt.scatter(model.predict(x), (Y-model.predict(x)))
    plt.tight_layout()
    plt.savefig("fig2dTeste1.png")
    plt.close()

## 2.e Questão
def quest2e():
    print("\n## 2.e Questão")
    modelo = sm.OLS(Y, sm.add_constant(x)).fit()
    var1 = pd.DataFrame([[(2**20)/8, 0]])
    y_pred = np.array(modelo.get_prediction(var1).conf_int(0.1)).reshape(2)
    print("O valor previsto de y está contido no intervalo: (%s, %s)" %(y_pred[0], y_pred[1]))

def main():
    quest2aTest1()
    quest2aTest2()
    quest2b()
    quest2c()
    quest2d()
    quest2dTeste1()
    quest2e()

main()