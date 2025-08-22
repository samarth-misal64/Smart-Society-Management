# 📱 Smart Society SMS Notification  

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Fast2SMS](https://img.shields.io/badge/API-Fast2SMS-orange)](https://www.fast2sms.com/)  

A lightweight **SMS notification system** built in Python 🐍 to help **housing societies & communities** send instant alerts (like power cuts ⚡, water supply updates 💧, or meeting reminders 📢) via the **Fast2SMS API**.  

---

## ✨ Features
- ✅ Send custom SMS to one or multiple numbers  
- ✅ Powered by [Fast2SMS](https://www.fast2sms.com/) for fast & reliable delivery  
- ✅ Plug-and-play — integrate into bigger society management systems  
- ✅ Minimal dependencies, simple usage  

---

## 📂 Project Structure
```
📦 GIT Smart Society Management
 └── 📜 sms.py   # Main script to send SMS using Fast2SMS
```

---

## ⚙️ Requirements
- Python **3.7+**  
- Libraries:  
  - `requests`  
  - `boto3` *(reserved for future AWS SNS integration)*  

Install dependencies:
```bash
pip install requests boto3
```

---

## 🔑 Setup
1. Create an account at [Fast2SMS](https://www.fast2sms.com/) and get your **API Key**.  
2. Open `sms.py` and replace the placeholder key in the headers section:  

   ```python
   headers = {
       'authorization': "YOUR_FAST2SMS_API_KEY",
       'Content-Type': "application/x-www-form-urlencoded",
       'Cache-Control': "no-cache",
   }
   ```

💡 **Best Practice:** Store your API key in an environment variable or `.env` file instead of hardcoding it.  

---

## ▶️ Usage
Run directly:
```bash
python sms.py
```

Or import in another Python script:
```python
from sms import send_sms

# Single number
send_sms("Meeting at clubhouse at 6 PM", "9876543210")

# Multiple numbers (comma-separated)
send_sms("Water supply will be off tomorrow 9am-12pm", "9876543210,9123456780")
```

---

## 🖼️ Example Output
```
SMS Sent Successfully :)
{"return": true, "request_id": "abc123", "message": ["SMS sent successfully."]}
```

---

## 🔒 Security Note
⚠️ **Never commit your API key to GitHub**.  

Use environment variables instead:
```python
import os
API_KEY = os.getenv("FAST2SMS_API_KEY")
```

---

## 🚀 Roadmap
- 📇 Contact management via DB/CSV  
- 👥 Group SMS (Residents / Staff / Committee)  
- ☁️ AWS SNS integration (boto3)  
- 🖥️ GUI or web dashboard for non-technical users  

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).  

---

💡 *Built with ❤️ to make society communication smarter!*  
