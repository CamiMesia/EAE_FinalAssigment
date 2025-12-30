import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from layout import set_base_style, render_sidebar

set_base_style()
render_sidebar()
st.set_page_config(page_title="Temperatures Dashboard", page_icon="🌡")

st.title("🌡 Temperatures Dashboard")

st.write(
    """
    This page corresponds to the **Temperatures Dashboard** subproject of the IPLD final assignment.  
    We analyze temperature data with filters by city and date.
    """
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/temperatures.csv")
    df["date"] = pd.to_datetime(df["date"])
    if "temperature" not in df.columns:
        for c in df.columns:
            if c.lower() in ["temp", "avg_temp", "temperature_c", "tavg"]:
                df = df.rename(columns={c: "temperature"})
                break
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("The file `data/temperatures.csv` was not found. Add it to the `data` folder.")
    st.stop()

st.subheader("Dataset preview")
st.dataframe(df.head())

st.markdown("---")

st.sidebar.header("Temperature Filters")

cities = df["city"].dropna().unique()
selected_city = st.sidebar.selectbox("City", options=sorted(cities))

min_date = df["date"].min().date()
max_date = df["date"].max().date()

date_range = st.sidebar.date_input(
    "Date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(date_range, tuple):
    start_date, end_date = date_range
else:
    start_date = end_date = date_range

mask = (
    (df["city"] == selected_city) &
    (df["date"].dt.date >= start_date) &
    (df["date"].dt.date <= end_date)
)

filtered_df = df.loc[mask].sort_values("date")

st.subheader(f"Filtered data for {selected_city}")
st.write(f"Number of records: **{len(filtered_df)}**")
st.dataframe(filtered_df.head())

st.markdown("---")

if filtered_df.empty:
    st.warning("No data for the selected filters.")
    st.stop()

st.subheader("Summary statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Average temperature (°C)", f"{filtered_df['temperature'].mean():.2f}")
col2.metric("Min temperature (°C)", f"{filtered_df['temperature'].min():.2f}")
col3.metric("Max temperature (°C)", f"{filtered_df['temperature'].max():.2f}")

st.markdown("---")

# --------- GRÁFICO 1: SERIE TEMPORAL ---------
st.subheader(f"Daily temperature in {selected_city}")

fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(filtered_df["date"], filtered_df["temperature"], marker="o", linestyle="-")
ax1.set_xlabel("Date")
ax1.set_ylabel("Temperature (°C)")
ax1.set_title(f"Temperature over time in {selected_city}")
plt.xticks(rotation=45)
st.pyplot(fig1)

# --------- GRÁFICO 2: MEDIA MÓVIL ---------
st.subheader("7-day rolling average")

df_rolling = filtered_df.set_index("date").sort_index()
rolling = df_rolling["temperature"].rolling(window=7).mean()

fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(df_rolling.index, df_rolling["temperature"], alpha=0.4, label="Daily temperature")
ax2.plot(rolling.index, rolling.values, linewidth=2, label="7-day rolling avg")
ax2.set_xlabel("Date")
ax2.set_ylabel("Temperature (°C)")
ax2.set_title(f"Daily temperature & 7-day rolling average in {selected_city}")
ax2.legend()
plt.xticks(rotation=45)
st.pyplot(fig2)

