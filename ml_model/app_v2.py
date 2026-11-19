import streamlit as st
print("hello")
st.title("hours_studied", 0.0, 10.0, 5.0, step=0.1)
print("hello again")
attendance = st.slider("Attendance %", 40, 100, 75)
prev_marks = st.slider("previous marks", 0, 100, 60)
print("hello hello again")
st.write("you choose:" ,attendance, prev_marks)
print("file ands here")