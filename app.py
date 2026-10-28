from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="HKBK AQI Dashboard", page_icon="🌫️", layout="wide")

DATA_FILE = Path(__file__).parent / "data" / "air_quality_dummy_dataset.csv"
AQI_COLORS = {
    "Good": "#2FA65A", "Satisfactory": "#A9C83F", "Moderate": "#F2D33E",
    "Poor": "#F28A2E", "Very Poor": "#D83C32", "Severe": "#8D1717"
}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

st.markdown("""
<style>
.stApp {background: #F3F6F8; color: #101B2D;}
[data-testid="stSidebar"] {background: linear-gradient(180deg,#D7E3EF 0%,#C4D3E3 100%);}
[data-testid="stSidebar"] > div:first-child {padding-top: 1.6rem;}
[data-testid="stMetric"] {background:#fff;border:1px solid #CCD5DE;border-radius:10px;
padding:14px 16px;box-shadow:0 2px 7px rgba(25,45,65,.12);min-height:108px;}
[data-testid="stMetricLabel"] {font-size:14px;color:#28364A;}
[data-testid="stMetricValue"] {font-size:26px;color:#111827;}
div[data-testid="stVerticalBlockBorderWrapper"] {background:#fff;border:1px solid #D5DEE6;
border-radius:10px;box-shadow:0 2px 7px rgba(25,45,65,.10);}
h1 {font-size:29px !important;color:#111B2D !important;}
h2,h3 {color:#111B2D;}
.demo-banner {background:linear-gradient(90deg,#C9E2F9,#D9ECFC);border:1px solid #B7D7F1;
border-radius:8px;padding:10px 14px;color:#17283C;font-size:13px;margin-bottom:12px;}
.aqi-chip {display:inline-block;border-radius:20px;padding:3px 10px;color:#fff;
font-size:12px;font-weight:600;margin-left:7px;}
</style>
""", unsafe_allow_html=True)

def category(aqi):
    if aqi <= 50: return "Good"
    if aqi <= 100: return "Satisfactory"
    if aqi <= 200: return "Moderate"
    if aqi <= 300: return "Poor"
    if aqi <= 400: return "Very Poor"
    return "Severe"

@st.cache_data
def load_data(path):
    frame = pd.read_csv(path)
    frame["Month_ID"] = pd.to_datetime(frame["Month_ID"], format="%Y-%m")
    frame["AQI_Category"] = frame["AQI"].apply(category)
    return frame.sort_values("Month_ID")

df = load_data(DATA_FILE)

with st.sidebar:
    st.markdown("### Dashboard filters")
    season_options = ["All seasons"] + list(df["Season"].drop_duplicates())
    season = st.selectbox("Season", season_options, index=1 if "Winter" in season_options else 0)
    month = st.selectbox("Month", ["All months"] + MONTH_ORDER)
    st.divider()
    st.markdown("### AQI bands used")
    bands = [
        ("Good 0–50", "#2FA65A"), ("Satisfactory 51–100", "#A9C83F"),
        ("Moderate 101–200", "#E5C82C"), ("Poor 201–300", "#E9822D"),
        ("Very Poor 301–400", "#D83C32"), ("Severe 401–500", "#8D1717")
    ]
    for label, color in bands:
        st.markdown(
            f'<div style="background:{color};color:white;border-radius:18px;'
            f'padding:4px 10px;margin:7px 0;width:max-content;font-size:12px">{label}</div>',
            unsafe_allow_html=True
        )
    st.divider()
    st.caption("Dataset: simulated monthly averages for 2025.")

st.markdown(
    '<div class="demo-banner">ⓘ &nbsp; Environmental Analytics & Air Quality Assessment | HKBK College of Engineering : Project (Course BCV755B).</div>',
    unsafe_allow_html=True
)
st.markdown("""
    <h1 style="
        font-size: 54px;
        font-weight: 800;
        color: #2D3040;
        margin-bottom: 8px;
        line-height: 1.2;
    ">
        Environmental Monitoring and AQI
    </h1>
""", unsafe_allow_html=True)
st.caption("HKBK College of Engineering · Department of Civil Engineering · BCV755B")

selected = df.copy()
if season != "All seasons":
    selected = selected[selected["Season"] == season]
if month != "All months":
    selected = selected[selected["Month"] == month]
if selected.empty:
    st.info("No records match the selected filters.")
    st.stop()

avg_aqi = round(selected["AQI"].mean())
avg_pm25 = selected["PM2_5_ug_m3"].mean()
avg_pm10 = selected["PM10_ug_m3"].mean()
avg_co = selected["CO_mg_m3"].mean()
avg_no2 = selected["NO2_ug_m3"].mean()

top = st.columns([1, 1, 1, 1.55], gap="medium")
with top[0]:
    st.metric("Average AQI", avg_aqi, help="AQI band: " + category(avg_aqi))
    st.markdown(f'<span class="aqi-chip" style="background:{AQI_COLORS[category(avg_aqi)]}">{category(avg_aqi)}</span>',
                unsafe_allow_html=True)
with top[1]:
    st.metric("PM₂.₅ average", f"{avg_pm25:.1f} µg/m³")
with top[2]:
    st.metric("PM₁₀ average", f"{avg_pm10:.1f} µg/m³")
with top[3]:
    st.markdown("#### Regional Air Quality Map")
    st.caption("Illustrative monitoring spots · simulated, not geographic readings")
    map_values = [42, 68, 91, 118, 146, 178, 214, 236]
    spots = ["North Gate", "West Park", "Lake Road", "Campus East",
             "Market Street", "Central Junction", "South Layout", "East Gate"]
    xs = [1.0, 2.1, 3.0, 4.1, 1.5, 2.6, 3.7, 4.7]
    ys = [4.3, 3.2, 4.0, 3.0, 1.9, 2.5, 1.6, 2.0]
    points = pd.DataFrame({"Spot": spots, "AQI": map_values, "x": xs, "y": ys})
    points["AQI band"] = points["AQI"].apply(category)
    fig_map = go.Figure()
    streets = [
        ([0.5, 1.4, 2.3, 3.2, 4.1, 5.1], [3.8, 3.4, 3.0, 2.6, 2.2, 1.8]),
        ([0.6, 1.5, 2.4, 3.3, 4.2, 5.0], [1.3, 1.8, 2.3, 2.8, 3.3, 3.8]),
        ([1.2, 1.3, 1.4, 1.5], [1.1, 2.0, 3.0, 4.4]),
        ([2.6, 2.7, 2.8, 2.9], [1.1, 2.0, 3.0, 4.5]),
        ([4.0, 4.1, 4.2, 4.3], [1.2, 2.0, 3.0, 4.4]),
    ]
    for sx, sy in streets:
        fig_map.add_trace(go.Scatter(x=sx, y=sy, mode="lines",
            line=dict(color="#FFFFFF", width=10), hoverinfo="skip", showlegend=False))
        fig_map.add_trace(go.Scatter(x=sx, y=sy, mode="lines",
            line=dict(color="#D1D9D8", width=1), hoverinfo="skip", showlegend=False))
    fig_map.add_trace(go.Scatter(
        x=points["x"], y=points["y"], mode="markers",
        marker=dict(size=13, color=[AQI_COLORS[x] for x in points["AQI band"]],
                    line=dict(color="white", width=1.5)),
        text=points["Spot"] + "<br>AQI " + points["AQI"].astype(str) + " · " + points["AQI band"],
        hovertemplate="%{text}<extra></extra>", name="Monitoring spots"
    ))
    fig_map.update_layout(height=205, margin=dict(l=0,r=0,t=0,b=0),
        paper_bgcolor="#FFFFFF", plot_bgcolor="#EAF2EB", showlegend=False)
    fig_map.update_xaxes(visible=False, range=[0.4,5.2], fixedrange=True)
    fig_map.update_yaxes(visible=False, range=[1.0,4.6], fixedrange=True, scaleanchor="x")

lower_metrics = st.columns(4, gap="medium")
lower_metrics[0].metric("CO average", f"{avg_co:.2f} mg/m³")
lower_metrics[1].metric("NO₂ average", f"{avg_no2:.1f} µg/m³")
if avg_aqi > 200:
    st.error(f"Poor AQI alert: the selected data peak is {int(selected['AQI'].max())}. Increase dust control, construction-site checks and public updates.")
elif avg_aqi > 100:
    st.warning(f"Moderate AQI period: the selected-data average is {avg_aqi}. Continue monitoring and manage local emission sources.")
else:
    st.success(f"The selected-data average AQI is {avg_aqi}. Continue routine monitoring.")

left, right = st.columns([1.35, 1], gap="medium")
with left:
    st.subheader("Pollutant concentrations by month")
    pollutant_cols = ["PM2_5_ug_m3", "PM10_ug_m3", "NO2_ug_m3"]
    long_df = selected.melt(id_vars=["Month", "Month_ID"], value_vars=pollutant_cols,
                            var_name="Pollutant", value_name="Concentration")
    labels = {"PM2_5_ug_m3":"PM₂.₅ (µg/m³)", "PM10_ug_m3":"PM₁₀ (µg/m³)",
              "NO2_ug_m3":"NO₂ (µg/m³)"}
    long_df["Pollutant"] = long_df["Pollutant"].map(labels)
    fig = px.line(long_df, x="Month", y="Concentration", color="Pollutant",
                  markers=True, color_discrete_sequence=["#147D92","#E6814B","#8067A8"],
                  category_orders={"Month": MONTH_ORDER})
    fig.update_layout(height=350, margin=dict(l=8,r=8,t=8,b=8),
                      legend_title_text="", paper_bgcolor="white", plot_bgcolor="white")
    fig.update_xaxes(title="", showgrid=False)
    fig.update_yaxes(title="Concentration", gridcolor="#E7EDF1")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("AQI by month")
    fig_aqi = px.bar(selected, x="Month", y="AQI", color_discrete_sequence=["#111B2D"],
                     category_orders={"Month": MONTH_ORDER}, text="AQI")
    fig_aqi.update_traces(textposition="outside")
    fig_aqi.add_hline(y=200, line_dash="dot", line_color="#C44E52",
                      annotation_text="Poor band begins (200)")
    fig_aqi.update_layout(height=350, margin=dict(l=8,r=8,t=8,b=8),
                          showlegend=False, paper_bgcolor="white", plot_bgcolor="white")
    fig_aqi.update_xaxes(title="", tickangle=35, showgrid=False)
    fig_aqi.update_yaxes(title="AQI", gridcolor="#E7EDF1")
    st.plotly_chart(fig_aqi, use_container_width=True)

with st.expander("Observations and recommendations", expanded=True):
    st.markdown("**Observations from this simulated series**")
    st.markdown(
        "- Winter has the highest monthly AQI: January 236 and December 211 (Poor band).\n"
        "- August is lowest at AQI 68 (Satisfactory band).\n"
        "- PM₂.₅ falls from 92 µg/m³ in January to 24 µg/m³ in August.\n"
        "- AQI rises 143 points from August to December."
    )
    st.markdown("**Recommended management measures**")
    st.markdown(
        "- Increase public updates and inspections during dry months when validated readings show higher AQI.\n"
        "- Cover construction materials; use site barriers, wheel washing, suitable dust suppression and prompt debris removal.\n"
        "- Improve public transport access and traffic flow; discourage unnecessary vehicle idling.\n"
        "- Protect tree cover and lake buffers as supporting measures alongside direct source controls.\n"
        "- Compare verified station data before and after targeted actions."
    )

with st.expander("Dataset details"):
    st.dataframe(selected[["Month","Season","PM2_5_ug_m3","PM10_ug_m3","CO_mg_m3",
                           "NO2_ug_m3","AQI","AQI_Category"]].rename(columns={
        "PM2_5_ug_m3":"PM₂.₅ (µg/m³)", "PM10_ug_m3":"PM₁₀ (µg/m³)",
        "CO_mg_m3":"CO (mg/m³)", "NO2_ug_m3":"NO₂ (µg/m³)",
        "AQI_Category":"AQI band"
    }), use_container_width=True, hide_index=True)

st.caption("The AQI values are simulated monthly summary indices and are not calculated from the pollutant averages. They are not official measurements or a regulatory compliance assessment.")
