import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Hide menu
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Title
st.title("Student Performance Dashboard")

# Load data
df = pd.read_csv("student_performance_data.csv")

# Show basic stats
st.write(f"**Total Students:** {len(df)}")
st.write(f"**Average Score:** {df['Final_Score'].mean():.1f}")
st.write(f"**Pass Rate:** {(df['Result'] == 'Pass').mean() * 100:.1f}%")

st.markdown("---")

# Chart 1: Score Distribution
st.subheader("Score Distribution")
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(df["Final_Score"], bins=20, color="skyblue", edgecolor="black")
ax.axvline(50, color="red", linestyle="--", linewidth=2, label="Pass mark")
ax.set_xlabel("Final Score")
ax.set_ylabel("Number of Students")
ax.legend()
st.pyplot(fig)

# Chart 2: Gender Performance
st.subheader("Average Score by Gender")
gender_avg = df.groupby("Gender")["Final_Score"].mean()

fig, ax = plt.subplots(figsize=(6, 4))
gender_avg.plot(kind='bar', ax=ax, color='lightcoral')
ax.set_ylabel("Average Score")
ax.set_xticklabels(gender_avg.index, rotation=0)
st.pyplot(fig)

# Chart 3: Subject Scores
st.subheader("Average Score by Subject")
subject_data = {
    'Math': df['Math_Score'].mean(),
    'Science': df['Science_Score'].mean(),
    'English': df['English_Score'].mean()
}

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(subject_data.keys(), subject_data.values(), color='lightgreen')
ax.set_ylabel("Average Score")
st.pyplot(fig)

# Chart 4: Pass Rate by Education
st.subheader("Pass Rate by Parental Education")
pass_rate = df.groupby("Parental_Education")["Result"].apply(
    lambda x: (x == "Pass").mean() * 100
).sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8, 4))
pass_rate.plot(kind='bar', ax=ax, color='orange')
ax.set_ylabel("Pass Rate (%)")
ax.set_xticklabels(pass_rate.index, rotation=45, ha='right')
st.pyplot(fig)

# Show data table
if st.checkbox("Show Data"):
    st.dataframe(df)
