# SpOccSum (Species Occurrence Summary)

An easy-to-use Python tool to summarize species occurrence data from material examined lists in taxonomic revisions.

## Installation

You will need to have a current Python 3 installation to use SpOccSum. We recommend the Anaconda Python distribution (https://www.anaconda.com/distribution/), which is available for Linux, Windows, and Mac OS X.

With Python installed, you can simply run:

```
pip install spoccsum
```

This will install both the Python library and the command line interface.

## Command line interface

```
$ spoccsum summary -i microphontes_dwc.csv

species                      specimens    collecting_events    earliest_collection    most_recent_collection
-------------------------  -----------  -------------------  ---------------------  ------------------------
Microphontes ericfisheri             1                    1                   2015                      2015
Microphontes gaiophanes             17                    1                   2017                      2017
Microphontes jasonlondti             4                    3                   1986                      1998
Microphontes kryphios                3                    2                   1990                      2002
Microphontes megoura                 9                    1                   1936                      1936
Microphontes safra                   5                    3                   1974                      2012
Microphontes sp.                     1                    1                   1999                      1999
Microphontes whittingtoni            3                    2                   1990                      2008

```

```
$ spoccsum seasonal -i microphontes_dwc.csv
```

## Python interface

## Next steps
