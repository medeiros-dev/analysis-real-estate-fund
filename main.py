import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# fundos = ['ONEF11.SA', 'VLOL11.SA', 'BRCR11.SA', 'HGRE11.SA', 'JSRE11.SA']
# fundos2 = ['ONEF11.SA', 'VLOL11.SA', 'BRCR11.SA', 'HGRE11.SA', 'JSRE11.SA', 'PVBI11.SA', 'HGLG11.SA', 'SDIL11.SA', 'VILG11.SA', 'XPLG11.SA', 'XPIN11.SA',
#            'HGBS11.SA', 'HSML11.SA', 'HGCR11.SA', 'CPTS11.SA', 'IRDM11.SA', 'KNCR11.SA', 'KNIP11.SA', 'RBRR11.SA', 'XPCI11.SA', 'HGRU11.SA', 'KNRI11.SA']


msft = yf.Ticker('msft')
df = msft.get_info()

for key, value in df.items():
    print(key, ":", value)
