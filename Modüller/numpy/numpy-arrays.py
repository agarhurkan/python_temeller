import numpy as np

result = np.array([1,3,5,7,9])
result = np.arange(1,10)
result = np.arange(10,150,13)
result = np.ones(10)
result = np.linspace(0,100,4)
result = np.linspace(0,5,6)
result = np.random.randint(0,10,5)
result = np.random.randint(20)
result = np.random.rand(5,10)
result = np.random.rand(5)
result = np.arange(0,100,2)
result = result.reshape(10,5)

# print(result.sum(axis=1))
# print(result.sum(axis=0))
result = np.random.randint(1,100,10)
print(result)

result = result.max()

print(result)