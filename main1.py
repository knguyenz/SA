import math
import random
import numpy as np

# Hàm chi phí (Objective Function): f(x) = x^2 - 4x + 4
def objective_function(x):
    return x**2 - 4*x + 4

# Sửa thuật toán SA để chạy một số vòng lặp cố định
def simulated_annealing():
    current_solution = random.uniform(-10, 10)  # Giá trị ngẫu nhiên trong khoảng [-10, 10]
    current_cost = objective_function(current_solution)
    
    T = 1000
    cooling_rate = 0.99
    min_temp = 0.01
    max_iterations = 10000  # Tăng số vòng lặp để thuật toán có nhiều thời gian hơn
    
    iterations = 0
    while T > min_temp and iterations < max_iterations:
        new_solution = current_solution + random.uniform(-1, 1)
        new_cost = objective_function(new_solution)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current_solution = new_solution
            current_cost = new_cost
        
        T *= cooling_rate
        iterations += 1
    
    return current_solution, current_cost

# Chạy thuật toán SA và lấy kết quả
best_solution, best_cost = simulated_annealing()

# In kết quả cuối cùng
print("Best solution found:", best_solution)
print("Objective function at best solution:", best_cost)
