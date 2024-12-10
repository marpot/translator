```markdown
# Django Translator Application

This is a simple web application built with Django that allows users to translate text using the Google Translate API.

## Features

- Input text for translation.
- Select a target language for translation.
- View the translated text on the same page.

## Requirements

- Python 3.x
- Django 3.x or above
- googletrans (Google Translate API Python client)

## Installation

Follow these steps to set up the application locally:

1. Clone the repository:


   ```
   bash
   git clone https://github.com/yourusername/translator-app.git
   cd translator-app
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations (if necessary):

   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to:

   ```
   http://127.0.0.1:8000
   ```

## Usage

1. Enter the text you want to translate in the input field.
2. Choose the target language from the dropdown list.
3. Click the "Translate" button to see the translated text.

## Error Handling

- If either the text or the language field is empty, an error message will be displayed: "Both fields (text and language) must be filled."
- If there is an issue with the translation process, an error message will show the details of the problem.
```
