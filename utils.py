import os

def extract_username(url: str) -> str:
    return url.rstrip('/').split('/')[-1]

def save_output(username: str, content: str):
    os.makedirs("examples", exist_ok=True)
    with open(f"examples/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(content)
