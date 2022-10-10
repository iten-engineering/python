
import pandas as pd
import streamlit as st

# read sales
df = pd.read_excel('sales.xlsx')
df = df.set_index('Monat', drop=True)

# Write out title
st.write("# Sales 2022")
st.image("sales.png")

# Show raw data
st.subheader('Raw data')
if st.checkbox('Show'):
    st.dataframe(df)

# Show chart
st.subheader('Chart')

selections = ['All']
selections.extend(list(df.columns))

option = st.selectbox(
     'Select town',
     selections)

if option == 'All':
     st.bar_chart(df)
else:
     st.bar_chart(df[option])

# Show footer
st.write("---")
st.write("__Copyright 2022 - MyCompany.com__")

