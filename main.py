import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


msft = yf.Ticker('msft')
df = msft.get_info()

for key, value in df.items():
    print(key, ":", value)


########################################################################
# Indicadores de Valuation
# EV (Valor da Empresa)/EBITDA
# P/L Estimado
# PEG Ratiq
########################################################################
# Indicares de Individamento
# Indice de Líquidez
# Débito total/Patrimônio Líquido
########################################################################
# Indicadores de Eficiência
# Margem de Lucro
# Margem Operacional
########################################################################
# #Indicadores de Rentabilidade
# ROA - Rentabilidade sobre ativo
# ROE - Rentabilidade sobre PL
# Fluxo de caixa livre alavancado
# Índice de payout
########################################################################
# #Indicadores Crescimento
# Aumento de receita trimestral(yoy)
# Aumento de ganhos trimestral (yoy)
