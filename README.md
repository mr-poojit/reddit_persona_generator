# 🤖 Reddit Persona Generator

Generate detailed psychological **user personas** from public Reddit profiles using **Gemini 1.5 Flash** and Reddit API.  
This is a submission for the **BeyondChats Generative AI Internship Assignment**.

---

## 📌 Features

- ✅ Scrapes a user's public Reddit **comments** and **posts**
- 🧠 Builds an **AI-generated persona** using Google Gemini 1.5 Flash
- 📎 Cites source Reddit content for each personality trait
- 📝 Saves result as a `.txt` file

---

## 🛠️ Technologies Used

- [Gemini 1.5 Flash](https://aistudio.google.com/app/apikey) (Google Generative Language API)
- [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/en/latest/)
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

Create a file named `.env` in the root directory:

```
GEMINI_API_KEY=your_google_api_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
```

You can get:

- Gemini API key → https://aistudio.google.com/app/apikey
- Reddit client credentials → https://www.reddit.com/prefs/apps

---

## 🚀 Usage

### Run the script:

```bash
python main.py https://www.reddit.com/user/kojied/
```

Output will be saved in the `examples/` folder as `kojied_persona.txt`.

### Sample Outputs Provided:

- `examples/kojied_persona.txt`
- `examples\buhaydigital_persona.txt`

---

## 📂 Folder Structure

```
reddit_persona_generator/
├── main.py
├── reddit_scraper.py
├── persona_builder.py
├── utils.py
├── .env
├── README.md
├── requirements.txt
└── examples/
    ├── kojied_persona.txt
    └── buhaydigital_persona.txt
```

---

## ✅ Notes

- This project follows [PEP8](https://peps.python.org/pep-0008/) conventions.
- No third-party paid tools are used. Gemini 1.5 Flash is used via free API.
- Data is sourced from public Reddit user profiles.

---

## 📧 Contact

Feel free to reach out via GitHub issues if you have questions or want to extend this project.

---

> 🚀 By Poojit Jagadeesh Nagaloti
