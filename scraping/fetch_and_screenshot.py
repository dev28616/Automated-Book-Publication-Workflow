import asyncio
from playwright.async_api import async_playwright
import os

def save_to_file(content, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

async def fetch_chapter(url, screenshot_path, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.screenshot(path=screenshot_path, full_page=True)
        content = await page.inner_text("body")
        await browser.close()
        save_to_file(content, output_path)

if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    os.makedirs("../data/screenshots", exist_ok=True)
    os.makedirs("../data/chapters_raw", exist_ok=True)
    asyncio.run(fetch_chapter(
        url,
        "../data/screenshots/chapter1.png",
        "../data/chapters_raw/chapter1.txt"
    ))
