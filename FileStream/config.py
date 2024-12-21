from os import environ as env
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = "21851558"
    API_HASH = "045a99f29cbc003618d9786d0b4683d0"
    BOT_TOKEN = "8142840152:AAHg3DtFZbDAt0TQtR4Xt1gvoxR-nK6u8vQ"
    OWNER_ID = int(env.get('OWNER_ID', '1152213967'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    db_password = quote_plus("Sato#321")
    DATABASE_URL = env.get(f"DATABASE_URL", f"mongodb+srv://Kazuma:{db_password}@deployment.zwliu.mongodb.net/?retryWrites=true&w=majority&appName=deployment")
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "filelinktesting"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", "-1002127549042"))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", "-1002127549042"))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))
    AUTH_GROUPS = list(set(int(x) for x in str(env.get("AUTH_GROUPS", "-4583650175")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



