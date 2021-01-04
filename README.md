
# S&P500 Index Predictor

-   authors: Eric(Zhenrui) Yu, Guanshu Tao, William Xu

A data science collaboration project during the 2020 winter break.

## Introduction

Stock price prediction has always been a hot topic because it is highly
related to capital markets and some changes of state systems are
associated with capitals especially in capitalism counties. While it is
very difficult to predict the stock market because there are so many
factors relating to the price and for some factors we are unaware of
their values, such as irrational behaviours and psychological factors of
humans on the stock prices. How well can machine learning algorithms do
with predicting stock prices? Are machine learning techniques useful on
these problems? In this project, we would like to start with L1 and L2
regularization with linear regression and then move to LSTM from
recurrent neural network and auto arima in time series forecasting to
approach stock price prediction. We chose S&P500 to be our example and
we would like to explore whether the historical price plays an important
role in future prices. This question will be focused on by the project:
given the price history of S&P500 index, what is the price of S&P500
index today?

Our dataset is from Yahoo Finance and was sourced from Pandas
Datareader(“Pandas-Datareader 0.6.0 Documentation” 2020). The timeline
of the analysis is set from January 1, 2012 to December 17, 2020. Each
row in the data set represents the daily performance of the S&P500, and
each column represents an attribute of S&P500 (e.g., date, daily high,
daily low, opening price, close price, volume, adjusted close price).

To answer the predictive question posed above, we plan to build a
recurrent neural networks model called Long Short-Term Memory (LSTM).
Recurrent neural networks are more effective for sequence data, which
can be suitable for our time series analysis. Before building the model,
we will partition the data into a training and test data set (split
80%:20%) and perform some exploratory data analysis. We will use a
minimum and maximum scaler to scale the price index in the dataset
between 0 and 1. In the training data set, we will use the past 60-day
(approximately 2 months) index price as a window size to train the
model. When compiling the model, we will use Adam optimizer with default
learning rate and select mean squared error loss as our criterion. Then
we will use the Long Short-Term Memory (LSTM) model to predict on our
validation set, plot data with comparison on prediction data and
validation data, and report validation data and predicted prices in a
table. In our prediction analysis we will look at root mean squared
error to assess prediction performance.

After validating the model, we plan to use the Long Short-Term Memory
(LSTM) model to predict the stock index one day beyond the dataset range
as a starting point. In the future, we plan to use the Long Short-Term
Memory (LSTM) model to predict a longer time horizon.

Thus far we have performed some data analysis, and the report for that
can be found [here](src/analysis.ipynb).

## Usage

To replicate the analysis, clone this GitHub repository, install the
[dependencies](#dependencies) listed below, and run the following
commands at the command line/terminal from the root directory of this
project:

    python src/download_data.py --ticker=^GSPC --data=yahoo --start=2012-01-01 --end=2020-12-17 --out_file=data/raw/SP500_data.csv

## Dependencies

-   Python 3.8.6 and Python packages:
    -   docopt==0.6.2
    -   Keras==2.4.3
    -   matplotlib==3.3.3
    -   mplcyberpunk==0.1.11
    -   numpy==1.19.4
    -   pandas==0.24.2
    -   pandas-datareader==0.9.0
    -   scikit-learn==0.23.2
-   R version 4.0.2 and R packages:
    -   knitr==1.30
    -   rmarkdown==1.25
    -   reticulate==1.18
    -   tidyverse==1.3.0

## License

The Stock Price Predictor materials here are licensed under the Creative
Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If
re-using/re-mixing please provide attribution and link to this webpage.

# References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-pandas-datareader" class="csl-entry">

“Pandas-Datareader 0.6.0 Documentation.” 2020.
<https://pandas-datareader.readthedocs.io/en/latest/>.

</div>

</div>
