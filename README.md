# 🖼️ Ubuntu-Inspired Image Fetcher

> *"I am because we are" – Ubuntu Philosophy*

This project is a Python program that fetches images from the internet, inspired by the Ubuntu principle of **community and sharing**.  
It connects to the global community of shared resources, downloads images respectfully, and organizes them for later use.

---

## ✨ Features
- Fetch images from one or multiple URLs
- Automatically creates a **Fetched_Images** directory
- Prevents downloading duplicate images
- Validates **HTTP headers** to ensure only image files are saved
- Handles errors gracefully (e.g., connection issues, invalid URLs)
- Provides meaningful terminal feedback

---

## 🛠️ Technologies Used
- **Python 3**
- [Requests](https://docs.python-requests.org/) – for making HTTP requests
- **os** – for directory management
- **urllib.parse** – for handling filenames from URLs

---

## 📂 Project Structure
```
Ubuntu_Requests/
│── Fetched_Images/        # Folder where all downloaded images are stored
│── fetch_images.py        # Main Python script
│── README.md              # Project documentation
```

---

## 🚀 How to Run the Program

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Ubuntu_Requests.git
cd Ubuntu_Requests
```

### 2. Install dependencies
```bash
pip install requests
```

### 3. Run the script
```bash
python3 fetch_images.py
```

---

## 🖥️ Example Usage
```bash
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Enter one or more image URLs (separated by spaces): https://www.python.org/static/community_logos/python-logo.png https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg.png

✓ Successfully fetched: python-logo.png
✓ Image saved to Fetched_Images/python-logo.png
✓ Successfully fetched: Tux.svg.png
✓ Image saved to Fetched_Images/Tux.svg.png

Connection strengthened. Community enriched.
```

---

## ⚖️ Ubuntu Principles Applied
- **Community:** Connects to the wider web to fetch shared resources  
- **Respect:** Handles errors gracefully without crashing  
- **Sharing:** Organizes images neatly for reuse  
- **Practicality:** Provides a real, usable tool  

---

## 🔒 Safety Precautions
- Checks `Content-Type` header to ensure only images are downloaded  
- Skips duplicate files  
- Handles network and permission errors safely  

---

## 📌 Challenge Extensions
- Support multiple URLs at once ✅  
- Prevent duplicate downloads ✅  
- Validate HTTP headers ✅  
- (Optional) Add a **file size check** to skip very large files  

---

## 📜 License
This project is created for educational purposes.  
Feel free to fork, modify, and share. 🌍

---

*"A person is a person through other persons." – Ubuntu Philosophy*
