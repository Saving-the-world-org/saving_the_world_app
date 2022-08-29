#Imports 
from collections import namedtuple
from multiprocessing.dummy import current_process
from sqlite3 import DatabaseError
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
from saving_the_world_app import get_cities,get_donors,get_orgs


#Session state was throwing errors 
# page2.py
# st.write(st.session_state["shared"])

#setting up dataframes from functions 
cities_df = get_cities()
donors_df = get_donors()
org_df = get_orgs() 


#TO BE UPDATED
#Header information 
st.title("Donor", anchor=None)
#st.subheader("Project 1 by Phoebe Gunter")
#st.caption("This Bot allows professors of UC Berkeley courses to see which students are falling behind and not actively participating in class", unsafe_allow_html=False)

org_names = org_df['Organization'].drop_duplicates()
selected_org_by_donar = st.selectbox('Select Organization to Donate to:', org_names)

st.info("You selected " + selected_org_by_donar + " to donate to.")