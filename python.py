running=True
while running:
    import mysql.connector
    conn = mysql.connector.connect(host = "localhost", user = "root",password = "newpass123",database ="result_project")
    cursor = conn.cursor()

    # ADDING STUDENT
    
    def add ():
        std_id = int(input("Enter the std_id:"))
        n = input("Enter the name of student:")
        c = input("Enter the class of student:")
        r = int(input("Enter the roll_no :"))
        ct = input("Enter the city:")
        
        cursor.execute(f"insert into student values({std_id},'{n}','{c}',{r},'{ct}');")
        conn.commit()
        print("\nStudent Added Succesfully\n")
        cursor.close()
        conn.close()

    # ENTERING MARKS

    def marks():
        std_id = int(input("Enter the std_id:"))
        sub = ["English","Maths","Hindi","Science","Social_Science"]
        for s in sub:
            cursor.execute(f"select subject_id from subject where subject_name = '{s}';")
            sub_id=cursor.fetchone()[0]
            m = int(input(f"Enter marks for {s}: "))
            cursor.execute(f"insert into marks (std_id,subject_id,marks) values({std_id},{sub_id},{m});")
            conn.commit()
        print("\nMarks entered successfully\n")
        cursor.close()
        conn.close()

    # GENERATING RESULT

    def result():
        std_id = int(input("Enter the std_id to generate the result:"))
        cursor.execute(f"select sum(marks) from marks group by (std_id) having std_id = {std_id};")
        total = cursor.fetchone()
        t1,=total
        avg=t1/5
        if avg>=85:
            grade="A"
        elif avg >= 75 and avg < 85:
            grade="B"
        elif avg >= 60 and avg < 75:
            grade="C"
        elif avg >= 45 and avg < 60:
            grade="D"
        elif avg >= 33 and avg < 45:
            grade="E"
        else:
            grade="F"
        cursor.execute(f"insert into result values ({std_id},{t1},{avg},'{grade}');")
        conn.commit()
        print("\nResult Generated Succesfully\n")
        cursor.close()
        conn.close()
        
    # SHOW RESULT

    def show():
        std_id=int(input("Enter the student id: "))
        cursor.execute(f"select s.std_id,s.name,r.total,r.percentage,r.grade from student s left join result r on s.std_id=r.std_id where s.std_id = {std_id};")
        result=cursor.fetchone()
        sid,name,total,page,grade=result
        print(f"\nStudent ID : {sid}\nStudent Name : {name}\nTotal Marks : {total}\nPercentage : {page}%\nGrade : {grade}\n")
        cursor.close()
        conn.close()

    # TOPPERS LIST
        
    def toppers():
        top=int(input("Enter the number of toppers: "))
        query=f"select s.name from student s left join result r on s.std_id=r.std_id order by total desc limit {top};"
        cursor.execute(query)
        result=cursor.fetchall()
        print(f"\nToppers list (Top {top})")
        for r in result:
            x,=r
            print(x)
        print()
        cursor.close()
        conn.close()

    # UPDATE DATA

    def update():
        while True:
            choice=int(input("\n1 Update Student Data\n2 Update Marks\n3 Result Update\n0 Go Back\nEnter Choice: "))
            match choice:
                case 1:
                    std_id=int(input("Enter the student ID: "))
                    def student_update():
                        choice=int(input("\n1 Update Name\n2 Update Class\n3 Update Roll No.\n4 Update City\n0 Go Back\nEnter Your Choice: "))
                        match choice:
                            case 1:
                                name=input("Enter the name: ")
                                cursor.execute(f"Update students set name = '{name}' where student_id = {std_id};")
                                conn.commit()
                                print("\nName Updated")
                                student_update()
                            case 2:
                                cls=input("Enter the class: ")
                                cursor.execute(f"Update students set class_name = '{cls}' where student_id = {std_id};")
                                conn.commit()
                                print("\nClass Updated")
                                student_update()
                            case 3:
                                rn=int(input("Enter the roll number: "))
                                cursor.execute(f"Update students set roll_no = {rn} where student_id = {std_id};")
                                conn.commit()
                                print("\nRoll No. Updated")
                                student_update()
                            case 4:
                                ct=input("Enter the city: ")
                                cursor.execute(f"Update students set city = '{ct}' where student_id = {std_id};")
                                conn.commit()
                                print("\nCity Updated")
                                student_update()
                            case 0:
                                print("\nGoing Back")
                            case _:
                                print("\nInvalid Input")
                                student_update()
                    student_update()

                case 2:
                    std_id=int(input("Enter the student ID: "))
                    def marks_update():
                        choice=int(input("\nSubjects:\n1 English\n2 Hindi\n3 Maths\n4 Science\n5 Social Science\n0 Go Back\nEnter your choice: "))
                        match choice:
                            case 1:
                                cursor.execute("select subject_id from subjects where subject_name = 'English';")
                                sub_id=cursor.fetchone()[0]
                                m = int(input(f"Enter marks for English: "))
                                cursor.execute(f"update marks set marks = {m} where student_id = {std_id} and subject_id = '{sub_id}';")
                                conn.commit()
                                print("\nMarks Update")
                                marks_update()
                            case 2:
                                cursor.execute("select subject_id from subjects where subject_name = 'Hindi';")
                                sub_id=cursor.fetchone()[0]
                                m = int(input(f"Enter marks for Hindi: "))
                                cursor.execute(f"update marks set marks = {m} where student_id = {std_id} and subject_id = '{sub_id}';")
                                conn.commit()
                                print("\nMarks Update")
                                marks_update()
                            case 3:
                                cursor.execute("select subject_id from subjects where subject_name = 'Maths';")
                                sub_id=cursor.fetchone()[0]
                                m = int(input(f"Enter marks for Maths: "))
                                cursor.execute(f"update marks set marks = {m} where student_id = {std_id} and subject_id = '{sub_id}';")
                                conn.commit()
                                print("\nMarks Update")
                                marks_update()
                            case 4:
                                cursor.execute("select subject_id from subjects where subject_name = 'Science';")
                                sub_id=cursor.fetchone()[0]
                                m = int(input(f"Enter marks for Science: "))
                                cursor.execute(f"update marks set marks = {m} where student_id = {std_id} and subject_id = '{sub_id}';")
                                conn.commit()
                                print("\nMarks Update")
                                marks_update()
                            case 5:
                                cursor.execute("select subject_id from subjects where subject_name = 'Social_Science';")
                                sub_id=cursor.fetchone()[0]
                                m = int(input(f"Enter marks for Social_Science: "))
                                cursor.execute(f"update marks set marks = {m} where student_id = {std_id} and subject_id = '{sub_id}';")
                                conn.commit()
                                print("\nMarks Updated")
                                marks_update()
                            case 0:
                                print("\nGoing Back")
                            case _:
                                print("\nInvalid Input")
                                marks_update()
                    marks_update()
                case 3:
                    def result_update():
                        std_id = int(input("Enter the std_id to update the result:"))
                        cursor.execute(f"select sum(marks) from marks group by (student_id) having student_id = {std_id};")
                        total = cursor.fetchone()[0]
                        avg=total/5
                        if avg>=85:
                            grade="A"
                        elif avg >= 75 and avg < 85:
                            grade="B"
                        elif avg >= 60 and avg < 75:
                            grade="C"
                        elif avg >= 45 and avg < 60:
                            grade="D"
                        elif avg >= 33 and avg < 45:
                            grade="E"
                        else:
                            grade="F"
                        cursor.execute(f"update result set total = {total}, percentage = {avg},grade ='{grade}' where student_id = {std_id};")
                        conn.commit()
                        print("\nResult Updated Succesfully")
                    result_update()
                case 0:
                    print("\nGoing Back")
                    cursor.close()
                    conn.close()
                    break

                case _:
                    print("\nInvalid Input")

    choice=int(input("1 Add Student\n2 Enter Marks\n3 Generate Result\n4 Show Results\n5 Topper List\n6 Exit\nEnter your choice: "))
    match choice:
        case 1:
            add()
        case 2:
            marks()
        case 3:
            result()
        case 4:
            show()
        case 5:
            toppers()
        case 6:
            update()
        case 7:
            print("GOODBYE")
            cursor.close()
            conn.close()
            running=False
        case _:
            print("INVALID INPUT, TRY AGAIN")