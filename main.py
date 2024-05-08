import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sample pivot")
table=pd.read_csv("sample_pivot.csv").head()
st.text("Sample pivot is the dataset we use to check for exploratory Analysis on clothing brand")
st.write(table)

##  Add visualization 
bar_plot_fig=px.bar(table,x="Region",y="Units",title="Bar plot")
st.plotly_chart(bar_plot_fig,use_container_width=True)

## Add a line plot
pie_chart_fig=px.pie(table,values="Sales",names="Region",title="Distribution of Sales in Regions")
st.plotly_chart(pie_chart_fig,use_container_width=True)

## import data
st.title("Tips Dataset")
table2=px.data.tips()
hide=st.checkbox("Hide/show Dataset")
if not hide:
    st.write(table2)
## Create sunburst
sun_fig=px.sunburst(table2,path=["day","time","sex","smoker"],values="tip",title="SUNBURST FOR THE DAY.")
st.plotly_chart(sun_fig,use_container_width=True)