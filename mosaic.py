import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

# Load the CSV file into a DataFrame
file_path = 'ResultXY.csv'
df = pd.read_csv(file_path)

# Extract the data for the last day (day 365)
final_day_data = df.iloc[-1, 1:]

final_day_data[['RecoveredX', 'RecoveredY', 'RecoveredXY', 'DeadX', 'DeadY', 'DeadXY']].values.flatten()

data = {
    ('X', 'Recovered'): final_day_data['RecoveredX'],
    ('Y', 'Recovered'): final_day_data['RecoveredY'],
    ('XY', 'Recovered'): final_day_data['RecoveredXY'],
    ('X', 'Dead'): final_day_data['DeadX'],
    ('Y', 'Dead'): final_day_data['DeadY'],
    ('XY', 'Dead'): final_day_data['DeadXY']
}
mosaic_data = pd.DataFrame({
    'Disease': ['X', 'Y', 'XY'] * 2,
    'Outcome': ['Recovered', 'Dead'] * 3,
    'Count': final_day_data[['RecoveredX', 'RecoveredY', 'RecoveredXY', 'DeadX', 'DeadY', 'DeadXY']].values.flatten()
})

# Plot the mosaic plot
plt.figure(figsize=(10, 6))
mosaic(data, gap=0.01, title='Recovered/Dead by Disease',
       axes_label=True,
       labelizer=lambda k: '')
plt.show()
