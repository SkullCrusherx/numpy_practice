import numpy as np

a = np.arange(6).reshape(2,3)

print(a)

it = np.nditer(a, flags=['external_loop'])
for x in it:
    print(x)