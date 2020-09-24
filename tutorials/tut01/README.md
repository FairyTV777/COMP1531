# Tutorial 1 - Solutions

## A. Introduction (10 minutes)

1. Your tutor will split you up into pairs (unrelated to your project groups). Once in a pair, introduce yourself.

2. Your tutor will start a timer. Try to come up with a new name for your partnership comprised of all or some of the letters of your full names (bonus points for using ALL the letters)

3. The class will pick their favourite from the whole class and write it on the board.

4. Find another person in the class you don't know and repeat the process, trying to come up with a "better" name than the one on the board.

5. Reflect with your tutor on any challenges you faced in the exercise

## B. Problem solving (15 minutes)

1. Your tutor will help separate you into your project groups.

2. As a group, your tutor is going to give you a problem to solve in 10 minutes. At the end, they'll ask for your answers.

3. Come back together, and reflect with your tutor on how you came up with those answers

## C. Python (15 minutes)

1. Your tutor will write a basic python program that:
 * Prompts the user to enter a number
 * Reads in a number from command line
 * Prints the square of that number; unless the number is not valid, then prints an error

```python
print("Please enter a number: ", end='')
number = input()
if number.strip('-').isnumeric():
    print(f"{int(number)**2}")
else:
    print("Please enter a valid number")
```

2. How would you modify this program to re-prompt the user for input if an invalid number is given? Your tutor *may* break you up into groups for this.

> You could perhaps try and give students access to this? So they can collaborate on code: https://repl.it/

```python
success = False
while not success:
  print("Please enter a valid number: ", end='')
  number = input()
  if number.isnumeric():
      print(f"{int(number)**2}")
      success = True
```

## D. Discussion (10 minutes)

> *Ask the questions you feel comfortable chairing. This entire section is meant to be a discussion with your class. There aren't really "model answers" for this because students will express a range of perspectives and you should try and encourage discussion. One recommendation is when someone answers a question, point to another student (ideally by name) and ask them what they think of that person's answer.*

Your tutor will break you up into your project groups for 5 minutes. During this 5 minutes your team should write down answers to 3 of these questions. You will come back together and discuss the answers.

1. Should a software engineering process always yield the same result for the same requirements, regardless of who is involved?

> *No*

2. How important is detail in the requirements? Can you have too much or too little detail?

> *Sometimes under-speccing can yield wrong results, and sometimes over-speccing (over-engineering) can be too costly*

3. Should a process require all requirements to be fully known and specified in detail before the project starts?

> *Depends on your approach. Old school (waterfall) yes, nowadays less so as we accept the changing nature of requirements*

4. What is the distinction between good practices and a process?

> *Good practices are principles used to inform approaches, i.e. processes*

5. What are traits you believe make good team members? How do you decide who you to pick in a group for the project?

> *It depends what you're using it for! For scripting, yes. For backend servers, it's good enough. For data science, very useful*

6. Is python a good programming language? Why or why not?

> *Process is just a procedure, good practice is often the well accepted procedure*
