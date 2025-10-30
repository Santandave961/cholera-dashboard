import streamlit as st
import pandas as pd
import plotly.express as px
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\USER\Documents\cholera_analysis.csv")
    
    # Clean up column names
    df.columns = df.columns.str.strip()

    # Compute Case Fatality Rate safely:
    df["who_region"] = (df["death_total"] / df["case_total"].replace(0, pd.NA)) * 100
    df["who_region"] = df["who_region"].round(2)

    # Convert dates
    df["first_epiwk"] = pd.to_datetime(df["first_epiwk"], errors='coerce')
    df["last_epiwk"] =pd.to_datetime(df["last_epiwk"], errors='coerce')

    # Outbreak duration
    df["Outbreak_Duration_days"] = (df["last_epiwk"] - df["first_epiwk"]).dt.days

    return df

    df = load_data()


# Page config
st.set_page_config(page_title="Global Cholera Dashboard", layout="wide")

# Header
st.title("Global Cholera Outbreak Dashboard (2024-2025)")
st.markdown("""This dashboard provides insights into global cholera outbreaks using WHO-reported data. You can explore case counts, death rates and regional trends interactively.""")

df = pd.read_csv(r"C:\Users\USER\Documents\cholera_analysis.csv")

# Key Metrics
total_cases=df["case_total"].sum()
total_deaths=df["death_total"].sum()

col1, col2 = st.columns(2)
col1.metric("Total Cases", f"{total_cases:,}")
col2.metric("Total Deaths", f"{total_deaths:,}")

st.markdown("--")

print(df.columns)

# Regional summary
region_summary = df.groupby("who_region")[["case_total","death_total"]].sum().reset_index()
region_summary["CFR (%)"] = (region_summary["death_total"] / region_summary["case_total"] * 100).round(2)

st.subheader("Regional Overview")
st.dataframe(region_summary)

# Bar chart by region
fig_bar = px.bar(region_summary,x="who_region", y="case_total", color="who_region",
                 title="Cholera Cases by WHO Region", text_auto=True)
st.plotly_chart(fig_bar,use_container_width=True)

# Scatter: cases vs deaths
fig_scatter = px.scatter(df, x="case_total", y="death_total", color="who_region",
                         hover_name="adm0_name", title="Cases vs Deaths by Country")
st.plotly_chart(fig_scatter, use_container_width=True)

# Chloropeth Map
fig_map = px.choropleth(df, locations="iso_3_code", color="CFR (%)", hover_name="adm0_name",
                        color_continuous_scale="Reds", title="Global Cholera Case Fatality Rate (CFR %) ")
st.plotly_chart(fig_map, use_container_width=True)

df['first_epiwk_num'] = pd.to_numeric(df['first_epiwk'], errors='coerce')
df['last_epiwk_num'] = pd.to_numeric(df['last_epiwk'], errors='coerce')
df['duration_weeks'] = df['last_epiwk_num'] - df['first_epiwk_num']

fig_duration = px.bar(df.sort_values("duration_weeks", ascending=False).head(20),
                      x="adm0_name", y="duration_weeks",
                      title="Outbreak Duration by Country (in weeks)")
st.plotly_chart(fig_duration, use_container_width=True)
                                    
