# Script: Compute the Convex Hull of a set of points using the Graham Scan
import sys
import numpy as np
import matplotlib.pyplot as plt


def Orientation_test(p1, p2, p3):
    if (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0]):
        return True
    return False


def graham_algorithm(X):
    n = len(X) 
    P = [None] * n
    l = np.where(X[:, 0] == np.min(X[:, 0]))    # select the Bottom-Most Point = lowest y-coordinates
    pointOnHull = X[l[0][0]]
    
    i = 0
    while True:
        P[i] = pointOnHull  # current point, guranteed to belong to C
        
        # pick an end point
        endpoint = X[0]
        for j in range(1, n):
            if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not Orientation_test(X[j], P[i], endpoint):
                endpoint = X[j] 
                
        i = i + 1
        pointOnHull = endpoint
        if endpoint[0] == P[0][0] and endpoint[1] == P[0][1]:
            break
        
    for i in range(n):
        if P[-1] is None:
            del P[-1]
            
    return np.array(P)


def main():
    # Input
    try:
        N = int(sys.argv[1])
    except:
        N = int(input("Introduce N: "))

    # Build a random set of N points with coordinates in [0,300)x[0,300):
    X = np.array([(np.random.randint(0, 300), np.random.randint(0, 300)) for i in range(N)])
    
    # Run lgorithm
    L = graham_algorithm(X)
  
    # Plot the computed Convex Hull:
    plt.figure()
    plt.plot(L[:, 0], L[:, 1], 'b-', picker=5)
    plt.plot([L[-1, 0], L[0, 0]], [L[-1, 1], L[0, 1]], 'b-', picker=5)
    plt.plot(X[:, 0], X[:, 1], ".r")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()