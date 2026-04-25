import streamlit as st
import random

st.title("AI Talent Scouting Agent")

# Input Job Description
jd = st.text_area("Enter Job Description")

# Dummy candidates
candidates = [
    {"name": "Ravi", "skills": ["python", "sql"]},
    {"name": "Anjali", "skills": ["html", "css", "javascript"]},
    {"name": "Rahul", "skills": ["python", "machine learning"]},
    {"name": "Sneha", "skills": ["excel", "communication", "sales"]}
]

# Matching function (Improved)
def match_score(jd, skills):
    jd_words = jd.lower().split()
    score = 0
    matched_skills = []

    for skill in skills:
        if skill.lower() in jd_words:
            score += 1
            matched_skills.append(skill)

    return score, matched_skills

# Button logic
if st.button("Find Candidates"):
    results = []

    for c in candidates:
        score, matched = match_score(jd, c["skills"])
        interest = random.randint(50, 100)

        results.append({
            "name": c["name"],
            "match": score,
            "interest": interest,
            "skills": c["skills"],
            "matched": matched
        })

    # Sort by match score
    results = sorted(results, key=lambda x: x["match"], reverse=True)

    st.subheader("Top Candidates")
    st.success("Candidates ranked based on skill match and interest level")

    for r in results:
        st.write(f"### {r['name']}")
        st.write(f"Match Score: {r['match']}")
        st.write(f"Interest Score: {r['interest']}")

        if r["matched"]:
            st.write(f"Matched Skills: {', '.join(r['matched'])}")
        else:
            st.write("Matched Skills: None")

        st.write("---")