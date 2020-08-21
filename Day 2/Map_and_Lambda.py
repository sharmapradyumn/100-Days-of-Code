# Problem Url: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    a=[0,1]
    # return a list of fibonacci numbers
    for i in range(1,n-1):
        a.append(a[i-1]+a[i])
    return a
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
