from enum import Enum
from dotenv import dotenv_values


class Templates(Enum):
    HOME = "firestore/index.html"
    CREATE = "firestore/create.html"
    LIST = "firestore/list.html"
    NEWSLETTER = "email_templates/newsletter.html"


class Urls(Enum):
    ADMIN = "admin"
    INDEX = "index"
    CREATE = "create"
    LIST = "list"
    LOGIN_REVERSE = "login"
    REGISTER_REVERSE = "register"
    NEWLETTER_REVERSE = "newsletter"


class SettingsConstants(Enum):
    TEMPLATE = "templates/"
    LANGUAGE_CODE = "en-us"
    TZ_INFO = "Asia/Kolkata"
    STATIC_URL = "static/"
    STATIC_DIRES = "templates/static"
    STATIC_ROOT = "assets"
    FIRESTORE_CERTIFICATE_PATH = ".json/certificate.json"
    STORAGE_BUCKET = "STORAGE_BUCKET"


class ModelsConstants(Enum):
    TABLE_NAME = "Articles"


class Constants(Enum):
    FORM_CLASS = "input input-bordered w-full"
    TEXT_AREA = "textarea textarea-bordered textarea-lg w-full"
    SELECT_CLASS = "select select-bordered w-full select-sm"
    NOT_AUTHENTICATED = "Please Login to Continue"
    THEME_CHOICES = (
        ("light", "light"),
        ("dark", "dark"),
        ("cupcake", "cupcake"),
        ("bumblebee", "bumblebee"),
        ("emerald", "emerald"),
        ("corporate", "corporate"),
        ("synthwave", "synthwave"),
        ("retro", "retro"),
        ("cyberpunk", "cyberpunk"),
        ("valentine", "valentine"),
        ("halloween", "halloween"),
        ("garden", "garden"),
        ("forest", "forest"),
        ("aqua", "aqua"),
        ("lofi", "lofi"),
        ("pastel", "pastel"),
        ("fantasy", "fantasy"),
        ("wireframe", "wireframe"),
        ("black", "black"),
        ("luxury", "luxury"),
        ("dracula", "dracula"),
        ("cmyk", "cmyk"),
        ("autumn", "autumn"),
        ("business", "business"),
        ("acid", "acid"),
        ("lemonade", "lemonade"),
        ("night", "night"),
        ("coffee", "coffee"),
        ("winter", "winter"),
        ("dim", "dim"),
        ("nord", "nord"),
        ("sunset", "sunset"),
    )


# Email Constants
class EmailConstants(Enum):
    config = dotenv_values(".env")
    NEWSLETTER = "QuickReads Newsletter Subscribed"
    HOST = config.get("EMAIL_HOST_USER")


# Extra Constants
# -------------------------------------------------------
DESCENDING = "DESCENDING"
TYPE_HTML = "text/html"
NEWSLETTER_SUCCESS = "Newsletter Subscribed Successfully"
