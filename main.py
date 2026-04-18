import os
import json
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

SHEET_ID = "DAN_ID_SHEET_CUA_BAN"
SHEET_NAME = "Sheet1"

def connect_sheet():
    raw = os.getenv("GOOGLE_CREDENTIALS")

    # ✅ nếu có secret
    if raw:
        creds_dict = json.loads(raw)

    # ✅ nếu KHÔNG có secret → dùng file local
    else:
        print("⚠️ Không có secret → dùng credentials.json")
        with open("credentials.json", "r") as f:
            creds_dict = json.load(f)

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    return client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)


def main():
    sheet = connect_sheet()
    sheet.update_acell("A1", "OK " + datetime.now().strftime("%H:%M:%S"))
    print("✅ DONE")


if __name__ == "__main__":
    main()
