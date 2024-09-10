# TIC-TAC-TOE
Hello everyone! I am on a mission to make a tic-tac-toe analyzer completely from scratch, without numpy, pandas or any other Python library(except for math, I will explain that later).
I am not using ChatGPT or Google for any help of any sort and completely making this from my thinking.(Atleast I tried to.)
I want it to be completely defeat-proof, it could get a draw.

# Concept
    sStarting date: 10-9-2024, 10:24am
    
    Finishing date: 10-9-2024, 11:13pm

Tic tac toe is a game that could have multiple possible combinations. So my idea was if the game is in the form of a list, i.e.,

    [
    1, 0, 0,
    0, 0, 0,
    0, 2, 0
    ]

This would represent the board. The zero represents blank, 1 represents X and 2 represents O.

So in a game of tic-tac-toe, if you are 1, I would play my move on any one of the corners. Only and ONLY if the 2 makes its move in the centre, it would be either a win for the bot or just a draw.

For example:




    X   |   O   |

        |       |

        |       |

is a garenteed win. Cuz:

    X   |   O   |

        |       |

    X   |       |

and then:

    X    |   O   |
    
    O    |   X   |
    
    X    |       |

And no matter where the other player moves, you can make your move on either the 3 or the 9. How this works is that when your opponent makes the mistake, you make a threat to win the game. And since your opponent is forced, you want him to make the move where he doesn't threatens to defeat you like in the previous example I showed. It should be like after he makes his move, you are not threatened by him to win the game on the next move and you are free to make a move anywhere.

In this example, your third move would be to make a move in the center of the board so that no matter whatever your opponent does, you will have one place to win.

If your opponent makes a move on the corner too:
For example:

       X|       |O
    
        |       |
    
        |       |

then:
    
    X    |       |O
    
    O    |       |
    
    X    |       |

and finally:

    X   |       |O
    
    O   |       |
    
    X   |       |X

And its a win.

# But why?
I wanted to improve my skills and be familiar with algorithm and other stuff.
I want to be a successful software engineer and have a good job or even better, start my own bussiness. I did had a couple of ideas in the past but *almost* all of them were already done by others. I would be working on the couple of them left once I completely master python and turn 18. Till then I am chillin'.

# Spoiler alert!
I did use ChatGPT a bit cuz I figured out how to make the board etc myself, but the method I was trying to use was like a machine learning algorithm and I wasn't able to figure out how to write it in code. So I copied and pasted my idea to ChatGPT and asked him for what formula to use for the bot. Guess I got something new to learn!

# Things learnt
I learn about that there are so many algarithms. In order to become a successful software engineer, you have to have a good foundation in maths. I also got to learn about markdown while writing this ;)