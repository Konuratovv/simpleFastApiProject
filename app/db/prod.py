SQLITE_FILE_NAME = 'database.db'

def get_db_url():
    return f"sqlite:///{SQLITE_FILE_NAME}"