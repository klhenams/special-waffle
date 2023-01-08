import gspread
from django.conf import settings
from django.utils.html import strip_tags

from app.spreadsheets.models import Item

conf = getattr(settings, "GOOGLE_API", {})


class Spreadsheet:
    gc = None

    def __init__(self) -> None:
        try:
            self.gc = gspread.service_account(
                filename=conf.get("GOOGLESHEET_SERVICE_ACCOUNT", None)
            )
        except Exception as err:
            # Handle exceptions here
            print("Initialization error: ", err)

    def get(self):
        try:
            sh = self.gc.open_by_key(conf.get("GOOGLESHEET_KEY", None))
            worksheet = sh.get_worksheet(0)
            return self.serialze_data(worksheet.get_all_records())
        except Exception as err:
            print("Fetching error: ", err)

    def serialize_item(self, item) -> Item:
        # Clean description
        item["description"] = strip_tags(item["description"])
        return Item(**item)

    def serialze_data(self, records):
        return [self.serialize_item(item) for item in records]

    # def save_to_db(self, records):
    #     # works for first time, and fails other scenarios
    #     Item.objects.bulk_create(
    #         [self.serialize_item(item) for item in records], batch_size=1000
    #     )

    # def save(self):
    #     """
    #     unset cache key if it exist
    #     save to cache and then save to db
    #     """
    #     pass
