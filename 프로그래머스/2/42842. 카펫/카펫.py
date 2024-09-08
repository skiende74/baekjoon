import math

def solution(brown, yellow):
    mult = brown + yellow
    add = (brown/2+2)
    # a*b, a+b x^2 + (a+b) x + ab = x^2 + add*x + mult. (-add+- sqrt(add^2-4*mult))//2
    
    a = -add/2
    b = math.sqrt(add**2 - 4*mult)/2
    return [-a+b,-a-b]