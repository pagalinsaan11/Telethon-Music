import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538")
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6094467638:AAGTYJEP5z_PpGIdIRPDfykevUqbFvvdmNs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKwBu68OHKTXVswMWIIVuDpI2GKMJqpdnAMXquwvgmy6y1lRSb1wm-yyITawqb1j2MgQdD1JDqpIgHdSil6oCF8cTMCuD5oxAtryciTCQws7H9H-kOR50snbE-z2zAbn9TlkzHaXuus3ViI-3Ji0L0eIOlxfQIO0dpvcdyxSVg-uZh_hBmGqrXLiCRtjDbCJ4qnN_wnLAInlKifpHwFIki2dRxi9c3-gBcgvdDMm9dNa3EsQc4Ior-IaLcHLGwOpWVldlQrHami4ehRcZ5lSwzMGXSmz6CNxESxzaOxo1XQwQ7T2IMRRs9TFBKw7weeCeS1nm8enZ-VnlQMq94D12NJHmd4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
