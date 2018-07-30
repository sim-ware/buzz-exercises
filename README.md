# Ex1
## Binary Plateau
Solutions are in a file called 'exercise_one.py', containing four methods. The method 'solution()' runs all the other methods, to return the Binary Plateau, or any maximal sequence of consecutive ones in the binary representation of N. The 3 other methods show the incremental steps to a solution. binaryConversion() converts the inputted integer into a Binary. maximalOnes() takes the converted Binary and returns a list of all the consecutive ones. Finally, the method binaryPlateau() returns the length of the longest consecutive one chain, or the Binary Plateau.

![Screenshot](ex1.png)

# Ex2
Event API

to run
initialise db
```
python init_db.py
```
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
to test
```
cd test
```
```
python -m unittest discover
```

SQLite is convenient because it doesn’t require setting up a separate database server and is built-in to Python.


Using PostMan to test API responses - intuitive interface, stops me from saving/downloading ics files a lot as it renders them instead
