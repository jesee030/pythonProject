import math
from bbp import *
 
data = int(input())
if data == 1000:
	print(estimate_pi_by_bbp())
else:
	print(estimate_pi_by_bbp(data))