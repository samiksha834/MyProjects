from dbconfig1 import *


def callAdmin():
    while (True):
        print("1.Add Theater")
        print("2.Add Movie")
        print("3.Add Screening")
        print("4.Modify Screening")
        print("5.Seat Management")
        print("6.View Reservation Details")
        print("7.Logout")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            tname = input("Enter theater name:")
            loc = input("Enter location:")
            mycursor.execute(
                "insert into theater(title, location) values ('{}', '{}')".format(
                    tname, loc))
            mydb1.commit()
            print("Theater added!!")
        elif ch == 2:
            nme = input("Enter Movie name:")
            dur = int(input("Enter duration of the movie in minute format:"))
            prc=int(input("Enter Price of the movie:"))
            mycursor.execute("select * from theater")
            th_all = mycursor.fetchall()
            for i in th_all:
                print(i[0], i[1])
            thid=int(input("Enter theater id to add movie to that theater:"))
            mycursor.execute(
                "insert into moviee(title, duration_min, theater_id, price) values ('{}', '{}', '{}','{}')".format(
                    nme, dur, thid, prc))
            mydb1.commit()
            print("Movie added!!")
        elif ch == 3:
            name = input("Enter name of the screen:")
            tseat = int(input("Enter total number of seats in the screen:"))
            tid=int(input("Enter theater id for this screen:"))
            aseat=tseat
            mycursor.execute(
                "insert into auditorium(name, seatno, theat_id,avalseat) values ('{}', '{}', '{}','{}')".format(
                    name, tseat, tid, aseat))
            mydb1.commit()
            print("Screening added!!")
        elif ch == 4:
            mycursor.execute("select distinct * from moviee")
            mov_all = mycursor.fetchall()
            print("S.no", "Name", "Duration")
            for i in mov_all:
                print("---------------")
                print(i[0], i[1], i[2])
                print("---------------")

            mid = int(input("Enter movie id to set movie to this screen:"))

            mycursor.execute("select * from auditorium")
            aud_all = mycursor.fetchall()
            for i in aud_all:
                print("---------")
                print(i[0], i[1])
                print("---------")
            aid = int(input("Enter auditorium id to add movie to the screen:"))
            sst = int(input("Enter the timestamp for the movie in format(yyyymmddhhmmss):"))
            print("Screening details added!!!")
            mycursor.execute(
                "insert into screening(movie_id, auditorium_id, screening_start)values('{}','{}',{})".format(
                    mid, aid, sst))
            mydb1.commit()
        elif ch == 5:
            mycursor.execute("select * from auditorium")
            mov_all = mycursor.fetchall()
            print("S.no", "Name", "Seats")
            for i in mov_all:
                print("---------------")
                print(i[0], i[1], i[2])
                print("---------------")
            aud=int(input("Enter auditorium id:"))
            rw=int(input("Enter row number:"))
            n=int(input("How many seats do you want to add to this row:"))
            for i in range(n):
                in1 = input("Enter the seatid (A to J) for this row:")
                mycursor.execute(
                    "insert into seat(row, seatnumber, auditorium_id)values('{}','{}',{})".format(
                        rw, in1, aud))
                mydb1.commit()
            print("Seats Successfully Added!!!")

        elif ch == 6:
            mycursor.execute("select * from reservation")
            mov_all = mycursor.fetchall()
            print("S.no", "Screening id", "Reserved","TotalSeatsBooked", "Price","UserID")
            for i in mov_all:
                print(i[0], i[1], i[2],i[3],i[4],i[5])

        elif ch == 7:
            break


def callUser():
    while (True):
        print("1.View Theater List")
        print("2.View Movie List")
        print("3.Search Theater By Location")
        print("4.Search Movie By Theater")
        print("5.Book Ticket Reservation")
        print("6.Logout")
        ch = int(input("Enter your choice:"))
        if ch==1:
            mycursor.execute("select * from theater")
            mov_all = mycursor.fetchall()
            print("S.no", "Name", "Location")
            for i in mov_all:
                print("---------------")
                print(i[0], i[1], i[2])
                print("---------------")
        elif ch==2:
            mycursor.execute("select * from moviee")
            mov_all = mycursor.fetchall()
            print("Name", "Duration")
            for i in mov_all:
                print("---------------")
                print(i[1], i[2])
                print("---------------")
        elif ch==3:
            loc=input("Enter location:")
            mycursor.execute("select * from theater where location='{}'".format(loc))
            mov_all = mycursor.fetchall()
            print("S.no", "Name")
            for i in mov_all:
                print("------------------------")
                print(i[0], i[1])
                print("------------------------")
        elif ch==4:
            mov=input("Enter name of the movie:")
            mycursor.execute("select * from theater where tid IN(select theater_id from moviee where title='{}')".format(mov))
            mov_all = mycursor.fetchall()
            print("S.no", "Name", )
            for i in mov_all:
                print("--------------------")
                print(i[0], i[1])
                print("--------------------")

        elif ch==5:
            mycursor.execute("select * from user_profile where role='User'")
            usd = mycursor.fetchall()
            for i in usd:
                print(i[0], i[3])
            idd = int(input("Select your user id from the user details given above:"))

            mov = input("Enter name of the movie:")
            mycursor.execute("select * from theater where tid in(select theater_id from moviee where title='{}')".format(mov))
            mov_all = mycursor.fetchall()
            print("Movies are screening at following theaters:")
            for i in mov_all:
                print("------------------------")
                print(i[0], i[1])
                print("------------------------")

            ti=int(input("Select theater id:"))
            mycursor.execute("select * from auditorium where theat_id='{}'".format(ti))
            mov_all = mycursor.fetchall()
            print("Screens available at this are:")
            print("S.no", "Name", "Total Seats")
            for i in mov_all:
                print("---------------")
                print(i[0], i[1], i[2])
                print("---------------")

            sc=int(input("Enter Screen Id:"))
            mycursor.execute("select avalseat from auditorium where aid='{}'".format(sc))
            a = mycursor.fetchone()
            print("Available seats are:", list(a))
            n = int(input("Enter number of seats you want to book:"))
            mycursor.execute("select * from seat where auditorium_id='{}'".format(sc))
            mov_all = mycursor.fetchall()
            print("Row", "Seat No.")
            for i in mov_all:
                if i[4]==None:
                    print(i[0], i[1], i[2])

            for i in range(n):
                id1=int(input("Select seat id to book the seat:"))
                mycursor.execute("update seat set STATUS='B' where id = {}".format(id1))
                mydb1.commit()
                mycursor.execute("update auditorium set avalseat=avalseat-1 where theat_id='{}'".format(ti))
                mydb1.commit()
            print("Seats Booked!!")

            mycursor.execute("select price from moviee where title='{}'".format(mov))
            movie = mycursor.fetchone()
            x=movie[0]
            price=n*x
            print("--------------RECEIPT--------------")
            print("Movie Booked at theater id:",ti)
            print("Movie Screening at Screen id:",sc)
            print("Total number of tickets booked:",n)
            print("Total price for {} tickets is :{}".format(n,price))
            print("-----------------------------------")


            mycursor.execute(
                "insert into reservation(screening_id,reserved,tseatsb,amount,user_id) values('{}','Y','{}','{}','{}')".format(sc,n,price,idd))
            mydb1.commit()


        elif ch==6:
            break


while(True):
    print("Hi, Welcome to online movie ticket booking!!")
    print("1.Register")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        nm = input("Enter your name:")
        unm = input("Enter your username:")
        pwd = input("Enter your password")
        em = input("Enter your email id:")
        pno = int(input("Enter your phone number:"))

        mycursor.execute(
            "insert into user_profile(username,password,name,email,mob_no, role) values ('{}', '{}', '{}', '{}', '{}', "
            "'User')".format(
                unm, pwd, nm, em, pno))
        mydb1.commit()
        print("User Added!")

    elif ch == 2:
        un = input("Enter UserName: ")
        pwd = input("Enter Password: ")

        mycursor.execute("select * from user_profile where username='{}' and password='{}'".format(un, pwd))
        data = mycursor.fetchone()

        if data:
            print("=====Welcome {}======".format(data[3]))
            if data[6] == 'Admin':
                callAdmin()
            elif data[6] == "User":
                callUser()
        else:
            print("Invalid Username or Password!")

    elif ch==3:
        break
