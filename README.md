# SimRetain: Decision Support System for HR Analytics

**SimRetain** is a Decision Support System (DSS) designed for Human Resources professionals to predict employee turnover and assess the impact of HR policy interventions. It leverages an **Agent-Based Model** with a **Monte Carlo simulation engine** to forecast attrition rates under different scenario conditions.

---

## Overview

Employee turnover is one of the most significant costs to organizations. SimRetain enables HR teams to:

- **Simulate** 12-month workforce dynamics under various policy scenarios
- **Forecast** cumulative attrition rates with statistical rigor
- **Evaluate** the impact of salary adjustments, burnout reduction, and environmental improvements
- **Calculate** projected turnover costs to inform strategic HR decisions

The system models each employee as an autonomous agent with baseline characteristics (burnout, satisfaction, tenure), applies HR policy modifiers, and uses stochastic decision logic to determine resignation probabilities each month.

---

## Key Features

✅ **Agent-Based Simulation** — 500 individual employee agents with realistic behavioral rules  
✅ **Monte Carlo Engine** — Probabilistic outcome generation with multiple decision triggers  
✅ **Interactive Dashboard** — Real-time policy adjustment and forecast visualization  
✅ **Cost Analytics** — Automatic turnover cost estimation (₱75,000 per departure)  
✅ **Sensitivity Analysis** — Explore impact of compensation, workload, and environment changes  

---

## How It Works

### 1. **The Agent Model**
Each employee is modeled as an agent with:
- **Base Burnout**: Random score (0–100) representing stress/fatigue
- **Base Satisfaction**: Random score (0–100) representing job satisfaction
- **Tenure**: Years of service (0–10)
- **Department**: IT or Engineering (influences dynamics)
- **Status**: Active or Resigned

### 2. **The Simulation Logic**
For each of 12 months:

1. **Apply Policy Modifiers**: Salary changes, burnout interventions, and environment improvements adjust baseline metrics
2. **Calculate Quit Probability**: Base rate (0.5%) is modified by:
   - **Burnout Effect**: High burnout + pay cuts → 15% boost to quit probability
   - **Loyalty Factor**: Tenure >5 years + high satisfaction → 5% reduction
   - **Environment Trigger**: Low satisfaction (<30) → 12% boost

3. **Stochastic Roll**: Random draw determines if agent resigns this month
4. **Accumulate**: Track monthly resignations and running attrition rate

### 3. **Interactive Dashboard**
Streamlit web interface allows HR teams to:
- Adjust **Market Salary Gap** (−20% to +20%)
- Modify **Burnout / Workload Level** (0–100)
- Change **Job Environment** quality (0–100)
- Instantly visualize impact on attrition forecast

---

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

1. **Clone or download the project**
   ```bash
   cd path/to/MAS
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas matplotlib
   ```

3. **Run the dashboard**
   ```bash
   streamlit run app.py
   ```

4. **Access the dashboard**
   - The app opens automatically at `http://localhost:8501`
   - Or manually visit that URL in your browser

---

## Usage

### Running a Scenario

1. **Adjust Policies** in the left sidebar:
   - Increase salary to reduce attrition from pay-related quits
   - Reduce burnout to lower stress-driven resignations
   - Improve environment to boost overall satisfaction

2. **Click "▶ Run Simulation"** to execute a 12-month forecast

3. **Review Results**:
   - **Predicted Attrition (12 Mo)**: Expected % of workforce lost
   - **Staff Remaining**: Headcount after 12 months
   - **Est. Turnover Cost**: Monetary impact in millions of pesos

4. **Examine the Chart**: Line graph shows cumulative attrition trend


### Example Scenarios

**Scenario A: Cost-Cutting**
- Market Salary Gap: −5% (pay reduce)
- Burnout: +20 (stress increases)
- Environment: −10 (morale drops)
- → Expect high attrition

**Scenario B: Strategic Retention**
- Market Salary Gap: +5% (competitive pay)
- Burnout: −30 (workload reduction)
- Environment: +15 (improve culture)
- → Expect low attrition, ROI positive

---

## Project Structure

```
MAS/
├── app.py              # Streamlit dashboard (web UI)
├── test.py             # Simulation engine + standalone runner
├── README.md           # This file
├── index.html          # (Optional) Static page
├── presentation.html   # (Optional) Presentation slides
└── sample.html         # (Optional) Sample data
```

### File Descriptions

**app.py**
- Streamlit web application
- Interactive sidebar for policy inputs
- Real-time simulation execution
- Dashboard KPI display and charting

**test.py**
- Core simulation engine (`run_simretain` function)
- Agent class definition
- Standalone script for batch runs and debugging

---

## Technical Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit 1.x |
| **Computation** | Python 3.8+ |
| **Data Processing** | Pandas |
| **Visualization** | Matplotlib, Streamlit Charts |
| **Simulation** | Monte Carlo (Python `random` module) |

---

## Model Parameters

| Parameter | Range | Default | Effect |
|-----------|-------|---------|--------|
| Market Salary Gap | −20% to +20% | 0% | Affects satisfaction and quit probability |
| Burnout / Workload | 0–100 | 50 | Centered at 0; positive = high stress |
| Job Environment | 0–100 | 50 | Centered at 0; positive = better culture |
| Workforce Size | 500 | 500 | Number of agents in simulation |
| Simulation Months | 12 | 12 | Forecast horizon |

---

## Limitations & Assumptions

⚠️ **Assumptions**
- Employee decisions are independent (no contagion effects)
- Baseline stats are uniformly distributed
- Policy effects are linear and additive
- External factors (market downturns, acquisitions) are not modeled
- Cost per departure is fixed at ₱75,000

⚠️ **Limitations**
- Model is stylized; real organizational dynamics are more complex
- Results are probabilistic — actual outcomes will vary
- Historical validation against real HR data recommended before deployment
- Does not account for rehiring, internal transfers, or seasonal patterns

---

## Future Enhancements

- [ ] Non-linear policy effects and interaction terms
- [ ] Department-specific parameters and turnover rules
- [ ] Historical data calibration and sensitivity testing
- [ ] Probability threshold visibility for resignation decisions
- [ ] Export simulation data to CSV/Excel
- [ ] Multi-year forecasting with cohort analysis
- [ ] Integration with HR information systems (HRIS)

---

## License

This project is provided as-is for educational and organizational use.

---

## Contact & Support

For questions, feedback, or improvements, please reach out to your HR analytics team.

---

**Last Updated**: April 2026  
**Version**: 1.0
