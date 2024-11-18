import psycopg2 as sql


db = sql.connect(
    database = 'test',
    host = 'localhost',
    user = 'postgres',
    password = '123456'
)


cursor = db.cursor()

cursor.execute(
    '''
        create table if not exists students(
            id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
            name varchar(100),
            age int check(age > 0),
            grade int check(grade > 0)
        );
        
        
        insert into students (name , age , grade)
        values
        ('Ali', 21 , 85),
        ('Vali', 22 , 90),
        ('Oleg', 20 , 75);
        
        select age , grade from students where age > 21;
        
        
        update students
        set grade = 90
        where name = 'Ali';
        
        
        delete from students
        where grade > 90;
        
        
        alter table students
        add column email varchar(100);
        
        
        drop table students;
        
        
        create table if not exists courses(
            id int primary key,
            student_id int ,
            course_name varchar(100)
        );
        
        
        select students.name, courses.course_name
        from students
        join courses on students.course_id = courses.id;
    '''
)


db.commit()
db.close()