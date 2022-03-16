# CH 15: INTRO TO STRUCTURED QUERY LANGUAGE

# STEP 2: adding data to the table
import sqlite3
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Umbrella', 53))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)', ('Dos Orugitas', 20))
# commit used to force data entry
conn.commit()
print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
# Deletion rational: 'so the program can repeat'. Don't fully understand what this means
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()
cur.close()
quit()

# STEP 1: creating the table
import sqlite3
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
conn.close()
quit()





# CH 14: INTRO TO OBJECT-ORIENTED PROGRAMMING


# making my own class of objects
class Dog:

    def bark(self, x):
        sound = 'Bow-wow! '
        x = int(x)
        bark = sound*x
        return bark

chihuahua = Dog()
print(type(chihuahua))
print(dir(chihuahua))
chihuahua.bark(4)

havanese_poodle = Dog()
print('My Havanese-Poodle says:', havanese_poodle.bark(8))