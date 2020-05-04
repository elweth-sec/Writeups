```
nc challenges1.france-cybersecurity-challenge.fr 4009
================================
== Patchinko Gambling Machine ==
================================

We present you the new version of our Patchinko Gambling Machine!
This is a game of chance: you need to guess a 64-bit random number.
As we have been told that it is quite hard, we help you.
Before the machine executes its code, you can patch *one* byte of its binary.
Choose wisely!

At which position do you want to modify (base 16)?
>>> 8EF
Which byte value do you want to write there (base 16)?
>>> dd
== Let's go!
Hello! Welcome to Patchinko Gambling Machine.
Is this your first time here? [y/n]
>>> y
Welcome among us! What is your name?
>>> cat flag
FCSC{b4cbc07a77bb0984b994c9e34b2897ab49f08524402c38621a38bc4475102998}
```
