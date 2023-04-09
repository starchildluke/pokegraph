# Pokegraph

A command-line tool that draws basic Pokémon base stat graphs in the terminal, written in Python.

Graph types supported:

**Primary use**

- Bar Graphs

**Available from termgraph**

- Color charts
- Multi-variable
- Stacked charts
- Histograms
- Horizontal or Vertical
- Emoji!


### Examples

```
pokegraph data/pikachu.csv

# Reading data from data/pikachu.csv

hp             : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 35.00
attack         : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 55.00
defense        : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 40.00
special-attack : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 50.00
special-defense: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 50.00
speed          : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 90.00
```

Most results can be copied and pasted wherever you like, since they use standard block characters. However the color charts will not show, since they use terminal escape codes for color. A couple images to show color examples:

```
pokegraph data/pikachu.csv --color yellow
```

<img src="https://github.com/starchildluke/pokegraph/raw/main/pikachu-yellow-base-stats.jpg" alt="Bar chart in yellow" />

### Install

Requires Python 3.7+, install from [PyPI project](https://pypi.org/project/pokegraph/)

```
python3 -m pip install pokegraph
```

Note: Be sure your PATH includes the pypi install directory, for me it is `~/.local/bin/`

### Usage

* Create data file with two columns either comma or space separated.
  The first column is your labels, the second column is a numeric data

* pokegraph [datafile]

* Help: pokegraph -h

```
usage: pokegraph.py [-h] [(optional arguments)] [filename]

draw basic graphs on terminal

positional arguments:
  filename              data file name (comma or space separated). Defaults to stdin.

optional arguments:
  -h, --help            show this help message and exit
  --title TITLE         Title of graph
  --width WIDTH         width of graph in characters default:50
  --format FORMAT       format specifier to use.
  --suffix SUFFIX       string to add as a suffix to all data points.
  --no-labels           Do not print the label column
  --no-values           Do not print the values at end
  --space-between       Print a new line after every field
  --color [COLOR ...]   Graph bar color( s )
  --vertical            Vertical graph
  --stacked             Stacked bar graph
  --histogram           Histogram
  --bins BINS           Bins of Histogram
  --different-scale     Categories have different scales.
  --calendar            Calendar Heatmap chart
  --start-dt START_DT   Start date for Calendar chart
  --custom-tick CUSTOM_TICK
                        Custom tick mark, emoji approved
  --delim DELIM         Custom delimiter, default , or space
  --verbose             Verbose output, helpful for debugging
  --label-before        Display the values before the bars
  --version             Display version and exit
```

### Background

I wanted a quick way to visualize Pokémon base stats instead of having to search in Google and going to Bulbapedia or checking an app. Since I'm always in Terminal anyway, I thought this was work well for my workflow. I then found termgraph which did exactly what I wanted and decided to customise it for my use case, so shout out to [mkaz](https://github.com/mkaz/termgraph/) for creating this awesome tool!

### Contribute

All contributions are welcome, for feature requests or bug reports, use [Github Issues](https://github.com/starchildluke/pokegraph/issues). Pull requests are welcome to help fix or add features.

**Code contributions**: This repository uses the [black code formatter](https://github.com/psf/black) to automatically format the code. A Github Action is setup to lint your code, to avoid failures it is recommended to [setup your editor to auto format on save](https://github.com/psf/black/blob/master/docs/editor_integration.md).

Thanks again to [mkaz](https://github.com/mkaz/)!

### License

MIT License, see [LICENSE.txt](LICENSE.txt)