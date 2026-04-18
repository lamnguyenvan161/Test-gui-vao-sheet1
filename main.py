import os
import json
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

SHEET_ID = "1Y31SSWQ18svGk2cdTZzpVFR8kCk2yVPlGDFyVOFrAx4"
SHEET_NAME = "Sheet1"

def connect_sheet():
    raw = os.getenv("GOOGLE_CREDENTIALS")

    if not raw:
        raise Exception("❌ Không đọc được GOOGLE_CREDENTIALS")

    creds_dict = json.loads(raw)

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
