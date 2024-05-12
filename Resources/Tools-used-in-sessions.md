# Resouces that are used in sessions

## To play CTF's

1. picoCTF - https://play.picoctf.org/
2. Google CTF Beginner's quest - https://capturetheflag.withgoogle.com/

# Tools to use

## Cryptography and Ciphers

1. CyberChef - https://gchq.github.io/CyberChef/
2. dCode - https://www.dcode.fr/
3. Cryptii - https://cryptii.com/
4. Boxentriq - https://www.boxentriq.com/cipher-identifier
5. For base 64 decode, you can run `echo "string" | base64 -d` in terminal

## Binary Exploitation and Reverse Engineering

The softwares that are used in sessions are:

1. Ghidra - https://ghidra-sre.org/
2. IDA Pro - https://www.hex-rays.com/products/ida/
3. JADX
4. ghex - https://wiki.gnome.org/Apps/Ghex

Terminal commands to use:

5. `strings` - To extract strings from a binary file
   Eg: `strings binary_file` or `strings binary_file | grep "string_to_search"` or `strings binary_file | less`

6. `objdump` - To disassemble a binary file
7. `radare2` - To disassemble a binary file
   Eg. `r2 -d binary_file
8. `gdb` or any debugger - To debug a binary file
9. `file` - To get the type of file
   Eg. `file binary_file`
10. `ltrace` - To trace library calls
    Eg. `ltrace binary_file`
11. `strace` - To trace system calls
    Eg. `strace binary_file`
12. `readelf` - To read the ELF file
    Eg. `readelf -h binary_file`
13. `hexdump` - To dump the hex values of a file
    Eg. `hexdump -C binary_file`
14. `xxd` - To dump the hex values of a file
15. `hexedit` - To edit the hex values of a file
16. `hexcurse` - To edit the hex values of a file using good terminal UI.
17. `exiftool` - To extract metadata from a file
    Eg. `exiftool binary_file`

## Web Exploitation

The softwares you can use are:

1. Burp Suite - https://portswigger.net/burp
2. Wireshark - https://www.wireshark.org/

Terminal commands to use:

1. `curl` - To get the response from a website
   Eg. `curl http://example.com`
2. `wget` - To download a file from a website
3. `nmap` - To scan a website
   Eg. `nmap -sV -sC -A website.com`
4. `nc` - To connect to a port
   Eg. `nc website.com 80`

## Forensics

Terminal commands to use:

1. `binwalk` - To extract files from a binary file
   Eg. `binwalk binary_file`
2. `steghide` - To extract hidden files from an image
3. `stegsolve` - To solve steganography challenges
