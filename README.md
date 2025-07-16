# 🤖 Reddit Persona Generator

Generate detailed psychological **user personas** from public Reddit profiles using **Gemini 1.5 Flash** and Reddit API.  
[Reddit Persona Gen](https://reddit-persona-gen.streamlit.app/)

---

## 📌 Features

- ✅ Scrapes a user's public Reddit **comments** and **posts**
- 🧠 Builds an **AI-generated persona** using Google Gemini 1.5 Flash
- 📎 Cites source Reddit content for each personality trait
- 🖼️ Interactive Streamlit frontend with emoji-based dark/light mode toggle
- 📝 Saves result as a `.txt` file

---

## 🛠️ Technologies Used

- [Gemini 1.5 Flash](https://aistudio.google.com/app/apikey)
- [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/en/latest/)
- [Streamlit](https://streamlit.io/) + [streamlit-lottie](https://github.com/andfanilo/streamlit-lottie)
- Python 3, `dotenv`, `tqdm`

---

## 🧪 Setup Instructions

### 🔧 1. Clone the Repo

```bash
git clone https://github.com/mr-poojit/reddit_persona_generator.git
cd reddit_persona_generator
```

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 3. Create `.env` File

Create a file named `.env` and add:

```
GEMINI_API_KEY=your_google_api_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
```

You can get:

- Gemini API key → https://aistudio.google.com/app/apikey
- Reddit API credentials → https://www.reddit.com/prefs/apps

---

## 🚀 Usage

### Run the Streamlit App (Frontend)

```bash
streamlit run app.py
```

Or use the simpler version:

```bash
streamlit run app_clean.py
```

### Run from Terminal (Optional CLI mode)

```bash
python main.py https://www.reddit.com/user/kojied/
```

---

## 📂 Folder Structure

```
reddit_persona_generator/
├── app.py                # Streamlit frontend (animated theme switch)
├── app_clean.py          # Streamlit frontend (plain emoji toggle)
├── main.py               # CLI script version
├── reddit_scraper.py     # Reddit post & comment scraper
├── persona_builder.py    # Gemini-powered persona generation logic
├── utils.py              # Helper functions
├── .env                  # Store your API keys
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── examples/             # Sample generated personas
    ├── kojied_persona.txt
    └── buhaydigital_persona.txt
```

---

## ✅ Notes

- 💡 Fully follows PEP-8 coding style
- 🌐 Works entirely on publicly accessible Reddit data
- 🎨 Includes a fully styled frontend to showcase output professionally
- 🔒 Uses environment variables to keep keys safe

---

## 📧 Contact

Built with ❤️ by **Poojit Jagadeesh Nagaloti**

---

> Ready to deploy, demonstrate, or submit.
