# Python Cheatsheet for Basic Data Structures and Language Features
This cheatsheet is a reference guide for the building blocks of Python (the concepts here can be extended to many languages). More can be found at https://docs.python.org/3/tutorial/datastructures.html.

## Variables
They hold an item that can be referenced later
```
x = 5
x = "hello"
x = None
```
None is a special word that means the absence of a value. Useful for saying "I don't have anything useful to give you".

Use whenever you want to use something later and for making code more readable.

## Conditions
This is the concept of yes (true) or no (false).
```
x == 5
```

## Lists
This is a collection of any kind of item (numbers, strings).
```
x = [3, "hello", 4.5]
```

Each item in a list is stored in a certain position called an index. The first position (index) starts at 0.
```
x[0] = 3
x[1] = "hello"
x[2] = "4.5"
```

Common things you'll want to do with lists are:
* Adding to a list (will always add to the end)
```
x.append("got you")
# [3, 'hello', 4.5, 'got you']
```
* Going through a list (iteration)
```
for item in x:
  print(item)

3
hello
4.5
got you
```
* Finding an item in the list
```
x.index("hello")
# 1
x[x.index("hello")]
# "hello"
```
* How long the list is (length)
```
len(x)
# 4
```

Use whenever you have a collection of similar items and would like to store it.

## Loops
A feature that allows you to do something multiple times. There are different kinds of loops:

```
for <variable> in <list>:
  # Do something
```

Example:
```
for item in x:
  # Do something
```
This says "Do something `len(x)` number of times where each time `item` will hold the value of the next item in the list.

Example:
```
for number in range(10):
  # Do something
```
This says "Do something 10 times"

```
while <condition>:
  # Do something
```
This says "Do something until condition is not true anymore"

Example:
```
tries = 0
hasCookies = false
while (not hasCookies or tries < 5):
  isLoved = askForCookies(person)
  tries = tries + 1
```
This will ask for cookies until a cookie is given or until we've asked 5 times.

Use whenever you want to do something multiple times (usually by using a list of items).

## Functions
A feature that allows you to breakout logic into manageable chunks.

```
def askForCookies(person="toiletpapar"):
  # Do something

askForCookies()
askForCookies("You")
askForCookies(person="You")
```
Theres a couple of things going on here:
* The name of the function is `askForCookies`. If you want to "Do Something" you'll have the call the function by it's name.
* The function has access to one variable called `person`. This variable is called a parameter. This parameter is optional (more on that below).
* `askForCookies()` will invoke the function to "Do Something" and because a variable (called an argument) was not provided in the parenthesis the default value `"toiletpapar"` will be assigned to `person`.
* `askForCookies("You")` will invoke the function to "Do Something" and because an argument was passed the value of `person` will be `"You"`
* `askForCookies(person="You")` is exactly the same as above. It's a fancy way of saying that you want to specifically assigned `"You"` to `person`. This can come in handy when you only want to pass an argument to a parameter that is much further away from a parameter list (or if the API is likely to change, or for readablility purposes).
* Functions can return values via `return` keyword. This immediately terminates the execution of the function (as in no code after it will be invoked).

Use whenever there are logical chunks you can separate out. This helps manage your codebase and ensure your brain doesn't explode.

## If..Else
A feature that allows you to control the flow of the program using **conditionals**.
```
if <condition 1>:
  # Do one thing
elif <condition 2>:
  # Do another thing
else:
  # Do even another thing
```
Theres a couple things going on here:
* You can use if without `elif` or `else` (but not vice versa)
* The conditions are ordered top to bottom
* One one condition is satisfied the others are ignored

Example:
```
if isRaining(today):
  # Bring an umbrella
elif likesDogs(person):
  # Buy dog
elif recentlyConsumedDairy("tyler"):
  # Run away
else
  # Appreciate the sunny day
```

Use whenever you want to do different things based on some data you provide in the conditions.

## Combine All The Things
What if there's someone you find attractive and you want to ask them out? You don't want to be annoying though because you're **super** cool so you'll only ask a couple hundred times. How would you do that?

```
# Returns if `person` answered with yes (true)
def askOut(person):
  # Some text to analysis magic that talks to your potential SO

# Returns whether to ask again or not
def handleRejection(timesAsked):
  return timesAsked + 1

maximum_rejections = 888
timesAsked = 0
successful = false
while (not successful and timesAsked < maximum_rejections):
  successful = askOut(person)
  if successful:
    # Congrats, I hope you grow old together
  else:
    timesAsked = handleRejection(timesAsked)
```

Lets break this down:
* We define two functions that help abstract some of the functionality so that the codebase is legible
* We define some variables to help us track whether we're successful and to ensure that we don't keep asking forever
* We define a loop to help us continue asking
* We define a control flow inside the loop to help us determine whether `askOut(person)` was successful and to change our variables accordingly

That sums up some of the building blocks that will help us create beautiful applications (or at least automate mundane parts of our lives).