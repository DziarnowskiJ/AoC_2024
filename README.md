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

## [Day 5: Print Queue](https://adventofcode.com/2024/day/5)
Analysis and custom sort for list

Input for the challenge was split into two parts:
- List of order rules in form of `X|Y` determining that if both
_X_ and _Y_ appear in the list, _X_ has to be before _Y_
- Lines to perform operations on - `X,Y,Z` 

First part of the exercise required to analyse each line and determine
whether they are following the proper order and follow all rules.
Second part required to fix the lines that were in incorrect order.

```
Order rules:
47|53       
97|75       
97|61       

Part 1:
Lines:               Relevant rules        Result
97,61,53,29,13   ->  97|61              -> Correct
97,61,75         ->  97|75 97|61        -> Correct
75,97,47,61,53   ->  47|53 97|75 97|61  -> Incorrect - 75 should be after 97
61,13,29         ->  None               -> Correct

Part 2:
Incorrect lines:     Relevant rules        Fixed line
75,97,47,61,53   ->  47|53 97|75 97|61  -> 97,75,47,61,5 

```

## [Day 6: Guard Gallivant](https://adventofcode.com/2024/day/6)
Path finding and loops in a grid

First part of the exercise consisted of traveling in straight lines through the grid, starting at position `^`. 
The goal was to find the number of distinct places visited before moving out of the bounds of the grid.
At every collision with `#`, the direction of movement was rotated to the right.

Second part required to find all possible spots to place a single obstacle 
that would cause path to loop indefinitely.

```
Part 1:
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.    -> 41 distinct places 
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#v..

Part 2:
....#.....      ....#.....      ....#.....
....+---+#      ....+---+#      ....+---+#
....|...|.      ....|...|.      ....|...|.
..#.|...|.      ..#.|...|.      ..#.|...|.
....|..#|.      ..+-+-+#|.      ..+-+-+#|.
....|...|.      ..|.|.|.|.      ..|.|.|.|.
.#.O^---+.      .#+-^-+-+.      .#+-^-+-+.
........#.      ......O.#.      .+----+O#.
#.........      #.........      #+----+...
......#...      ......#...      ......#...
                                                --> 6 possible spots
....#.....      ....#.....      ....#.....
....+---+#      ....+---+#      ....+---+#
....|...|.      ....|...|.      ....|...|.
..#.|...|.      ..#.|...|.      ..#.|...|.
..+-+-+#|.      ..+-+-+#|.      ..+-+-+#|.
..|.|.|.|.      ..|.|.|.|.      ..|.|.|.|.
.#+-^-+-+.      .#+-^-+-+.      .#+-^-+-+.
..|...|.#.      ....|.|.#.      .+----++#.
#O+---+...      #..O+-+...      #+----++..
......#...      ......#...      ......#O..

```


## [Day 7: Bridge Repair](https://adventofcode.com/2024/day/7)
Regression with basic math expressions

First part presented the list of equations in form `T: X Y Z`, where _T_ was the target number
to be achieved by performing multiplication and addition on the remaining numbers. 
Operators had to be always evaluated left-to-right, not according to precedence rules.

Second part of the challenge introduced new operation - concatenation (`||`). This allowed
the numbers to be added together as a string instead of number.

```
Part 1:
190: 10 19      -> 190 = 10 * 19
3267: 81 40 27  -> 3267 = 81 * 40 + 27
83: 17 5        -> Not possible
156: 15 6       -> Not possible
7290: 6 8 6 15  -> Not possible
292: 11 6 16 20 -> 292 = 11 + 6 * 16 + 20

Part 2:
83: 17 5        -> Still not possible
156: 15 6       -> 156 = 15 || 6
7290: 6 8 6 15  -> 7290 = 6 * 8 || 6 * 15
```

## [Day 8: Resonant Collinearity](https://adventofcode.com/2024/day/8)
Finding vectors between spots in a grid

Challenge's input could be interpreted as a grid with multiple nodes marked with a letter or digit.
The first part required finding distinct locations of `antinodes`. Those are the spots that are formed in line
of two nodes of the same type but twice as far from each other than the original nodes. 

Second part changed the condition of forming antinodes - now a pair of nodes create as many antinodes
as possible, all located at `X` times the distance between original nodes `(-inf < X < inf and X is integer)` 

```
Part 1:
....                #...
.B..   antinodes    .B..
..B.  ----------->  ..B.
....                ...#

..........                ..........  
..........                ...#......  
..........   antinodes    #.........  
....a.....  ----------->  ....a.....  ---> 3 visible antinodes
........a.                ........a.       + 1 in place of A  
.....a....                .....a....       = 4 antinodes
..........                ..#.......  
......A...                ......A...  
..........                ..........  

Part 2:
T.........                T....#....
...T......                ...T......
.T........   antinodes    .T....#...
..........  ----------->  .........#  ---> 6 visible antinodes
..........                ..#.......       + 3 in place of each T
..........                ..........       = 9 antinodes
..........                ...#......
..........                ..........
..........                ....#.....
..........                ..........

```
