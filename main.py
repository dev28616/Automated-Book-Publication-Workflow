import asyncio
import os
from scraping.fetch_and_screenshot import fetch_chapter
from ai_writer.writer import spin_content
from ai_writer.reviewer import review_content
from storage.chromadb_utils import store_version

import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# Paths
URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
SCREENSHOT_PATH = "data/screenshots/chapter1.png"
RAW_PATH = "data/chapters_raw/chapter1.txt"
SPUN_PATH = "data/versions/chapter1_spun.txt"
REVIEWED_PATH = "data/versions/chapter1_reviewed.txt"

# Ensure directories exist
os.makedirs("data/screenshots", exist_ok=True)
os.makedirs("data/chapters_raw", exist_ok=True)
os.makedirs("data/versions", exist_ok=True)

def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def write_file(content, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

async def run_pipeline():
    print("[1] Scraping chapter...")
    await fetch_chapter(URL, SCREENSHOT_PATH, RAW_PATH)
    raw_text = read_file(RAW_PATH)

    print("[2] Running AI Writer...")
    spun_text = spin_content(raw_text)
    write_file(spun_text, SPUN_PATH)
    store_version("chapter1_spun", spun_text)

    print("[3] Running AI Reviewer...")
    reviewed_text = review_content(spun_text)
    write_file(reviewed_text, REVIEWED_PATH)
    store_version("chapter1_reviewed", reviewed_text)

    print("[!] Pipeline complete. Files saved in data/versions/")

if __name__ == "__main__":
    asyncio.run(run_pipeline())
