# 🛡️ Phishing Detection Security System

A machine learning–based system that detects **phishing URLs** to protect users from malicious websites that attempt to steal sensitive information like passwords, credit card numbers, or personal data.

This project leverages **NLP + ML techniques** to automatically classify URLs as **phishing** or **legitimate**, helping improve cyber awareness and email/web link security.

---

## 📌 Features

* ✅ Detects phishing websites based on URL content
* ✅ Uses TF-IDF vectorization to convert URL text to features
* ✅ Trained using a Random Forest Classifier
* ✅ Includes a real-time test function to check any input URL
* ✅ Lightweight and fast model ideal for integration in web apps or plugins

---

## 🧰 Technologies Used

* Python 3
* Pandas
* Scikit-learn
* TfidfVectorizer
* Machine Learning (RandomForest)

---

## 📁 Project Structure

```
Phishing-Detection-Security-System/
│
├── phishing_detector.py       # Main script for training and testing
├── dataset.csv                # Dataset of URLs with labels (1 = phishing, 0 = legit)
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation
```

---

## 🧠 Dataset Format

The dataset should contain:

* `url`: the full URL to be analyzed
* `label`: `1` if phishing, `0` if legitimate

Example:

```csv
url,label
"http://secure-login-update-banking.com",1
"https://github.com/login",0
```

You can get datasets from:

* [Kaggle Phishing Datasets](https://www.kaggle.com/datasets)
* [PhishTank](https://phishtank.org/)

---

## 🚀 How to Run the Project

1. 📦 **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. 📂 **Place your dataset.csv** in the project directory.

3. ▶️ **Run the script**:

```bash
python phishing_detector.py
```

4. 💬 **Enter a URL to test** when prompted:

```txt
Enter a URL to check: http://login-verification-update.com
Result: Phishing URL
```

---

## 📊 Model Evaluation

After training, the model outputs:

* **Accuracy score**
* **Precision, Recall, F1-score**
* Helps you assess how well the model detects phishing links

---

## 💡 Future Improvements

* Add GUI with Tkinter or web UI with Flask
* Integrate with browser extension for real-time protection
* Use WHOIS/domain registration features for enhanced detection
* Implement deep learning for more complex patterns

---

## 🛡️ Disclaimer

This tool is created for **educational and ethical hacking purposes only**.
It must not be used for any malicious activities or real-world classification without further security validation.

---

## 👨‍💻 Author

Developed by akash kumar shukla
Contributions, suggestions, and pull requests are welcome!

---

Would you like a version in **Hindi**, or a **GitHub description**, or want to convert this into a web app? Let me know!
