import streamlit as st

st.set_page_config(page_title="Skills", page_icon="💻", layout="wide")

st.title("💻 Technical Skills")

st.write(
    "A summary of my technical expertise in automation testing, cloud technologies, "
    "Python development, Linux administration, and quality assurance."
)

# -------------------------
# Programming Languages
# -------------------------
st.header("🐍 Programming Languages")

st.write("**Python**")
st.progress(95)

st.write("**Shell Scripting (Bash)**")
st.progress(90)

# -------------------------
# Automation Testing
# -------------------------
st.header("🤖 Automation Testing")

st.write("**Selenium WebDriver**")
st.progress(95)

st.write("**PyTest**")
st.progress(90)

st.write("**Page Object Model (POM)**")
st.progress(95)

st.write("**Data-Driven Framework**")
st.progress(90)

st.write("**Hybrid Framework**")
st.progress(90)

st.write("**Cross Browser Testing**")
st.progress(90)

# -------------------------
# Manual Testing
# -------------------------
st.header("✅ Manual Testing")

manual_skills = [
    "Functional Testing",
    "Regression Testing",
    "Smoke Testing",
    "Sanity Testing",
    "Integration Testing",
    "System Testing",
    "User Acceptance Testing (UAT)",
    "Test Case Design",
    "Bug Reporting",
    "Agile Methodology",
]

for skill in manual_skills:
    st.markdown(f"✔ {skill}")

# -------------------------
# Linux
# -------------------------
st.header("🐧 Linux")

linux_skills = [
    "Linux Administration",
    "Shell Scripting",
    "Cron Jobs",
    "User Management",
    "File Permissions",
    "Process Management",
    "Log Analysis",
    "System Monitoring",
]

for skill in linux_skills:
    st.markdown(f"✔ {skill}")

# -------------------------
# Azure
# -------------------------
st.header("☁ Azure Cloud")

azure_skills = [
    "Azure DevOps",
    "Azure Pipelines",
    "CI/CD",
    "Azure Virtual Machines",
    "Azure Storage",
    "Azure App Services",
    "Git Integration",
]

for skill in azure_skills:
    st.markdown(f"✔ {skill}")

# -------------------------
# Databases
# -------------------------
st.header("🗄 Databases")

st.write("**SQL**")
st.progress(85)

st.write("**SQLite**")
st.progress(80)

# -------------------------
# Version Control
# -------------------------
st.header("🔧 Version Control")

version_control = [
    "Git",
    "GitHub",
    "Azure Repos",
]

for tool in version_control:
    st.markdown(f"✔ {tool}")

# -------------------------
# Tools
# -------------------------
st.header("🛠 Tools & Technologies")

tools = [
    "Streamlit",
    "JIRA",
    "Azure DevOps",
    "Postman",
    "VS Code",
    "PyCharm",
    "Allure Reports",
    "Excel",
]

cols = st.columns(2)

for index, tool in enumerate(tools):
    cols[index % 2].success(tool)

# -------------------------
# Soft Skills
# -------------------------
st.header("🌟 Professional Skills")

soft_skills = [
    "Problem Solving",
    "Team Collaboration",
    "Analytical Thinking",
    "Communication",
    "Time Management",
    "Leadership",
    "Continuous Learning",
]

for skill in soft_skills:
    st.markdown(f"⭐ {skill}")

st.divider()

st.success(
    "Experienced in designing automation frameworks, developing Python solutions, "
    "managing Linux systems, implementing Azure DevOps CI/CD pipelines, and ensuring "
    "high-quality software delivery through comprehensive testing."
)