from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2), "OSL"))

print(data_oslo)