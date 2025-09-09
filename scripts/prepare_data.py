#!/usr/bin/env python3
import sys
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "crop_yield.csv"

def read_csv(path: Path):
    try:
        return pd.read_csv(path)  # padrão
    except Exception:
        # tenta padrão BR (;) e vírgula decimal
        return pd.read_csv(path, sep=';', decimal=',', encoding='latin1', engine='python')

df = read_csv(DATA)
cols = list(df.columns)

# Mapeia inglês -> PT-BR, se necessário
english_to_pt = {
    'Crop': 'Cultura',
    'Precipitation (mm day-1)': 'Precipitação (mm dia 1)',
    'Specific Humidity at 2 Meters (g/kg)': 'Umidade específica a 2 metros (g/kg)',
    'Relative Humidity at 2 Meters (%)': 'Umidade relativa a 2 metros (%)',
    'Temperature at 2 Meters (C)': 'Temperatura a 2 metros (ºC)',
    'Yield': 'Rendimento',
}

if set(english_to_pt.keys()).issubset(set(cols)):
    df = df.rename(columns=english_to_pt)
    df.to_csv(DATA, index=False, encoding='utf-8')
    print("✅ CSV normalizado para PT-BR e salvo em:", DATA)

expected = {
    "Cultura",
    "Precipitação (mm dia 1)",
    "Umidade específica a 2 metros (g/kg)",
    "Umidade relativa a 2 metros (%)",
    "Temperatura a 2 metros (ºC)",
    "Rendimento",
}

missing = expected - set(df.columns)
if missing:
    print("❌ Colunas ausentes:", missing)
    print("Colunas atuais:", list(df.columns))
    sys.exit(1)

print("✅ OK: colunas esperadas presentes. Shape:", df.shape)
