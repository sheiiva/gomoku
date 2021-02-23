Gomoku
===

Time:       4 weeks

Team:       3

Language:   python3


The project
----
The goal of this project is to implement a [*Gomoku Narabe*](https://en.wikipedia.org/wiki/Gomoku) game bot (also called *Wuzi Qi*, *Slope*, *Darpion or Five in a Row*), focusing on the performance of its artificial intelligence.

The goal is to create a boat communicating with the [`Piskvork`](https://sourceforge.net/projects/piskvork/) app.
Your bot must be compliant with the [communication protocol](https://svn.code.sf.net/p/piskvork/code/trunk/source/doc/protocl2en.htm), but only the mandatory part.

There are some technical constraints you must comply with:
* Whatever development language you choose, your program **must compile bothon Windows and on Linux**
* Only standard libraries are allowed. *No tensorflow or scikit-learn.*

# Rules
This is a 2-player game that is played on a **19x19 game board** (called *goban*). Contrary to full rules, we use a very simplified version here. Every player plays a stone at their turn, and the game ends as soon as one has a 5 stones in a row (vertically, horizontally or diagonaly) - and thus wins.

## USAGE:

### Prerequisites
* python3
* pip
* make *(Linux only)*


### Linux:

```
make
./pbrain-gomoku-ai
```
> Manual usage only


### Windows:

```
py -m compile.py
```

You'll then be able to give the path of the `.exe` file to `Piskvork`.


___________
Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva), [**Maxence DESROUSSEAUX**](https://github.com/handsomax), [**Hugo LACKAR**](https://github.com/HugoTkBCN/)