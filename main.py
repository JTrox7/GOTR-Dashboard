import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# First Streamlit command
st.set_page_config(page_title="GOTR Dashboard", layout="centered")

# Reset style to white background and black text
st.markdown("""
    <style>
    .main, .block-container {
        background-color: white !important;
        color: black !important;
    }

    /* Input styling */
    .stTextInput > div > input {
        background-color: white !important;
        color: black !important;
    }

    .stTextInput input::placeholder {
        color: #555 !important;
    }

    label, .stTextInput label {
        color: black !important;
        font-weight: 600;
    }

    .stSidebar, .stSidebar .stMarkdown {
        background-color: white !important;
        color: black !important;
    }

    details > summary {
        color: black !important;
    }
    details[open] > summary::before {
        color: black !important;
    }
    summary::marker {
        color: black !important;
    }

    .stMarkdown, .stTitle, .stExpander {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load CSV data
df = pd.read_csv("data.csv")

# Pre/post variable mappings
pre_post_pairs = {
    'PHYSACT': 'PHYSACTP',
    'CLASS': 'CLASSP',
    'RESPECT': 'RESPECTP',
    'FRIENDS': 'FRIENDSP',
    'RESPACTS': 'RESPACTSP',
    'HAPPYAM': 'HAPPYAMP',
    'MAKEFUN': 'MAKEFUNP',
    'MISTAKE': 'MISTAKEP',
    'LIKEPER': 'LIKEPERP',
    'PAYATT': 'PAYATTP',
    'TIMECOMM': 'TIMECOMMP',
    'SAD': 'SADP',
    'HELPCOMM': 'HELPCOMMP',
    'UPSET': 'UPSETP',
    'BADLY': 'BADLYP',
    'PICKED': 'PICKEDP',
    'ELEC': 'ELECP',
    'AGE': 'AGEP',
    'GRADE': 'GRADEP',
    'BLACK': 'BLACKP',
    'ASIAN': 'ASIANP',
    'WHITE': 'WHITEP',
    'OTHER': 'OTHERP',
    'PARTSEAS': 'PARTSEASP'
}

# Sidebar variable
