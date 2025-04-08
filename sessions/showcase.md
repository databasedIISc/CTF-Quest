---
title: Databased CTF-Quest
author: Anirudh Gupta, Aditya Arsh, Hasini G
sub_title: Welcome! Let's get HACKY!
---

# What is CTF?

<!-- pause-->

CTF means `Capture The Flag`. It is a cybersecurity competition where participants solve challenges to find hidden "flags" and test their skills.
CTF challenges can be in various categories, including:

<!-- pause-->

- Web Exploitation
<!-- pause-->
- Binary Exploitation
<!-- pause-->
- Forensics
<!-- pause-->
- Ciphers and Cryptography
<!-- pause-->
- Reverse Engineering
<!-- pause-->
- Miscellaneous
<!-- pause-->

Let's see some examples of these categories.

<!-- end_slide -->

# Let's get on with it!

<!-- pause-->

We are gonna be using pre-existing CTF challenges from mainly `picoCTF`.

<!-- pause-->

# 1. Web Exploitation

<!-- pause-->

Problem Link: `https://play.picoctf.org/practice/challenge/142`

We will be facing various obstacles. This is a classical examples for changing request Headers. Search google for them (like) `https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/DNT`

<!-- pause-->

## LET's HACK!

<!-- pause-->

Open BurpSuite and intercept the request, and then let's make the changes as below!

<!-- pause -->

Website:

<!-- pause -->

```
User-Agent: PicoBrowser
```

<!-- pause -->

Reference:

<!-- pause -->

```
Referer: https://mercury.picoctf.net:38322
```

<!-- end_slide-->

## CONTINUED

<!-- pause-->

Date:

<!-- pause -->

```
Date: Wed, 21 Oct 2018 07:28:00 GMT
```

<!-- pause -->

Do Not Track:

<!-- pause -->

```
DNT: 1
```

<!-- pause -->

Location: https://sweden.se

<!-- pause -->

```
X-Forwarded-For: 102.177.147.255
```

<!-- pause -->

Language

<!-- pause -->

```
Accept-Language: sv-fi
```

and we are done... !

<!-- end_slide -->

# 2. Binary Exploitation

<!-- pause-->

Binary exploitation is a technique used to manipulate or exploit vulnerabilities in binary programs. It involves analyzing the program's code, memory, and execution flow to `find weaknesses` that can be `exploited`.

<!-- pause-->

This can include `buffer overflows`, `format string vulnerabilities`, and other types of `attacks` that allow an attacker to gain control over the program's execution.

<!-- pause-->

## BUFFER OVERFLOW! Summon `Computer System's Knowledge`

<!-- pause-->

### Key IDEAS of Buffer Overflow

<!--pause-->

- Buffer Overflow is a vulnerability that occurs when a program writes more data to a buffer than it can hold, causing adjacent memory to be overwritten.
<!-- pause-->

- This can lead to unexpected behavior, crashes, or even remote code execution.
<!-- pause-->

Problem Link: `https://microcorruption.com/debugger/Hanoi`

<!-- end_slide -->

# 3. Forensics

<!-- pause-->

Forensics is analyzing data to find hidden information. It can involve examining image, videos, pdf, audios files, network traffic, or system logs to uncover evidence of cyber incidents, etc.

<!-- pause-->

We'll learn and see few concepts today:

<!-- pause-->

- Metadata Analysis

<!-- pause-->

- JPEG's Cant be Trusted
<!-- pause-->
- PNG Can't be either.

<!-- pause-->

## CATTYYYYYY

<!-- pause-->

## 1. Metadata Analysis

<!-- pause-->

```bash
exiftool catty.jpg
```

<!-- pause-->

## 2. JPEG's have hidden data

<!-- pause-->

```bash
binwalk -e catty.jpg
```

<!-- end_slide-->

## 3. PNG's have another way of hiding data

<!-- pause-->

There is something called `steganography`.

<!-- pause-->

# Let's understand `Steganography` a bit

<!-- pause-->

<!-- end_slide -->

# 4. Ciphers and Cryptography

<!-- pause-->

This is a fun exercise we will do TOGETHER!

<!-- pause-->

Problem Link: `https://play.picoctf.org/practice/challenge/473?category=2&page=1`

<!-- pause-->

## Let's Decipher!

<!-- pause-->

- The idea is `Substitution Cipher` where each letter is replaced by another letter. Clearly!!!!

<!-- pause-->

- Let's make a mapping and find some `patterns` in the text.

<!-- pause-->

### SOLUTION REVEIL!

<!-- pause-->

- It's a lmao `Linear Equation Relation mod 26`!

<!-- pause-->

## PART 2 is HW! Try it yourself!

<!-- end_slide -->

# How we gonna do CTF?

<!-- pause-->

## This is part of Summer Vacations activity!

<!-- pause-->

## DELTA!

<!-- pause-->

## COMPETITIONS

<!-- pause-->

## PAISA $$$ (if we win contests)

<!-- end_slide -->

# Bye Bye

## Any Questions?
