import random
import math
import numpy as np

# Hàm mục tiêu f(x, y) = x^2 + y^2 + 5sin(x) + 5cos(y)
def objective_function(x, y):
    return x**2 + y**2 + 5 * math.sin(x) + 5 * math.cos(y)

# Thuật toán Simulated Annealing để tối ưu hóa hàm
def simulated_annealing():
    # Khởi tạo giá trị ban đầu ngẫu nhiên
    current_x = random.uniform(-10, 10)
    current_y = random.uniform(-10, 10)
    current_cost = objective_function(current_x, current_y)
    
    # Nhiệt độ ban đầu và tỷ lệ giảm nhiệt độ
    T = 1000
    cooling_rate = 0.995
    min_temp = 0.01
    
    best_x, best_y = current_x, current_y
    best_cost = current_cost
    
    while T > min_temp:
        # Tạo trạng thái mới bằng cách thay đổi x, y ngẫu nhiên
        new_x = current_x + random.uniform(-0.5, 0.5)
        new_y = current_y + random.uniform(-0.5, 0.5)
        new_cost = objective_function(new_x, new_y)
        
        # Tính toán sự khác biệt giữa chi phí mới và cũ
        cost_diff = new_cost - current_cost
        
        # Nếu chi phí mới tốt hơn hoặc xác suất chấp nhận trạng thái xấu hơn
        if cost_diff < 0 or random.random() < math.exp(-cost_diff / T):
            current_x, current_y = new_x, new_y
            current_cost = new_cost
            
            # Cập nhật giá trị tốt nhất
            if new_cost < best_cost:
                best_x, best_y = new_x, new_y
                best_cost = new_cost
        
        # Giảm nhiệt độ
        T *= cooling_rate
    
    # Trả về kết quả tối ưu
    return best_x, best_y, best_cost

# Chạy thuật toán SA và in kết quả
best_x, best_y, best_cost = simulated_annealing()
print(f"Best solution: x = {best_x}, y = {best_y}")
print(f"Best cost: {best_cost}")
