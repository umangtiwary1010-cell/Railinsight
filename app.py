import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="RailInsight",
    page_icon="🚆",
    layout="wide"
)
@st.cache_data
def load_data():
    train=pd.read_csv('dashboard_data/train_summary')
    train2=pd.read_csv('dashboard_data/train_details.csv')
    station = pd.read_csv('dashboard_data/station_summary.csv')
    month = pd.read_csv('dashboard_data/month_delay')
    zone = pd.read_csv('dashboard_data/zonal4')
    progress = pd.read_csv('dashboard_data/journey_progress.csv')
    train_type=pd.read_csv('dashboard_data/type_delay')
    # return station
    return train, train2,station, month, zone, progress, train_type
station = load_data()
train, train2, station, month, zone, progress, train_type = load_data()


st.title("🚆 RailInsight")
st.caption("Indian Railways Delay Analytics Dashboard")

st.subheader("💡 Analysis")

st.success("🚄 Premium trains record the highest average delay.")

st.info("📅 Delays peak during December and January.")

st.warning("🗺 SCOR records the highest average delay.")

st.success("📈 Delays generally accumulate until the later stages of the journey.")
overall_delay = train["average_delay"].mean()


tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Dashboard",
    "🚆 Train Explorer",
    "🚉 Station Explorer",
    "ℹ️ About"
])

with tab1:
    
 avg_delay = round(train["average_delay"].mean(),2)

 median_delay = round(train["median_delay"].median(),2)

 total_trains = train["train_no"].nunique()

 avg_records = int(train["total_records"].sum())


 col1,col2,col3,col4 = st.columns(4)

 with col1:
    st.metric("🚆 Total Trains", total_trains)

 with col2:
    st.metric("⏱ Avg Delay", f"{avg_delay} min")

 with col3:
    st.metric("⏳ Median Delay", f"{median_delay} min")

 with col4:
    st.metric("📊 Records", f"{avg_records:,}")

 month_fig = px.line(
    month,
    x="month",
    y="delay",
    markers=True,
    title="Average Delay by Month"
 )

 month_fig.update_layout(
    
    xaxis_title="Month",
    yaxis_title="Delay (minutes)"
 )


 train_type_fig = px.bar(
    train_type,
    x="type_code",
    y="delay",
    orientation="v",
    title="Average Delay by Train Type",

    
 )

 col1, col2 = st.columns(2)

 with col1:
    st.plotly_chart(month_fig, use_container_width=True)

 with col2:
    st.plotly_chart(train_type_fig, use_container_width=True)

 fig = px.bar(
    zone,
    y="delay",
    x="station_zone",
    orientation="v",
    title="Average Delay by Railway Zone",
    
 )




 progress_fig = px.line(
    progress,
    x='progress_bin',
    y='average_delay',
    orientation='v',
    title='Average delay by progress in journey'
 )

 col1,col2= st.columns(2)
 with col1:
    st.plotly_chart(fig, use_container_width=True)

 with col2:
    st.plotly_chart(progress_fig, use_container_width=True)

 top_train = train.groupby('train_name')['average_delay'].mean().sort_values(ascending=False).head(10)
 top_train=top_train.reset_index()
 rogress_fig = px.bar(
    top_train,
    x='train_name',
    y='average_delay',
    orientation='v',
    title='Train with Maximum delay'
 )
 st.plotly_chart(rogress_fig, use_container_width=True)

 top_stations=pd.read_csv('dashboard_data/station_delay')
 ogress_fig = px.bar(
    top_stations,
    x='station_full_name',
    y='delay',
    orientation='v',
    title='station with Maximum delay')

 st.plotly_chart(ogress_fig,use_container_width=True)
#  st.divider()

#  st.caption(
#     "🚆 RailInsight v1.0 | Developed by Umang Tiwary |"
# )
with tab2:

    st.header("🚆 Train Explorer")
    selected_train = st.selectbox(
    "Search Train",
    sorted(train["train_name"].unique()) 
 )
    selected = train[
    train["train_name"] == selected_train
 ]
    col1, col2, col3, col4 = st.columns(4)
    with col1:
     st.metric(
        "Average Delay",
        f"{selected['average_delay'].iloc[0]:.2f} min"
    )

     selected_delay = selected["average_delay"].iloc[0]

     if selected_delay < overall_delay:

      st.success(
        f"🟢 {overall_delay-selected_delay:.1f} min better than network average"
    )

     elif selected_delay > overall_delay:

        st.error(
        f"🔴 {selected_delay-overall_delay:.1f} min worse than network average"
    )

     else:

      st.info("⚪ Equal to network average")
    with col2:
     st.metric(
        "Median Delay",
        f"{selected['median_delay'].iloc[0]:.2f} min"
    )

    with col3:
     st.metric(
        "Train Type",
        selected["type_code"].iloc[0]
    )

    with col4:
     st.metric(
        "Train Name",
        selected["train_name"].iloc[0]
     )
    col1,col2=st.columns(2)
    with col1:
       st.metric(
          "Source",
        
          selected["source_full_name"].iloc[0]
       )
    with col2:
       st.metric(
          "Destination",
          
          selected["destination_full_name"].iloc[0]
       )  
    with col3:
       st.metric(
          "Total Stations",
          
          selected["total_stops"].iloc[0]
       )  
    # st.divider() 
    # st.caption(
    # "🚆 RailInsight v1.0 | Developed by Umang Tiwary |"
    # ) 
with tab3:
    st.header("🚆 Station Explorer")
    selected_station = st.selectbox(
    "Search Station",
    sorted(station["station_full_name"].unique())
 )
    selected = station[
    station["station_full_name"] == selected_station
 ]
    col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average Delay",
        f"{selected['average_delay'].iloc[0]:.2f} min"
    )

with col2:
    st.metric(
        "Median Delay",
        f"{selected['median_delay'].iloc[0]:.2f} min"
    )

with col3:
    st.metric(
        "Station_Zone",
        selected["station_zone"].iloc[0]
    )

with col4:
    st.metric(
        "Station Name",
        selected["station_full_name"].iloc[0]
    )
st.divider()    
st.caption(
    "🚆 RailInsight v1.0 | Developed by Umang Tiwary |"
)
with tab4:


    st.title("🚆 About RailInsight")

    st.markdown("""
    ### Overview

    RailInsight is an interactive analytics dashboard designed to analyze train delay patterns across the Indian Railways network.

    The project transforms **38+ million delay records** into meaningful insights through interactive visualizations, train-wise analysis, station-wise exploration, and journey progress analytics.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛠 Tech Stack")

        st.markdown("""
        - Python
        - Pandas
        - Plotly
        - Streamlit
        """)

    with col2:
        st.subheader("📊 Dataset")

        st.markdown("""
        - 38+ Million delay records
        - Thousands of trains
        - Thousands of stations
        - Complete train schedule information
        """)

    st.divider()

    st.subheader("✨ Features")

    st.markdown("""
    - 📈 Delay Analytics Dashboard
    - 🚆 Train Explorer
    - 🚉 Station Explorer
    - 🗺 Zone-wise Analysis
    - 🚄 Train Type Analysis
    - 📍 Journey Progress Analysis
    - 📌 Executive Summary
    """)

    st.divider()

    
#     st.divider()
#     st.caption(
#     "🚆 RailInsight v1.0 | Developed by Umang Tiwary |"
# )
