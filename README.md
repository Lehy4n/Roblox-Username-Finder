# Roblox-Username-Finder
CHECK ALL THE REQUIREMENTS BEFORE USING THE TOOL OTHERWISE IT WON'T WORK
-----------
DESCRIPTION
-----------
Roblox Username Finder is a tool that automatically searches
for available 3 and 4 character Roblox usernames using the
official Roblox API.


------------------------------------------------------------
FEATURES
------------------------------------------------------------

  - Checks 3 and/or 4 character usernames automatically
  - Randomized search order so you never start from
    the same point twice
  - Saves all available usernames to a .txt file instantly
  - Handles API rate limiting automatically with smart pauses
  - Fully customizable (characters, delay, lengths)
  - Works directly with the official Roblox API


------------------------------------------------------------
REQUIREMENTS
------------------------------------------------------------

  - Windows (7, 10 or 11)
  - Python 3.10 or higher

  Download Python at : https://www.python.org/downloads/

  IMPORTANT : During the Python installation, make sure to
  check the box "Add Python to PATH" at the bottom of the
  first window before clicking "Install Now".


------------------------------------------------------------
HOW TO USE
------------------------------------------------------------

  1. Download and extract all files into the same folder
  2. Double-click START.bat
  3. Wait for the setup to finish
  4. Press ENTER to start the search
  5. Available usernames will appear in the terminal
     and be saved in available_usernames.txt

  To stop the search at any time : press Ctrl + C


------------------------------------------------------------
CUSTOMIZATION
------------------------------------------------------------

Open roblox_username_finder.py with Notepad and edit the
values at the top of the file :

  LENGTHS
    Lengths of usernames to check.
    [3, 4] = checks both 3 and 4 character usernames
    [3]    = checks 3 character usernames only
    [4]    = checks 4 character usernames only

  LOWERCASE (True/False)
    Include lowercase letters (a-z)

  UPPERCASE (True/False)
    Include uppercase letters (A-Z)

  DIGITS (True/False)
    Include digits (0-9)

  UNDERSCORE (True/False)
    Include the underscore character (_)

  DELAY_SECONDS
    Delay in seconds between each request.
    Lower delay = faster search but higher risk of
    being rate limited by Roblox.

  OUTPUT_FILE
    Name of the file where results are saved.


------------------------------------------------------------
RECOMMENDED DELAY
------------------------------------------------------------

  2.0 seconds  ->  Slow        No risk of rate limiting
  1.0 second   ->  Medium      Very low risk (Recommended)
  0.5 seconds  ->  Fast        Low risk
  0.3 seconds  ->  Very fast   Rate limiting possible


------------------------------------------------------------
OUTPUT FILE
------------------------------------------------------------

Available usernames are saved in available_usernames.txt
in the same folder as the script.

Example content :

  x9z  |  found on 2026-04-18 at 14:32:10
  k3w  |  found on 2026-04-18 at 15:01:44


------------------------------------------------------------
FREQUENTLY ASKED QUESTIONS
------------------------------------------------------------

Q : Is this tool safe to use ?
A : Yes. The tool only reads public data from the Roblox API,
    the same data anyone can access by visiting a profile
    page. It does not interact with any account.

Q : Why does the search take so long ?
A : With lowercase letters and digits (36 characters), there
    are over 1.7 million possible 3 and 4 character
    combinations. At 1 request per second that takes around
    20 days. However, available usernames are found along
    the way since the order is randomized.

Q : Can I run multiple windows at the same time ?
A : No, this is not recommended as it increases the risk of
    getting temporarily rate limited by Roblox.

Q : The terminal sometimes shows errors, is that normal ?
A : Yes, occasional network errors are normal. The script
    pauses and retries automatically.


------------------------------------------------------------
DISCLAIMER
------------------------------------------------------------

This tool is for personal use only. Use it responsibly
and in accordance with Roblox's Terms of Service.
The author is not responsible for any misuse.



 Roblox Username Finder — Credits: !Lehy4n (discord: 7lhn)

