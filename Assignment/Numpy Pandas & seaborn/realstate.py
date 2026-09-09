import numpy as np
brokered_by,price  ,bed ,bath  = np.genfromtxt('RealEstate-USA.csv', delimiter=',', usecols=(2,3,4,5), unpack=True, dtype=None,skip_header=1)
print(brokered_by);
print(price)
print(bed)
print(bath)
#statistic operation 
print("USA Realstate price mean",np.mean(price))
print("USA Realstate price average", np.average(price))
print("USA Realstate price std",np.std(price))
print("USA Realstate price mod",np.median(price))
print("USA Realstate price min",np.min(price))
print("USA Realstate price max",np.max(price))
#Math  Operation
print("USA Realstate price  Square:",np.square(price)  )
print("USA Realstate price sqrt:",np.sqrt(price))
print("USA Realstate price power",np.power( np.absolute(price),np.absolute(price)))
print("USA Realstate price abs",np.abs(price))
