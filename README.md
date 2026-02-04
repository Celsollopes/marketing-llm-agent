# 🤖 Marketing AI Agent

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.34-FF4B4B?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-0.1-green?style=for-the-badge)
![Llama 3](https://img.shields.io/badge/Model-Llama_3-blueviolet?style=for-the-badge)

> **Project mkp01:** An intelligent digital marketing assistant capable of generating high-engagement social media posts using Large Language Models (LLMs).

## 📋 Project Overview

This project is an **AI-powered Marketing Agent** designed to automate content creation for social media platforms. By leveraging **Groq's API** (running Llama-3-70b) and **LangChain**, the agent understands context, tone of voice, and platform specifics to generate ready-to-publish posts.

This is part of a broader initiative to build **8 Applied AI Projects** for different business sectors, demonstrating MLOps best practices and Agentic Workflows.

### 🌟 Key Features 
* **Multi-Platform Support:** Generates optimized content for Instagram, LinkedIn, Twitter/X, and Blogs.
* **Tone Customization:** Adjusts the writing style (Professional, Casual, Persuasive, etc.).
* **Structured Output:** Delivers Headlines, Body Copy, Hashtags, and CTAs automatically.
* **Fast Inference:** Uses Groq LPU inference engine for near-instant results.

## 🛠 Tech Stack

* **Language:** Python 3.12+
* **Orchestration:** LangChain (Prompts & Chains)
* **LLM Provider:** Groq API (Llama-3-70b-versatile)
* **Interface:** Streamlit
* **Environment:** Linux (WSL/Native)

## 📂 Project Structure

```text
marketing-llm-agent/
├── src/
│   ├── __init__.py
│   ├── app.py           # Frontend (Streamlit UI)
│   └── backend.py       # Backend Logic (LangChain Agent)
├── .env.example         # Example of environment variables
├── .gitignore           # Ignored files for Git
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
## 🚀 Getting Started
Follow these steps to run the project locally.

**Prerequisites**
- Python 3.10 or higher installed.
- A valid API Key from Groq Cloud.

**Installation**
1. **Clone the repository:**

```text
    git clone [https://github.com/celsollopes/marketing-llm-agent.git]  (https://github.com/celsollopes/marketing-llm-agent.git)
```
cd marketing-llm-agent

2. **Create the Virtual Environment:**
```
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```
3. **Install Dependences:**
```
    pip install -r requirements.txt
```
4. **Configure Environment Variables:** 

- Create a ```.env``` file in the root directory and add your API Key:
    ```
    GROQ_API_KEY=your_gsk_key_here
    ```
5. **Run the Application:**
```
    streamlit run src/app.py
```
## 📸 **Usage Example**

1. **Select the target platform (e.g., _LinkedIn_).**
2. **Choose the tone (e.g., _Professional_).**
3. **Input the topic: "_The importance of MLOps for modern enterprises_".**
4. **Click Generate and copy the result.**

---

📄 **License** 

![GitHub License](https://img.shields.io/github/license/Celsollopes/marketing-llm-agent)  
_This project is open-source and available under the MIT License._