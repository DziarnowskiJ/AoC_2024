# Advent Of Code 2024
This is my repository for the annual [**Advent of Code**](https://adventofcode.com/).
</br>

# Notes on each day's challenge
## [Day 1: Historian Hysteria](https://adventofcode.com/2024/day/1)
Simple operations on lists

First part required to find the absolute difference between items at the 
same index in two sorted lists.
Second part of the problem required determining how many times each item 
from first list occurs in the second one and multiplying item by that value.

```
Part 1:
3   4         1   3            2
4   3  sort   2   3   abs()    1
2   5 ------> 3   3 -------->  0
1   3         3   4            1
3   9         3   5            2
3   3         4   9            5
                             +---
                              11
Total = 11

Part 2:
3   4         1   0           0
4   3  calc   2   0   mul()   0
2   5 ------> 3   3 --------> 9
1   3         3   3           9
3   9         3   3           9
3   3         4   1           4
                            +---
                             31
                                    
Total = 31                                    
```

## [Day 2: Red-Nosed Reports](https://adventofcode.com/2024/day/2)
Comparing values inside each list

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
Extracting values based on regex

First part of the challenge consisted of extracting parts that had a 
form of `mul(X,Y)` where _X_ and _Y_ are 1-3 digit numbers. Then _X_ and _Y_ in each
part had to be multiplied and added together to produce result.

Second part was similar, but strings `do()` and `don't()` determined whether 
parts following it should be ignored.

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
Searching elements in a grid 

First part of the task was a crossword puzzle. The only word to find was the phrase `XMAS`.
The goal was to find the number of all instances of that word, knowing that it can be written
both normally or backwards in horizontal, vertical or diagonal directions.
  
Second part was _conceptually_ the same, however it required find a different _'phrase'_. 
Goal was to find two words `MAS` in a shape of `X`.

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
as possible, all located at `X` times the distance between original nodes `(-inf < X < inf and X is integer)`. 

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

## [Day 9: Disk Fragmenter](https://adventofcode.com/2024/day/9)
Advanced list manipulation and reordering

Challenges input was a single line of digits representing files and free space on the disk. 
The digits alternate between indicating the length of a file and the length of free space.
Each file on disk has an ID number based on the order of the files as they appear before they are rearranged.
Part one required to unpack the disk and move files one at a time from the end of the disk to the leftmost free space block.
Second part, instead of moving one file part required moving the whole file block. 

```
Part 1:
Input: 12345

Unpacking and sorting:
0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......

Part 2:
Input: 2333133121414131402

Unpacking and sorting:
00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
```

## [Day 10: Hoof It](https://adventofcode.com/2024/day/10)
Simple path finding in a grid

Input for the puzzle was a topographical map with numbers 0-9 determining the height of the point.
The only possible move on that map is in 4 cardinal directions onto the point that is one higher than the current position.
The goal of the first part was to find number of reachable points with height `9` starting at each point with height `0`.
Second part asked about number of distinct paths to that point instead.

```
Part 1:
0..0...                     0......   ...0...   .......  
...1210    reachable 9s     .......   .......   ......0  
...2345     for each 0      .......   .......   .......   
6543456  ---------------->  .......   .......   .......  
7..4..7                     .......   .......   .......  
8..5..8                     .......   .......   .......  
9876..9                     .......   9.....9   9.....9  

Part 2:
.....0.                     .....0.   .....0.   .....0.
..4321.   distinct paths    ..4321.   .....1.   .....1.
..5..2.  ---------------->  ..5....   .....2.   .....2.
..6543.                     ..6....   ..6543.   .....3.
..7..4.                     ..7....   ..7....   .....4.
..8765.                     ..8....   ..8....   ..8765.
..9....                     ..9....   ..9....   ..9....
```

## [Day 11: Plutonian Pebbles](https://adventofcode.com/2024/day/11)
Dealing with quickly expanding lists

The puzzle presented a line of numbers and rules for a special `blink` operation. 
`Blink` is a function modifying a number that can preform 3 different operations based on the value of the number:
1) `0 -> 1` &emsp;&emsp;&emsp;&emsp;- If number is _0_ return _1_
2) `XY -> X, Y` &emsp;&emsp;- Else if length of the number is even, split that number into two parts
3) `Z -> 2024 * Z` &ensp;- Else multiply the number by _2024_

Both parts of the challenge asked for the amount of numbers after _X_ blinks. 
For first part it was _25_, for the second - _75_.

```
Initial arrangement:
125 17

After 1 blink:      --> 3 numbers
253000 1 7

After 2 blinks:     --> 4 numbers
253 0 2024 14168

After 3 blinks:     --> 5 numbers
512072 1 20 24 28676032

After 4 blinks:     --> 9 numbers
512 72 2024 2 0 2 4 2867 6032

After 5 blinks:     --> 13 numbers
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

After 6 blinks:     --> 22 numbers
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2

...

After 25 blinks:     --> 55312 numbers
...
After 75 blinks:     --> 65601038650482 numbers
```

## [Day 12: Garden Groups](https://adventofcode.com/2024/day/12)
Splitting grid into regions and determining number of sides of a shape

Another challenge with grid as an input. This time the goal was to split
it into the smaller areas that contain the same character. 
Part one required to get the size of the area (number of characters in a region) and its perimeter.
Part two instead of the perimeter asked for a number of sides.

```
           
                                            ┌─┬─┬─┬─┐      size 4    ┌─┐      size 1                
                                            │A A A A│  --> per. 10   │D│  --> per. 4  
                    ┌───────┐               └─┴─┴─┴─┘      sides 4   └─┘      sides 4        
                    │A A A A│                                                                         
AAAA                ├───┬─┬─┤               ┌─┬─┐                      ┌─┐                  
BBCD    regions     │B B│C│D│    values     │B B│      size 4          │C│        size 4 
BBCC   --------->   │   │ └─┤   -------->   ├   ┤  --> per. 8          ├ ┼─┐  --> per. 10        
EEEC                │B B│C C│               │B B│      sides 4         │C C│      sides 8                    
                    ├───┴─┐ │               └─┴─┘                      └─┼ ┤                    
                    │E E E│C│                                            │C│                    
                    └─────┴─┘               ┌─┬─┬─┐      size 3          └─┘                    
                                            │E E E│  --> per. 6                               
                                            └─┴─┴─┘      sides 4                                     
```

## [Day 13: Claw Contraption](https://adventofcode.com/2024/day/13)
Linear algebra and system of equations

Challenge described the set of configurations for claw machines 
and their unusual controls. Instead of joysticks, these machines operate 
using buttons A and B, each causing the claw to move a specific distance 
along the X and Y axes. To win a prize, the claw must be perfectly 
aligned above it in both axes. This means that the input was basically 
a set of systems of equations requiring to solve for A and B.


The solution for both parts involved finding the sum of results of `3A + B`
for each winning machine. Some machines were not able to generate the prize
as the number of button presses to align the claw wasn't an integer number
 
Part two differed only slightly to part one - `10000000000000` was added
to both coordinates of the prize.

```
Part 1:
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400       --> A = 80, B = 40

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176     --> Not achievable for {A, B ∈ Z} 

Part 2:
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=10000000008400, Y=10000000005400   --> Not achievable for {A, B ∈ Z}

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=10000000012748, Y=10000000012176   --> A = 118679050709, B = 103199174542
```

## [Day 14: Restroom Redoubt](https://adventofcode.com/2024/day/14)
Moving points around the grid and grid-image analysis

Exercise presented a list of coordinates and vectors in which to move at each step.
If the step lands outside the grid's boundaries, the point it moved to the other side 
of the gird and continues the movement. 

The first part required to perform _100_ steps from each starting point and determine
number of points that end in each quadrant.  
Second part stated that after some number of steps, the majority of points will create
an image of a Christmas tree - the goal was to find after how many steps that happens.

```
Example:
p=1,2 v=1,-2

.....           .....           .....            .....            .#...
.....   step    .....   step    ...#.    step    .....    step    .....
.#...  ------>  .....  ------>  .....   ------>  .....   ------>  .....
.....           .....           .....            ....#            .....
.....           ..#..           .....            .....            .....


Part 1:
                                                         ┌─────┬─────┐
1.12.......                  ......2..1.                 │.....│2..1.│
...........                  ...........                 │.....│.....│           ┌─┬─┐
...........    100 steps     1..........    quadrants    │1....│.....│   sums    │1│3│
......11.11   ----------->   .11........   ----------->  ├─────┼─────┤  ------>  ├─┼─┤              
1.1........                  .....1.....                 │.....│.....│           │4│1│
.........1.                  ...12......                 │...12│.....│           └─┴─┘
.......1...                  .1....1....                 │.1...│1....│
                                                         └─────┴─────┘
* Numbers on the grid represent 
  amount of points at that place
                                                        
Part 2:
Image to find:
▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
▪                             ▪
▪                             ▪
▪                             ▪
▪                             ▪
▪              ▪              ▪
▪             ▪▪▪             ▪
▪            ▪▪▪▪▪            ▪
▪           ▪▪▪▪▪▪▪           ▪
▪          ▪▪▪▪▪▪▪▪▪          ▪
▪            ▪▪▪▪▪            ▪
▪           ▪▪▪▪▪▪▪           ▪
▪          ▪▪▪▪▪▪▪▪▪          ▪
▪         ▪▪▪▪▪▪▪▪▪▪▪         ▪
▪        ▪▪▪▪▪▪▪▪▪▪▪▪▪        ▪
▪          ▪▪▪▪▪▪▪▪▪          ▪
▪         ▪▪▪▪▪▪▪▪▪▪▪         ▪
▪        ▪▪▪▪▪▪▪▪▪▪▪▪▪        ▪
▪       ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪       ▪
▪      ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪      ▪
▪        ▪▪▪▪▪▪▪▪▪▪▪▪▪        ▪
▪       ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪       ▪
▪      ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪      ▪
▪     ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪     ▪
▪    ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪    ▪
▪             ▪▪▪             ▪
▪             ▪▪▪             ▪
▪             ▪▪▪             ▪
▪                             ▪
▪                             ▪
▪                             ▪
▪                             ▪
▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
```

## [Day 15: Warehouse Woes](https://adventofcode.com/2024/day/15)
Advanced movement through grid

Input for the challenge consisted of two parts: text grid and lines of `v^<>` characters.
Grid was made out of 4 character types:
- _._ - empty space
- _O_ - movable point
- _#_ - immovable point
- _@_ - starting point

The first part of the challenge required to move around the grid in the directions specified 
by `v^<>` characters. When next step required moving into an immovable point nothing was happening 
and simply the next step was made. When colliding with _O_, it was possible to push
that point in the direction of movement (provided the _#_ wasn't obstructing the further way).
In case of multiple _Os_, all of them where pushed simultaneously.

Second part stretched the grid in horizontal direction. Each empty space and immovable object doubled, 
and _0_ became two combined points represented by _[ ]_. All other rules remained constant, with the
exception that the movable point can be pushed the same direction from two different places causing 
more points to move.

```
Part 1:
movements: <vv<<^^<<^^

#######              #######              #######              #######
#...#.#              #...#.#              #...#.#              #...#.#
#.....#    move <    #.....#    move v    #.....#    move v    #.....#
#..OO@#   ───────>   #.OO@.#   ───────>   #.OO..#   ───────>   #.OO..#
#..O..#              #..O..#              #..O@.#              #..O..#
#.....#              #.....#              #.....#              #...@.#
#######              #######              #######              #######
                                move <                             │
   ┌───────────────────────────────────────────────────────────────┘
   v
#######              #######              #######              #######
#...#.#              #...#.#              #...#.#              #...#.#
#.....#    move <    #.....#    move ^    #.....#    move ^    #.O...#
#.OO..#   ───────>   #.OO..#   ───────>   #.OO..#   ───────>   #.@O..#
#..O..#              #..O..#              #.@O..#              #..O..#
#..@..#              #.@...#              #.....#              #.....#
#######              #######              #######              #######
                                move <                             │
   ┌───────────────────────────────────────────────────────────────┘
   v
#######              #######              #######              #######
#...#.#              #...#.#              #...#.#              #@..#.#
#.O...#    move <    #.O...#    move ^    #@O...#    move ^    #.O...#
#@.O..#   ───────>   #@.O..#   ───────>   #..O..#   ───────>   #..O..#
#..O..#              #..O..#              #..O..#              #..O..#
#.....#              #.....#              #.....#              #.....#
#######              #######              #######              #######

Part 2:

   #######                ##############  │  ##############            ##############
   #...#.#                ##......##..##  │  ##......##..##            ##......##..##
   #.....#    stretch     ##..........##  │  ##....@.....##   move v   ##..........##
   #..OO@#   ─────────>   ##....[][]@.##  │  ##...[][]...##  ───────>  ##....@[]...##
   #..O..#                ##....[]....##  │  ##....[]....##            ##...[].....##
   #.....#                ##..........##  │  ##..........##            ##....[]....##
   #######                ##############  │  ##############            ##############
──────────────────────────────────────────┼──────────────────────────────────────────
##############            ##############  │  ##############            ##############  
##......##..##            ##......##..##  │  ##......##..##            ##......##..##  
##..........##   move <   ##..........##  │  ##..........##   move ^   ##...[][]...##  
##....[][]@.##  ───────>  ##...[][]@..##  │  ##...[][]...##  ───────>  ##....[]....##  
##....[]....##            ##....[]....##  │  ##....[]....##            ##.....@....##  
##..........##            ##..........##  │  ##.....@....##            ##..........##  
##############            ##############  │  ##############            ##############  
──────────────────────────────────────────┼──────────────────────────────────────────
##############            ##############  │  ##############            ##############
##......##..##            ##...[].##..##  │  ##......##..##            ##......##..##
##..........##            ##..........##  │  ##.....@....##            ##.....@....##
##..........##            ##..........##  │  ##..........##            ##..........##
##############            ##############  │  ##############            ##############

```

## [Day 16: Reindeer Maze](https://adventofcode.com/2024/day/16)
Shortest path search

The requirements of the first part of the challenge were simple - find the shortest path
between two points, each step adds _1_ to the path's length and each turn adds _1000_.

Second part required finding __all possible shortest paths__ and determining how many nodes
are visited when traversing any of them.

```
Maze:                           Part 1:                             Part 2:     
███████████████                 ███████████████                     ███████████████
█.......█....E█                 █.......█....E█                     █.......█....○█
█.█.███.█.███.█                 █.█.███.█.███^█                     █.█.███.█.███○█
█.....█.█...█.█                 █.....█.█...█^█                     █.....█.█...█○█
█.███.█████.█.█                 █.███.█████.█^█                     █.███.█████.█○█
█.█.█.......█.█    shortest     █.█.█.......█^█    all shortest     █.█.█.......█○█
█.█.█████.███.█      path       █.█.█████.███^█       paths         █.█.█████.███○█
█...........█.█   ---------->   █..>>>>>>>>v█^█   -------------->   █..○○○○○○○○○█○█
███.█.█████.█.█                 ███^█.█████v█^█                     ███○█○█████○█○█
█...█.....█.█.█                 █>>^█.....█v█^█                     █○○○█○....█○█○█
█.█.█.███.█.█.█                 █^█.█.███.█v█^█                     █○█○█○███.█○█○█
█.....█...█.█.█                 █^....█...█v█^█                     █○○○○○█...█○█○█
█.███.█.█.█.█.█                 █^███.█.█.█v█^█                     █○███.█.█.█○█○█
█S..█.....█...█                 █S..█.....█>>^█                     █○..█.....█○○○█
███████████████                 ███████████████                     ███████████████
```

## [Day 17: Chronospatial Computer](https://adventofcode.com/2024/day/17)
Basic Processing Language

Challenge's description defined 8 possible 
operations that could be performed on a set of 7 registers.
Four of the registers were constant, always returning values 0-3, the three remaining were variable registers _A_, _B_, _C_. 
A number called the instruction pointer identified the position in the program 
from which the next opcode would be read. Except for jump instructions, the instruction pointer increases by 2 after each instruction is processed 
(to move past the instruction's opcode and its operand). If the computer tries to read an opcode past the end of the program, it instead halts

There were two types of operands. The value of a literal operand was the operand itself. Second type of operand was combo, 
value of it could be found by following these rules:
- Combo operands __0 through 3__ represent literal __values 0 through 3__.
- Combo operand __4__ represents the value of __register A.
- Combo operand __5__ represents the value of __register B__.
- Combo operand __6__ represents the value of __register C__.
- Combo operand __7__ is reserved and will __not appear in valid programs__.

Possible operations:
1) __adv__ -> reg_A = reg_A // 2**combo
2) __bxl__ -> reg_B = reg_B ^ literal
3) __bst__ -> reg_B = combo % 8
4) __jnz__ -> if reg_A != 0: pointer = literal
5) __out__ -> print(combo % 8)
6) __bdv__ -> reg_A = reg_B // 2**combo
7) __cdv__ -> reg_A = reg_C // 2**combo


For part one, the goal was to find the output of the  _program (list of operations)_.

Second part stated that there is a number, that when used at the start for register _A_, 
returns the copy of the program it was running on. The goal was to find this number. 

```
Example input:
Register A: 5
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0

Part 1:


Part 2:
```

## [Day 18: RAM Run](https://adventofcode.com/2024/day/18)
Simple path finding in a grid

Exercise provided the list of points for a 2D grid. Each of these points was added
one-by-one to the grid and from that time possibly started blocking the path.  
First part of the challenge required finding the shortest path through the grid (from north-west corner to south-east)
after _some_ number of points have been added. Second part asked to determine the first point
that will cut off the path to the south-east corner.

```
Input:          (For space efficiency wrapped in 3 lines)
     ┌───┐   ┌──┐
5,4  │   v   │  v
4,2  │  3,3  │ 0,4
4,5  │  2,6  │ 6,4
3,0  │  5,1  │ 1,1
2,1  │  1,2  │ 6,1
6,3  │  5,5  │ 1,0
2,4  │  2,5  │ 0,5
1,5  │  6,5  │ 1,6
0,6  │  1,4  │ 2,0
 └───┘   └───┘
 
Part 1:
.......                ...#...               >v.#>>v
.......     after      ..#..#.   shortest    .v#>^#v
.......   12 points    ....#..     path      .>>^#v<   
.......  ----------->  ...#..#  ---------->  ...#v<#
.......                ..#..#.               ..#v<#.
.......                .#..#..               .#.v#..
.......                #.#....               #.#>>>>

Part 2:
.......                ...#...            ...#...
.......     after      .##..#.   next     .##..#■
.......   20 points    .#..#..   point    .#..#..
.......  ----------->  ...#..#  ------->  ...#..# 
.......                ###..##            ###..##
.......                .##.###            .##.###
.......                #.#....            #.#....
```

## [Day 19: Linen Layout](https://adventofcode.com/2024/day/19)
Arranging items to match patterns.

The challenge involved checking whether a string can be constructed 
from the supplied tokens. First line of the input file listed all possible
tokens, while the subsequent lines had the strings that needed to be matched.

Solution for the first part of the challenge required determining how many
of the supplied strings can be constructed. Second part required not only checking
_whether_ the string can be constructed but also in _how many different ways_


```
Sample input:
r, wr, b, g, bwu, rb, gb, br

bwurrg
rrbgbr
bbrgwb

Part 1:
-- bwurrg --> can be made with bwu, r, r, g
-- rrbgbr --> can be made with r, rb, g, br
-- bbrgwb --> impossible
----> result = 2

Part 2:
-- bwurrg --> one possible way:
                (bwu, r, r, g)
-- rrbgbr --> six possible ways:
                (r, r, b, g, b, r)
                (r, r, b, g, br)
                (r, r, b, gb, r)
                (r, rb, g, b, r)
                (r, rb, g, br)
                (r, rb, gb, r)
-- bbrgwb --> still impossible
----> result = 7
```

## [Day 20: Race Condition](https://adventofcode.com/2024/day/20)
Shortest distance between points on a grid path

The problem presented a grid consisting of 4 elements:
- `.` - path step
- `#` - wall
- `S` - start position
- `E` - end position

There was only one path connecting start and end position, it went through 
all the steps in the grid. Additionally there was a rule that once during the 
traversal of the grid it was possible to make a shortcut. This is a special
condition that allowed to treat wall element (_#_) as a regular path (_._) for 
two steps. 

For part one, the goal was to find the number of all possible shortcuts
that allowed to shorten the path to the end by at least _100_ steps.
Part two modified the length on the shortcut such that instead of 2 steps, it 
allowed to make at most 20.

```
Original grid:
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

Part 1:

Shortcut saving      Shortcut saving      Shortcut saving
12 steps:            64 steps:            38 steps:      
███████████████      ███████████████      ███████████████     
█>>v█>>>12>>>v█      █>>v█>>v█     █      █>>v█>>v█     █  
█^█v█^█ █ ███v█      █^█v█^█v█ ███ █      █^█v█^█v█ ███ █  
█S█>>^█ █ █v<<█      █S█>>^█v█ █   █      █S█>>^█v█ █   █  
███████ █ █v███      ███████v█ █ ███      ███████v█ █ ███  
███████ █ █>>v█      ███████v█ █   █      ███████v█ █   █  
███████ █ ███v█      ███████v█ ███ █      ███████v█ ███ █  
███>>E█   █v<<█      ███>>E█>>>12  █      ███>>E█>v █   █  
███^███████v███      ███^███████v███      ███^████1██ ███  
█>>^███v<<█>>v█      █>>^███v<<█>>v█      █>>^███v2 █   █  
█^█████v█^███v█      █^█████v█^███v█      █^█████v█ ███ █  
█^█v<<█v█^█v<<█      █^█v<<█v█^█v<<█      █^█v<<█v█ █   █  
█^█v█^█v█^█v███      █^█v█^█v█^█v███      █^█v█^█v█ █ ███  
█^<<█^<<█^<<███      █^<<█^<<█^<<███      █^<<█^<<█   ███  
███████████████      ███████████████      ███████████████  

Part 2:

Shortcut saving
76 steps:      
███████████████
█   █   █     █
█ █ █ █ █ ███ █
█S█   █ █ █   █
█1█████ █ █ ███
█2█████ █ █   █
█3█████ █ ███ █
█456>E█   █   █
███ ███████ ███
█   ███   █   █
█ █████ █ ███ █
█ █   █ █ █   █
█ █ █ █ █ █ ███
█   █   █   ███
███████████████
```

## [Day 21: Keypad Conundrum](https://adventofcode.com/2024/day/21)
Nested keypad usage simulation

This challenge presented a problem of using one controller with another one.
The task described in the exercise was to press the sequence of numbers on the _output controller_.
However, specifying which button is pressed was done with _directional controller_. To complicate
the task even more, button presses on that _directional controller_ were controlled by another _directional controller_, 
which in turn was controlled by yet another one. The 'chain' of controllers consited of
one _input (directional) controller_, followed by two _directional controllers_ and ending with _output controller_.

The first part of the task required finding the number of presses required to make on the input controller to force the 
output controller to print out a specified sequence of numbers.
The second part of the exercises extended the number of directional controllers to 25, causing the number of 
button presses to be in the magnitude of few billions.


```
Output            Directional     
controller        controller                     
┌───┬───┬───┐         ┌───┬───┐                         
│ 7 │ 8 │ 9 │         │ ^ │ A │                              
├───┼───┼───┤     ┌───┼───┼───┤                                 
│ 4 │ 5 │ 6 │     │ < │ v │ > │                                 
├───┼───┼───┤     └───┴───┴───┘                                 
│ 1 │ 2 │ 3 │                   
└───┼───┼───┤         
    │ 0 │ A │     
    └───┴───┘

Flow of operations:
User input        --> <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
Controller 1      --> v<<A>>^A<A>AvA<^AA>A<vAAA>^A
Controller 2      --> <A^A>^^AvvvA
Output Controller --> 029A

Effect of user input on controllers:
User input        --> <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
Controller 1      -->   v <<   A >>  ^ A   <   A > A  v  A   <  ^ AA > A   < v  AAA >  ^ A
Controller 2      -->          <       A       ^   A     >        ^^   A        vvv      A
Output Controller -->                  0           2                   9                 A
```

## [Day 22: Monkey Market](https://adventofcode.com/2024/day/22)
Generating sequences

The problem explained the rules to generate a sequence of numbers - _secrets_. Each 
new value depended on the previous item and was determined by performing a set of operations:
1) multiply _secret_ by 64
2) divide it by 32 and round down to integer
3) multiply it by 2048

Additionally, each step was followed by 2 operations - mixing and pruning
- mixing - bitwise XOR of given value and secret number 
- pruning - secret number modulo 16777216

So to create a new secret following operations had to be performed:
```
step_1 = old_secret * 64
mix_step_1 = step_1 ^ old_secret
prune_step_1 = mix_step_1 % 16777216

step_2 = prune_step_1 // 32
mix_step_2 = step_2 ^ prune_step_1
prune_step_2 = mix_step_2 % 16777216

step_3 = prune_step_2 * 2048
mix_step_3 = step_3 ^ prune_step_2
prune_step_3 = mix_step_3 % 16777216

new secret = prune_step_3
```

The first part of the challenge was finding the **_2000th_** secret for each of the provided starting numbers.

Second part redefined the exercise by interconnecting sequences and introducing _price_ - the _ones_ digit of the secret.
From each sequence only one price could be chosen and the goal was to maximise the sum of those prices. However,
determining which price is chosen depended on the **singular** list of four consecutive price changes that was used **across 
all sequences**.


```
  secrets   │   price   │   change     
────────────┼───────────┼────────────
      123   │     3     │    ─────
 15887950   │     0     │     -3
 16495136   │     6     │      6
   527345   │     5     │     -1
   704524   │     4     │     -1
  1553684   │     4     │      0
 12683156   │     6     │      2
 11100544   │     4     │     -2
 12249484   │     4     │      0
  7753432   │     2     │     -2
  
Best price occurs after sequence -1, -1, 0, 2
* However that might not be the case for other sequences
and optimal change sequence might be different
```

## [Day 23: LAN Party](https://adventofcode.com/2024/day/23)
Analyzing graph structure

The exercise presented a list of connections between nodes creating a graph. Each
node was uniquely marked with 2 letters. 
The first part of the challenge required finding all sets of 3 nodes that are
fully connected to each other. And out of them, selecting only these which had 
at least one node starting with letter _t_.
Second part asked for the biggest set of nodes in which all of them where fully connected.

## [Day 24: Crossed Wires](https://adventofcode.com/2024/day/24)
Recursive binary operations

The problem presented a list of initial states of some _wires_ 
(marked with a letter and two-digit number). Additionally list of **_AND_**, **_XOR_** and **_OR_**
_boolean logic gates_, determined the result of remaining _wires_. 

The goal for first part, was to find the values of all wires starting with letter `z`, 
sort them in descending order based on the number from _wire's_ name and convert resulting 
number to base 10.

In part two it was stated that the values of _wires_ starting with `x` and `y` are actually 
numbers in binary and result calculated with the method from part 1 is supposed to be equal to `x + y`. 
To achieve it, _4_ logic gates had to be swapped.

For example, set of gates<br>
`x00 AND x01 -> z01`<br>
`x03 AND x04 -> z02`<br>
after the swap would become<br>
`x00 AND x01 -> z02`<br>
`x03 AND x04 -> z01`

The answer for part two was the list of swapped gates in alphabetical order - `z01,z02`

```
Sample input:
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00

Part 1:

x00 AND y00 -> z05      --> 0 & 0 = 0
x01 AND y01 -> z02      --> 1 & 0 = 0
x02 AND y02 -> z01      --> 0 & 1 = 0
x03 AND y03 -> z03      --> 1 & 1 = 1
x04 AND y04 -> z04      --> 0 & 0 = 0
x05 AND y05 -> z00      --> 1 & 1 = 1

Results:                                      Sorted:
┌─────┬─────┬─────┬─────┬─────┬─────┐         ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ z05 │ z02 │ z01 │ z03 │ z04 │ z00 │   -->   │ z05 │ z04 │ z03 │ z02 │ z01 │ z00 │
├─────┼─────┼─────┼─────┼─────┼─────┤         ├─────┼─────┼─────┼─────┼─────┼─────┤
│  0  │  0  │  0  │  1  │  0  │  1  │         │  0  │  0  │  1  │  0  │  0  │  1  │
└─────┴─────┴─────┴─────┴─────┴─────┘         └─────┴─────┴─────┴─────┴─────┴─────┘

Conversion:
┌────────┬─────────┐
│ Binary │ Base 10 │
├────────┼─────────┤
│ 001001 │    9    │
└────────┴─────────┘

Part 2:

X value:                                Conversion:
┌─────┬─────┬─────┬─────┬─────┬─────┐   ┌────────┬─────────┐
│ x05 │ x04 │ x03 │ x02 │ x01 │ x00 │   │ Binary │ Base 10 │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├────────┼─────────┤    ─┐
│  1  │  0  │  1  │  0  │  1  │  0  │   │ 101010 │   42    │     │
└─────┴─────┴─────┴─────┴─────┴─────┘   └────────┴─────────┘     │      ┌─────────┬─────────┐
                                                                 │      │ Base 10 │ Binary  │
Y value:                                Conversion:              ├──>   ├─────────┼─────────┤
┌─────┬─────┬─────┬─────┬─────┬─────┐   ┌────────┬─────────┐     │      │   86    │ 1010110 │
│ x05 │ x04 │ x03 │ x02 │ x01 │ x00 │   │ Binary │ Base 10 │     │      └─────────┴─────────┘
├─────┼─────┼─────┼─────┼─────┼─────┤   ├────────┼─────────┤    ─┘   
│  1  │  0  │  1  │  1  │  0  │  0  │   │ 101010 │   44    │
└─────┴─────┴─────┴─────┴─────┴─────┘   └────────┴─────────┘

Investigation*
┌──────────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ Bit      │ z06 │ z05 │ z04 │ z03 │ z02 │ z01 │ z00 │
├──────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ Expected │  1  │  0  │  1  │  0  │  1  │  1  │  0  │  --> differences on bits z00, z01, z02, z05 
├──────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤           └> swap something responsible          
│ Actual*  │  1  │  1  │  1  │  0  │  0  │  1  │  1  │              for creation of these bits
└──────────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘


* Sample input behaved differently to the actual input,
  to properly demonstrate the problem different --Actual-- value was used 

```

## [Day 25: Code Chronicle](https://adventofcode.com/2024/day/25)
Simple search on product of two lists

The last challenge required to properly parse the input to split it into _keys_ and _locks_.
Each structure was consisting of 7 lines of `.` and `#` characters. _Key_ was determined by 
having its last line made entirely of `#`, while the lock by having its first line of these characters.

The goal of the puzzle was to find the number of unique combinations of key-lock pairs where 
both structures didn't overlap each other (so where the key could fit into the lock). 

```
Example locks:
[05343]    [12054]
 #####      #####
 .####      ##.##
 .####      .#.##
 .####      ...##
 .#.#.      ...#.
 .#...      ...#.
 .....      .....

Example keys:
 .....      .....      .....
 █....      .....      .....
 █....      █.█..      .....
 █...█      ███..      █....
 █.█.█      ███.█      █.█..
 █.███      ███.█      █.█.█
 █████      █████      █████
[50214]    [43402]    [30201]

Part 1:

[12054]
 #####
 ##.##
 .#.##
 █..##   --> No overlap - key fits
 █.█#.
 █.█#█
 █████
[30201]

[05343]
 ##### 
 .####  
 █#X## 
 █XX##   --> Overlap - key doesn't fit
 █X█#█ 
 █X█.█ 
 █████ 
[43402]
```
