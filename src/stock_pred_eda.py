# authors: Eric(Zhenrui) Yu, Guanshu Tao, William Xu
# date: 2021-01-07

"""
Creates exploratory data visualizations and tables to be used in final report

Usage: stock_pred.py --in_file=<in_file> --output_file=<output_file> 

Options:
--in_file=<in_file>               File path and filename of the input cleaned csv file
--output_file=<output_file>       Path of where to locally write .png EDA figures
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from docopt import docopt
plt.style.use('fivethirtyeight')

opt = docopt(__doc__)

def main(in_file, output_file):
    df = pd.read_csv(in_file)
    
    # Plot the closing price hisroty of S&P 500 and save as .png file
    plt.figure(figsize=(16, 8))
    plt.title('S&P500 Close Price History')
    plt.plot(df['Close'])
    plt.xlabel('Data', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.savefig(output_file + 'price_hist.png')

if __name__ == "__main__":
    main(opt["--in_file"], opt["--output_file"])
