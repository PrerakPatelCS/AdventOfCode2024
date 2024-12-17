# Chinese Remainder Theorem

noticed that maps 14 and 94 look interesting.
14 has many verticle lines.
94 has many horizontal lines.
103 tall so the horizontal lines would repeat after 103x + 94.
101 wide so the vertical lines would repeat after 101x + 14.
We can apply Chinesse Remainder Theorem to solve this to get the answer.
(x mod 103 = 94) and (x mod 101 = 14) First check that the modulos are coprime.
103 and 101 are coprime because gcd(101, 103) == 1.
Because of Modular arithmetic and this rule.
a = b mod m same as b = a mod m.
so we have x = 94 mod 103 and x = 14 mod 101.
The goal is to have mod 103 cancel out the other 14 mod 101, and vice versa.
x = 101 mod 103 + 103 mod 101 x = 101 mod 103 + 2 mod 101 we want 94 mod 103 and
14 mod 101.
Multiply the 103 by 7 and we get 721 mod 101 = 14 mod 101 And Multiply 101 by 56
and we get 5656 mod 103 = 94 mod 103 x = 101 * 56 mod 103 + 103 * 7 mod 101 x =
5656 mod 103 + 721 mod 101 x = 6377 mod 10403 When both the vertical and
horizontal line up is at 6377 + 10403x
