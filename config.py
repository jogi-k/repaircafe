import datetime

REPAIRCAFE_DATE_ISO="2026-10-17"

my_date = datetime.date.fromisoformat(REPAIRCAFE_DATE_ISO)
REPAIRCAFE_DATE_HUMAN=my_date.strftime("%d. %b %Y")
REPAIRCAFE_DATE_GERMAN=my_date.strftime("%d.%m.%Y")
REPAIRCAFE_DATE_YEAR=my_date.strftime("%Y") 


