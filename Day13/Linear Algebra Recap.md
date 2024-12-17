# Linear Algebra

We have solve a system of linear equations.

```text
prize_x = a(x1) * b(x2)
prize_y = a(y1) * b(y2)
and Cost = 3a + b
```

# Determinant

Determinant helps us get the inverse of a matrix.
Is the determinant is 0 then we have more than 1 solution and have to get the
minimum for our cost function.
```text
1 / (ad) - (bc)
```

# Inverse

We need the inverse because we are solving this.

```text
Ax = b
A*A^-1 = I (identity matrix)
I(x) = x
A*(A^-1)x = b(A^-1)
x = b(A^-1)
```

How to find the inverse?

```
Find the determinant
[[a, b], [c, d]] = (1 / (ad) - (bc)) * [[d, -b], [-c, a]]
```

# Matrices

```text
prize_x = a(x1) * b(x2)
prize_y = a(y1) * b(y2)
and Cost = 3a + b
```

This makes these matrices.

```text
[a, b] * [[x1, x2], [y1, y2]] = [prize_x, prize_y]
```

We are solving for a and b.
The input is nice which means the determinant is not going to be 0.
Therefore we do not need to optimize for cost as there is only 1 solution.

Lets find A^-1.

```text
A = [[x1, x2], [y1, y2]]
Determinant = 1 / (x1 * y2) - (x2 * y1)
A^-1 = [[y2, -x2], [-y1, x1]] / ((x1 * y2) - (x2 * y1))
```

With the inverse we can single out [a, b].
```text
[a, b] = [prize_x, prize_y] * [[y2, -x2], [-y1, x1]] / ((x1 * y2) - (x2 * y1))
a = ((prize_x * y2) - (prize_y * x2)) / ((x1 * y2) - (x2 * y1))
b = ((prize_x * -y1) + (prize_y * x1)) / ((x1 * y2) - (x2 * y1))
```

Filled in with the example.
```text
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

a, b = 80, 40.
determinant = 1 / ((94 * 67) - (22 * 34))
a = ((8400 * 67) - (5400 * 22)) / 5550 = 80
b = ((8400 * -34) - (5400 * 94)) / 5550 = 40
```
