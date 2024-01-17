import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'ResultXY.csv'
df = pd.read_csv(file_path)

# Define color mapping for each category
color_mapping = {
    'InfectedX': 'darkblue',
    'RecoveredX': 'lightskyblue',
    'DeadX': 'royalblue',
    'InfectedY': 'darkred',
    'RecoveredY': 'lightcoral',
    'DeadY': 'firebrick',
    'InfectedXY': 'darkgreen',
    'RecoveredXY': 'lightgreen',
    'DeadXY': 'forestgreen',
    'HospitalX': 'blue',
    'HospitalY': 'red',
    'HospitalXY': 'green',
    'ICUX': 'dodgerblue',
    'ICUY': 'indianred',
    'ICUXY': 'mediumseagreen',
    'Susceptible': 'lightgray'
}

# Create a new DataFrame with the desired columns for SIR plot
df_plot_sir = pd.DataFrame({
    'day': df['day'],
    'Susceptible': df['Susceptible'],
    'InfectedX': df['StayAtHomeX'] + df['StayInHospitalX'] + df['StayInICUX'] + df['InfectiousX'],
    'InfectedY': df['StayAtHomeY'] + df['StayInHospitalY'] + df['StayInICUY'] + df['InfectiousY'],
    'InfectedXY': df['StayAtHomeXY'] + df['StayInHospitalXY'] + df['StayInICUXY'] + df['InfectiousXY'],
    'RecoveredX': df['RecoveredX'],
    'RecoveredY': df['RecoveredY'],
    'RecoveredXY': df['RecoveredXY'],
    'DeadX': df['DeadX'],
    'DeadY': df['DeadY'],
    'DeadXY': df['DeadXY']
})

# Create a new DataFrame with the desired columns for Hospital plot
df_plot_hospital = pd.DataFrame({
    'day': df['day'],
    'HospitalX': df['StayInHospitalX'],
    'HospitalY': df['StayInHospitalY'],
    'HospitalXY': df['StayInHospitalXY']
})

df_plot_icu = pd.DataFrame({
    'day': df['day'],
    'ICUX': df['StayInICUX'],
    'ICUY': df['StayInICUY'],
    'ICUXY': df['StayInICUXY']
})

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 9))

# Plot the SIR data
df_plot_sir.plot(x='day', kind='area', stacked=True,
                 title='Spread of Disease X and Y', xlabel='Day',
                 ylabel='Population', grid=True, ax=ax1, color=[color_mapping[col] for col in df_plot_sir.columns[1:]])

# Plot the Hospital data
df_plot_hospital.plot(x='day', kind='area', stacked=True,
                      title='Hospitalized Cases', xlabel='Day',
                      ylabel='Population', grid=True, ax=ax2, color=[color_mapping[col] for col in df_plot_hospital.columns[1:]])

df_plot_icu.plot(x='day', kind='area', stacked=True,
                 title='ICU Cases', xlabel='Day',
                 ylabel='Population', grid=True, ax=ax3, color=[color_mapping[col] for col in df_plot_icu.columns[1:]])

plt.tight_layout()
plt.show()
