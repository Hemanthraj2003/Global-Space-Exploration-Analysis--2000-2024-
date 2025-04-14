import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from prophet import Prophet
import networkx as nx
from wordcloud import WordCloud
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="Global Space Exploration Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Cache data loading for optimization
@st.cache_data
def load_data():
    return pd.read_csv("data/Global_Space_Exploration_Dataset.csv")

data = load_data()

# Sidebar controls
st.sidebar.header("Filters")
year_range = st.sidebar.slider("Year Range", 2000, 2024, (2000, 2024))
selected_countries = st.sidebar.multiselect("Select Countries", options=sorted(data['Country'].unique()))
mission_type = st.sidebar.selectbox("Mission Type", options=['All'] + sorted(data['Mission Type'].unique().tolist()))
satellite_type = st.sidebar.selectbox("Satellite Type", options=['All'] + sorted(data['Satellite Type'].unique().tolist()))
collaborative_only = st.sidebar.checkbox("Collaborative Missions Only")
environmental_friendly = st.sidebar.checkbox("Environmental Friendly Missions")

# Filter data based on selections
filtered_data = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]
if selected_countries:
    filtered_data = filtered_data[filtered_data['Country'].isin(selected_countries)]
if mission_type != 'All':
    filtered_data = filtered_data[filtered_data['Mission Type'] == mission_type]
if satellite_type != 'All':
    filtered_data = filtered_data[filtered_data['Satellite Type'] == satellite_type]
if collaborative_only:
    filtered_data = filtered_data[filtered_data['Collaborating Countries'].notna()]
if environmental_friendly:
    filtered_data = filtered_data[filtered_data['Environmental Impact'] == 'Low']

# Main tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Overview", "Budget & Success", "Mission Duration & Type",
    "Collaboration Analysis", "Technology & Environmental", "ML Insights"
])

# Tab 1: Overview
with tab1:
    st.header("Overview")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Missions", len(filtered_data))
    with col2:
        st.metric("Avg Budget (Billion $)", f"${filtered_data['Budget (in Billion $)'].mean():.2f}B")
    with col3:
        st.metric("Avg Success Rate", f"{filtered_data['Success Rate (%)'].mean():.1f}%")
    
    # Missions by Country
    st.subheader("Missions by Country")
    fig_country = px.bar(
        filtered_data['Country'].value_counts().reset_index(),
        x='Country', y='count',
        title="Number of Missions by Country"
    )
    st.plotly_chart(fig_country, use_container_width=True)
    
    # Missions Over Time
    st.subheader("Missions Over Time")
    missions_time = filtered_data.groupby('Year').size().reset_index(name='count')
    fig_time = px.line(missions_time, x='Year', y='count', title="Missions Over Time")
    st.plotly_chart(fig_time, use_container_width=True)

# Tab 2: Budget & Success
with tab2:
    st.header("Budget & Success Analysis")
    
    # Scatter plot: Budget vs Success Rate
    fig_scatter = px.scatter(
        filtered_data,
        x='Budget (in Billion $)',
        y='Success Rate (%)',
        color='Country',
        title="Budget vs Success Rate"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Box plot: Budget by Country
    fig_box = px.box(
        filtered_data,
        x='Country',
        y='Budget (in Billion $)',
        title="Budget Distribution by Country"
    )
    st.plotly_chart(fig_box, use_container_width=True)

# Tab 3: Mission Duration & Type
with tab3:
    st.header("Mission Duration & Type Analysis")
    
    col1, col2 = st.columns(2)
    with col1:
        # Duration Distribution
        fig_hist = px.histogram(
            filtered_data,
            x='Duration (in Days)',
            title="Mission Duration Distribution"
        )
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Satellite Types Distribution
        fig_pie = px.pie(
            filtered_data,
            names='Satellite Type',
            title="Distribution of Satellite Types"
        )
        st.plotly_chart(fig_pie, use_container_width=True)

# Tab 4: Collaboration Analysis
with tab4:
    st.header("Collaboration Network Analysis")
    
    # Create collaboration network
    collab_data = filtered_data[filtered_data['Collaborating Countries'].notna()]
    
    if len(collab_data) > 0:
        # Create a NetworkX graph for layout calculation
        G = nx.Graph()
        edge_weights = {}
        
        # Process collaborations and build edge weights
        for _, row in collab_data.iterrows():
            countries = row['Collaborating Countries'].split(', ')
            countries = [c.strip() for c in countries if c.strip()]  # Clean country names
            for i in range(len(countries)):
                for j in range(i + 1, len(countries)):
                    edge = tuple(sorted([countries[i], countries[j]]))
                    edge_weights[edge] = edge_weights.get(edge, 0) + 1
                    G.add_edge(countries[i], countries[j], weight=edge_weights[edge])
        
        if len(G.edges()) > 0:
            # Calculate spring layout with adjusted parameters for better spacing
            pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
            
            # Prepare edge traces with different weights
            edge_traces = []
            max_weight = max(edge_weights.values())
            
            # Create a trace for each edge weight
            for (node1, node2, weight) in G.edges(data='weight'):
                x0, y0 = pos[node1]
                x1, y1 = pos[node2]
                weight_scaled = weight / max_weight
                
                # Calculate edge color based on weight (neon effect)
                edge_color = f'rgba(0, 255, 255, {max(0.2, weight_scaled)})'  # Cyan with opacity based on weight
                
                edge_trace = go.Scatter(
                    x=[x0, x1, None],
                    y=[y0, y1, None],
                    line=dict(
                        width=weight_scaled * 2,  # Thinner lines
                        color=edge_color
                    ),
                    hoverinfo='text',
                    text=f'{node1} ↔ {node2}<br>Collaborations: {weight}',
                    mode='lines',
                    showlegend=False
                )
                edge_traces.append(edge_trace)
            
            # Prepare nodes
            node_x = []
            node_y = []
            node_text = []
            node_sizes = []
            node_colors = []
            
            # Calculate node metrics
            for node in G.nodes():
                x, y = pos[node]
                node_x.append(x)
                node_y.append(y)
                
                # Calculate node metrics
                degree = G.degree(node)
                weighted_degree = sum(G[node][neighbor]['weight'] for neighbor in G.neighbors(node))
                
                node_text.append(
                    f'Country: {node}<br>' +
                    f'Number of Partners: {degree}<br>' +
                    f'Total Collaborations: {weighted_degree}'
                )
                node_sizes.append(weighted_degree)
                # Calculate node color based on number of partners (neon effect)
                node_colors.append(degree)
            
            # Create figure
            fig = go.Figure()
            
            # Add all edge traces
            for edge_trace in edge_traces:
                fig.add_trace(edge_trace)
            
            # Add nodes with correct colorbar configuration
            node_trace = go.Scatter(
                x=node_x, y=node_y,
                mode='markers+text',
                hoverinfo='text',
                text=node_text,
                textposition="top center",
                textfont=dict(
                    size=10,
                    color='white'
                ),
                marker=dict(
                    showscale=True,
                    colorscale=[[0, '#00ff87'], [1, '#00ffff']],  # Neon green to cyan
                    color=node_colors,
                    size=[10 + (5 * size / max(node_sizes)) for size in node_sizes],
                    line=dict(color='#ffffff', width=1),
                    colorbar=dict(
                        thickness=15,
                        title='Number of Partners',
                        xanchor='left'
                    )
                ),
                name='Countries'
            )
            fig.add_trace(node_trace)
            
            # Update layout with dark theme
            fig.update_layout(
                title=dict(
                    text="Space Mission Collaboration Network",
                    x=0.5,
                    font=dict(size=24, color='white')
                ),
                paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
                plot_bgcolor='rgba(0,0,0,0)',   # Transparent background
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20, l=5, r=5, t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                width=800,
                height=600,
                dragmode='zoom',  # Enable zoom drag mode
                modebar=dict(
                    bgcolor='rgba(0,0,0,0)',
                    color='white'
                )
            )
            
            # Display the network
            st.plotly_chart(fig, use_container_width=True)
            
            # Add KPIs with neon styling
            st.markdown("""
            <style>
            .stMetric {
                background: rgba(0, 255, 255, 0.1);
                border: 1px solid rgba(0, 255, 255, 0.2);
                border-radius: 5px;
            }
            .stMetric:hover {
                background: rgba(0, 255, 255, 0.2);
            }
            </style>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                total_collabs = sum(edge_weights.values())
                st.metric("Total Collaborations", total_collabs)
            with col2:
                collab_ratio = len(collab_data) / len(filtered_data) * 100
                st.metric("Collaborative Missions (%)", f"{collab_ratio:.1f}%")
            with col3:
                avg_partners = np.mean([G.degree(node) for node in G.nodes()])
                st.metric("Avg Partners per Country", f"{avg_partners:.1f}")
            
            # Show top collaborating pairs with styled table
            st.subheader("Top Collaborating Country Pairs")
            collab_pairs = pd.DataFrame(
                [(c1, c2, w) for (c1, c2), w in edge_weights.items()],
                columns=['Country 1', 'Country 2', 'Collaborations']
            ).sort_values('Collaborations', ascending=False)
            
            st.dataframe(
                collab_pairs.head(10),
                column_config={
                    "Collaborations": st.column_config.NumberColumn(
                        "Collaborations",
                        help="Number of joint missions",
                        format="%d 🤝"
                    )
                }
            )
        else:
            st.warning("No collaboration connections found in the filtered data.")
    else:
        st.warning("No collaborative missions found in the selected data range.")

# Tab 5: Technology & Environmental
with tab5:
    st.header("Technology & Environmental Impact")
    
    # Word cloud of technologies
    if len(filtered_data) > 0:
        tech_text = ' '.join(filtered_data['Technology Used'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(tech_text)
        
        fig_cloud, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig_cloud)
    
    # Environmental Impact over time
    env_impact = filtered_data.groupby(['Year', 'Environmental Impact']).size().unstack(fill_value=0)
    fig_env = px.area(env_impact, title="Environmental Impact Over Time")
    st.plotly_chart(fig_env, use_container_width=True)

# Tab 6: ML Insights
with tab6:
    st.header("Machine Learning Insights")
    
    if len(filtered_data) >= 3:
        # Prepare data for clustering
        cluster_features = ['Budget (in Billion $)', 'Duration (in Days)', 'Success Rate (%)']
        X = filtered_data[cluster_features].fillna(filtered_data[cluster_features].mean())
        
        # Standardize features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Perform K-means clustering
        n_clusters = 3
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        filtered_data['Cluster'] = kmeans.fit_predict(X_scaled)
        
        # 3D scatter plot with clusters
        fig_3d = px.scatter_3d(
            filtered_data,
            x='Budget (in Billion $)',
            y='Duration (in Days)',
            z='Success Rate (%)',
            color='Cluster',
            title="Mission Clusters"
        )
        st.plotly_chart(fig_3d, use_container_width=True)
        
        # Download clustered data
        st.download_button(
            label="Download Clustered Data",
            data=filtered_data.to_csv(index=False),
            file_name="space_missions_clustered.csv",
            mime="text/csv"
        )
        
        # Forecasting
        st.subheader("Mission Count Forecast")
        forecast_data = filtered_data.groupby('Year').size().reset_index()
        forecast_data.columns = ['ds', 'y']
        
        model = Prophet(yearly_seasonality=True)
        model.fit(forecast_data)
        
        future = model.make_future_dataframe(periods=5, freq='Y')
        forecast = model.predict(future)
        
        fig_forecast = go.Figure()
        fig_forecast.add_trace(go.Scatter(x=forecast_data['ds'], y=forecast_data['y'], name='Historical'))
        fig_forecast.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Forecast'))
        fig_forecast.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], name='Upper Bound', line=dict(dash='dash')))
        fig_forecast.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], name='Lower Bound', line=dict(dash='dash')))
        fig_forecast.update_layout(title='Mission Count Forecast', xaxis_title='Year', yaxis_title='Number of Missions')
        st.plotly_chart(fig_forecast, use_container_width=True)
    else:
        st.warning("Not enough data for clustering and forecasting. Please adjust filters.")