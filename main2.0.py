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

# Variable descriptions
variable_descriptions = {
    'PHYSACT': 'I am good at most physical activities',
    'CLASS': 'I have classmates who like me the way I am',
    'RESPECT': 'I show respect for others',
    'FRIENDS': 'I have classmates I can become friends with',
    'RESPACTS': 'I accept responsibility for my actions',
    'HAPPYAM': 'I am happy the way I am',
    'MAKEFUN': 'I have classmates who sometimes make fun of me',
    'MISTAKE': 'I admit when I make a mistake',
    'LIKEPER': 'I like the kind of person I am',
    'PAYATT': 'I have classmates who pay attention to what I say',
    'STANDUP': 'I stand up for kids who are being picked on',
    'TIMECOMM': 'I spend time helping my community',
    'SAD': 'It makes me sad to see a girl who can’t find anyone to play with',
    'HELPCOMM': 'I help others in my community',
    'UPSET': 'I feel upset when I see a girl getting her feelings hurt',
    'BADLY': 'I feel badly for other girls who are sad',
    'PICKED': 'I feel badly when I see a girl getting picked on',
    'ELEC': 'On a school day, hours spent on electronics',
    'AGE': 'Participant age',
    'GRADE': 'Participant grade',
    'BLACK': 'Identifies as Black',
    'ASIAN': 'Identifies as Asian',
    'WHITE': 'Identifies as White',
    'OTHER': 'Identifies as Other race/ethnicity',
    'PARTSEAS': 'Participates in a seasonal sport'
}


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
    'STANDUP': 'STANDUPP',
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

    # Show the variable description
    for var in matched_metrics:
        description = variable_descriptions.get(var, "No description available.")
        st.markdown(f"<div style='font-size:20px; font-weight:bold;'>{var}: {description}</div>", unsafe_allow_html=True)


    
    labels = []
    values = []
    colors = []

    for var in matched_metrics:
        post_var = pre_post_pairs[var]
        avg_pre = df[var].mean()
        avg_post = df[post_var].mean()
        labels.extend([f"{var} Pre", f"{var} Post"])
        values.extend([avg_pre, avg_post])
        colors.extend(["pink", "purple"])

    fig, ax = plt.subplots()
    x = np.arange(len(labels))
    ax.bar(x, values, color=colors)
    ax.set_ylabel("Average Score")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_title("Results")
    st.pyplot(fig)

    for var in matched_metrics:
        post_var = pre_post_pairs[var]
        avg_pre = df[var].mean()
        avg_post = df[post_var].mean()
        difference = avg_pre - avg_post
        percent_change = ((avg_post - avg_pre) / avg_pre) * 100 if avg_pre != 0 else 0

        # NEW: Distribution bar chart for survey scores
        with st.container():
            st.markdown(f"**Distribution of Scores for {var}**")
            fig_dist, ax_dist = plt.subplots()

            bins = [1, 2, 3, 4, 5]
            pre_counts = df[var].value_counts().reindex(bins, fill_value=0)
            post_counts = df[post_var].value_counts().reindex(bins, fill_value=0)

            ax_dist.bar(bins, pre_counts, width=0.4, label=f"{var} Pre", alpha=0.6, align='center')
            ax_dist.bar([b + 0.4 for b in bins], post_counts, width=0.4, label=f"{post_var} Post", alpha=0.6, align='center')

            ax_dist.set_xlabel("Survey Score (1–5)")
            ax_dist.set_ylabel("Number of Responses")
            ax_dist.set_xticks([b + 0.2 for b in bins])
            ax_dist.set_xticklabels(bins)
            ax_dist.legend()
            ax_dist.set_title(f"{var} Score Distribution")

            st.pyplot(fig_dist)




        with st.container():
            st.subheader(f"Summary for {var}")
            st.write(f"**Pre Survey Mean ({var})**: {avg_pre:.2f}")
            st.write(f"**Post Survey Mean ({post_var})**: {avg_post:.2f}")
            st.write(f"**Difference (Pre - Post)**: {difference:.2f}")
            st.write(f"**Percent Change**: {percent_change:.2f}%")


# Show chart on input
if user_input:
    generate_grouped_chart(user_input)
