import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your CSV data
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

# Streamlit page setup
st.set_page_config(page_title="GOTR Dashboard", layout="centered")

# Custom background color with HTML
st.markdown("""
    <style>
    .main {
        background-color: #ffe6f0;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("GOTR AI Interactive Dashboard")

# User input
user_input = st.text_input("Ask something like: 'Compare RESPECT and PHYSACT' or 'Show the change in MAKEFUN'")

def generate_grouped_chart(prompt):
    prompt = prompt.lower()
    matched_metrics = []

    # Match keywords from the prompt to known pre/post variables
    for pre in pre_post_pairs:
        if pre.lower() in prompt:
            matched_metrics.append(pre)

    if not matched_metrics:
        st.info("Please include at least one known category like RESPECT, PHYSACT, or MAKEFUN.")
        return

    # Build data for chart
    labels = []
    values = []
    colors = []

    for var in matched_metrics:
        post_var = pre_post_pairs[var]
        avg_pre = df[var].mean()
        avg_post = df[post_var].mean()

        labels.extend([f"{var} Pre", f"{var} Post"])
        values.extend([avg_pre, avg_post])
        colors.extend(["lightgreen", "purple"])

    # Plot chart
    fig, ax = plt.subplots()
    x = np.arange(len(labels))
    ax.bar(x, values, color=colors)
    ax.set_ylabel("Average Score")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_title("GOTR AI Interactive Dashboard")
    st.pyplot(fig)

# Run the chart when the user submits a prompt
if user_input:
    generate_grouped_chart(user_input)
