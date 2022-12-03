def is_alias(account_id: str) -> bool:
    if len(account_id) != 22:
        return True
    try:
        int(account_id)
        return False if len(account_id) == 22 else True
    except ValueError:
        return True
