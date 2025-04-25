import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ✅ Page config must be the first Streamlit command!
st.set_page_config(page_title="GOTR Dashboard", layout="centered")

# Custom background color with HTML
st.markdown("""
    <style>
    .main {
        background-color: #ffe6f0;
    }
    </style>
""", unsafe_allow_html=True)

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

# Sidebar: list variable codes
st.sidebar.title("📋 Survey Variables")
st.sidebar.write("These are the variable codes:")
for var in pre_post_pairs:
    st.sidebar.markdown(f"- `{var}`")

# App title
st.title("GOTR Interactive Dashboard")

# ✅ Input prompt FIRST
user_input = st.text_input("Ask something like: 'Compare RESPECT and PHYSACT' or 'Show the change in MAKEFUN'")

# 👇 Then the variable definitions
with st.expander("🧠 What do the variable names mean?"):
    st.markdown("""
    - **PHYSACT** — I am good at most physical activities  
    - **CLASS** — I have classmates who like me the way I am  
    - **RESPECT** — I show respect for others  
    - **FRIENDS** — I have classmates I can become friends with  
    - **RESPACTS** — I accept responsibility for my actions  
    - **HAPPYAM** — I am happy the way I am  
    - **MAKEFUN** — I have classmates who sometimes make fun of me  
    - **MISTAKE** — I admit when I make a mistake  
    - **LIKEPER** — I like the kind of person I am  
    - **PAYATT** — I have classmates who pay attention to what I say  
    - **STANDUP** — I stand up for kids who are being picked on  
    - **TIMECOMM** — I spend time helping my community  
    - **SAD** — It makes me sad to see a girl who can’t find anyone to play with  
    - **HELPCOMM** — I help others in my community  
    - **UPSET** — I feel upset when I see a girl getting her feelings hurt  
    - **BADLY** — I feel badly for other girls who are sad  
    - **PICKED** — I feel badly when I see a girl getting picked on  
    - **ELEC** — On a school day, hours spent on electronics  
    - **AGE / GRADE / PARTSEAS** — Demographic information  
    """)

# Chart function
def generate_grouped_chart(prompt):
    prompt = prompt.lower()
    matched_metrics = []

    for pre in pre_post_pairs:
        if pre.lower() in prompt:
            matched_metrics.append(pre)

    if not matched_metrics:
        st.info("Please include at least one known category like RESPECT, PHYSACT, or MAKEFUN.")
        return

    labels = []
    values = []
    colors = []

    for var in matched_metrics:
        post_var = pre_post_pairs[var]
        avg_pre = df[var].mean()
        avg_post = df[post_var].mean()
        labels.extend([f"{var} Pre", f"{var} Post"])
        values.extend([avg_pre, avg_post])
        colors.extend(["lightgreen", "pink"])

    fig, ax = plt.subplots()
    x = np.arange(len(labels))
    ax.bar(x, values, color=colors)
    ax.set_ylabel("Average Score")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_title("Results")
    st.pyplot(fig)

    # Display the mean values and difference
    for var in matched_metrics:
        post_var = pre_post_pairs[var]
        avg_pre = df[var].mean()
        avg_post = df[post_var].mean()
        difference = avg_pre - avg_post

        with st.container():
            st.subheader(f"Summary for {var}")
            st.write(f"**Pre Survey Mean ({var})**: {avg_pre:.2f}")
            st.write(f"**Post Survey Mean ({post_var})**: {avg_post:.2f}")
            st.write(f"**Difference (Pre - Post)**: {difference:.2f}")


# Show chart on input
if user_input:
    generate_grouped_chart(user_input)
