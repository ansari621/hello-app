import streamlit as st

name = st.text_input("Enter your name: ")
fname = st.text_input("Enter your father's name: ")
add = st.text_area("Enter your address: ")
classdata = st.selectbox("Enter your class:",(1,2,3,4,5,6,7,8,9,10))


button = st.button("Submit")

if button:
    st.markdown(f"""
    Name: {name}
    Father's Name: {fname}
    Address: {add}
    Class: {classdata}
    '""")