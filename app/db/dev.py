SQLITE_FILE_NAME = 'database.db'

def get_db_url():
    return f"sqlite+aiosqlite:///{SQLITE_FILE_NAME}"