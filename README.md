# Write Yourself A Git
https://wyag.thb.lt

This article is an attempt at explaining the Git version control system from the bottom up, that is, starting at the most fundamental level moving up from there. This does not sound too easy, and has been attempted multiple times with questionable success. But there’s an easy way: all it takes to understand Git internals is to reimplement Git from scratch.

---

## What it is about

I'm going to implement my own git client for the sake of learning how it works, and being full conscious at my decisions when it comes to git usage.

Although, while all the help and code is gonna come in a direct or indirect way from the article, it's a possibility that I may add my own features in the future. Not a necessity, only if I feel like it. 

## Why am I doing it

The reason I decided to learn and to implement it, is not just because I like learning new things. But because I like learning new stuff that will actually be of use in my career. Otherwise, I would forget almost everything about it after sometime of not practicing that knowledge somewhere and it would be just a waste of time to learning it. And by the way, the experience I'm gonna get from a project like this will be useful in the future.

## Why Python

Because the article is writing in it. Specifically, **Python 3**.

Python is an easy language to create efficiently and fast a project. Not necessarily good for everything else though, but it comes in handy when you want just to create something without bothering with micro-optimizations, nitpicky algorithms and methods and other syntactical and methodical gabs.

So in this case, making that same project in a language like C++ would be a way to distract you from the main course here, which is to make your own git, and not to learn C++ and how to do correct memory management and how to use pointers or even trying to debug them in the process. And at the same point, python offers you a huge amount of tools for everything and it's widely supported on a huge amount of micro-projects, while this might not be the case with C++ or other similarly complex languages. Plus, it can produce a single excecutable file and tie up all the libraries in one executable file (unlike NodeJS) and is very much supported by other OSes in a way that it runs fluently.

So, in conclusion, I can see why the author selected to write the project in this language specifically. It's such an easy and elegant choice to make, that is very hard to come against to and pick something else, and almost everyone has dealt sometime in his life with a little bit of Python. So, for a huge audience, it wouldn't be distracting in a way that the project would be more about learning Python than the actual point of the project itself.