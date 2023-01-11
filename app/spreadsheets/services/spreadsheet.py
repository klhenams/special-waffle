import gspread
from django.conf import settings
from django.core.cache import cache
from django.utils.html import strip_tags

from app.spreadsheets.models import Item

conf = getattr(settings, "GOOGLE_API", {})


class Spreadsheet:
    gc = None
    chuck = conf.get("GOOGLESHEET_CHUNK")
    lower_boundary = conf.get("GOOGLESHEET_LOW_BOUNDARY")
    data = []

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

    def get_list(self):

        try:
            sh = self.gc.open_by_key(conf.get("GOOGLESHEET_KEY", None))
            worksheet = sh.get_worksheet(0)
        except gspread.exceptions.SpreadsheetNotFound as err:  # noqa F841
            pass
        except gspread.exceptions.WorksheetNotFound as err:  # noqa F841
            pass
        else:
            return self.read_sheet_chunks(worksheet)

    def serialize_item(self, item) -> Item:
        # Clean description
        # TODO: Clean other data cols
        item[2] = strip_tags(item[2])
        return Item(*item)

    def serialze_data(self, records):
        return [self.serialize_item(item) for item in records]

    def read_sheet_chunks(self, worksheet):
        while 1 > 0:
            try:
                upper_boundary = self.lower_boundary + self.chuck
                results = worksheet.get_values(
                    f"A{self.lower_boundary}:C{upper_boundary}"
                )
                self.lower_boundary = upper_boundary + 1
                self.data += self.serialze_data(results)
                self.save_to_cache(self.data)
            except gspread.exceptions.APIError as err:
                if "exceeds grid limits" in str(err):
                    break
                else:
                    pass
            except Exception as err:
                print("Fetching/serializing error: ", err, type(err))
                return []
        return self.data

    def save_to_cache(self, records):
        cache.set("items", records, timeout=settings.CACHE_TTL)
