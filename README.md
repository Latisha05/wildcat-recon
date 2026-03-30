<img width="648" height="686" alt="image" src="https://github.com/user-attachments/assets/bb98a080-3979-4c1c-8fc8-1b8b061d8a28" />

# 🐆 WILDCAT RECON

> Adaptive Recon & Vulnerability Surface Mapper
> Built for modern web reconnaissance with intelligent filtering and attack surface discovery.

---

## 🚀 Overview

WILDCAT is an automated reconnaissance engine designed to:

* Discover subdomains
* Identify live hosts
* Aggregate URLs from multiple sources
* Extract API endpoints
* Prioritize high-risk attack surfaces

Unlike basic recon scripts, WILDCAT focuses on **signal over noise**, helping security researchers quickly identify potentially vulnerable endpoints.

---

## ⚙️ Features

1. Subdomain Enumeration (subfinder)
2. Alive Host Detection (httpx)
3. URL Crawling (katana)
4. Historical URL Collection (gau, waybackurls)
5. API Endpoint Extraction
6. Smart URL Risk Scoring
7. Automatic Installation of Required Tools

---

## 🧠 How It Works

```
Target Domain
↓
Subdomain Discovery
↓
Alive Host Filtering
↓
URL Aggregation (Crawling + Historical Sources)
↓
API Detection
↓
Risk Scoring
↓
High-Value Targets
```

---

## 🛠️ Installation

### Requirements

* Python 3.10+
* Go (for installing recon tools)

### Setup

```bash
git clone https://github.com/Latisha05/wildcat-recon.git
cd wildcat-recon
python3 main.py
```

> ⚡ WILDCAT automatically installs required tools on first run.

---

## 🧪 Usage

```bash
python3 main.py
```

Enter target domain:

```
example.com
```
---

## 🔥 Example Output

```
🔥 High Risk URLs:

https://target.com/api/user?id=1       [Score: 8]
https://admin.target.com/login         [Score: 7]
https://target.com/debug               [Score: 9]
```

---

## ⚠️ Disclaimer

This tool is intended for:

* Educational purposes
* Authorized security testing only

Do NOT use against systems without permission.

---

## 🧩 Future Improvements

* ⚡ Parallel / Async scanning
* 🧠 AI-based vulnerability prediction
* 📜 JavaScript endpoint extraction
* 🎯 Parameter mining (XSS / IDOR detection)
* 🌈 CLI UI enhancements

---

## 👤 Author

**Latisha05**

---

## ⭐ Support

If you found this useful:

* Star ⭐ the repo
* Share with others in cybersecurity community
