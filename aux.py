import re
import unicodedata
import pandas as pd
from datetime import datetime

def fix_name(text):
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError):
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    text = re.sub(r'\W+', '_', text.lower())

    return str(text)

def fix_ts(ts):
    ts = pd.to_datetime(ts, format="%d/%m/%Y %H:%M:%S")

    return ts

def fix_dt(dt):
    dt = pd.to_datetime(dt, format="%d/%m/%Y")

    return dt

def fix_tm(tm):
    if pd.isnull(tm) or tm == '':
        return tm
    else:
        return datetime.strptime(tm, '%H:%M').time()
