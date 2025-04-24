import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Pre/post pairs from your dataset
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

# UI setup
st.set_page_config(layout="centered")
st.title("Girls on the Run - AI Dashboard (No API)")
user_input = st.text_input("Ask a question about the survey data (e.g. 'How did respect change?'):")

# Chart generator
def generate_chart(prompt):
    prompt = prompt.lower()
    matched = None

    # Try to find a keyword that matches one of the survey metrics
    for pre in pre_post_pairs:
        if pre.lower() in prompt:
            matched = pre
            break

    if matched:
        post = pre_post_pairs[matched]
        st.subheader(f"Average {matched} (Pre vs. Post)")
        avg_pre = df[matched].mean()
        avg_post = df[post].mean()

        plt.bar(["Pre", "Post"], [avg_pre, avg_post], color=["skyblue", "lightgreen"])
        plt.ylabel("Average Score")
        plt.title(matched)
        st.pyplot(plt)
    else:
        st.info("Sorry, I didn't recognize that question. Try asking about one of the survey categories like 'respect', 'friends', or 'mistake'.")

# Show chart if input exists
if user_input:
    generate_chart(user_input)
