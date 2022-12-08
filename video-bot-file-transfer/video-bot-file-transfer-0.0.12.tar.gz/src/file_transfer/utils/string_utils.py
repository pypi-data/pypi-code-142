def remove_special_chars_and_upper(content):
    new_str = ''.join(e for e in content if e.isalnum())
    new_str = str(content).upper()
    return new_str