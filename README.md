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
2   5 -- calc --> 3   3 -- mul() --> 9
1   3             3   3              9
3   9             3   3              9
3   3             4   1              4
                                   +---
                                    31
                                    
Total = 31                                    
```

## [Day 2: Red-Nosed Reports](https://adventofcode.com/2024/day/2)
Problem consisted of comparing values inside each list.

First part of the exercises required checking whether the list is in order (either ascending or descending)
and each item in the list differs by at least 1 and at most 3 from the adjacent one.   
Part two introduced possibility of removing one value from the list in hopes it makes it valid.

```
Part 1:
7 6 4 2 1 --> valid     --> each value decreases by 1 or 2
1 2 7 8 9 --> not valid --> there's increase of 5 between 2 and 7
9 7 6 3 4 --> not valid --> values are not in order

Part 2:
7 6 4 2 1 --> valid     --> valid from start
1 2 7 8 9 --> not valid --> no matter which value is removed list is never valid
9 7 6 3 4 --> valid     --> valid if 4 is removed
```

## [Day 3: Mull It Over](https://adventofcode.com/2024/day/3)
Challenge required extracting values based on regex.

First part of the challenge consisted of extracting parts that had a 
form of `mul(X,Y)` where _X_ and _Y_ are 1-3 digit numbers. Then _X_ and _Y_ in each
part had to be multiplied and added together to produce result.

Second part was similar, but strings `do()` and `don't()` determined whether 
parts following it should be ignored

```
Part 1:
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
 ¯¯¯¯¯¯¯¯                   ¯¯¯¯¯¯¯¯            ¯¯¯¯¯¯¯¯¯       ¯¯¯¯¯¯¯¯
Extarcted values: mul(2,4), mul(5,5), mul(11,8), mul(8,5)
Result: 2*4 + 5*5 + 11*8 + 8*5 = 161
 
Part 2:
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
 ¯¯¯¯¯¯¯¯           ¯¯¯¯¯¯¯                                ¯¯¯¯ ¯¯¯¯¯¯¯¯
Extarcted values: mul(2,4), mul(8,5)
Result: 2*4 + 8*5 = 48
```

## [Day 4: Ceres Search](https://adventofcode.com/2024/day/4)
Task consisted of searching elements in a grid 

First part of the task was a crossword puzzle. The only word to find was the phrase `XMAS`.
The goal was to find the number of all instances of that word, knowing that it can be written
both normally or backwards in horizontal, vertical or diagonal directions.
  
Second part was _conceptually_ the same, however it required find a different _'phrase'_. 
Goal was to find two words `MAS` in a shape of `X`

```
Part 1 - possible phrases (8 in total): 
S..S..S
.A.A.A.
..MMM..
SAMXAS.
..MMM..
.A.A.A.
S..S..S

Part 2 - possible phrases (4 in total):
M.S...S.M...M.M...S.S
.A.....A.....A.....A.
M.S...S.M...S.S...M.M

```
