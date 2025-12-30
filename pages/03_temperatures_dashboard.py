import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

from layout import set_base_style, render_sidebar

set_base_style()
render_sidebar()

st.title("🌡️ Temperatures Dashboard")

st.write(
    """
    This page explores a global **temperatures dataset**. You can filter by region, 
    country and city to analyse how the average temperature evolved over the years 
    and by month
    """
)

file_paths = sorted(glob("temperatures_part*.csv"))

if file_paths:
    df_list = [pd.read_csv(path) for path in file_paths]
    df = pd.concat(df_list, ignore_index=True)
else:
   
    try:
        df = pd.read_csv("temperatures.csv")
    except FileNotFoundError:
        st.error(
            "❌ Could not find any 'temperatures_part*.csv' or 'temperatures.csv' "
            "in the project root."
        )
        st.stop()

df["Region"] = df["Region"].astype("string")
df["Country"] = df["Country"].astype("string")
df["State"] = df["State"].astype("string")
df["City"] = df["City"].astype("string")

df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
df["Month"] = pd.to_numeric(df["Month"], errors="coerce").astype("Int64")
df["Day"] = pd.to_numeric(df["Day"], errors="coerce").astype("Int64")
df["AvgTemperature"] = pd.to_numeric(df["AvgTemperature"], errors="coerce")

df = df.dropna(subset=["Year", "Month", "AvgTemperature", "City"])

df["Date"] = pd.to_datetime(
    dict(year=df["Year"], month=df["Month"], day=df["Day"]),
    errors="coerce",
)
df = df.dropna(subset=["Date"])

st.subheader("📊 Basic Information")

min_year = int(df["Year"].min())
max_year = int(df["Year"].max())
n_records = int(len(df))
n_regions = int(df["Region"].nunique())
n_countries = int(df["Country"].nunique())
n_cities = int(df["City"].nunique())
global_avg_temp = round(df["AvgTemperature"].mean(), 2)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("Min Year", min_year)
with col2:
    st.metric("Max Year", max_year)
with col3:
    st.metric("Records", n_records)
with col4:
    st.metric("Regions", n_regions)
with col5:
    st.metric("Countries", n_countries)
with col6:
    st.metric("Global Avg Temp (°F)", global_avg_temp)

st.markdown("---")

st.subheader("🌍 Filters")

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    region_options = sorted(df["Region"].dropna().unique())
    selected_region = st.selectbox("Region", region_options)

df_region = df[df["Region"] == selected_region]

with col_f2:
    country_options = sorted(df_region["Country"].dropna().unique())
    selected_country = st.selectbox("Country", country_options)

df_country = df_region[df_region["Country"] == selected_country]

with col_f3:
    city_options = sorted(df_country["City"].dropna().unique())
    selected_city = st.selectbox("City", city_options)

df_city = df_country[df_country["City"] == selected_city].copy()

if df_city.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

st.markdown(
    f"### 📌 Selected: **{selected_city}**, {selected_country} ({selected_region})"
)

st.subheader("📈 Avg Temperature by Year")

yearly_city = (
    df_city.groupby("Year")["AvgTemperature"]
    .mean()
    .reset_index()
    .sort_values("Year")
)

fig1, ax1 = plt.subplots(figsize=(9, 4))
ax1.plot(yearly_city["Year"], yearly_city["AvgTemperature"], linewidth=2)
ax1.set_title(f"Average Temperature in {selected_city} Across Years")
ax1.set_xlabel("Year")
ax1.set_ylabel("Avg Temperature (°F)")
st.pyplot(fig1)

st.markdown("---")

st.subheader("📊 Avg Temperature by Month (extra chart)")

available_years = sorted(yearly_city["Year"].dropna().astype(int).unique())
default_year = int(available_years[-1])

selected_year = st.slider(
    "Select a year:",
    min_value=int(available_years[0]),
    max_value=int(available_years[-1]),
    value=default_year,
    step=1,
)

df_city_year = df_city[df_city["Year"] == selected_year]

if df_city_year.empty:
    st.warning(f"No temperature data for {selected_city} in {selected_year}.")
else:
    monthly = (
        df_city_year.groupby("Month")["AvgTemperature"]
        .mean()
        .reset_index()
        .sort_values("Month")
    )

    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.bar(monthly["Month"], monthly["AvgTemperature"])
    ax2.set_xticks(range(1, 13))
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Avg Temperature (°F)")
    ax2.set_title(f"Average Monthly Temperature in {selected_city} ({selected_year})")
    st.pyplot(fig2)

st.markdown("---")

st.subheader("🌡️ Comparing the Temperatures of the Cities")

all_cities = sorted(df["City"].dropna().unique())

default_cities = [c for c in ["Buenos Aires", "Dakar"] if c in all_cities]
if not default_cities and len(all_cities) >= 2:
    default_cities = all_cities[:2]

selected_cities_compare = st.multiselect(
    "Select the cities to compare:",
    options=all_cities,
    default=default_cities,
)

if selected_cities_compare:
    min_date = df["Date"].min().date()
    max_date = df["Date"].max().date()

    col_d1, col_d2 = st.columns(2)
    with col_d1:
        start_date = st.date_input(
            "Select the start date:",
            value=min_date,
            min_value=min_date,
            max_value=max_date,
        )
    with col_d2:
        end_date = st.date_input(
            "Select the end date:",
            value=max_date,
            min_value=min_date,
            max_value=max_date,
        )

    mask = (
        (df["City"].isin(selected_cities_compare))
        & (df["Date"] >= pd.to_datetime(start_date))
        & (df["Date"] <= pd.to_datetime(end_date))
    )
    df_compare = df.loc[mask, ["Date", "City", "AvgTemperature"]].copy()

    if df_compare.empty:
        st.warning("No data for the selected cities and date range.")
    else:
       
        df_compare["TempC"] = (df_compare["AvgTemperature"] - 32) * 5.0 / 9.0

        fig3, ax3 = plt.subplots(figsize=(9, 4))
        for city in selected_cities_compare:
            city_data = (
                df_compare[df_compare["City"] == city]
                .sort_values("Date")
            )
            ax3.plot(
                city_data["Date"],
                city_data["TempC"],
                label=city,
                linewidth=1,
            )

        start_str = pd.to_datetime(start_date).strftime("%Y-%m-%d")
        end_str = pd.to_datetime(end_date).strftime("%Y-%m-%d")

        ax3.set_title(
            f"Temperatures in {', '.join(selected_cities_compare)} "
            f"from {start_str} to {end_str}"
        )
        ax3.set_xlabel("Date")
        ax3.set_ylabel("Temperature (°C)")
        ax3.legend()
        st.pyplot(fig3)

st.markdown("---")

with st.expander("📂 Show filtered dataset"):
    st.write(
        "Below you can see the subset of the dataset for the selected "
        "Region, Country and City."
    )
    st.dataframe(
        df_city.sort_values(["Year", "Month", "Day"]),
        use_container_width=True,
    )

with st.expander("📂 Show full dataset (warning: large)"):
    st.dataframe(df.head(5000), use_container_width=True)
    st.caption("Only first 5,000 rows are shown for performance reasons.")
