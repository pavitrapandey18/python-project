import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Study Analyzer")

st.title("📚 Study Performance Analyzer")
st.caption("Analyze marks, find weaknesses, and predict performance")

file=st.file_uploader("Upload Student Data CSV", type=["csv"])

if file:
    df=pd.read_csv(file)
    df.dropna(inplace=True)
    st.subheader("Data Preview")
    st.dataframe(df)

    students=df["Name"].unique()
    selected_student=st.selectbox("Select Student", students)

    student_data=df[df["Name"]==selected_student]
    subjects=[col for col in df.columns if col not in ["Name"]]

    scores=student_data[subjects].values.flatten()

    st.subheader("📊 Subject Scores")

    plt.bar(subjects, scores)
    plt.xticks(rotation=45)
    st.pyplot(plt)

    avg=np.mean(scores)
    max_score=np.max(scores)
    min_score=np.min(scores)

    col1, col2, col3 = st.columns(3)
    col1.metric("Average", f"{avg:.2f}")
    col2.metric("Highest", f"{max_score}")
    col3.metric("Lowest", f"{min_score}")

    st.subheader("✌️😭  Weak Subjects")
    weak=[subjects[i] for i in range(len(scores)) if scores[i] < avg]

    if weak:
        st.write(", ".join(weak))
    else:
        st.success("No weak subjects ✌️😁")

    st.subheader("📈 Class Average Comparison")
    class_avg=df[subjects].mean()

    plt.figure()
    plt.plot(subjects, class_avg.values, label="Class Avg")
    plt.plot(subjects, scores, label="Student")
    plt.legend()
    plt.xticks(rotation=45)

    st.pyplot(plt)

    st.subheader("🥇 Rank Estimation")
    df["Total"]=df[subjects].sum(axis=1)
    df["Rank"]=df["Total"].rank(ascending=False)

    student_rank=df[df["Name"]==selected_student]["Rank"].values[0]

    st.write(f"Estimated Rank: {int(student_rank)} out of {len(df)}")
    st.subheader("📈Performance Trend")

    trend=scores+np.random.randint(-5,5,size=len(scores))

    plt.figure()
    plt.plot(subjects, trend)
    plt.xticks(rotation=45)

    st.pyplot(plt)

else:
    st.info("Upload a CSV like: Name,Math,Physics,Chemistry,...")
    