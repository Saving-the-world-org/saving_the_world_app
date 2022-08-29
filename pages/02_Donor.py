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
from saving_the_world_app import get_cities,get_donors,get_orgs, get_quantity_to_donate


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

#setting up dataframes from functions 
cities_df = get_cities()
donors_df = get_donors()
org_df = get_orgs() 





org_names = org_df.index.drop_duplicates()
selected_org_by_donar = st.selectbox('Select Organization to Donate to:', org_names)
st.info("You selected " + selected_org_by_donar + " to donate to.")


items_to_donate = donors_df["Items donated"].drop_duplicates 
#quantity_to_donate = get_donors.loc["qantity"]
selected_item_to_donate = st.selectbox("Select Item to Donate ", items_to_donate)
st.info("You would like to donate"  + selected_item_to_donate + " to donate to.")


quantity_to_donate = get_quantity_to_donate(selected_item_to_donate)
selected_item_to_donate = st.selectbox("Select quantity to donate ", quantity_to_donate)
st.info("You would like to donate" + quantity_to_donate + "of" + selected_item_to_donate)
