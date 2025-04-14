# Global Space Exploration Analysis (2000–2024)

## 1. Objective
To analyze and visualize global space mission data from 2000 to 2024, uncovering insights into budget trends, mission success, collaboration patterns, and environmental impact. The project includes an interactive Streamlit dashboard for real-time data exploration.

---

## 📦 2. Dataset Information
- **File Name**: Global_Space_Exploration_Dataset.csv  
- **Format**: CSV  
- **Rows**: 10,000+  
- **Columns**: 12  
- **Time Period**: 2000–2024  

*(See earlier version for column breakdown)*

---

## 📌 3. Functional Requirements

### 📊 3.1 Exploratory Data Analysis (EDA)
- Data cleaning
- Summaries
- Charts

### 🧠 3.2 Insights & Correlation
- Budget vs Success Rate (scatter)
- Duration vs Success Rate
- Technology frequency
- Environmental Impact trends
- Collaboration patterns and network

### 📈 3.3 Time Series Forecasting (Prophet / ARIMA)
- Forecast future mission count and budgets

### 🧪 3.4 Hypothesis Testing
- Collaborative success rate comparison
- Post-2015 tech performance

### ⚙️ 3.5 Clustering (K-Means)
- Cluster missions by budget, duration, success rate

---

## 🖥️ 4. Streamlit Dashboard (Core MVP)

### 4.1 General Structure

#### Sidebar Controls:
- Year Range Slider (2000–2024)
- Country Multiselect
- Mission Type Dropdown
- Satellite Type Dropdown
- Checkbox: Collaborative Missions Only
- Toggle: Environmental Friendly Missions

#### Main Tabs (Streamlit Tabs or Expanders):
1. **Overview**
   - KPIs: Total Missions, Avg Budget, Avg Success Rate
   - Bar Chart: Missions by Country
   - Line Chart: Missions Over Time

2. **Budget & Success**
   - Scatter Plot: Budget vs. Success Rate
   - Boxplot: Budget by Country
   - Line/Bar Chart: Avg Budget per Year

3. **Mission Duration & Type**
   - Histogram: Mission Duration Distribution
   - Grouped Bar: Avg Duration by Type
   - Pie Chart: Satellite Types

4. **Collaboration Analysis**
   - Network Graph of Collaborating Countries
   - Bar Chart: Top Country-Pairs
   - KPI: Collaborative vs Solo Missions

5. **Technology & Environmental**
   - Word Cloud: Technologies Used
   - Line Chart: Avg Environmental Impact Over Time
   - Bar: Missions per Environmental Impact Level

6. **ML Insights**
   - Cluster Explorer (3D scatter with clusters)
   - Download CSV with cluster labels
   - Forecast Chart (Prophet Output)

---

## 📂 5. Deliverables
- `cleaned_space_missions.csv`
- `eda_report.ipynb`
- `insight_modeling.ipynb`
- `app.py` (Streamlit dashboard)
- Final Report (PDF)
- `README` + `Requirements.txt`

---

## ⚙️ 6. Non-Functional Requirements (Updated)
- Streamlit app must launch with a single `streamlit run app.py` command
- Dashboard should load quickly, be mobile-friendly, and support all browsers
- Use caching where needed (`@st.cache_data`) for optimization