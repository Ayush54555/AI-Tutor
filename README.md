# AI Tutor 🎓

An intelligent, conversational AI-powered tutor built with Streamlit and Google's Gemini API. This app helps students understand complex problems by providing smart hints for mathematical questions and clear explanations for theoretical concepts.

[![Made with Streamlit](https://img.shields.io/badge/Made_with-Streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## ✨ Features

* **Dual Input Methods**: Ask questions by typing text or by uploading an image of your problem.
* **Smart Hint System**: For math problems, the AI provides helpful hints first, encouraging the student to solve it themselves before revealing the full solution.
* **Conceptual Explanations**: For theory-based questions, the AI provides simple, easy-to-understand explanations.
* **Interactive Chat Interface**: A clean, conversational UI powered by Streamlit's chat elements.
* **Powered by Gemini**: Utilizes the powerful and efficient Gemini Flash models for fast and accurate responses.
* **Themed UI**: A sleek, professional dark theme for a comfortable user experience, fully configurable without CSS.

---

## 🚀 Live Demo

[**➡️ Click here to view the live application**](https://ai-tutor-e4yxgmvke2f4chhjdewpqr.streamlit.app/)

---

## 🛠️ Tech Stack

* **Backend**: Python
* **Frontend**: Streamlit
* **AI Model**: Google Gemini 1.5 Flash
* **Libraries**: `google-generativeai`, `Pillow`

---

## ⚙️ Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/ai-tutor.git](https://github.com/your-username/ai-tutor.git)
cd ai-tutor
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to keep dependencies isolated.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all the required libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up Your API Key

This project requires a Google Gemini API key.

* Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
* Create a file at this exact location: `.streamlit/secrets.toml`.
* Add your API key to the `secrets.toml` file as shown below:

    **File: `.streamlit/secrets.toml`**
    ```toml
    # Your Google Gemini API Key
    GEMINI_API_KEY = "YOUR_API_KEY_HERE"
    ```
    *Note: The `.gitignore` file is configured to prevent this file from being uploaded to GitHub.*

### 5. Run the Application

Launch the Streamlit app using the following command:

```bash
streamlit run your_app_name.py
```

Your app should now be running in your web browser!

---

## 🎨 How to Create the Dark Theme

The visual appearance of this app is controlled by a configuration file, not by complex CSS. This makes it easy to change the entire color scheme.

### Step 1: Create the Theme File

1.  In the main folder of your project, create a new folder and name it exactly `.streamlit` (with the dot at the beginning).
2.  Inside the `.streamlit` folder, create a new file named `config.toml`.
3.  Copy and paste the theme settings into this file.

### Step 2: Design the Theme

A great dark theme is about clarity and comfort. Here’s the design philosophy:

* **Base:** Start with a dark charcoal or gray (`#1e1e1e`) for the main background. This is easier on the eyes than pure black.
* **Accent:** Pick one single, vibrant color (`#4285F4`) that contrasts well with the dark background. This will be the `primaryColor` for buttons and interactive elements.
* **Depth:** Use a slightly lighter shade of your base color (`#2e2e2e`) for the `secondaryBackgroundColor`. This subtly lifts containers and chat bubbles off the main background.
* **Readability:** Select a soft, light color for text (`#f0f2f6`) that is easy to read against the dark base.

### Step 3: Write the Configuration

Here is the complete code for the `config.toml` file, which creates the professional "Carbon & Cobalt" theme for this app:

```toml
[theme]
# A confident, classic cobalt blue for interactive elements.
primaryColor = "#4285F4"

# A deep, neutral carbon black for the main background.
backgroundColor = "#1e1e1e"

# A slightly lighter charcoal for depth in containers.
secondaryBackgroundColor = "#2e2e2e"

# A very light, soft gray for text to ensure high contrast and readability.
textColor = "#f0f2f6"

# Font family for all text in the app.
font = "sans serif"

# Hides the default Streamlit menu and header
[server]
headless = true
[ui]
hideTopBar = true
```

---

## ☁️ Deployment

This app is ready to be deployed using [Streamlit Community Cloud](https://streamlit.io/cloud), which offers a free tier for hosting public apps.

1.  Push your project to a public GitHub repository.
2.  Sign up for Streamlit Community Cloud.
3.  Click "New app" and connect your GitHub repository.
4.  Remember to add your `GEMINI_API_KEY` in the advanced settings under "Secrets".

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, please feel free to fork the repository, make your changes, and create a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.
