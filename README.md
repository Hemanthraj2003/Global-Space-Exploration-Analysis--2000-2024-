# Global Space Exploration Analysis (2000–2024)

## 📋 Project Overview

An interactive dashboard analyzing global space missions from 2000 to 2024. The project provides insights into budget trends, mission success rates, collaboration patterns, and environmental impact of space missions worldwide.

## 🌟 Key Features

### 1. Interactive Dashboard

- **Dynamic Filtering:**
  - Year range selection (2000-2024)
  - Country-specific analysis
  - Mission type filtering
  - Satellite type selection
  - Environmental impact filtering
  - Collaboration-based filtering

### 2. Analysis Sections

#### Overview Tab

- Total mission count
- Average budget metrics
- Success rate statistics
- Mission distribution by country
- Timeline visualization

#### Budget & Success Analysis

- Interactive scatter plots showing budget vs success rate
- Country-wise budget distribution
- Temporal budget analysis

#### Mission Duration & Type Analysis

- Mission duration distribution
- Satellite type breakdown
- Type-wise duration analysis

#### Collaboration Network

- Interactive network visualization of international collaborations
- Thickness of connections indicates collaboration frequency
- Node size represents country's collaboration level
- Hover effects for detailed collaboration information
- Top collaborating country pairs analysis

#### Technology & Environmental Impact

- Technology word cloud visualization
- Environmental impact trends
- Interactive timeline of environmental effects

#### Machine Learning Insights

- K-means clustering of missions
- 3D interactive cluster visualization
- Time series forecasting for future missions
- Downloadable clustered dataset

## 🛠️ Technical Stack

- **Python 3.8+**
- **Key Libraries:**
  - Streamlit (Dashboard Framework)
  - Plotly (Interactive Visualizations)
  - NetworkX (Collaboration Network)
  - Prophet (Time Series Forecasting)
  - Scikit-learn (Machine Learning)
  - Pandas & NumPy (Data Processing)

## 📦 Installation & Setup

1. **Clone the Repository**

```bash
git clone <repository-url>
cd "Global Space Exploration Analysis (2000-2024)"
```

2. **Create & Activate Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Application**

```bash
streamlit run app.py
```

## 📊 Data Structure

The analysis uses the `Global_Space_Exploration_Dataset.csv` containing:

- Mission details (name, type, satellite type)
- Budget information
- Success rates
- Environmental impact metrics
- Collaboration data
- Duration information

## 🎯 Features in Detail

### Data Filtering

- **Year Range:** Select specific time periods for analysis
- **Country Selection:** Focus on specific countries
- **Mission Types:** Filter by different mission categories
- **Environmental Impact:** Focus on eco-friendly missions
- **Collaboration Filter:** Analyze joint missions

### Visualization Features

- **Interactive Charts:** All visualizations support zoom, pan, and hover interactions
- **Network Graph:** Dynamic collaboration visualization with:
  - Adjustable node sizes
  - Weighted connections
  - Hover information
  - Neon theme for better visibility
- **3D Clustering:** Interactive cluster exploration
- **Time Series:** Prophet-based forecasting with confidence intervals

### Analysis Tools

- **Correlation Analysis:** Budget vs Success relationships
- **Pattern Recognition:** Mission duration and type correlations
- **Collaboration Metrics:** Partnership effectiveness
- **Environmental Tracking:** Impact assessment over time
- **Technology Trends:** Word cloud visualization

## 📊 Dashboard Tabs in Detail

### 1. Overview Tab

- **Purpose:** High-level summary of space mission activities
- **Key Features:**
  - Three main KPIs displayed prominently:
    - Total Missions Count
    - Average Mission Budget (in billions)
    - Overall Mission Success Rate
  - Mission Distribution Bar Chart:
    - Shows mission count by country
    - Interactive tooltips with exact numbers
    - Helps identify leading countries in space exploration
  - Timeline Visualization:
    - Tracks mission frequency over time (2000-2024)
    - Reveals trends and patterns in space mission launches
    - Interactive zoom for detailed period analysis

### 2. Budget & Success Analysis Tab

- **Purpose:** Financial insights and mission outcomes analysis
- **Key Features:**
  - Interactive Scatter Plot:
    - X-axis: Mission Budget
    - Y-axis: Success Rate
    - Color-coded by country
    - Reveals budget-success relationships
  - Budget Distribution Box Plot:
    - Country-wise budget breakdown
    - Shows median, quartiles, and outliers
    - Identifies spending patterns across nations
    - Highlights budget disparities and extremes

### 3. Mission Duration & Type Analysis Tab

- **Purpose:** Analysis of mission characteristics and patterns
- **Key Features:**
  - Duration Distribution Histogram:
    - Shows typical mission lengths
    - Identifies common duration patterns
    - Interactive bins for detailed analysis
  - Satellite Type Breakdown:
    - Pie chart of mission categories
    - Interactive tooltips with percentages
    - Shows distribution of mission types

### 4. Collaboration Network Tab

- **Purpose:** Visualize international space cooperation
- **Key Features:**
  - Interactive Network Visualization:
  
    - Nodes represent countries
    - Lines show collaboration connections
    - Line thickness indicates collaboration frequency
    - Node size reflects collaboration activity
    - Neon theme for enhanced visibility
  - Hover Effects:
    - Country collaboration details
    - Partnership counts
    - Total joint missions
  - Top Collaborators Table:
    - Lists strongest country partnerships
    - Shows collaboration frequencies
    - Sortable by different metrics

### 5. Technology & Environmental Tab

- **Purpose:** Track technological trends and environmental impact
- **Key Features:**
  - Technology Word Cloud:
    - Visual representation of common technologies
    - Size indicates usage frequency
    - Interactive tooltips with exact counts
  - Environmental Impact Timeline:
    - Shows impact trends over years
    - Categories: Low, Medium, High impact
    - Interactive trend analysis
  - Impact Level Distribution:
    - Bar chart of environmental categories
    - Temporal changes in impact levels
    - Sustainability insights

### 6. ML Insights Tab

- **Purpose:** Advanced analytics and future predictions
- **Key Features:**
  - K-means Clustering Analysis:
    - 3D interactive scatter plot
    - Clusters missions by:
      - Budget allocation
      - Mission duration
      - Success rates
    - Color-coded cluster visualization
  - Time Series Forecasting:
    - Prophet model predictions
    - Future mission count estimates
    - Confidence intervals
    - Trend analysis
  - Data Export:
    - Download clustered dataset
    - Complete mission details
    - Cluster labels included

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔍 Future Improvements

- Advanced filtering options
- More ML models for prediction
- Additional visualization types
- API integration for real-time data
- Mobile app development

## 📧 Contact

For questions and feedback, please contact [Your Contact Information]

---
**Note:** This project is part of a data analysis and visualization initiative to understand global space exploration trends and patterns.
