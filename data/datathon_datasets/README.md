# Datathon datasets

> ~3h of coding on one data set
> You can choose your own, but you need to agree in your group


There are four datasets available, which are described in 
[dataframes_description.pdf](dataframes_description.pdf)

## Suggested Questions to start

1.	Get an overview of the individual variables in your dataset, 
    you could do this with some descriptive plots, like histograms or boxplots.
2.	Generate some summary statistics of the variables in your dataset, 
    e.g. mean, median, sd, max, min, sum etc.
3.	Do the variables in your dataset appear to be correlated in any way, 
    you could visually inspect this with scatterplots, 
    plotting one variable as the predictor (x) and another variable as the response (y).

## Use raw csv view

In order to load your data directly into pandas from the csv files in this order.

![Find raw file button for csv files](../../figures/github_raw_file_view.png)


```python
import pandas as pd
url = 'https://raw.githubusercontent.com/<missing>/data.csv'
df = pd.read_csv(url)
```

