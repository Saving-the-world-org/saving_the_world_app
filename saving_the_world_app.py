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

#Function to get the cities data 
def get_cities():
    url = 'https://github.com/Saving-the-world-org/saving_the_world_app/blob/a1d8e00dcd1ac6aeb50d8dc14601847e382abe5f/Data/Cities%20-%20Cities.csv'
    cities_df = pd.read_csv(url, delimiter="," index_col=0)
    #data = Path("Data/Cities - Cities.csv")
    #cities_df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Instance"})
    return cities_df

#Function to return the donor_df
def get_donors():
    url = 'https://github.com/Saving-the-world-org/saving_the_world_app/blob/3480cc3cfcfb14f904130666e1d8989ad148d2e7/Data/Donations%20-%20Donations.csv'
    donor_df = pd.read_csv(url, delimiter="," index_col=0)
    #data = Path("/Users/phoebegunter/Documents/FinTech-Workspace/project3/Data/Donations - Donations.csv")
    #donor_df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Instance"})
    return donor_df

#Function to return the org_df
def get_orgs():
    url = 'https://github.com/Saving-the-world-org/saving_the_world_app/blob/3480cc3cfcfb14f904130666e1d8989ad148d2e7/Data/Organizations%20-%20Organizations.csv'
    org_df = pd.read_csv(url, delimiter="," index_col=0)
    # data = Path("/Users/phoebegunter/Documents/FinTech-Workspace/project3/Data/Organizations - Organizations.csv")
    # org_df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Instance"})
    return org_df


