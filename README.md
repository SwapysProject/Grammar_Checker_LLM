# 📚 Automatic Grammar Checker

This is a simple **Automatic Grammar Checker** built using **Streamlit** and the **`prithivida/grammar_error_correcter_v1`** model from Hugging Face. It automatically corrects grammar mistakes in the given text.

## ✨ Features
- 📝 Fixes grammatical errors in English sentences
- ✔️ Runs locally on **CPU** (No GPU needed)
- 🌐 Deployable for free on **Streamlit Cloud**

---

## ⚡ Installation

### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/grammar_checker.git
cd grammar_checker
```

### **2. Create Virtual Environment (Optional, Recommended)**
```sh
python -m venv venv
```
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🌐 Running the App Locally
```sh
streamlit run app.py
```
This will launch the **Streamlit web app** in your browser.

---

## ☁️ Deploy on Streamlit Cloud
1. Push the code to **GitHub**:
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-repo-URL>
   git push -u origin main
   ```
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and deploy the app by connecting your GitHub repo.

---

## 🔧 Project Structure
```
grammar_checker/
├── app.py              # Streamlit App Script
├── requirements.txt    # Dependencies
├── README.md           # Project Documentation
```

---

## ⚙ Technologies Used
- **Python**
- **Streamlit**
- **Hugging Face Transformers**
- **PyTorch**

---

## 🔍 Example
**Input:** "He go to school every day."

**Corrected Output:** "He goes to school every day."

---

## ✨ Contributing
Feel free to **fork** this repo and submit a PR if you improve the project!

