# Advent Of Code 2024
This is my repository for the annual [**Advent of Code**](https://adventofcode.com/).
</br>

# Notes on each day's challenge
## [Day 1: Historian Hysteria](https://adventofcode.com/2024/day/1)
The problem considered simple operations on lists.

First part required to find the absolute difference between items at the 
same index in two sorted lists.
Second part of the problem required determining how many times each item 
from first list occurs in the second one and multiplying item by that value.

```
Part 1:
3   4             1   3              2
4   3             2   3              1
2   5 -- sort --> 3   3 -- abs() --> 0
1   3             3   4              1
3   9             3   5              2
3   3             4   9              5
                                   +---
                                    11
Total = 11

Part 2:
3   4             1   0              0
4   3             2   0              0
2   5 -- sort --> 3   3 -- mul() --> 9
1   3             3   3              9
3   9             3   3              9
3   3             4   1              4
                                   +---
                                    31
                                    
Total = 31                                    
```