# Ex1
## Binary Plateau
Solutions are in a file called 'exercise_one.py', containing four methods. The method 'solution()' runs all the other methods, to return the Binary Plateau, or any maximal sequence of consecutive ones in the binary representation of N. The 3 other methods show the incremental steps to a solution. binaryConversion() converts the inputted integer into a Binary. maximalOnes() takes the converted Binary and returns a list of all the consecutive ones. Finally, the method binaryPlateau() returns the length of the longest consecutive one chain, or the Binary Plateau.

![Screenshot](ex1.png)

# Ex2
## Event API
### To Test
We change into the test directory, and run the following command to run all tests.
```
cd test
```
```
python -m unittest discover
```

### To Run
Run the following command to initialise a database. This creates a table called 'events', and populates it with some sample data to interact with.
```
python init_db.py
```
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
### Endpoints
The following endpoints are available:
```
GET /api/events/
```
- Returns all events in Database
```
GET /api/events/:id/
```
- Returns an event, specified by ID
```
POST /api/events/:start/:end/:label/:category/
# e.g.: /api/events/'2016-08-01T10:00:00Z'/'2016-08-01T15:00:00Z'/'Event one'/'blue'/
```
- Creates an event with attributes. All attributes must be included, and written between single quotes.
```
GET /api/events/:id/export/
```
- Exports an event as an ICS file. Event specified by ID. Works with iCal.
```
GET /api/events/:id/delete/
```
- Deletes an event, specified by ID

## Notes
I used SQLite3 for my database, as it didn't require setting up a separate database server, and is in-built to Python. For the problem at hand it seemed like a simple and clear solution to the problem.

I used Flask for similar reasons - it is lightweight and simple to configure, and consequently the code is easy to read and debug.

For testing the API responses, I used PostMan. It has a GUI for testing API's, making it easy to enter requests and see the results. It was especially helpful for testing if the .ics file was being exported, as it rendered the file rather than requiring me to open it externally.
