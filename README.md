# 🌍 Django Translator Application

A user-friendly web application built with Django that leverages the Google Translate API to provide quick and accurate text translations.

---

## ✨ Features

- **Text Input**: Easily input text to be translated.
- **Target Language Selection**: Choose from a wide range of languages for translation.
- **Instant Output**: View the translated text immediately on the same page.
- **Error Handling**: Clear and descriptive error messages for invalid input or translation issues.

---

## 📋 Requirements

- Python 3.x
- Django 3.x or above
- `googletrans` Python package (Google Translate API client)

---

## 🚀 Installation

Follow the steps below to set up and run the application on your local machine:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/translator-app.git
   cd translator-app
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations** (if applicable):

   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the application**:

   Open your web browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

---

## 🛠 Usage

1. Enter the text you want to translate in the input box.
2. Select the target language from the dropdown menu.
3. Click the **"Translate"** button to generate and view the translated text.

---

## 🐛 Error Handling

- **Empty Fields**: If the text or language fields are not filled, the application will display an error message:  
  _"Both fields (text and language) must be filled."_
- **Translation Issues**: If an error occurs during the translation process, a message will be displayed detailing the problem.

---

## 🏗️ Future Enhancements

- Support for detecting the source language automatically.
- Improved UI for a better user experience.
- Integration with additional translation APIs for redundancy and accuracy.

---

### 🎉 Enjoy translating with Django Translator Application!
```

---
