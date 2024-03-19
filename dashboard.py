import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")

## streamlit emoji.com
st.set_page_config(page_title="Sample-SuperStore",page_icon=":bar_chart:",layout="wide")

st.title(":bar_chart: Sample-SuperStore")
st.markdown("<style>div.block-container{padding-top:irem;}</style>",unsafe_allow_html=True)

#fl=st.file_uploader(":file_folder: Upload a data file",type=(["csv","txt","xlsx","xls"]))
#if fl is not None:
   # st.success("File uploaded succesfully!!")
    #filename= fl.name
    #st.write(filename)
#df = pd.read_csv(filename,encoding="ISO-8859-1")
#else:
    #os.chdir(r"C:\Users\DIVINE FAVUR\Documents\streamlit")
df = pd.read_csv("Sample - Superstore.csv",encoding="ISO-8859-1")
col1,col2= st.columns((2))
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Getting the min and max date
startDate= pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()

with col1:
    date1=pd.to_datetime(st.date_input('start Date',startDate))

with col2:
    date2=pd.to_datetime(st.date_input('start Date',endDate))

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()

# create Region side bar
st.sidebar.header("Choose your filter: ")
region= st.sidebar.multiselect("pick your Region",df["Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2= df[df["Region"].isin(region)]

# create State side bar
state = st.sidebar.multiselect("select your state",df2["State"].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)]
# create City side bar
city= st.sidebar.multiselect("Pick the city",df3["City"].unique())

# filter the data based on Region, state and city.
if not region and not state and not city:
    filtered_df=df
elif not state and not city:
    filtered_df=df[df["Region"].isin(region)]
elif not region and not city:
    filtered_df= df[df["State"].isin(state)]
elif not region and not state:
    filtered_df=df[df["City"].isin(state)]
elif state and city:
    filtered_df=df3[df["State"].isin(state) & df3["City"].isin(city)]
elif region and city:
    filtered_df=df3[df["Region"].isin(region) & df3["City"].isin(city)]
elif region and state:
    filtered_df=df3[df["Region"].isin(state) & df3["State"].isin(state)]
elif city:
    filtered_df=df3[df3["City"].isin(city)]
else:
    filtered_df=df3[df3["Region"].isin(region)& df3["State"].isin(state) & df3["City"].isin(city)]
## sum up the rgion column first
category_df= filtered_df.groupby(by= ["Category"],as_index=False)["Sales"].sum()

with col1:
    st.subheader("Category with sales")
    fig=px.bar(category_df,x="Category",y="Sales",text= ["${:,.2f}".format(x) for x in category_df["Sales"]],
               template = "seaborn")
    st.plotly_chart(fig,use_container_width=True,height=200)

with col2:
    st.subheader("Region with Sales")
    fig=px.pie(filtered_df,values= "Sales",names="Region",hole=0.5,template="gridon")
    fig.update_traces(text= filtered_df["Region"], textposition= "outside")
    st.plotly_chart(fig,use_container_width=True)
    
cl1, cl2 = st.columns((2))
with cl1:
        with st.expander("category_viewData"):
            st.write(category_df.style.background_gradient(cmap="Blues"))
            csv = category_df.to_csv(index = False).encode("UTF-8")
            st.download_button("Download Data", data = csv, file_name= "category.csv",mime="text/csv",
                               help= "click here to download the csv file")
            
with cl2:
        with st.expander("Region_viewData"):
            region = filtered_df.groupby(by = "Region", as_index=False)["Sales"].sum()
            st.write(region.style.background_gradient(cmap="Oranges"))
            csv = region.to_csv(index = False).encode("UTF-8")
            st.download_button("Download Data", data = csv, file_name= "region.csv",mime="text/csv",
                               help= "Download_button")

df["Order Date"]= pd.to_datetime(df["Order Date"])
filtered_df["month_year"]=filtered_df["Order Date"].dt.to_period("M")
st.subheader('Time series Analysis')

linechart= pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y: %b"))["Sales"].sum()).reset_index()
fig2= px.line(linechart, x= "month_year", y="Sales",labels={"Sales":"Amount"},height=500,width=1000,template="gridon")
st.plotly_chart(fig2,use_container_width=True)

with st.expander("View Data of TimeSeries:"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv= linechart.to_csv(index=False).encode("utf-8")
    st.download_button("Download Data", data = csv, file_name="TimeSeries.csv",mime="text/csv")
# create a treemap bases on Region, category, sub-Category
st.subheader("Hierarchical View of Sales using TreeMap")
fig3= px.treemap(filtered_df,path=["Region","Category","Sub-Category"], values= "Sales",hover_data=["Sales"],
                 color= "Sub-Category")
fig3.update_layout(width=800, height = 600)
st.plotly_chart(fig3,use_container_width=True)

chart1, chart2= st.columns((2))
with chart1:
    st.subheader("Segment with Sales")
    fig= px.pie(filtered_df, values= "Sales",names = "Segment",template="plotly_dark")
    fig.update_traces(text= filtered_df["Segment"], textposition= "inside")
    st.plotly_chart(fig,use_container_width=True)
# plotly templates for colors
# "ggplot2"
# "seaborn"
# "simple_white"
# "plotly"
# "plotly_white"
# "plotly_dark"
# "presentation"
# "xgridoff"
# "ygridoff"
# "gridon"
# "none"
with chart2:
    st.subheader("Category with Sales")
    fig= px.pie(filtered_df, values= "Sales",names = "Category",template="presentation")
    fig.update_traces(text= filtered_df["Category"], textposition= "inside")
    st.plotly_chart(fig,use_container_width=True)

import plotly.figure_factory as ff
st.subheader(":point_right: Month with Sub-Category Sales Summary")
with st.expander("Summary_Table_Dataset"):
    df_sample= df[0:10][["Region","State","City","Category","Sales","Profit","Quantity"]]
    fig= ff.create_table(df_sample, colorscale="Cividis")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("Month With Sub-Category Table")
    filtered_df["Month"] = filtered_df["Order Date"].dt.month_name()
    sub_category_Year= pd.pivot_table(data= filtered_df, values="Sales", index=["Sub-Category"],columns="Month")
    st.write(sub_category_Year.style.background_gradient(cmap="Blues"))
# Different colorscale for plotly.
# Plasma
# Cividis
# Magma
# Jet
# Rainbow
# Inferno
# Virdis

# Create a scatter plot.
data1=px.scatter(filtered_df, x="Sales",y="Profit",size= "Quantity")
data1["layout"].update(title="Relationship between Sales and Profits using Scatter Plot.",
                       titlefont=dict(size=20),xaxis= dict(title="Sales",titlefont=dict(size=19)),
                       yaxis= dict(title= "Profit",titlefont= dict(size=19)))
st.plotly_chart(data1,use_container_width=True)


with st.expander("View Data"):
    st.write(filtered_df.iloc[:500,1:20:2].style.background_gradient(cmap="Oranges"))

# Download the original dataset
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download Data", data= csv, file_name="Sample - Superstore.csv",mime="text/csv")
