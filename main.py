import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Must be first Streamlit command
st.set_page_config(page_title="GOTR Dashboard", layout="centered")

# Custom style: dark purple background + white text
st.markdown("""
    <style>
    .main, .block-container {
        background-color: #61346B !important;
        color: white !important;
    }
    .stTextInput > div > input,
    .stTextArea > div > textarea,
    .stSelectbox > div > div {
        background-color: white !important;
        color: black !important;
    }
    .stMarkdown, .stTitle, .stExpander, .stSidebar {
        color: white !important;
        background-color: #61346B !important;
    }
    .stSidebar > div {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
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

# Sidebar
st.sidebar.title("📋 Survey Variables")
st.sidebar.write("These are the available variable codes:")
for var in pre_post_pairs:
    st.sidebar.markdown(f"- `{var}`")

# App title
st.title("GOTR AI Interactive Dashboard")

# Input prompt
user_input = st.text_input("Ask something like: 'Compare RESPECT and PHYSACT' or 'Show the change in MAKEFUN'")

# Variable name descriptions
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

# Chart generator
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
        colors.extend(["lightgreen", "purple"])

    fig, ax = plt.subplots()
    x = np.arange(len(labels))
    ax.bar(x, values, color=colors)
    ax.set_ylabel("Average Score")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_title("GOTR AI Interactive Dashboard", color='white')
    ax.tick_params(colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.yaxis.label.set_color('white')
    st.pyplot(fig)

# Display chart
if user_input:
    generate_grouped_chart(user_input)
