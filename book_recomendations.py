#######################################################
#program: book_recomendations.py
#author: Crass93
#version: 1.0
#date: 14.01 2021
#description: the aim of this program is to recomend the user books based on his prefferences and data from the database.
#######################################################

#The problem:
#user likes lord of the rings, what else should he read? 

#problem analysis:
#in order to even be able to implement solution, we need to analyzie the problem istelf and define the criteria
#used to determine what books would be suitable for that user. We will do this by making assumptions about users prefferences based on the book that he likes.
#in this case, Lord Of The Rings by  J.R.R. Tolkien, we will assume that user that liked this book might be interested in other books from the same author, we will also 
#assume that user that liked this book will be interested in books from the same genre, in this case (fantasy) however, we shall pick only the ones that have
#reached highest score based on the database we have available.
#
#problem solution:
# 
#I will approach solving this problem by writing a program that will consist of two fucntions, one will take the user input of a book he likes, it will search that book
#in a database and if found, fetch its author, then it will use that author to search the database for all books from same author and print the name of each book in a 
#terminal. Second function will take user input of a book he likes, it will search that book in a database and if found, fetch all books from the same genre which
#received rating 8/10 or higher and print them to the terminal.
#This solution could be made even better if we had a database of users who read and rated the same book, we could select
#every user that liked the Lord Of The Rings book (gave it a high rating), and then iterate trhough every other book of that user that he rated highly as well 
#as other users who liked lord of the rings and add that book to a list of books our user might like, and count the amount of times that book has been liked by users who
#also liked Lord of the Rings,
#and return those books that would have the highest number of repetitions, for example if based on the data, we know that 50 other users liked lord of the rings, we could scan
#what other books these users liked the most, if we found out that out of 50 people who read Lord Of The Rings, 20 of them also liked Game Of Thrones by George R.R.Martin for example
#we could add that book to a list of recomendations for our Lord of the Rings fan. I am affraid such solution is currently outside of timeframe and my expertise for a moment, so
#i will try to implement simple solution first, which will take books from the same author and best books from genre and recomend them to the user.

import sqlite3

#since i couldnt connect to the MySQL database provided in the assignment and couldnt find any similar SQLite3 database online
# i will have to create my own database with couple of entries, i didnt want to spend time tryin to implement technologies i am not
#familiar with, MySQL requires python 3.6, i am currently using 3.1, spending time getting it to work could cause me to miss the timeline
#so i decided not to take that risk



#first we need to create a databse


def create_database():
    conn = sqlite3.connect("books.db")  #this code would be better in a try block, connecting to the database always has a high chance of failure
                                        # and this would make the debugging easier i decided no to do it because i wanted to produce a working code
                                        #first and not add functionalities that could result in spending unecessary time debuging or missing the timeline 

    cur = conn.cursor()

    cur.execute("""CREATE TABLE books (
       genre text,
        author text,
        book text,
        rating integer
        )""")

    cur.execute("INSERT INTO books VALUES ('fantasy','J.R.R. Tolkien', 'The Hobbit', '6')" )
    cur.execute("INSERT INTO books VALUES ('fantasy','J.R.R. Tolkien', 'Lord Of The Rings Fellowship Of The Ring', '9')" )
    cur.execute("INSERT INTO books VALUES ('fantasy','J.R.R. Tolkien', 'Lord Of The Rings Two Towers', '8')" )
    cur.execute("INSERT INTO books VALUES ('fantasy','J.R.R. Tolkien', 'Lord Of The Rings Return Of The King', '8')" )
    cur.execute("INSERT INTO books VALUES ('fantasy','J.R.R. Tolkien', 'The Silmarillion', '7')" )
    cur.execute("INSERT INTO books VALUES ('fantasy','George R.R. Martin', 'Game Of Thrones A Song Of Ice And Fire', '10')" )
    cur.execute("INSERT INTO books VALUES ('fantasy','George R.R. Martin', 'Clash Of Kings A Song Of Ice And Fire', '9')" )
    cur.execute("INSERT INTO books VALUES ('fantasy','George R.R. Martin', 'A Storm Of Swords A Song Of Ice And Fire', '8')" )
    cur.execute("INSERT INTO books VALUES ('fantasy','George R.R. Martin', 'A Feast Of Crows A Song Of Ice And Fire', '7')" )
    cur.execute("INSERT INTO books VALUES ('fantasy','George R.R. Martin', 'A Dance With Dragons A Song Of Ice And Fire', '7')" )

    conn.commit()

    conn.close()

#then we create a function that will turn the result of a cursor, which is a list of tuples into a string and strip it so we can use the resulting string
# as a SQL command

def cursor_strip(cursor): #i find this function useful so i made this a seperate function so it is easily reusable in other programs or part of code
    """
    this function turns a list of tuples into a string, making the text directly usable for insertion into other parts of the program.

    function takes no arguments
    """
    y = cursor
    result = '\n'.join([str(x) for t in y for x in t])
    return result

#now we will create a fucntion that will recommend the books from the same author

def recomend_by_author():
    """
    this function is designed to recomend books of the same author, provided that user enters the name of the book as an input, function works
    by defalt with a built in 'books.db' database, if you want it to work with a different database make sure to change that database name in a sqlite3.connect,
    keep in mind that new database should have same table name and tab names in order for function to work, if you use other database than sqlite3,
    further corrrections to the sql code and program might be needed. function also uses dependent cursor_strip function
    you will need to copy or import if you use this function outside of the program.

    function takes no arguments
    """
    choice = input("what book do you like?: ")
    conn = sqlite3.connect("books.db")                                      #would be better in a try block...
    cur = conn.cursor()
    author = cur.execute(f"SELECT author FROM books WHERE book='{choice}'") #uses F string to insert user input in a database and select an author
    strip_author = cursor_strip(author)                                     #turns the list of tuples returned by the execute method into a string
    cur.execute(f"SELECT book FROM books WHERE author='{strip_author}'")    #inserts that string into database to select all the books from the same author
    booklist = cur.fetchall()                                               #returns the list of touples containing books from the same author
    result = cursor_strip(booklist)                                         #turns list of touples of books from same author into a string
    print("perhaps you would be interested in these books from the same author:\n" + result)


#next we create a function that will recomend best rated books from the same genre

def recomend_best_from_genre():
    """
    this function is designed to recomend best books from the same genre, provided that user enters the name of the book as an input, function works
    by defalt with a built in 'books.db' database, if you want it to work with a different database make sure to change that database name in a sqlite3.connect,
    keep in mind that new database should have same table name and tab names in order for function to work, if you use other database than sqlite3,
    further corrrections to the sql code and program might be needed. function also uses dependent cursor_strip function
    you will need to copy or import if you use this function outside of the program.

    function takes no arguments
    """
    choice = input("what book do you like?: ")
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    genre = cur.execute(f"SELECT genre FROM books WHERE book='{choice}'")
    strip_genre = cursor_strip(genre)
    cur.execute(f"SELECT book FROM books WHERE genre='{strip_genre}' AND rating='8' OR rating='9' OR rating='10'")  #you can change the sql code to include books with lower rating
    booklist = cur.fetchall()
    result = cursor_strip(booklist)

    print("perhaps you would be interested in best rated books from the same genre:\n" + result)

#this is basicaly a heart of our program, this function will select one of two recomender fucntions based on user input.
def book_recomender():
    """
    this function is used to direct user to the recomend_by_author() or recomend_best_from_genre() functions based on what he preffers, 
    or terminate the program, its basicaly a simple whileloop that checks for user input with if/elif/else statements.

    function takes no arguments
    """
    print("Welcome to my book recomender program! Would you like to recomend you books by the same author,\nor best books from the same genre?\n")
    user_input = None
    while user_input != 'q':
        user_input = input("type 'author' to recomend books by author or 'genre' to recomend books by genre or type 'q' to quit: ").lower() #.lower() because uppercase input wouldnt otherwise terminate the program or run other functions
        if user_input == "author":
            recomend_by_author()
        elif user_input == "genre":
            recomend_best_from_genre()
        elif user_input == 'q':          #if user inputs 'q' terminate the program
            break
        else:                            #if input doesnt match any if elif statement, its an invalid input. notify user and repeat function
            print("invalid input, try again!")
        continue

if __name__ == "__main__":
    #if you are runing program for the first time, uncomment the create_database() function, for consecutive runs you should comment it again
    #it basicaly just creates the database used by the program
    #create_database()
    book_recomender()
