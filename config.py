class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = "mysql+aiomysql://u0501959_super:VladA2004!@server177.hosting.reg.ru/u0501959_tapper"
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    BASE_URL = "https://fastapi.space/"
    TELEGRAM_BOT_TOKEN = "7914552269:AAH8-2B-Ks8c9Bc2FBBmO3AkqsB6l9GiP4I"
    ADMIN_ID = 639238101
    
    def get_webhook_url(self) -> str:
        return f"{self.BASE_URL}/webhook"
    
config = Config()     