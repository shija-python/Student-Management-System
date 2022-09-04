import sqlite3

#Backend

def studentData():
    con = sqlite3.connect("student.db")
    cur = con.cursor
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text, Surname text , DOB text, \
    Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()

    def addStdRec():
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?,?,?,?,?,?)", \
        (StdID, Firstname,Surname,DoB,Age,Gender, Address, Mobile))
        con.commit()
        con.close()

    def viewData():
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM student")
        row = cur.fetchall()
        con.close()
        return rows

    def deleteRec():
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("DELETE  FROM student WHERE id=?", (id,))
        con.commit()
        con.close()

    studentData()