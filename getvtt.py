#!/usr/bin/env python3
import csv
import subprocess

INPUT_CSV = "data.csv"


def safe_filename(s: str) -> str:
    return s.strip().lower().replace(" ", "-")


def main():
    with open(INPUT_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):
            title = safe_filename(row["title"])
            url = row["url"]
            vtt_filename = f"{idx}.{title}.vtt"

            print(f"[+] Downloading manual subtitles for: {title}")

            try:
                subprocess.run([
                    "yt-dlp",
                    "--write-subs",          # manual subs
                    "--write-auto-sub",      # auto subs
                    "--skip-download",       # don't download video
                    "--sub-format", "vtt",   # directly save as VTT
                    "-o", vtt_filename,
                    url
                ], check=True)
                print(f"   Saved: {vtt_filename}")
            except subprocess.CalledProcessError:
                print(f"   No manual subtitles found for {title}")


if __name__ == "__main__":
    main()
