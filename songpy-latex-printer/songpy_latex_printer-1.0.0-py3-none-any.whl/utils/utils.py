def insert_at(text: str, inserted_text: str, starting_index: int) -> str:
    if starting_index <= 0:
        return inserted_text + text
    if starting_index >= len(text):
        return text + inserted_text
    return text[:starting_index] + inserted_text + text[starting_index:]
