"""
8BIT PYTHON - Instagram Followers Extractor
Author: BossDuck
Project: 8bit Python
"""

from instagrapi import Client
from dotenv import load_dotenv
import os
import csv

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")


def login():
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    return cl


def get_followers(cl, username):
    user_id = cl.user_id_from_username(username)
    return cl.user_followers(user_id)


def save_to_csv(followers):
    with open("followers.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "full_name", "is_private"])

        for user in followers.values():
            writer.writerow([
                user.username,
                user.full_name,
                user.is_private
            ])


def main():
    cl = login()
    followers = get_followers(cl, USERNAME)

    print(f"Total followers: {len(followers)}")

    save_to_csv(followers)
    print("Saved to followers.csv")


if __name__ == "__main__":
    main()