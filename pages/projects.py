import streamlit as st

st.set_page_config(page_title="Projects", page_icon="📂", layout="wide")

st.title("📂 My Projects")

st.markdown("""
Explore some of the automation, cloud, Python, Linux, and testing projects that demonstrate my technical expertise.
""")

# -----------------------------
# Project 1
# -----------------------------
with st.expander("🤖 Selenium Automation Framework"):
    st.subheader("Objective")
    st.write("Developed a scalable Hybrid Automation Framework to automate web application testing.")

    st.subheader("Technologies")
    st.write("""
    - Python
    - Selenium WebDriver
    - PyTest
    - Page Object Model (POM)
    - Allure Reports
    - Azure DevOps
    """)

    st.subheader("Key Features")
    st.write("""
    ✔ Data-Driven Testing

    ✔ Cross Browser Testing

    ✔ Parallel Execution

    ✔ Screenshot Capture on Failure

    ✔ HTML & Allure Reports

    ✔ CI/CD Integration
    """)

    st.success("Result: Reduced manual testing effort by 80%.")

# -----------------------------
# Project 2
# -----------------------------
with st.expander("🐧 Linux Server Monitoring Tool"):
    st.subheader("Objective")
    st.write("Automated Linux server monitoring using Python and Shell scripting.")

    st.subheader("Technologies")
    st.write("""
    - Linux
    - Shell Scripting
    - Python
    - Cron Jobs
    """)

    st.subheader("Features")
    st.write("""
    ✔ CPU Monitoring

    ✔ Memory Usage

    ✔ Disk Space Monitoring

    ✔ Service Status

    ✔ Email Alerts

    ✔ Log Collection
    """)

    st.success("Result: Improved server uptime and proactive monitoring.")

# -----------------------------
# Project 3
# -----------------------------
with st.expander("☁ Azure DevOps CI/CD Pipeline"):
    st.subheader("Objective")
    st.write("Automated build, testing, and deployment using Azure DevOps.")

    st.subheader("Technologies")
    st.write("""
    - Azure DevOps
    - YAML Pipelines
    - Git
    - Python
    """)

    st.subheader("Features")
    st.write("""
    ✔ Automated Build

    ✔ Automated Selenium Tests

    ✔ Continuous Integration

    ✔ Continuous Deployment

    ✔ Release Pipelines
    """)

    st.success("Result: Faster software delivery with automated deployments.")

# -----------------------------
# Project 4
# -----------------------------
with st.expander("🐍 Python API Automation Framework"):
    st.subheader("Objective")
    st.write("Designed an API automation framework for REST services.")

    st.subheader("Technologies")
    st.write("""
    - Python
    - Requests
    - PyTest
    - JSON
    - SQL
    """)

    st.subheader("Features")
    st.write("""
    ✔ GET, POST, PUT, DELETE Requests

    ✔ Authentication Testing

    ✔ Database Validation

    ✔ JSON Schema Validation

    ✔ HTML Reports
    """)

    st.success("Result: Increased API testing coverage and reduced regression effort.")

# -----------------------------
# Project 5
# -----------------------------
with st.expander("📊 Streamlit Test Dashboard"):
    st.subheader("Objective")
    st.write("Developed an interactive dashboard to visualize automation execution results.")

    st.subheader("Technologies")
    st.write("""
    - Streamlit
    - Python
    - Pandas
    - Plotly
    """)

    st.subheader("Features")
    st.write("""
    ✔ Dashboard Analytics

    ✔ Pass/Fail Charts

    ✔ Execution Trends

    ✔ Download Reports

    ✔ Interactive Filters
    """)

    st.success("Result: Improved visibility into automation execution metrics.")

# -----------------------------
# Project 6
# -----------------------------
with st.expander("🌐 Web Scraping Automation"):
    st.subheader("Objective")
    st.write("Collected data from dynamic websites for reporting and analysis.")

    st.subheader("Technologies")
    st.write("""
    - Python
    - Selenium
    - BeautifulSoup
    - Pandas
    """)

    st.subheader("Features")
    st.write("""
    ✔ Dynamic Website Scraping

    ✔ Excel Export

    ✔ CSV Export

    ✔ Scheduled Execution

    ✔ Data Cleaning
    """)

    st.success("Result: Automated data collection and reporting.")

# -----------------------------
# Project 7
# -----------------------------
with st.expander("✅ Manual Testing Management"):
    st.subheader("Objective")
    st.write("Performed end-to-end manual testing for enterprise web applications.")

    st.subheader("Responsibilities")
    st.write("""
    ✔ Test Planning

    ✔ Test Case Design

    ✔ Smoke Testing

    ✔ Regression Testing

    ✔ Functional Testing

    ✔ Defect Reporting

    ✔ UAT Support

    ✔ Agile Scrum Participation
    """)

    st.success("Result: Delivered high-quality software with reduced production defects.")

st.divider()

st.info("💡 Passionate about building scalable automation solutions, improving software quality, and leveraging cloud technologies to streamline software delivery.")