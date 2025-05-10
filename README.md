# LangChain Q&A Chatbot

This project is a chatbot built using the **LangChain** framework and various language models from **HuggingFace** and **Groq**. It uses **Streamlit** for the user interface and allows dynamic interaction with different models for answering user queries in a conversational style.

---

## 🔍 Features

- **Dynamic Model Switching** — Choose between Open-Source (HuggingFace) and Closed-Source (Groq) models.
- **Chat History Tracking** — Maintains the conversation history across multiple turns.
- **Multiple Model Options** — Supports local and API-hosted HuggingFace models, and Groq’s high-speed LLMs.
- **Streamlit Interface** — Easy-to-use web UI with model selection and real-time response display.

---

## 📁 What’s Included

📄 chatbot.py # Main Python file with chatbot logic
📝 .env.example # Example environment file with variable names
📄 .gitignore # Ensures sensitive files like .env are ignored
📘 README.md # Project documentation


> 🚫 **Note:** The `.env` file containing API keys is intentionally **not included** for security reasons. Use the `.env.example` to create your own `.env`.

---

## ✅ Prerequisites

- Python 3.7 or higher
- A Hugging Face account + API token (for HuggingFace models)
- A Groq account + API key (for Groq models)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install Dependencies
Make sure your environment is activated (e.g., using venv), then install:
pip install -r requirements.txt

3. Set Up Environment Variables
Copy the .env.example file to .env and add your API keys:

cp .env.example .env

Edit .env and replace placeholders with your actual tokens:
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key

🚀 Running the App
Launch the Streamlit chatbot UI using:

streamlit run chatbot.py
Open your browser to the URL displayed in the terminal to interact with the chatbot.

💬 How to Use
Choose the model type: Open-Source (HuggingFace) or Closed-Source (Groq).

Select a specific model from the dropdown.

Ask any question in the text input.

Optionally, toggle the chat history view to see previous interactions.

🔐 Security Note
The .env file is not included in this repository to protect API keys.

Ensure .env is listed in your .gitignore so that it’s not committed accidentally.

Only the safe .env.example file is shared to show required variables.

🤝 Contributing
Feel free to fork this repo, make improvements, and submit a pull request!

📄 License
This project is licensed under the MIT License.
