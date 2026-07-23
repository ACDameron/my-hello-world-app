import streamlit as st
import pandas as pd
import time

st.title("Hello world!")

with st.sidebar:
    st.header("About app")
    st.write("This is my first app!")

st.header("This is a header with a divider", divider="rainbow")
st.markdown("This is created using st.markdown")

st.subheader("st.column")
col1, col2 = st.columns(2)

with col1:
    x = st.slider("Choose an x value",1,1000)

progress_bar = col1.progress(0)

for perc_completed in range (100):
    time.sleep(0.05)
    progress_bar.progress(perc_completed+1)

col1.success("Value chosen successfully")



with col2:
    st.write("The value of :orange[***x***] is",x)

col2.metric(label="Temperature", value="80 °F", delta="5 °F")


from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

col3, col4 = st.columns(2)

with col3:
     st.area_chart(df)
with col4:
     st.bar_chart(df)
