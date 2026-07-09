# 🚆 RailInsight
### An Interactive Railway Delay Analytics Dashboard

RailInsight is an end-to-end data analytics project built to analyze delay patterns across the Indian Railways network. The project processes **38+ million train delay records** and transforms raw operational data into meaningful business insights through interactive visualizations and dashboards.

Built using **Python, Pandas, Plotly, and Streamlit**, RailInsight enables users to explore train performance, station-wise delays, seasonal trends, and journey progress through an intuitive web application.

---

## 📸 Dashboard Preview



### 📊 Dashboard

(<img width="1865" height="783" alt="Screenshot 2026-07-10 022225" src="https://github.com/user-attachments/assets/e8061671-c892-43c1-9979-d48b12b359e8" />)

### 🚆 Train Explorer
<img width="1813" height="667" alt="Screenshot 2026-07-10 014630" src="https://github.com/user-attachments/assets/057fe848-eb57-4ff9-acf8-4767c3edcaad" />

### 🚉 Station Explorer
<img width="1797" height="414" alt="Screenshot 2026-07-10 014707" src="https://github.com/user-attachments/assets/3d28452b-1f38-499d-977f-f9a31fbb8cfc" />


---

# ✨ Features

### 📊 Dashboard
- KPI cards summarizing railway performance
- Executive Summary highlighting major findings
- Monthly delay trend analysis
- Train type-wise delay analysis
- Zone-wise delay analysis
- Journey progress analysis
- Top delayed trains
- Top delayed stations

### 🚆 Train Explorer
Search any train and view:
- Train Number
- Train Name
- Train Type
- Source Station
- Destination Station
- Total Stops
- Average Delay
- Median Delay
- Total Delay Records
- Comparison with network average

### 🚉 Station Explorer
Search any station and view:
- Station Name
- Railway Zone
- Average Delay
- Median Delay
- Total Records

### 📈 Business Analytics
- Executive Summary
- Seasonal delay trends
- Zone performance comparison
- Journey progress delay analysis
- Train category comparison

---

# 📊 Dataset

The project uses Indian Railways operational datasets containing over **38 million records**.

The datasets include:

- Train Delay Data
- Train Information
- Station Information
- Train Schedule Information

After preprocessing and feature engineering, the dashboard uses optimized summary datasets for faster loading.

---

# 🔍 Key Insights

Some major findings from the analysis include:

- 🚄 Premium trains recorded the highest average delays among all train categories.
- 📅 Delay levels were highest during winter months.
- 🗺️ Certain railway zones consistently experienced higher average delays.
- 📈 Train delays generally accumulated as journeys progressed.
- 🚉 A relatively small number of stations contributed disproportionately to severe delays.

---

# ⚙️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| Dashboard | Streamlit |
| Static Visualization | Matplotlib, Seaborn |

---

# 📂 Project Structure

```text
RailInsight/
│
├── app.py
├── README.md
├── requirements.txt
│
├── dashboard_data/
│   ├── train_summary.csv
│   ├── station_summary.csv
│   ├── monthly_delay.csv
│   ├── zone_summary.csv
│   ├── journey_progress.csv
│
│
├── screenshots/
│   ├── dashboard.png
│   ├── train_explorer.png
│   └── station_explorer.png
│
└── assets/
```

---

# 🚀 Installation


Move into the project directory

```bash
cd RailInsight
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📈 Dashboard Modules

### 📊 Dashboard

Provides an overall view of railway delay performance using interactive charts and KPI cards.

---

### 🚆 Train Explorer

Allows users to search for any train and analyze its operational performance.

---

### 🚉 Station Explorer

Allows users to search for any railway station and inspect station-level delay statistics.

---

### ℹ️ About

Contains project overview, dataset information, technologies used, and project highlights.

---

# 📊 KPIs Included

- Total Trains Analysed
- Average Delay
- Median Delay
- Total Delay Records
- Better/Worse than Network Average

---

# 🧠 Skills Demonstrated

This project showcases practical skills in:

- Data Cleaning
- Data Wrangling
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Business Analytics
- Data Storytelling
- Dashboard Development
- Interactive Data Visualization
- Streamlit Application Development

---

# 🔮 Future Improvements

Future versions of RailInsight may include:

- 🤖 Machine Learning-based Delay Prediction
- ⭐ Train Reliability Score
- 📍 Live Train Status Integration
- 🗺️ Route Visualization
- 📈 Delay Forecasting
- 🔄 Real-Time Railway Dashboard
- 📱 Mobile-Friendly Dashboard

---

# 💡 Project Highlights

✔ Processed **38+ million railway delay records**

✔ Built an interactive analytics dashboard using Streamlit

✔ Designed Train Explorer and Station Explorer modules

✔ Performed feature engineering and  EDA

✔ Optimized large datasets into lightweight dashboard datasets

✔ Developed an end-to-end data analytics application

---


**From raw railway data to actionable operational insights.**
