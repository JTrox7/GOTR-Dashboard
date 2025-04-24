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
st.set_page_config(layout="centered")
st.title("Girls on the Run - Pre/Post Comparison")

# Input prompt
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

    # Collect bar chart data
    labels = []
    values = []

    for var in matched_metrics:
        post_var = pre_post_pairs[var]
        avg_pre = df[var].mean()
        avg_post = df[post_var].mean()

        labels.append(f"{var} Pre")
        labels.append(f"{var} Post")
        values.append(avg_pre)
        values.append(avg_post)

    # Plotting the grouped bar chart
    fig, ax = plt.subplots()
    x = np.arange(len(labels))
    ax.bar(x, values, color=["skyblue" if 'Pre' in label else "lightgreen" for label in labels])
    ax.set_ylabel("Average Score")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_title("Pre vs Post Comparison")
    st.pyplot(fig)

# Run chart if input is given
if user_input:
    generate_grouped_chart(user_input)
