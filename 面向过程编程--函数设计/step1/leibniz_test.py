import math
from leibniz import *


data = int(input())
if data == 1000:
    print(estimate_pi_by_leibniz())
else:
    print(estimate_pi_by_leibniz(data))