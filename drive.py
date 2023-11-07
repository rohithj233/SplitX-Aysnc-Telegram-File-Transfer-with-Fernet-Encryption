import os
from telegram import Bot
from telegram import InputFile
from telegram.error import TelegramError
import asyncio

telegram_token = '6826065618:AAGhqItoCkTve1oW2k44zGA9O5_e_RUQnAY'

bot = Bot(token=telegram_token)

folder_path = 'key_parts'

text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

#Read user chat IDs from the user_ids.txt file
user_chat_ids = []
with open('user_ids.txt', 'r') as user_ids_file:
    user_chat_ids = [line.strip() for line in user_ids_file]

#Define an asynchronous function for sending a file to a specific user
async def send_file_to_user(user_index, file_path):
    try:
        chat_id = user_chat_ids[user_index]
        with open(file_path, 'rb') as file:
            await bot.send_document(chat_id=chat_id, document=InputFile(file))
        print(f'Sent file "{file_path}" to user with chat ID {chat_id}')
    except TelegramError as e:
        print(f'Error sending file "{file_path}" to user with chat ID {chat_id}: {e}')

# Create an asynchronous event loop
async def main():
    for user_index, file_path in enumerate(text_files):
        await send_file_to_user(user_index, os.path.join(folder_path, file_path))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
