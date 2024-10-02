# app.py

import streamlit as st
import subprocess

def run_main_script():
    """Runs the main.py script and captures the output."""
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
    return result.stdout

# Streamlit app UI
st.title("mailBot - Email Summarizer App")

st.write("Click the button below to process and summarize your emails.")

# Button to trigger main.py
if st.button("Process Emails"):
    st.write("Processing emails...This may take a while. Please wait.")
    
    # Run the main.py script and capture output
    result = run_main_script()
    
    # Display the result
    st.write(result)
