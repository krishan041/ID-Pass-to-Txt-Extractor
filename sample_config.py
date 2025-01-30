import os

api_id = 23442913
api_hash = os.environ.get("API_HASH", "864a97e16b4ff7dc65ff5e2d1549b4a2")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "7841326954,6428531614")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "7841326954,6428531614")
owner_users = [int(num) for num in osowner_users.split(",")]
