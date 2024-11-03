#!python

import os
import random
from datetime import datetime, timedelta

emojis = ['🚀', '✨', '🐛', '🔥', '🎉', '📝', '✅', '🔨', '🔧', '🛠', '📦', '⚡']

def get_random_emoji():
    return random.choice(emojis)

files_to_add = input("Enter the file(s) you want to add (space separated) or type 'cancel' to exit: ")
if files_to_add.lower() == 'cancel':
    exit()

os.system(f"git add {files_to_add}")

commit_message = input("Enter the commit message or type 'cancel' to exit: ")
if commit_message.lower() == 'cancel':
    exit()

date_offset = input("Enter the date offset (0 for today, -1 for yesterday, 1 for tomorrow, etc.) or type 'cancel' to exit: ")
if date_offset.lower() == 'cancel':
    exit()

try:
    offset = int(date_offset)
    commit_date = (datetime.now() + timedelta(days=offset)).strftime("%Y-%m-%d")
except ValueError:
    print("Invalid date offset.")
    exit()

emoji1 = get_random_emoji()
emoji2 = get_random_emoji()
emoji3 = get_random_emoji()

commit_length = len(commit_message)
mid_point = commit_length // 2
commit_message_with_emojis = f"{emoji1} {commit_message[:mid_point]} {emoji2} {commit_message[mid_point:]} {emoji3}"

os.system(f'git commit --date="{commit_date}" -m "{commit_message_with_emojis}"')

print("Files added and committed with emojis!")
