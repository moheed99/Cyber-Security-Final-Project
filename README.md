<div align="center">

# 🔒 PayBuddy Security Toolkit

### Advanced Penetration Testing & Security Assessment Framework

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

**Developed by Team CyberGuard | FAST-NUCES Islamabad**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Team](#-team)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-features)
- [System Architecture](#-system-architecture)
- [Installation](#-installation)
- [Configuration](#%EF%B8%8F-configuration)
- [Usage Guide](#-usage-guide)
- [Attack Modules](#-attack-modules)
- [Evidence & Reporting](#-evidence--reporting)
- [Screenshots](#-screenshots)
- [Security & Ethics](#-security--ethics)
- [Team Members](#-team-members)
- [Supervisor](#-supervisor)
- [License](#-license)

---

## 🎯 Overview

**PayBuddy Security Toolkit** is a comprehensive penetration testing and security assessment framework developed as part of the **Cyber Security Final Project** at **FAST-NUCES Islamabad**. This toolkit provides authorized security professionals with a suite of tools to assess network security, test password strength, analyze network traffic, and identify potential vulnerabilities in controlled environments.

### 🎓 Academic Information

- **Course:** Cyber Security
- **Institution:** FAST National University of Computer & Emerging Sciences, Islamabad
- **Semester:** Fall 2025
- **Project Type:** Final Year Project
- **Supervisor:** Dr. Usama Arshad
- **Target Application:** PayBuddy (Payment Processing System)

### 🎯 Project Objectives

This project fulfills the requirements of authorized penetration testing on the PayBuddy application with:
- Written authorization and consent documentation
- Rate limiting (maximum 200 concurrent requests)
- Comprehensive evidence collection
- Detailed reporting with SHA-256 hash verification
- Ethical testing practices within authorized scope

---

## ✨ Features

### 🛡️ Core Security Modules

#### 1️⃣ **Port Scanner**
- Comprehensive TCP port scanning (1-65535)
- Service detection and banner grabbing
- Real-time scan progress visualization
- Detailed service identification
- Multi-format report generation (CSV, JSON, TXT)

#### 2️⃣ **Password Strength Analyzer**
- Entropy-based strength calculation
- Character composition analysis
- Multiple hash generation (MD5, SHA-256, SHA-512, bcrypt)
- Interactive strength gauge visualization
- Hash verification functionality

#### 3️⃣ **DOS/Stress Testing**
- Controlled HTTP load testing
- Configurable request parameters (max 200 concurrent)
- Real-time latency monitoring
- Success/failure rate analysis
- Rate limiting enforcement

#### 4️⃣ **Web Discovery**
- Directory enumeration
- Subdomain discovery
- HTTP status code analysis
- Response size tracking

#### 5️⃣ **Packet Analyzer**
- Live network traffic capture
- Protocol distribution analysis (TCP, UDP, ICMP, HTTP, HTTPS, DNS)
- BPF filter support
- Packet size analysis
- PCAP file upload and analysis

#### 6️⃣ **Comprehensive Reporting**
- Full security assessment reports
- Evidence collection and archival
- Multiple export formats (JSON, TXT, HTML, CSV)
- SHA-256 hash verification
- Automated timestamp logging

### 🔐 Authorization & Compliance

- Identity verification system (identity.txt)
- Written consent documentation (consent.txt)
- Rate limiting (200 concurrent requests max)
- Complete activity logging
- Evidence preservation with timestamps

---

## 🏗️ System Architecture


**Evidence Includes:**
- Test parameters and configuration
- Complete results data
- Timestamp (ISO 8601 format)
- Team information
- Summary statistics

### Report Generation

**Full Security Report Includes:**
- Executive summary with metrics
- All test results from evidence files
- Protocol analysis
- Security recommendations
- Team information and supervisor details
- Timestamp verification
- SHA-256 hash for report integrity

**Export Formats:**
- **JSON:** Structured data for automation and parsing
- **TXT:** Plain text for documentation and archival
- **HTML:** Web-viewable formatted report
- **CSV:** Spreadsheet-compatible for data analysis

---

## 📸 Screenshots

### Dashboard
*Real-time security monitoring with global threat map, live system activity graphs, and quick action panels*

### Port Scanner
*Live port scanning with real-time performance graphs showing scan progress per port*

### Password Analyzer
*Circular strength gauge, entropy calculation, character composition analysis, and multi-algorithm hash generation*

### Packet Capture
*Network traffic analysis with protocol distribution pie chart, packet size histogram, and detailed packet table*

---

## 🔒 Security & Ethics

### Legal Notice

⚠️ **IMPORTANT:** This toolkit is designed for **AUTHORIZED SECURITY TESTING ONLY** on the PayBuddy application. Unauthorized access to computer systems is illegal and punishable under:
- Pakistan Electronic Crimes Act 2016 (PECA)
- Computer Fraud and Abuse Act (CFAA) - USA
- Computer Misuse Act - UK

### Ethical Guidelines

✅ **DO:**
- Use only on PayBuddy or systems you own/have explicit written permission to test
- Respect rate limits (200 concurrent requests max)
- Document all testing activities
- Follow responsible disclosure practices
- Maintain confidentiality of findings
- Report vulnerabilities to application owners
- Preserve evidence with timestamps and hashes

❌ **DON'T:**
- Test production systems without approval
- Exceed authorized testing scope
- Share vulnerabilities publicly before patching
- Use for malicious purposes
- Bypass authentication without authorization
- Exceed rate limiting thresholds
- Modify or delete production data

### Rate Limiting & Compliance

Built-in safeguards as per project guidelines:
- Maximum 200 concurrent requests (enforced)
- Configurable request delays
- Automated logging of all activities
- Evidence collection for audit trails
- SHA-256 hash verification for evidence integrity

### Authorization Requirements

Before using this toolkit:
1. Obtain written authorization from system owner
2. Review and sign consent agreement
3. Verify identity documentation is complete
4. Understand scope and limitations of testing
5. Ensure rate limiting compliance

---

## 👥 Team Members

### Team CyberGuard

| Name | Roll Number | Role | Responsibilities |
|------|-------------|------|-----------------|
| **Moheed Ul Hassan** | 22I-7451 | Team Lead & Backend Developer | Port Scanner, DOS Testing, Architecture |
| **Ali Abbas** | 22I-2285 | Frontend & UI/UX Developer | Dashboard Design, Visualization, Reports |
| **Abdur Rehman** | 22I-2291 | Security Analyst & Tester | Password Analysis, Packet Capture, Testing |


---

## 👨‍🏫 Supervisor

**Dr. Usama Arshad**  
Assistant Professor, Computer Science Department  
FAST National University of Computer & Emerging Sciences, Islamabad

**Course:** Cyber Security (Fall 2025)

---

## 🛠️ Technology Stack

- **Frontend Framework:** Streamlit 1.28+
- **Data Visualization:** Plotly 5.17+ (Interactive charts and graphs)
- **Data Processing:** Pandas 2.0+ (DataFrame manipulation)
- **Security:** bcrypt 4.0+ (Password hashing)
- **Programming Language:** Python 3.8+
- **UI/UX:** Custom CSS with hacking-themed design
- **Background Images:** Unsplash API integration

---

## 📝 Project Structure


---

## 🔄 Version History

### v1.0.0 (November 2025)
- ✅ Initial release
- ✅ All core modules implemented (Port Scanner, Password Tester, DOS Testing, Web Discovery, Packet Analyzer)
- ✅ Full documentation and user guide
- ✅ Evidence collection system with SHA-256 hashing
- ✅ Comprehensive reporting (JSON, TXT, HTML, CSV)
- ✅ Rate limiting enforcement (200 concurrent max)
- ✅ Authorization and consent system
- ✅ Real-time visualization with Plotly
- ✅ Professional hacking-themed UI

---

## 🎓 Project Compliance

This project fulfills all requirements of the Cyber Security course final project:

✅ **Written Authorization:** identity.txt and consent.txt included  
✅ **Rate Limiting:** Maximum 200 concurrent requests enforced  
✅ **Evidence Collection:** All tests logged with timestamps  
✅ **SHA-256 Verification:** Evidence integrity verification  
✅ **Comprehensive Testing:** Multiple attack vectors covered  
✅ **Professional Reporting:** Multiple export formats available  
✅ **Ethical Guidelines:** Legal notices and warnings included  
✅ **Documentation:** Complete README and inline code documentation  

---

## 📧 Contact

For questions, suggestions, or collaboration:

- **Primary Contact:** Moheed Ul Hassan 
- **Institution:** FAST-NUCES Islamabad
- **Course:** Cyber Security (Fall 2025)
- **Supervisor:** Dr. Usama Arshad

---

## 📜 License

This project is developed for **educational purposes** as part of the Cyber Security course at FAST-NUCES Islamabad under the supervision of Dr. Usama Arshad.

**Educational Use Only** - Not licensed for commercial distribution.

All testing must be conducted on authorized systems with proper consent documentation.

---

## 🙏 Acknowledgments

- **Dr. Usama Arshad** - Course Instructor & Project Supervisor
- **FAST-NUCES Islamabad** - Educational Institution & Resources
- **Streamlit Community** - For the excellent web framework and documentation
- **Plotly** - For interactive and professional visualizations
- **PayBuddy Application** - Target application for authorized testing
- **Open Source Community** - For various security tools and libraries

---

## 📚 References & Resources

- Python Documentation: https://docs.python.org/
- Streamlit Documentation: https://docs.streamlit.io/
- Plotly Documentation: https://plotly.com/python/
- OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- Penetration Testing Framework: http://www.vulnerabilityassessment.co.uk/Penetration%20Test.html
- Pakistan Electronic Crimes Act 2016: https://www.pta.gov.pk/en/laws

---

## ⭐ Star This Repository

If you find this project helpful for educational purposes, please consider giving it a ⭐ on GitHub!

---

<div align="center">

**Made with 💻 by Team CyberGuard**

**FAST-NUCES Islamabad | Fall 2025**

**Supervised by Dr. Usama Arshad**

[⬆ Back to Top](#-paybuddy-security-toolkit)

</div>

