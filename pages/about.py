import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

st.title("👨‍💻 About Me")

st.markdown("""
## Welcome!

I am an experienced QA Automation Engineer and Python Developer with strong expertise in software testing, automation, cloud technologies, and Linux system administration. I have hands-on experience designing scalable automation frameworks, improving software quality, and deploying applications on cloud platforms.

### Technical Skills

- 🐧 **Linux Expert**
  - Shell Scripting
  - Process Management
  - File System Administration
  - User & Permission Management
  - Cron Jobs
  - Log Analysis
  - Networking Basics

- 🤖 **Selenium Expert**
  - Selenium WebDriver
  - TestNG / PyTest
  - Page Object Model (POM)
  - Data-Driven Framework
  - Hybrid Automation Framework
  - Cross Browser Testing
  - Selenium Grid

- ✅ **Manual Testing**
  - Functional Testing
  - Regression Testing
  - Smoke & Sanity Testing
  - Integration Testing
  - UAT
  - Test Case Design
  - Defect Lifecycle Management
  - Jira & Azure DevOps

- ☁️ **Azure**
  - Azure DevOps
  - Azure Pipelines
  - Azure Virtual Machines
  - Azure Storage
  - Azure App Services
  - CI/CD
  - ARM Templates (Basics)

- 🐍 **Python Expert**
  - Object-Oriented Programming
  - Automation Scripts
  - API Testing
  - Data Processing
  - Web Scraping
  - Flask
  - Streamlit
  - Pandas
  - NumPy

### Strengths

✔ Automation Framework Development

✔ Problem Solving

✔ CI/CD Integration

✔ Agile Methodology

✔ Test Strategy Planning

✔ Performance Optimization

✔ Team Collaboration

✔ Continuous Learning
""")

st.header("📂 Sample Projects")

projects = [
    {
        "title": "Enterprise Selenium Automation Framework",
        "description": """
        • Developed Hybrid Automation Framework using Selenium + Python + PyTest.
        • Implemented Page Object Model.
        • Integrated with Azure DevOps Pipelines.
        • Generated Allure Reports.
        • Reduced manual testing effort by 80%.
        """
    },
    {
        "title": "Linux Server Health Monitoring",
        "description": """
        • Developed Python and Shell scripts to monitor CPU, Memory, Disk, and Services.
        • Automated log collection.
        • Email alerts on threshold breaches.
        """
    },
    {
        "title": "Azure CI/CD Automation",
        "description": """
        • Configured Azure Pipelines for automated testing.
        • Automated deployments to Azure App Service.
        • Integrated Selenium test execution.
        """
    },
    {
        "title": "API Testing Framework",
        "description": """
        • Developed REST API automation using Python Requests.
        • JSON Schema Validation.
        • Database Verification.
        • HTML Report Generation.
        """
    },
    {
        "title": "Web Scraping & Data Analytics",
        "description": """
        • Built Python web scraper using BeautifulSoup and Selenium.
        • Stored data in Excel and SQL.
        • Dashboard using Streamlit.
        """
    },
    {
        "title": "Streamlit Test Dashboard",
        "description": """
        • Interactive dashboard for automation execution.
        • Displayed test reports.
        • Generated execution trends.
        • Downloadable Excel reports.
        """
    }
]

for project in projects:
    with st.expander(project["title"]):
        st.write(project["description"])

st.success("Always passionate about building scalable automation solutions and improving software quality through innovation.")