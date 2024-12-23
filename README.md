# AdventOfCode2024
Advent Of Code 2024

# Days

1. Easy
2. Learned about unpacking in python.
   Optimization, fix the first mistake.
3. Parsing wall of text, interesting solution finite state machine or regex.
4. Find XMAS in word search, and then MAS in a X shape in the word search.
   Cool optimization where you make all coordinates an entry in a map so you
   never need to do out of bounds checks.
5. Make the rules set.
   You can make a custom comparator because the input is given as a total
   ordering.
6. Find where the Guard will go.
   Worked with the matrix with complex numbers so we can add and subtract easily
   and for fun.
   There are some optimizations for the possible spots.
7. Backtracking.
8. Anntennas, complex numbers and map trick.
9. Getting rid of Internal fragmentation, but part 2 make more internal
   fragmentation?
10. Find Paths from 0 to 9s
11. Dynamic programming, stones change for every blink
12. Find Perimeter and then find number of sides.
    Number of sides can be solved many different ways I chose to use math and
    figure out the number of corners which has 2 edge cases you can figure them
    out!
13. Linear Algebra solving a system of linear equations, very fun.
14. Figure out where the christmas tree is.
    I used hueristics to find it.
    There is also a math solution with Chinese Remainder Theorem.
15. Robot moves through a matrix and moves blocks, what happens when it becomes
    twice as wide and the robot has to deal with edges where you can push
    boxes from their edge.
16. Find the fastest route from S to E, djikstras and then use DFS knowing the
    best route so you can find all of the fastest routes.
17. Mini 3-bit computer, there are soltuions like a disassembler but I found a
    pattern in the outputs and used ranges to find the answer.
18. Bytes are falling on our map and we need to find the last time we can make
    it out.
    This is escape the spreading fire but with falling bytes and no spreading
    fire.
    Cool Union find solution.
19. Find the number of ways to make a pattern from a dictionary, used a trie and
    dfs and cached the patterns.
20. We have a race track and want to enable cheats which can pass walls for
    either 2 or 20 seconds.
    This was pretty easy with our generating function.
21. We have a number pad and 2 to 25 directional pads all controlled by robots.
    We control the chain of robots through a directional pad manually.
    This is a pretty clean recursive solution with caching but it was really
    hard to visuallize what moves you had to do and how many you had to make
    when testing on smaller inputs.
    Only around 11k people got this.
22. Monkey market, the monkeys make psuedorandom numbers, ask a monkey to look
    for a sequence and it will sell when it finds that sequence, so I just
    stored all sequences and their value and the max sequence is the answer.
23.
24.
25.

# New Things

Using Complex numbers as coordinates so you can add and multiply.
But you lose the ability to compare like normal numbers so you have to still do
that normally.

Converting the matrix to a map so you do not need to check the bounds ever since
it will just not be in the map.

Using *list to unpack the list.

Using yield to make a generating function.

Using itertools.product to make looping through a matrix easy.

Refresher on solving linear systems.

Refresher on solving chinese remainder theorem and modulus arthimetic.

Counting corners to calculate all the sides.

Regex "\\d+" is very useful.
