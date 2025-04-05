import random
import math
import numpy as np

# Hàm tính quãng đường giữa hai thành phố (dùng khoảng cách Euclid)
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Hàm tính tổng quãng đường của một chuỗi
def total_distance(cities, path):
    dist = 0
    for i in range(len(path) - 1): # trừ 1 vì không cần tính quãng đường quay lại điểm xuất phát
        dist += distance(cities[path[i]], cities[path[i + 1]])
    dist += distance(cities[path[-1]], cities[path[0]])  # Quay lại điểm xuất phát
    return dist

# Thuật toán Simulated Annealing cho TSP
def simulated_annealing(cities):
    # Khởi tạo đường đi ngẫu nhiên
    current_path = list(range(len(cities))) # Danh sách các chỉ số thành phố
    random.shuffle(current_path) # Đảo ngẫu nhiên thứ tự các thành phố
    
    current_distance = total_distance(cities, current_path) 
    
    # Nhiệt độ ban đầu và tỷ lệ giảm nhiệt độ
    T = 1000
    cooling_rate = 0.995
    min_temp = 0.01
    
    while T > min_temp:
        # Tạo trạng thái mới bằng cách hoán đổi hai thành phố
        new_path = current_path[:]
        i, j = random.sample(range(len(cities)), 2)  # Chọn hai thành phố ngẫu nhiên để hoán đổi
        new_path[i], new_path[j] = new_path[j], new_path[i]
        
        new_distance = total_distance(cities, new_path)
        
        # Nếu đường đi mới tốt hơn, chấp nhận nó
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / T):
            current_path = new_path
            current_distance = new_distance
    
        # Giảm nhiệt độ
        T *= cooling_rate
    
    return current_path, current_distance

# Ví dụ với 5 thành phố
cities = [(0, 0), (1, 3), (4, 3), (6, 1), (2, 0)]  # Các thành phố (x, y)

# Chạy Simulated Annealing cho TSP
best_path, best_distance = simulated_annealing(cities)

print("Best path:", best_path)
print("Best distance:", best_distance)
