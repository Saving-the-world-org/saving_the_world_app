#Imports 
from collections import namedtuple
from multiprocessing.dummy import current_process
#from tkinter.filedialog import test
from webbrowser import get
import altair as alt
import math
import pandas as pd
import streamlit as st
import pickle 
from pickle import load
from math import log, floor
from pathlib import Path
from saving_the_world_app import get_cities, get_donors, get_orgs 


# page2.py
st.write(st.session_state["shared"])

#setting up dataframes from functions 
cities_df = get_cities()
donors_df = get_donors()
org_df = get_orgs() 

#Cities Data Imports
st.subheader("City Data")
st.dataframe(cities_df)

#Donations Data Imports
st.subheader("Donation Data")
st.dataframe(donors_df)

#Organization Data Imports
st.subheader("Organization Data")
st.dataframe(org_df)

