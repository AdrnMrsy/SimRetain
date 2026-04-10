import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

class EmployeeAgent:
    def __init__(self, agent_id):
        self.id = agent_id
        self.base_burnout = random.uniform(0, 100)
        self.base_sat = random.uniform(0, 100)
        self.tenure = random.uniform(0, 10) 
        self.status = 'active'
        self.department = random.choice(['IT', 'Engineering'])

def run_simretain(num_agents=500, salary_mod=0, burnout_mod=0, env_mod=0):
    agents = [EmployeeAgent(i) for i in range(num_agents)]
    total_resigned = 0
    monthly_data = []

    for month in range(1, 13):
        resigned_this_month = 0
        for agent in agents:
            if agent.status == 'resigned':
                continue
                
            current_burnout = agent.base_burnout + burnout_mod
            current_sat = agent.base_sat + env_mod + (salary_mod * 1.5)
            
            quit_chance = 0.005 
            
            if current_burnout > 75 and salary_mod < 0:
                quit_chance += 0.15 
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
            'Month_Label': f"Month {month}",
            'Cumulative_Attrition_Rate': round(attrition_rate, 2)
        })
        
    return monthly_data

st.set_page_config(page_title="SimRetain Dashboard", layout="wide")

st.title("SimRetain: Executive Dashboard")
st.markdown("Agent-Based Predictive Simulation for IT & Engineering")

st.sidebar.header("Policy Adjustments")
salary_slider = st.sidebar.slider("Market Salary Gap (%)", -20, 20, 0)
burnout_slider = st.sidebar.slider("Burnout / Workload Level", 0, 100, 50) - 50 # Centered at 0
env_slider = st.sidebar.slider("Job Environment", 0, 100, 50) - 50

if st.sidebar.button("▶ Run Simulation", type="primary"):
    
    report = run_simretain(num_agents=500, salary_mod=salary_slider, burnout_mod=burnout_slider, env_mod=env_slider)
    df = pd.DataFrame(report)
    
    final_rate = df['Cumulative_Attrition_Rate'].iloc[-1]
    staff_remaining = 500 - int((final_rate / 100) * 500)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Predicted Attrition (12 Mo)", f"{final_rate}%")
    col2.metric("Staff Remaining", f"{staff_remaining} / 500")
    
    cost = ((500 - staff_remaining) * 75000) / 1000000
    col3.metric("Est. Turnover Cost", f"₱{cost:.1f}M")

    st.subheader("12-Month Cumulative Attrition Forecast")
    st.line_chart(df.set_index('Month')['Cumulative_Attrition_Rate'])
    st.caption("Month values are plotted numerically (1-12) to preserve proper sequence.")
    
else:
    st.info("👈 Adjust the policies in the sidebar and click 'Run Simulation' to generate the forecast.")