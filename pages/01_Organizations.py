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
from saving_the_world_app import get_cities,get_donors,get_orgs, get_city_for_org, get_phone_for_org, get_cred_for_org

#setting up dataframes from functions 
cities_df = get_cities()
donors_df = get_donors()
org_df = get_orgs() 

st.title("Explore Organizations")

st.write("Available Organizations to Donate to")


for i in org_df.index.drop_duplicates():
    st.subheader(i)
    city = get_city_for_org(i)
    phone = get_phone_for_org(i)
    cred = get_cred_for_org(i)
    st.write("City: " + city)
    st.write("Phone Number: ")
    st.write(phone)
    st.write("Credibility Rating (out of 5): " )
    st.write(cred)


#org_names = org_df.index.drop_duplicates()
