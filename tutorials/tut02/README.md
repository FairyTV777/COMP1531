# Tutorial 2

## A. Code Review

Review this piece of code.
* What does it do?
* What style could be improved here?
* Is this code [pythonic](https://www.computerhope.com/jargon/p/pythonic.htm)? Fix it.

```python
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for idx in range(len(x)):
  if x[idx] % 2 == 0:
    result.append(x[idx] * 2)
  else:
    result.append(x[idx])

print(result)
```

## B. Thinking about testing

The following `set_name` function is used to set a name according to the follow requirements on input:
 * First Name must be at least 3 characters, and no more than 30.
 * Last Name must be at least 3 characters, and no more than 50.
 * First Name can only contain letters (uppercase or lowercase), and dashes.
 * Last Name can only contain letters (uppercase or lowercase), spaces, and dashes.
 * Middle Name can be None, but if it's not none, it can be between 1 and 50 characters.
 * Middle Name cannot be longer than the first name, and it cannot be longer than the last name.

Your tutor will break you up into your project groups for this activity. Once completed you can come back together to discuss what you have.

The function returns `True` if the inputs are valid, and `False` if the inputs are invalid.

```python
def set_name(firstName, middleName, lastName):
	pass
```

Write a list of inputs and associated return values. This is good practice for trying to conceptualise edge case.

## C. Developing a feature with Python + Git

Consider this problem:

 > Given a list of integers, compute the average of only the *positive* elements.

Your tutor will fork (create a copy) of `tutorials.git` and go into the `tut02` folder.

There is a stub for a function that solves this problem in `rainfall.py`.

Before implementing it, create a new branch called `[tutorname]/rainfall` write some pytest compatible tests for the function.

* What needs to be tested for?
* What are the edge cases and how should they be handled?

Once the tests are written, commit them to git.

It's now time to implement the feature.

(Optional step to create a sub-branch like `[tutorname]/rainfall-implementation`).

On this new branch, or sub-branch, implement the function such that it passes all the tests.

* How confident are you that your solution is correct?
* Is your solution very different from how you might do it in C?

(Optional to merge your sub-branch in to `[tutorname]/rainfall` if you went down that path).

Create a merge request for your new branch in gitlab. Someone in the class will review it and approve it, which gives the initial or primary author permission to merge in.

## D. Git merge conflicts

There is a stubbed implementation of `printname.py`, which currently just has a `pass`.

There is a branch `tute02_merge1` that has one implementation of `printname.py`, and another branch `tute02_merge2` that has another implementation of it.

Try and `git merge tute02_merge1` into master. You will notice master updates successfully. Now try and `git merge tute02_merge2` into master. This will be unable to automatically merge and will create a merge conflict.