#Imports 
from collections import namedtuple
from multiprocessing.dummy import current_process
from tkinter.filedialog import test
import altair as alt
import math
import pandas as pd
import streamlit as st
import pickle 
from pickle import load
from math import log, floor
from pathlib import Path
from saving_the_world_app import get_cities,get_donors,get_orgs


if "shared" not in st.session_state:
   st.session_state["shared"] = True


#Header information 
st.title("Hummanitarian Aid Supply Chain Tracker Tool", anchor=None)
st.subheader("This app enabled you to safetly track donating and receiving aid products on a blockchain. ")
st.caption("Project 3 by Phoebe Gunter, Harry Oestreicher, Abhishek Banerjee, Gabriel Paganin, Gerald Cortright, Javier", unsafe_allow_html=False)


