import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n_records = 100
start_date = datetime(2024, 1, 1)
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']
prices = {'Laptop': 800, 'Mouse': 25, 'Keyboard': 75, 'Monitor': 300, 'Headphones': 150}

# Generate data
dates = [start_date + timedelta(days=int(x)) for x in np.random.randint(0, 365, n_records)]
product_list = np.random.choice(products, n_records)
quantities = np.random.randint(1, 10, n_records)
price_list = [prices[p] for p in product_list]

# Create DataFrame
df = pd.DataFrame({
    'fecha': dates,
    'producto': product_list,
    'cantidad': quantities,
    'precio': price_list
})

# Sort by date
df = df.sort_values('fecha').reset_index(drop=True)

# Save to CSV
df.to_csv('ventas_sinteticas.csv', index=False)

print(df)


