import sys
from reddit_scraper import scrape_user_data
from persona_builder import build_persona
from utils import save_output, extract_username

if __name__ == "__main__":
    profile_url = sys.argv[1]
    username = extract_username(profile_url)

    print(f"🔍 Scraping Reddit data for u/{username}...")
    posts_and_comments = scrape_user_data(username)

    print("🤖 Building user persona using Gemini...")
    persona = build_persona(username, posts_and_comments)

    save_output(username, persona)
    print(f"✅ Persona saved to: examples/{username}_persona.txt")
