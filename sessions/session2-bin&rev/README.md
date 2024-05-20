# Binary Exploitation and Reverse Engineering
The examples and Problem's shown here were solved within the session or given as HW.

# Notes of the class (slides)

`Title:` Databased CTF-Quest<br>
`Author:` Anirudh Gupta, Aditya Arsh & Databased team<br>
`sub_title:` Binary Files, Exploitation and Reverse Engineering

## Today  

We will we be going into binary files, how to extract flags out of them,
and also a bit on reverse engineering.
 
For all this, the use of terminal is very important so let's first get
to understand some basics of it.

## Terminal  
The following are some basic Terminal commands that we should know.

### Directory motion
- cd - for entering a directory 
- ls - for listing out sub file & directory
- ls -la or ll - above plus hidden files
- pwd - absolute address of your location

### Making and removing file
- rm - remove file
- rmdir - remove empty directory
- rm -rf - remove permanently any directory or file
- mkdir - make a directory
- touch - make a file
 

### Text editors
- vim or neovim(nvim)
- nano
  
### General Commands
- echo - print something in terminal
- echo "something" > filename.filetype - appends it
- chmod +x `filename` - for making a file executable
- ./*filename* - to run that executable file
- cat - view file in terminal
- bat - better cat
- wget - download file from a link
- mv - move things(cut), which also renames
- grep - finds text in directory
- clear -clears screen
- man or tldr - description of command, always helps

Now we are set to understand how to deal with some binary files
and understand how to work with them.

## What we will do today ->
We will hopefully (based on time) look at the following topics
 
#### - Dealing with binary files
 
#### - Software Application
 
- Ghidra (or you may use IDA Pro)
- Jadx
- Wireshark, etc.

#### - Debugger GDB, python debugger
 
## Dealing with Binary files ->
When you do `$ cat <binary_file>`, you get to see if its binary.

When you open it, it's total gibberish and non sense. You may see
some english test but that may or may not make any sense.

So here are few commands you should know in order to make sense 
out of what is going on around and in the file.

## Some commands for binary files  

Try to run these in order. Always best to follow your fav order.
 
### Commands are:
 
- file
- exiftool
- strings *filename* | less
- strings *filename* | grep `'{'`
- hexdump or hexedit or hexcurse
- objdump -d *filename*

## Download time
Before we move on to examples and problems, I hope everyone has the following commands and softwares available-
 
1) exiftool, file, strings
```bash
sudo apt install <command> # for linux
brew install <command> # for macOS
```
For windows, go to Google, search for it and download.
 
2) Ghidra, Jadx(optional)
```bash
`brew install ghidra` # for macOS
```
For linux and windows, you can download from net. (I never tried)
 
3) gdb or lldb
```bash
sudo apt install gdb # for linux
sudo port install gdb # for MacOS
brew install lldb # for MacOS as wellp
# ggdb (gdb) may cause errors so lldb
```
 
## Example 1  

Let's deal with our first example, a file called `example1`.
 
This is about basics tool usage of binary files.
Just use `strings example1 | grep "{"` and you have the flag!

I hope you found the flag!

## Problem 1  

Go to the repository of CTF-Quest and solve problem 1. Flag format is `dtbdCTF{...}`.
 
`A program has been provided to you, what happens if you try to run it on the command line?`

### Hint: 
```bash
chmod +x example1
./example <what argument should you write?>
```

## Solution Problem 1
1) Decrypt whatever you got
 
2) When you run `strings example1`, notice you will find the same base64 cipher. Just give it a
hit and trial and who knows that might be the flag. 

#### Flag is
```markdown
dtbdCTF{cipher_usages}
```
## Example 2

Here we will do some find some vulnerabilities of a C program file, and find the flag.
This is also something important we should all know.

Please see example2.c file from the repository. 

## Example 3 - GNU Debugger GDB

`GNU Debugger` 
 
### Commands
- b or breakpoint
- r or run
- next (for code line) `number`
- nexti (for assembly code) `number`
- step (for stepping into a function)
- c or continue
- help (important because you will forget these)
- x (for seeing the values of various registers or memory location)

Now we will see this simple example-

### Problem statement
 
`Can you figure out what is in the eax register at the end of the main function?`

Report flag in the format `dbdCTF{...}`

## Problem 2

Go to the repository of CTF-Quest and solve problem 2. 
 
### Problem statement
```markdown
`main` calls a function that multiplies `eax` by
a constant. The flag for this challenge is that
constant in decimal base. If the constant you find
is `0x1000`, then flag will be `dbdCTF{4096}`.
```
### Hint:
Keep a record of how rax is changing. What is relation between rax and eax? 

## Solution Problem 2
The solution is simple. We see a call happening at *(main +38).
Then we note the the values before the function and after the function.
We use the following commands-
 
```bash
chmod +x problem2
gdb ./problem2
layout reg
layout next # for my fav layout
b *(main + 38)
r # run the code till breakpoint
c # Note: eax value is 0x28e or 654
nexti # eax value becomes 8439870
```
 
Now we simply divide `8439870` with `654` to get `12905`.
 
#### Flag is
```markdown
dbdCTF{12905} 
```
  
## Problem 3
 
Let's do another problem! This one is easy!
 
### Problem Statement
 
Find the Flag. Format is `dbdCTF{...}`.

### Hints:
```
Just observe your hexeditted file closely!
```
 
## Solution 3

Look closely to your hexedit file. That's the solution! It's hidden like
`...C...T...F...{...`

### Flag is
 
```markdown
dbdCTF{6df215eb3cc734070267031a15b0ab36c}
```

## Example 4   
Let's do some debugging now of a python file. Let's solve *example4.py*.

_Note:_ flag format is *dtbdCTF{...}*

## Problem 4
 
Now let's do a problem. This will be based on a minor bug in the code.
You would need to apply some common sense on how you can get to the answer.
 
_Note:_ No hints for this.

## Solution problem 4

Well, you just needed to print the big strings.
You get the password as: `happychance`
 
Then you see `i = -1` in `arg122` function doesn't make sense. So by intuition, you
have to change to `i = 0`. And you get the flag!
 
### Final answer: 
```bash
dbdCTF{c30bfu5c4710n_f7w_b8062eec}
```

You need not to `pdb` though. Those who did well, look closely if it is actually needed and then move on!  

## Example 5  

Now let's do an example with ghidra. I hope everyone now has Ghidra installed.
 
#### Problem Statement
`What is the flag post 0x70?`

_Note:_ flag format is *dbdCTF{...}*


## Problem 5
Let's use some skills we learned to apply to another problem which we will need to use Ghidra for.
 
Please open problem5 from the repository. And try to figure it the flag.
No particular problem statement. Just find the flag of format `dtbdCTF{...}`
 
### Hint:
```markdown
Don't go overboard and move here and there.
Find a big list of functions, go over each of them.
```


## Solution 5
 
This problem might be hard, but once figured out, it shoudn't take much time.
Once you reach a function called `FUN_0010298a`, you see a big list of functions.
 

```java

void FUN_0010298a(void)

{
  ada__calendar__delays__delay_for(1000000000000000);
  FUN_001023a6();
  FUN_001026e6();
  FUN_0010233e();
  FUN_001023a6();
  FUN_00102852();
  FUN_00102886();
  FUN_001028ba();
  FUN_00102922();
  FUN_001023a6();
  FUN_00102136();
  FUN_00102206();
  FUN_0010230a();
    ...
    ...
    ...

  return;
}
```
Go over each of them, see the first argument, each has some corresponding text. Well that's it!
 
### Flag:
```markdown
dtbdCTF{d15a5m_ftw_eab78e4}
```

## Example 6 

This one is adopted from `picoCTF`. We will basically see where and how to use JADX. 
You can download it later on. 

##### `Why do we need jadx?`
JADX is crucial in CTFs for decompiling Android APKs and Java binaries, revealing their underlying code for analysis. It helps participants understand obfuscated code, identify vulnerabilities, and automate analysis tasks. By simplifying reverse engineering processes, JADX aids in debugging, testing exploits, and honing crucial cybersecurity skills. 

_Note:_ 
  
- You can't edit in jadx-gui
- Searching is really easy, better than Ghidra. 
- It's better to see a binary in jadx first, just for the sake of searching. If the file is supported great!

 
## That's it

### Summary
 
- Terminal basics
- Binary file tools
- Vulnerability
- GNU Debugger 
- PDB 
- Ghidra 
- JADX

