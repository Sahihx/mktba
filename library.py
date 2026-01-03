import os
import json

def load_books(local_repo_path):
    metadata_file = os.path.join(local_repo_path, "metadata.json")
    if not os.path.exists(metadata_file):
        return []

    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    books = []
    for key, data in metadata.items():
        epub_path = os.path.join(local_repo_path, "books", f"{key}.epub")
        if os.path.exists(epub_path):
            books.append({
                "id": key,
                "title": data.get("title", key),
                "author": data.get("author", "Unknown"),
                "path": epub_path
            })
    return books
