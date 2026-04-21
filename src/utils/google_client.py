import gspread
import os
from dotenv import load_dotenv

load_dotenv()

def google_client():
    """
    Connects to Google Sheets and returns the spreadsheet object.
    """
    gc = gspread.service_account(filename=('../credentials.json'))
    spreadsheet_id = os.getenv('SPREADSHEET_ID')
    sh = gc.open_by_key(spreadsheet_id)

    return sh