from datetime import datetime, timedelta

unix_ts = 1609462800
dt = (datetime.fromtimestamp(unix_ts)).strftime('%Y-%m-%d %H:%M:%S')
print(dt)