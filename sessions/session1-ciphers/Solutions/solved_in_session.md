# Problems discussed within session

Two problems were discussed within the session:
You find both in this link: https://play.picoctf.org/practice?category=2&page=3

1. la cifra de
2. Compress and Attack

## Solution to 1.

The problem contains various types of ciphers used. Each line is a different cipher. Once analysed using an online tool, to directly analyse
the third line of the cipher, we get the flag.
<br>
It turns out the third line has vigenere cipher and the final obtained was `picoCTF{b311a50_0r_v1gn3r3_c1ph3ra966878a}`

## Solution to 2.

The main key to the problem is that when we enter any string of say length n, we get some bunch of strings and a number.
This number becomes lesser as the string is closer to flag.<br>
For eg, `picoCTF{` gave a score of 48, but `picoCTFa` gave a score of 49, since `a` is not a part of the flag.<br>
So, we can keep on adding characters to the string and keep on checking the score. The score will decrease as we get closer to the flag.
<br>We can use the below code to brute force it.

```python
from pwn import *
import string

sh = remote("mercury.picoctf.net", 50899)
valid_chars= string.ascii_letters + string.digits + "}{_"
def oracle(text):
    sh.recvuntil("encrypted:")
    sh.sendline(text)
    sh.recvline()
    sh.recvline()
    return int(sh.recvline().decode())

known = "picoCTF{"

length = oracle(known)
print(known, end="")

current = ""
while current != "}":
    for c in valid_chars:
        if oracle(known + c) == length:
            known += c
            current = c
            print(c, end="")
            break

```

You may face disconnection issues, so you can run the code again but this time, you can add on the new characters you found out.<br>
The flag obtained was `picoCTF{sheriff_you_solved_the_crime}`.
