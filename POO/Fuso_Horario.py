import pytz
from datetime import datetime


data = datetime.now(pytz.timezone('Europe/Oslo'))

print(data)