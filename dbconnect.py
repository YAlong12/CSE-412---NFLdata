import psycopg2
import datetime
import os

conn = psycopg2.connect(database = "nfldata", user= "malavikanair", host = 'localhost')
print("successfuhl")


#print(cursor.fetchall())
print("successfssuhl")

def initDB():
    cursor = conn.cursor()


def exit():
    n = int(input(" Press 5 to exit : "))

    if n == 5:
        os.system('clear')  # For Windows
        run()
    else:
        print(" Invalid Option")
        exit()

def getAllSportsPersons():
    
    cursor = conn.cursor()
    print('------ All Users ------\n')
    cursor.execute("SELECT * FROM sportsPerson")
    userList = cursor.fetchall()
    i = 0
    for user in userList:
        i += 1
        print(" ----- User ",i,"-----")
        print(" Name : ", user[1])
        print(" Birthday : ", user[2])
        print(" College : ", user[3])
        print("\n")
    print('------ SUCCESS ------\n')
    exit()

def getAllPlayers():
    
    cursor = conn.cursor()
    print('------ All Players ------\n')
    cursor.execute("SELECT * FROM Player Order by spid")
    userList = cursor.fetchall()
    i = 0
    for user in userList:
        i += 1
        print(" ----- spID ",user[0],"-----")
        print(" Position : ", user[2])
        print(" Weight : ", user[3])
        print("\n")
    print('------ SUCCESS ------\n')
    exit()

def addPlayer():

    mycursor = conn.cursor()

    print('------ Add a Player ------\n')

    spID = int(input ('Enter sports person ID: '))
    position =  input('Enter player position : ')
    weight = input('Enter player weight : ')

    sql = 'INSERT INTO sportsPerson ("spid","Picture","position","weight") VALUES (%s,%s,%s,%s)'
    val = (spID,None,position,weight)
    mycursor.execute(sql,val)
    conn.commit()

    #sql = 'SELECT * FROM SportsPerson WHERE spID=' +  str(spID)               
    #mycursor.execute(sql)
    #user = mycursor.fetchall()
    #print(" ----- User -----")
    #print(" Name : ", user[0][1])
    #print(" Birthday : ", user[0][2])
    #print(" College : ", user[0][3])
    #print("\n")

    print('------ SUCCESS ------\n')
    exit()

def addSportsPerson():

    mycursor = conn.cursor()

    print('------ Add a Player ------\n')

    spID = int(input ('Enter sports person ID: '))
    name =  input('Enter player name : ')
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    college = input('Enter player college : ')

    sql = 'INSERT INTO sportsPerson ("spid","name","birthday","college") VALUES (%s,%s,%s,%s)'
    val = (spID,name,date1,college)
    mycursor.execute(sql,val)
    conn.commit()

    #sql = 'SELECT * FROM SportsPerson WHERE spID=' +  str(spID)               
    #mycursor.execute(sql)
    #user = mycursor.fetchall()
    #print(" ----- User -----")
    #print(" Name : ", user[0][1])
    #print(" Birthday : ", user[0][2])
    #print(" College : ", user[0][3])
    #print("\n")

    print('------ SUCCESS ------\n')
    exit()

def getAllPlayersbyPosition():
    
    mycursor = conn.cursor()
    print('------ Get All Players by Position ------\n')
    n = input("Enter Position : ")
    sql = "Select sportsperson.name, sportsperson.college, player.position, player.weight From sportsPerson, Player where sportsperson.spId = player.spid and player.position='%s'" % n            
    mycursor.execute(sql)
    userList = mycursor.fetchall()

    if len(userList) == 0:
        print(" This position doesn't exist")
    else:
        i = 0
        for user in userList:
            i += 1
            print(" ----- Player -----")
            print(" Name : ", user[0])
            print(" College : ", user[1])
            print(" Position : ", user[2])
            print(" Weight : ", user[3])
            print("\n")

    print('------ SUCCESS ------\n')
    exit()

def displayMainMenu():
    print('------- MENU -------')
    print('  1. All Players ')
    print('  2. Add a Sports Person')
    print('  3. All Sports Persons')
    print('  4. Get Players by Position')
    print('  5. Exit')
    print('--------------------')    



def run():
    displayMainMenu()
    n = int(input("Enter option : "))
    if n == 1:
        os.system('clear')  # For Windows
        getAllPlayers()
    elif n == 2:
        os.system('clear')
        addSportsPerson()
    elif n == 3:
        os.system('clear')
        getAllSportsPersons()
    elif n == 4:
        os.system('clear')
        getAllPlayersbyPosition()
    elif n == 5:
        os.system('clear')
        print('----- Thank You -----')
    else:
        os.system('clear')
        run()

if __name__ == '__main__':
    initDB()
    run()