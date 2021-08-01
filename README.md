# Student-Reg
Key features-

1. Capable of linking multiple clients to the server.
2. Optimised fetching from database by using class varaibles to store latest record by hitchhiking.
3. Generation of unique registration key by combining information provided by student and a unique id. (Eg, Btech student, year 2020, General category, Computer Science --> BT20GCS008 where '008' is a three digit string added to the info. given by the student.

The unique id generated refers to the details entered by student and previous database records to add a unique id in the form of a string. Fetching database for the entry of each record is not an optimized method. This code uses class variables instead that keep track of the last record. However, in case the server is restarted, the values of the variables are lost and in this case, data is fetched from the database.
