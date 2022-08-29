#Imports 
from collections import namedtuple
from multiprocessing.dummy import current_process
#from tkinter.filedialog import test
import altair as alt
import math
import pandas as pd
import streamlit as st
import pickle 
from pickle import load
from math import log, floor
from pathlib import Path
from saving_the_world_app import get_cities,get_donors,get_orgs

#session state was throwing errors 
# if "shared" not in st.session_state:
#    st.session_state["shared"] = True


#Header information 
st.title("Hummanitarian Aid Supply Chain Tracker Tool", anchor=None)
st.subheader("This app enabled you to safetly track donating and receiving aid products on a blockchain. ")
st.caption("Project 3 by Phoebe Gunter, Harry Oestreicher, Abhishek Banerjee, Gabriel Paganin, Gerald Cortright, Javier", unsafe_allow_html=False)

url = "https://github.com/Saving-the-world-org/saving_the_world_app/blob/50e3533a923e74d9cc8c5cfdb2483e9efac7d806/images/ActionagainstHunger.png"
st.image(url, caption="Photo from Action Against Hunger")
https://github.com/Saving-the-world-org/saving_the_world_app/blob/main/images/Hunger1.png