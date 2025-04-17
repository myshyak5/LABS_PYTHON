import numpy as np
import scipy.linalg as sl
import scipy.stats as ss
import time

N = int(input())
D = int(input())

X = np.random.rand(N, D)
m = np.random.rand(D)
C = np.random.rand(D, D)
C = np.dot(C, C.T)

C_inv = sl.inv(C)
C_det = sl.det(C)

const = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(C_det)

logp_custom = np.zeros(N)
start_time = time.time()
for i in range(N):
    diff = X[i] - m
    logp_custom[i] = const - 0.5 * np.dot(diff.T, np.dot(C_inv, diff))
custom_time = time.time() - start_time

start_time = time.time()
logp_scipy = ss.multivariate_normal(m, C).logpdf(X)
scipy_time = time.time() - start_time

print(f"Проверка точности вычислений: {np.max(np.abs(logp_custom - logp_scipy))}")
print(f"Скорость своей функции: {custom_time}")
print(f"Скорость SciPy функции: {scipy_time}")