import sys
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic


def main(file_path):
    # Load the CSV file into a DataFrame
    header_present = pd.read_csv(file_path, nrows=1).columns[0] == 'day'
    if header_present:
        df = pd.read_csv(file_path)
    else:
        df = pd.read_csv(file_path, header=None,
                         names=['day', 'Susceptible', 'InfectiousX', 'InfectiousY', 'InfectiousXY', 'StayAtHomeX',
                                'StayAtHomeY', 'StayAtHomeXY', 'StayInHospitalX', 'StayInHospitalY', 'StayInHospitalXY',
                                'StayInICUX', 'StayInICUY', 'StayInICUXY', 'RecoveredX', 'RecoveredY', 'RecoveredXY',
                                'DeadX', 'DeadY', 'DeadXY'])
    # df = pd.read_csv(file_path)

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

    # Plot the mosaic plot
    plt.figure(figsize=(10, 6))
    mosaic(data, gap=0.01, title='Recovered/Dead by Disease',
           axes_label=True,
           labelizer=lambda k: '')
    plt.show()


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python mosaic.py <file_path>")
    else:
        # Get the file path from the command line
        file_path_arg = sys.argv[1]
        main(file_path_arg)
