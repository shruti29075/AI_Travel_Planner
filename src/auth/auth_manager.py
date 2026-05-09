import hashlib
from src.database.db import get_connection

def hash_password(password: str) -> str:
    """Hashes a password with SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(username: str, password: str) -> bool:
    """Registers a new user in the database. Returns True if successful, False if exists."""
    password_hash = hash_password(password)
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        return True
    except Exception as e:
        # Likely a unique constraint failure
        return False
    finally:
        conn.close()

def login_user(username: str, password: str) -> dict:
    """Verifies user credentials. Returns a dict with user info if valid, None otherwise."""
    password_hash = hash_password(password)
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, username FROM users WHERE username=? AND password_hash=?", (username, password_hash))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return {"id": user[0], "username": user[1]}
    return None
