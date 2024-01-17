import sys
import pandas as pd
import matplotlib.pyplot as plt


def main(file_path):
    header_present = pd.read_csv(file_path, nrows=1).columns[0] == 'day'
    if header_present:
        df = pd.read_csv(file_path)
    else:
        df = pd.read_csv(file_path, header=None,
                         names=['day', 'Susceptible', 'InfectiousX', 'InfectiousY', 'InfectiousXY', 'StayAtHomeX',
                                'StayAtHomeY', 'StayAtHomeXY', 'StayInHospitalX', 'StayInHospitalY', 'StayInHospitalXY',
                                'StayInICUX', 'StayInICUY', 'StayInICUXY', 'RecoveredX', 'RecoveredY', 'RecoveredXY',
                                'DeadX', 'DeadY', 'DeadXY'])

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
                     ylabel='Population', grid=True, ax=ax1,
                     color=[color_mapping[col] for col in df_plot_sir.columns[1:]])

    # Plot the Hospital data
    df_plot_hospital.plot(x='day', kind='area', stacked=True,
                          title='Hospitalized Cases', xlabel='Day',
                          ylabel='Population', grid=True, ax=ax2,
                          color=[color_mapping[col] for col in df_plot_hospital.columns[1:]])

    df_plot_icu.plot(x='day', kind='area', stacked=True,
                     title='ICU Cases', xlabel='Day',
                     ylabel='Population', grid=True, ax=ax3,
                     color=[color_mapping[col] for col in df_plot_icu.columns[1:]])

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python plot.py <file_path>")
    else:
        # Get the file path from the command line
        file_path_arg = sys.argv[1]
        main(file_path_arg)
