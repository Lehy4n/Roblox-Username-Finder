import requests
import random
import time
import string
import itertools
import os
import sys
from datetime import datetime

# ============================================================
#  ROBLOX USERNAME FINDER — by !Lehy4n
#  Automatically finds available short Roblox usernames (3-4 chars)
# ============================================================
#
#  CONFIGURATION — Edit the values below to customize the search
# ============================================================

LENGTHS         = [3, 4]       # Username lengths to check (3 and/or 4)
LOWERCASE       = True         # Include lowercase letters (a-z)
UPPERCASE       = False        # Include uppercase letters (A-Z)
DIGITS          = True         # Include digits (0-9)
UNDERSCORE      = False        # Include underscore (_)
DELAY_SECONDS   = 0.1         # Delay between requests (recommended: 0.5 - 2.0)
OUTPUT_FILE     = "available_usernames.txt"  # File where results are saved

# ============================================================


def build_charset():
    c = ""
    if LOWERCASE:   c += string.ascii_lowercase
    if UPPERCASE:   c += string.ascii_uppercase
    if DIGITS:      c += string.digits
    if UNDERSCORE:  c += "_"
    return c


def build_queue(charset, lengths):
    all_names = []
    for n in lengths:
        for combo in itertools.product(charset, repeat=n):
            all_names.append("".join(combo))
    random.shuffle(all_names)
    return all_names


def check_username(session, username):
    try:
        url = "https://users.roblox.com/v1/usernames/users"
        payload = {"usernames": [username], "excludeBannedUsers": False}
        resp = session.post(url, json=payload, timeout=10)
        if resp.status_code == 429:
            return "ratelimit"
        if resp.status_code == 200:
            data = resp.json()
            users = data.get("data", [])
            return "available" if len(users) == 0 else "taken"
        # Fallback to old API
        url2 = f"https://api.roblox.com/users/get-by-username?username={username}"
        resp2 = session.get(url2, timeout=10)
        if resp2.status_code == 429:
            return "ratelimit"
        if resp2.status_code == 200:
            data2 = resp2.json()
            if not data2.get("Id") and not data2.get("id"):
                return "available"
            return "taken"
        return "error"
    except requests.exceptions.RequestException:
        return "error"


def save_result(username):
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username}  |  found on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}\n")


def clear_line():
    print("\r" + " " * 110 + "\r", end="")


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 60)
    print("   ROBLOX USERNAME FINDER — Short Username Hunter")
    print("   github.com/Lehy4n/Roblox-Username-Finder  |  Powered by Roblox API")
    print("   Credits: !Lehy4n (discord: 7lhn)")
    print("=" * 60)

    charset = build_charset()
    if not charset:
        print("[ERROR] No character set selected. Please edit the config.")
        sys.exit(1)

    queue = build_queue(charset, LENGTHS)
    total = len(queue)

    print(f"  Charset    : {charset[:50]}{'...' if len(charset) > 50 else ''}")
    print(f"  Lengths    : {LENGTHS}")
    print(f"  Total      : {total:,} usernames to check")
    print(f"  Delay      : {DELAY_SECONDS}s between each request")
    print(f"  Output     : {OUTPUT_FILE}")
    print("=" * 60)
    print("  TIP: Press Ctrl+C at any time to stop the search.")
    print("=" * 60)
    input("\n  Press ENTER to start...\n")

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": "https://www.roblox.com",
        "Referer": "https://www.roblox.com/"
    })

    checked = 0
    found = 0
    errors = 0
    start_time = time.time()
    consecutive_errors = 0

    try:
        for username in queue:
            result = check_username(session, username)
            checked += 1

            elapsed = time.time() - start_time
            rate = checked / elapsed if elapsed > 0 else 0
            pct = (checked / total) * 100

            if result == "available":
                consecutive_errors = 0
                found += 1
                clear_line()
                print(f"\n  [AVAILABLE] {username}  —  {datetime.now().strftime('%H:%M:%S')}")
                print(f"  Profile  : https://www.roblox.com/users/profile?username={username}")
                save_result(username)
                print()

            elif result == "ratelimit":
                consecutive_errors = 0
                clear_line()
                print(f"  [RATE LIMIT] Roblox is limiting requests — waiting 15s...", end="", flush=True)
                time.sleep(15)

            elif result == "error":
                consecutive_errors += 1
                errors += 1
                pause = min(consecutive_errors * 2, 20)
                clear_line()
                print(f"  [ERROR] Network error for {username} — waiting {pause}s...", end="", flush=True)
                time.sleep(pause)

            else:
                consecutive_errors = 0

            print(
                f"\r  [{pct:5.1f}%] Checked: {checked:,}/{total:,}  "
                f"| Found: {found}  "
                f"| Errors: {errors}  "
                f"| Speed: {rate:.1f}/s  "
                f"| Current: {username}    ",
                end="", flush=True
            )

            time.sleep(DELAY_SECONDS)

    except KeyboardInterrupt:
        print("\n\n  [STOPPED] Search interrupted by user.")

    print("\n\n" + "=" * 60)
    print(f"  Search finished!")
    print(f"  Checked  : {checked:,} usernames")
    print(f"  Found    : {found} available username(s)")
    if found > 0:
        print(f"  Saved in : {OUTPUT_FILE}")
    print("=" * 60)
    input("\n  Press ENTER to close.")


if __name__ == "__main__":
    main()
