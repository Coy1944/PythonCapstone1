from re import I
import sqlite3
from golfing import Courses

conn = sqlite3.connect('course.db')

c = conn.cursor()

# c.execute("""CREATE TABLE courses (
#             name text,
#             location text,
#             cost integer
#             )""")


cor_1 = Courses('Sun River', 'St George', 60)
cor_2 = Courses('Dixie Red Hills', 'St George', 40)
cor_3 = Courses('Southgate', 'St George', 50)
cor_4 = Courses('Sky Mountain', 'Hurricane', 70)



# c.execute("INSERT INTO courses VALUES (?, ?, ?)", (cor_1.name, cor_1.location, cor_1.cost))
# c.execute("INSERT INTO courses VALUES (?, ?, ?)", (cor_2.name, cor_2.location, cor_2.cost))
# c.execute("INSERT INTO courses VALUES (?, ?, ?)", (cor_3.name, cor_3.location, cor_3.cost))
# c.execute("INSERT INTO courses VALUES (?, ?, ?)", (cor_4.name, cor_4.location, cor_4.cost))

insert into courses (rating_score, course_difficulty, course_location, name) values (3, 2, 888, 'green hills');
insert into courses (rating_score, course_difficulty, course_location, name) values (1, 1, 777, 'Sunbrook');
insert into courses (rating_score, course_difficulty, course_location, name) values (1, 1, 777, 'Sand Hollow');


# # # conn.commit()

c.execute("SELECT * FROM courses WHERE location=?", ('Washington',))

print(c.fetchall())


conn.commit()

conn.close()