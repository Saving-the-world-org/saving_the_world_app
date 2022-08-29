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

    if isinstance(city, str):
        st.write("City: " + city)
    else:
        st.write(city.iloc[:, 0])
    phone = get_phone_for_org(i)
    cred = get_cred_for_org(i)
    
    st.write("Phone Number: " + phone)
    #st.write(phone)
    st.write("Credibility Rating (out of 5): " + cred )
    #st.write(cred)
    # if type(phone) is  : 
    #     st.write("series")


#org_names = org_df.index.drop_duplicates()
