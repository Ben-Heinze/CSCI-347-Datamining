import numpy as np
import matplotlib.pyplot as plt
import math as m

#Question 1
def q1(dataset):
    print("Question 1 : Scatter plot of Dataset")
    x = [i[0] for i in dataset]
    y = [i[1] for i in dataset]
    plt.scatter(x,y)
    plt.xlabel("X1 Attributes")
    plt.ylabel("X2 Attributes")
    plt.show()

#Question2
def q2(A, dataset):
    print("Question 2 : Linear Transformations on A")
    result = []
    for num, vector in enumerate(dataset,1):
        x_i = np.matrix([vector[0], vector[1]]).reshape((2,1))
        print("x_"+str(num)+" transformation:")
        ans = np.dot(A, x_i)
        result.append(ans)
        print(ans)
    return result

def q3(dataset, Tdataset):
    print("Question 3 : Scatter plot of dataset against Transformed dataset")
    #original x's and y's
    x = [i[0] for i in dataset]
    y = [i[1] for i in dataset]
    #transformed x's and y's
    xt = [i[0] for i in Tdataset]
    yt = [i[1] for i in Tdataset]

    plt.scatter(x,y, c= "b", label="Original")
    plt.scatter(xt,yt, c = "r", label = "Transformed")
    plt.xlabel("X AXIS")
    plt.ylabel("Y AXIS")
    plt.legend(loc = "upper left")
    plt.show()
    
#Question 4 multi variate mean
def q4(dataset):
    print("Question 4 : Multi-variate Mean of data")
    col1 = sum([i[0] for i in dataset])/len(dataset)
    col2 = sum([i[1] for i in dataset])/len(dataset)
    result = [col1, col2]
    print(result)
    return result

def q5(dataset, mvm):
    print("Question 5 : Mean-Centered Dataset")
    meanCenteredDS = []
    for i in dataset:
        centeredx1 = i[0]-mvm[0] #subracts mean from point
        centeredx2 = i[1]-mvm[1]
        meanCenteredDS.append([centeredx1,centeredx2])
    print(meanCenteredDS)
    return meanCenteredDS

def q6(dataset, centeredDS):
    print("Question 6 : Scatter plot of Dataset against Mean-Centered Dataset")
    #original x's and y's
    x = [i[0] for i in dataset]
    y = [i[1] for i in dataset]
    #transformed x's and y's
    xt = [i[0] for i in centeredDS]
    yt = [i[1] for i in centeredDS]

    plt.scatter(x,y, c= "b", label="Original")
    plt.scatter(xt,yt, c = "r", label = "Mean-centered")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.legend(loc = "upper left")
    plt.show()

#Question 7: sample covariance of dataset
def q7(dataset):
    print("Question 7 : Sample Covariance of Dataset")
    ds = np.array(dataset)
    result = np.cov(ds,rowvar=False)
    #rowvar=false calculates using cols instead of rows (default)
    print(result)
    return result

def q8(centeredDS):
    print("Question 8 : Sample Covariance of Centered Dataset")
    cds = np.array(centeredDS)
    result = np.cov(cds,rowvar=False)
    print(result)
    return result

def q9(dataset):
    print("Question 9 : Sample Covariance of Dataset after Standard Normalization")
    ds = np.array(dataset)
    result = np.cov(ds,rowvar=False, bias=True)
    #bias=true sets cov denominator to N instead of N-1 for normalization purposes
    print(result)
    return result

def main():
    #part 2 data:
    A = np.matrix([[(m.sqrt(3)/2) ,-0.5], [0.5, (m.sqrt(3)/2)]])
    dataset = [[1, 1.5], [1,2], [3,4],[-1,-1], [-1,1], [1,-2],[2,2],[2,3]]
    
    q1(dataset)
    tDS = q2(A,dataset)
    q3(dataset, tDS)
    multiVarMean = q4(dataset)
    centeredDS = q5(dataset, multiVarMean)
    q6(dataset, centeredDS)
    q7(dataset)
    q8(centeredDS)
    q9(dataset)
main()