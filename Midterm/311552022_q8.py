import math
def ExtendedEuclideanAlgorithm(a, b, s1 = 1, s2 = 0, t1 = 0, t2 = 1):
   if b == 0 :
      return abs(a), 1, 0
   q = math.floor(a/b)
   r = a - q * b
   s3 = s1 - q * s2
   t3 = t1 - q * t2
   return (abs(b), s2, t2) if (r == 0) else ExtendedEuclideanAlgorithm(b, r, s2, s3, t2, t3)
a = 48
b = 13
gcdAandB, x, y = ExtendedEuclideanAlgorithm(a, b)
if y < 0:
    x -= b
    y += a
print("d:", y)
