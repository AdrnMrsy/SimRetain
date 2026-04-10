import random
import pandas as pd
import matplotlib.pyplot as plt

class EmployeeAgent:
    def __init__(self, agent_id):
        self.id = agent_id
        # Assign random baseline stats for Monte Carlo variance
        self.base_burnout = random.uniform(0, 100)
        self.base_sat = random.uniform(0, 100)
        self.tenure = random.uniform(0, 10) # 0 to 10 years
        self.status = 'active'
        self.department = random.choice(['IT', 'Engineering'])

def run_simretain(num_agents=500, salary_mod=0, burnout_mod=0, env_mod=0):
    # Initialize the workforce
    agents = [EmployeeAgent(i) for i in range(num_agents)]
    
    total_resigned = 0
    monthly_data = []

    print("--- SimRetain: 12-Month Agent-Based Simulation ---")
    print(f"Parameters: Salary Gap={salary_mod}%, Burnout Mod={burnout_mod}, Env Mod={env_mod}\n")

    for month in range(1, 13):
        resigned_this_month = 0
        
        for agent in agents:
            if agent.status == 'resigned':
                continue # Skip if they already quit
                
            # Apply HR policy modifiers to baseline stats
            current_burnout = agent.base_burnout + burnout_mod
            current_sat = agent.base_sat + env_mod + (salary_mod * 1.5)
            quit_chance = 0.005 
            if current_burnout > 75 and salary_mod < 0:
                quit_chance += 0.15 # +15% chance
            elif current_burnout > 85:
                quit_chance += 0.10
            if agent.tenure > 5 and current_sat > 70:
                quit_chance -= 0.05 
            if current_sat < 30:
                quit_chance += 0.12 
            quit_chance = max(0.0, quit_chance) 
            if random.random() < quit_chance:
                agent.status = 'resigned'
                resigned_this_month += 1
                total_resigned += 1
        
        attrition_rate = (total_resigned / num_agents) * 100
        monthly_data.append({
            'Month': month,
            'Resigned_This_Month': resigned_this_month,
            'Total_Resigned': total_resigned,
            'Cumulative_Attrition_Rate': round(attrition_rate, 2)
        })
        
        print(f"Month {month:2d} | Resigned: {resigned_this_month:3d} | Total Lost: {total_resigned:3d} | Attrition: {attrition_rate:5.1f}%")
        
    return agents, monthly_data

final_agents, report = run_simretain(num_agents=500, salary_mod=-5, burnout_mod=20, env_mod=-10)

df = pd.DataFrame(report)
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Cumulative_Attrition_Rate'], marker='o', linestyle='-', color='b', linewidth=2)

plt.title('SimRetain: 12-Month Cumulative Attrition Forecast', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Attrition Rate (%)', fontsize=12)
plt.xticks(range(1, 13)) # Ensure all 12 months show on the X axis
plt.ylim(0, max(30, df['Cumulative_Attrition_Rate'].max() + 5))
plt.grid(True, linestyle='--', alpha=0.7)

final_rate = df['Cumulative_Attrition_Rate'].iloc[-1]
plt.annotate(f'Final: {final_rate}%', 
             xy=(12, final_rate), 
             xytext=(10, final_rate + 2),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=6))

# Show the chart
plt.show()