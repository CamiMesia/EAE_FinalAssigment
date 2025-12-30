import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from layout import set_base_style, render_sidebar

set_base_style()
render_sidebar()
st.set_page_config(page_title="Netflix Data Analysis", page_icon="🎬")

st.title("🎬 Netflix Data Analysis")

st.write(
    """
    This page corresponds to the **Netflix Data Analysis** subproject of the IPLD final assignment.  
    We use **Pandas** and **Matplotlib** to explore the dataset.
    """
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/netflix_titles.csv")
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("The file `data/netflix_titles.csv` was not found. Add it to the `data` folder.")
    st.stop()


st.subheader("Dataset preview")
st.dataframe(df.head())

st.markdown("---")

# --------- FILTROS EN SIDEBAR ---------
st.sidebar.header("Netflix Filters")

type_options = df["type"].dropna().unique()
selected_types = st.sidebar.multiselect(
    "Type",
    options=type_options,
    default=list(type_options)
)

min_year = int(df["release_year"].min())
max_year = int(df["release_year"].max())
year_range = st.sidebar.slider(
    "Release year range",
    min_year,
    max_year,
    (min_year, max_year)
)

country_options = df["country"].dropna().unique()
selected_countries = st.sidebar.multiselect(
    "Country (optional filter)",
    options=sorted(country_options)[:30],
    default=[]
)

# --------- APLICAR FILTROS ---------
filtered_df = df.copy()

if selected_types:
    filtered_df = filtered_df[filtered_df["type"].isin(selected_types)]

filtered_df = filtered_df[
    (filtered_df["release_year"] >= year_range[0]) &
    (filtered_df["release_year"] <= year_range[1])
]

if selected_countries:
    filtered_df = filtered_df[filtered_df["country"].isin(selected_countries)]

st.subheader("Filtered data")
st.write(f"Number of titles: **{len(filtered_df)}**")
st.dataframe(filtered_df.head())

st.markdown("---")

st.subheader("Number of titles by release year")

titles_per_year = (
    filtered_df.groupby("release_year")["title"]
    .count()
    .sort_index()
)

if titles_per_year.empty:
    st.warning("No data for the selected filters.")
else:
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(titles_per_year.index, titles_per_year.values, marker="o")
    ax1.set_xlabel("Release year")
    ax1.set_ylabel("Number of titles")
    ax1.set_title("Number of Netflix titles by release year")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

st.markdown("---")

st.subheader("Distribution by type (Movies vs TV Shows)")

type_counts = filtered_df["type"].value_counts()

if not type_counts.empty:
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    ax2.bar(type_counts.index, type_counts.values)
    ax2.set_xlabel("Type")
    ax2.set_ylabel("Number of titles")
    ax2.set_title("Distribution of titles by type")
    st.pyplot(fig2)
else:
    st.info("No type data for the selected filters.")

st.markdown("---")

# --------- GRÁFICO 3: TOP GENRES ---------
st.subheader("Top 10 genres / categories")

if "listed_in" in filtered_df.columns:
    genres = (
        filtered_df["listed_in"]
        .dropna()
        .str.split(", ")
        .explode()
    )
    top_genres = genres.value_counts().head(10)

    if not top_genres.empty:
        fig3, ax3 = plt.subplots(figsize=(10, 4))
        ax3.bar(top_genres.index, top_genres.values)
        ax3.set_xlabel("Genre")
        ax3.set_ylabel("Number of titles")
        ax3.set_title("Top 10 genres in the filtered dataset")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig3)
    else:
        st.info("No genre data available for the selected filters.")
else:
    st.info("Column `listed_in` not found in the dataset.")

