
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle

st.title("Google Stock")
@st.cache
def load_data(num_rows=1000):
    df = pd.read_csv(r"C:\Users\samina\Desktop\GA_DATA_SCIENCE\Data_Sci\Homework\Unit4\Final_project\google.csv", nrows=num_rows)
    return df

@st.cache
def create_group(x_axis, y_axis):
    grouping = df.groupby(x_axis)[y_axis].mean()
    return grouping


def make_charts(chart,grouping, xa, ya):
    if chart == 'line':
        #make line chart
        st.line_chart(grouping)
    elif chart == 'table':
        #make table
        st.write(grouping)          
    elif chart == 'bar':
        #make bar chart
        st.bar_chart(grouping)
    else:
        st.plotly_chart(px.strip(df[[xa, ya]], x=xa, y=ya))

#@st.cache
def load_model():
    with open('pipeline.pkl', 'rb')as f:
        mod = pickle.load(f)
        return mod
#________________________________________________________


#________________MAIN__________________________________________________________

def main(df, section):
        
    
    if section == 'Data Visulise':
        
        x_axis = st.sidebar.selectbox('Choose Your X-Axis Catagory', df.select_dtypes(include=np.object).columns, index=0)   #np.object, than index =0
        y_axis = st.sidebar.selectbox('Y-Axis ', df.select_dtypes(include=np.number).columns, index=2)
        #y_axis = st.sidebar.selectbox('Y-Axis ', ['stae', 'goal']) #other way to get required colums
        chart_type = st.sidebar.selectbox('Choose chart', ['table', 'line', 'bar', 'strip'])
        
        grouping = create_group(x_axis, y_axis)
        
        st.write(df)
        st.title('Data')
        
        #making charts
        make_charts(chart_type,grouping, x_axis, y_axis)
        st.write(grouping)

if __name__ == "__main__":
    section = st.sidebar.radio('App section', ['Data Visulise'])
    nrows = st.sidebar.number_input("Number of Rows to load", min_value=1000, max_value=10000, step=750)
        
    df = load_data(nrows)
    
    main(df, section)