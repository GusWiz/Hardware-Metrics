# find libray that import db or api that has data over pc components, and normal metrics
# Find a libray that allows of GUI stats over active pc components
# 

#   This file shoud, compare both stats.

import streamlit as st
import psutil
import GPUtil
import time

st.set_page_config(layout="wide", page_title="System Performance Dashboard")
st.title('Real-Time System Performance Metrics')

gpu_placeholder = st.empty()
mem_placeholder = st.empty()

quantum_interval = 1 # updates every 1 second

while True:
    gpus = GPUtil.getGPUs() # Gets GPU data
    if gpus: # If it detects any gpu then proceed
        gpu = gpus[0]
        gpu_utilization = gpu.load * 100 # load returns from 0-1, so we must convert to percentage
        with gpu_placeholder.container():
            st.subheader(f'GPU Usage for {gpu.name}')
            st.write(f'Utilization: {gpu_utilization}')
            st.progress(int(gpu_utilization)) # displays the data in a progress bar
    else:
        with gpu_placeholder.container():
            st.subheader('GPU Usage')
            st.write('No NVIDIA GPU detected')
time.sleep(quantum_interval)