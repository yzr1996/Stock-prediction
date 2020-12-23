# authors: Eric(Zhenrui) Yu, Guanshu Tao, William Xu
# date: 2020-12-22

"""Downloads data from the web to a local filepath as a csv using pandas datareader.
Usage: download_data.py --ticker=<ticker> --data=<data>  --start=<start> --end=<end> --out_file=<out_file> 
 
Options:
--ticker=<ticker>         Ticker symbol of the stock of which to download data
--data=<data>             Datasource
--start=<start>           Start date of the analysis (yyyy-mm-dd)
--end=<end>               End date of the analysis (yyyy-mm-dd)
--out_file=<out_file>     Path (including filename) of where to locally write the file
"""

import os
import pandas_datareader as web
from docopt import docopt

opt = docopt(__doc__)

def main(ticker, data, start, end, out_file):
    df = web.DataReader(ticker, data_source=data, start=start, end=end)
    try:
        df.to_csv(out_file, index=False)
    except:
        os.makedirs(os.path.dirname(out_file))
        df.to_csv(out_file, index=False)

if __name__ == "__main__":
    main(opt["--ticker"], opt["--data"], opt["--start"], opt["--end"], opt["--out_file"])
