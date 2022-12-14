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
import numpy as np

#Function to get the cities data 
def get_cities():
    url = 'https://raw.githubusercontent.com/Saving-the-world-org/saving_the_world_app/main/Data/Cities%20-%20Cities.csv'
    cities_df = pd.read_csv(url, index_col=0)

    #data = Path("Data/Cities - Cities.csv")
    #cities_df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Instance"})
    return cities_df

#Function to return the donor_df
def get_donors():
    url = 'https://raw.githubusercontent.com/Saving-the-world-org/saving_the_world_app/main/Data/Donations%20-%20Donations.csv'
    donor_df = pd.read_csv(url, index_col=0)
    #data = Path("/Users/phoebegunter/Documents/FinTech-Workspace/project3/Data/Donations - Donations.csv")
    #donor_df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Instance"})
    return donor_df

#Function to return the org_df
def get_orgs():
    url = 'https://raw.githubusercontent.com/Saving-the-world-org/saving_the_world_app/main/Data/Organizations%20-%20Organizations.csv'
    org_df = pd.read_csv(url, index_col=0)
    # data = Path("/Users/phoebegunter/Documents/FinTech-Workspace/project3/Data/Organizations - Organizations.csv")
    # org_df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Instance"})
    return org_df


def get_city_for_org(org_name): 
    org_df = get_orgs()
    city_name = org_df.loc[org_name, 'City']
    return city_name

def get_phone_for_org(org_name): 
    org_df = get_orgs()
    phone = org_df.loc[org_name, 'Phone number']
    #st.write(type(phone))
    if isinstance(phone, np.integer):
        phone = phone
    else:
        phone = phone[0]
    phone = str(phone)
    return phone

def get_cred_for_org(org_name): 
    org_df = get_orgs()
    cred = org_df.loc[org_name, 'Credibility rating(1-5)']
    if isinstance(cred, np.integer):
        cred = cred
    else:
        cred = cred[0]
    cred = str(cred)
    return cred

def get_quantity_to_donate(category):
    quantity = get_donors[category, 'quantity']
    return quantity