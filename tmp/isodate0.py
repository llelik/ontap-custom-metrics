#import isodate
from datetime import datetime, timedelta
t = datetime.strptime("PT3M2S", "PT%HH%MM%SS")
td = timedelta(minutes=t.minute,seconds=t.second)
td.total_seconds()
print(td)
