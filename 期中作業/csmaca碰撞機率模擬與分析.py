import numpy as np
import random
import matplotlib.pyplot as plt

def simulate_collision_probability(N, CW, trials=10000):
    collisions = 0
    
    for _ in range(trials):
        # 1 & 2. 每個節點隨機選一個 backoff (0 ~ CW)
        backoffs = [random.randint(0, CW) for _ in range(N)]
        
        # 3. 找出最小值
        min_val = min(backoffs)
        
        # 檢查有多少個節點選到同一個最小值
        count_min = backoffs.count(min_val)
        
        # 如果大於一個節點選到最小值，則發生碰撞
        if count_min > 1:
            collisions += 1
            
    return collisions / trials

def theoretical_collision_probability(N, CW):
    # 理論公式：P(Success) = Sum_{k=0 to CW} [ N * (1/W) * ((W-1-k)/W)^(N-1) ]
    # 其中 W = CW + 1 (可能的選擇總數)
    W = CW + 1
    p_success = 0
    for k in range(W):
        # 恰好有一個節點選到 k，且其他節點選到比 k 大的值
        term = N * (1/W) * ((W - 1 - k) / W)**(N - 1)
        p_success += term
    
    return 1 - p_success

def main():
    # 設定參數
    node_list = range(2, 51, 2)  # 節點數從 2 到 50
    CW = 31                      # 假設固定競爭窗口為 31 (即 32 個 slots)
    trials = 10000               # 每次模擬重複一萬次
    
    sim_results = []
    theory_results = []
    
    print(f"{'Nodes':<10} | {'Simulated P(coll)':<20} | {'Theoretical P(coll)':<20}")
    print("-" * 55)
    
    for n in node_list:
        # 模擬
        p_sim = simulate_collision_probability(n, CW, trials)
        sim_results.append(p_sim)
        
        # 理論計算
        p_theory = theoretical_collision_probability(n, CW)
        theory_results.append(p_theory)
        
        print(f"{n:<10} | {p_sim:<20.4f} | {p_theory:<20.4f}")
    
    # 4. 畫圖比較
    plt.figure(figsize=(10, 6))
    plt.plot(node_list, sim_results, 'bo', label='Simulation (10,000 trials)', markersize=8, alpha=0.6)
    plt.plot(node_list, theory_results, 'r-', label='Theoretical Analysis', linewidth=2)
    
    plt.title('CSMA/CA Collision Probability Simulation vs. Analysis')
    plt.xlabel('Number of Nodes (N)')
    plt.ylabel('Probability of Collision')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()
