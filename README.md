# Covid-19-analysis


## Members:

* Pablo López Martín
* Juan Tecedor Roa
* Elena Fernandez Jiménez

## Introduction
This project combines big data techniques and cloud computing to analyze covid-19 cases data in Spain in short period of time.

Unlike other sites, this is not another covid portal that shows the number of cases. We focused in cleaning up data, grouping
it by CCAA (autonomous communities) and add up the numbers. After the processing is done we analyze the data and try to find correlations and show the results as a graph.

These correlations do not imply causation.

[Main Site -- WEBPAGE](https://plopezq.github.io/Covid-19-analysis/index.html)

## How to run this program
First of all install all of the required software: python, spark, java, scala, numpy, matplotlib and pandas.

Python 2.7.18
Spark version 2.2.0
Python 3.x

For more details see: [How to use](https://plopezq.github.io/Covid-19-analysis/howtouse.html)

To run:

```
cd into /Application/src/
```

```
run run.sh
```
Now, the dataSets are ready. We only have to run the application

* if we have to display a chart of number of cases per community compared with population density:

```
$ python3 results.py 0
```
* If you want to display a chart of number of cases per community compared with population:

```
$ python3 results.py 1
```
* If you want to display a chart of cases by age range:

```
$ python3 results.py 2
```
* If you want to display a chart of Cases by community (men vs women):

```
$ python3 results.py 3
```

## Results
In the WebPage we have upload some images with the output of the programm

[Click Here](https://plopezq.github.io/Covid-19-analysis/results.html)
