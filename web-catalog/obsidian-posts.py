import json
import os
from notion_client import Client
import datetime

NOTION_TOKEN = ""
NOTION_PAGE_ID = ""
DATABASE_ID = ""  # Замените на ID вашей базы данных

client = Client(auth=NOTION_TOKEN)

def get_pages_and_blocks():
	# Получение содержимого страницы
	page_content = client.pages.retrieve(NOTION_PAGE_ID)

	# Получение блоков страницы
	blocks = client.blocks.children.list(NOTION_PAGE_ID)

	return page_content, blocks

page_content, blocks = get_pages_and_blocks()

import os

# Создание каталога 'pages', если он не существует
if not os.path.exists('pages'):
    os.makedirs('pages')

# Сохранение данных в JSON строку
page_content_json = json.dumps(page_content, ensure_ascii=False, indent=4)
blocks_json = json.dumps(blocks, ensure_ascii=False, indent=4)

# Сохранение данных в файл
with open(f"page.json", "w", encoding="utf-8") as file:
    file.write(page_content_json)
    file.write(blocks_json)