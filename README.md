# 📚 Automated Book Publication Workflow

A complete AI-powered pipeline to automate the book publishing process — from scraping public domain content to rewriting and reviewing chapters using Google's Gemini 1.5 Flash, with a human-in-the-loop interface for iterative editing.

---

## 🚀 Features

🔍 **Web Scraping**
Scrapes full-text chapters and screenshots from online public domain sources using Playwright.

✍️ **AI Writer (Gemini 1.5 Flash latest)**
Automatically spins (rewrites) chapters with creative language using generative AI.

🧠 **AI Reviewer**
Improves grammar, tone, and coherence through AI-driven review.

🧑‍💼 **Human-in-the-Loop UI**
Professionally designed Flask web app to let writers/editors refine the text manually at each stage.

💾 **Version Control & Search**
Stores each version in ChromaDB and retrieves them intelligently using a Reinforcement Learning-based search strategy.

---

## 🗂️ Folder Structure

```
automated_book_pipeline/
﹣﹣ main.py                     # Full pipeline automation
﹣﹣ config.py                   # Loads API key from .env
﹣﹣ requirements.txt
﹣﹣ .env                        # (not committed) Gemini API key
﹣﹣ scraping/
﹣﹣ └️ fetch_and_screenshot.py
﹣﹣ ai_writer/
﹣﹣ ├️ writer.py
﹣﹣ ├️ reviewer.py
﹣﹣ └️ __init__.py
﹣﹣ human_interface/
﹣﹣ └️ flask_app.py
﹣﹣ storage/
﹣﹣ └️ chromadb_utils.py
﹣﹣ rl_search/
﹣﹣ └️ search_policy.py
﹣﹣ data/
﹣﹣ ├️ screenshots/            # Scraped screenshots
﹣﹣ ├️ chapters_raw/           # Raw scraped chapters
﹣﹣ └️ versions/               # Spun + reviewed versions
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/dev28616/automated-book-pipeline.git
cd automated-book-pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
python -m playwright install
```

### 3. Set up your API key

Create a `.env` file:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

---

## ↺ Usage

### 🔧 Run the Full Pipeline

```bash
python main.py
```

This will:

- Scrape the chapter
- Generate the spun version
- Review it
- Save all versions in `data/versions/`

### 🌐 Run the Flask UI

```bash
python -m human_interface.flask_app
```

Then visit:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 AI Models

- **LLM Used**: [Gemini 1.5 Flash latest](https://ai.google.dev/)
- **Functions**:

  - `spin_content()` in `writer.py`
  - `review_content()` in `reviewer.py`

---

## 🎥 Demo Video

🎥 [Watch the Demo Here](#)
_(Link to your YouTube or Google Drive submission)_

---

## 🛡️ Notes

- ✅ No data is stored or shared externally.
- 🚫 `.env` is not committed to GitHub for security.
- 📜 All scraped content is from the public domain (Wikisource).

---

## 👨‍💻 Author

**Debojyoti Mondal**
📢 [LinkedIn](https://linkedin.com/debojyotimondal)
💻 Passionate about AI, NLP, and automation.
