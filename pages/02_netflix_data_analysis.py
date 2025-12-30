import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from layout import set_base_style, render_sidebar
set_base_style()
render_sidebar()

st.title("📺 Netflix Data Analysis")

st.write(
    """
    This page explores the public **Netflix titles dataset**.
    Below you can find some key indicators and visualizations
    similar to the official demo, plus your own charts.
    """
)
df = None
possible_paths = [
    "resources/netflix_titles.csv",
    "data/netflix_titles.csv",
    "netflix_titles.csv",
]

for p in possible_paths:
    try:
        df = pd.read_csv(p)
        break
    except Exception:
        continue

if df is None:
    st.error(
        "❌ Could not load `netflix_titles.csv`. "
        "Make sure it is in `resources/` or `data/` folder."
    )
    st.stop()
df["title"] = df["title"].astype(str)
df["director"] = df["director"].astype(str)
df["country"] = df["country"].astype(str)
df["release_year"] = df["release_year"].astype(int)

st.subheader("📊 Basic Information")

min_year = int(df["release_year"].min())
max_year = int(df["release_year"].max())
missing_directors = int((df["director"] == "" ) | (df["director"].str.lower()=="nan")).sum()

countries = (
    df["country"]
    .replace("nan", "")
    .str.split(",")
    .explode()
    .str.strip()
)
unique_countries = countries[countries != ""].nunique()

avg_title_len = round(df["title"].str.len().mean(), 2)

total_titles = len(df)
movies = df[df["type"] == "Movie"].shape[0]
tv_shows = df[df["type"] == "TV Show"].shape[0]

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("Min Release Year", min_year)
with col2:
    st.metric("Max Release Year", max_year)
with col3:
    st.metric("Missing Dir. Names", missing_directors)
with col4:
    st.metric("Countries", unique_countries)
with col5:
    st.metric("Avg Title Length", avg_title_len)
with col6:
    st.metric("Total Titles", total_titles)

st.markdown("---")

st.subheader("🌍 Top Year Producer Countries")

min_y = int(df["release_year"].min())
max_y = int(df["release_year"].max())

year = st.number_input(
    "Select a year:",
    min_value=min_y,
    max_value=max_y,
    value=2005,
    step=1,
)

df_year = df[df["release_year"] == year]

if df_year.empty:
    st.warning(f"No titles found for year {year}. Try another year.")
else:
    # contar países
    countries_year = (
        df_year["country"]
        .replace("nan", "")
        .str.split(",")
        .explode()
        .str.strip()
    )
    countries_year = countries_year[countries_year != ""]
    top_countries = countries_year.value_counts().head(10)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(
        top_countries.values,
        labels=top_countries.index,
        autopct="%1.2f%%",
        startangle=90,
    )
    ax.set_title(f"Top 10 Countries in {year}")
    ax.axis("equal")

    st.pyplot(fig)

st.markdown("---")

st.subheader("🎬 Titles by Type Over the Years")

# Conteo por año y tipo
type_year = (
    df.groupby(["release_year", "type"])["show_id"]
    .count()
    .reset_index()
    .rename(columns={"show_id": "count"})
)

fig2, ax2 = plt.subplots(figsize=(8, 4))
for t in type_year["type"].unique():
    subset = type_year[type_year["type"] == t]
    ax2.plot(subset["release_year"], subset["count"], marker="o", label=t)

ax2.set_xlabel("Release Year")
ax2.set_ylabel("Number of Titles")
ax2.set_title("Number of Movies and TV Shows by Year")
ax2.legend()
st.pyplot(fig2)

st.markdown("---")

st.subheader("⭐ Top 10 Directors by Number of Titles")
directors = (
    df["director"]
    .replace(["nan", ""], pd.NA)
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)
top_directors = directors.value_counts().head(10)

fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.barh(top_directors.index[::-1], top_directors.values[::-1])
ax3.set_xlabel("Number of Titles")
ax3.set_title("Top 10 Directors")
st.pyplot(fig3)

st.markdown("---")

st.subheader("📈 Your Existing Visualizations")

st.info(
    "The following section contains the charts you already built "
    "for this assignment. Do not remove them; just paste them below."
)
