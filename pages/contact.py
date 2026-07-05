import streamlit as st

st.title("📞 Contact Me")

st.markdown("""
Feel free to get in touch for collaboration, project discussions, automation consulting, or job opportunities.

---
### 📧 Email
**kapugantisanjay@gmail.com**

### 📱 Contact Number
**+91 9848012345**

### 💼 LinkedIn
https://www.linkedin.com/in/sanjaykapuganti

### 🐙 GitHub (Optional)
https://github.com/sanjaykapuganti

---
### 💡 Expertise
- 🐍 Python Development
- 🤖 Selenium Automation
- ✅ Manual Testing
- ☁️ Azure DevOps
- 🐧 Linux Administration

I am always open to discussing new opportunities, automation projects, and innovative software testing solutions.
""")

# Contact Buttons
col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "📧 Send Email",
        "mailto:kapugantisanjay@gmail.com"
    )

with col2:
    st.link_button(
        "💼 LinkedIn Profile",
        "https://www.linkedin.com/in/sanjaykapuganti"
    )

st.divider()

st.info("Thank you for visiting my portfolio. Looking forward to connecting with you!")