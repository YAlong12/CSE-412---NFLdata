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
def addplayedFor():

    mycursor = conn.cursor()

    print('------ Add Data to playedFor Table ------\n')

    ID = int(input('Enter ID: '))
    spID = int(input('Enter sports person ID: '))
    weight = float(input('Enter player weight: '))
    salary = float(input('Enter player salary: '))

    sql = 'INSERT INTO playedFor ("ID", "spID", "weight", "salary") VALUES (%s, %s, %s, %s)'
    val = (ID, spID, weight, salary)
    mycursor.execute(sql,val)
    conn.commit()
    print('------ SUCCESS ------\n')
    exit()
    
def selectPlayedfor():

    mycursor = conn.cursor()

    print('------ Select Data from playedfor Table ------\n')

    try:
        sql = 'SELECT * FROM playedfor'
        mycursor.execute(sql)

        rows = mycursor.fetchall()

        if rows:
            print("ID\tspID\tWeight\tSalary")
            for row in rows:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
        else:
            print("Not found in playedFor table")

    except psycopg2.Error as e:
        print(f'Error: {e}')
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
def addAward():
    mycursor = conn.cursor()

    print('------ Add Data to award Table ------\n')

    organizationName = input('Enter organization name: ')
    spID = int(input('Enter sports person ID: '))

    sql = 'INSERT INTO award ("organizationName", "spID") VALUES (%s, %s)'
    val = (organizationName, spID)
    mycursor.execute(sql, val)
    conn.commit()
    print('------ SUCCESS: Data added to award Table ------\n')
    exit()

def selectAward():

    mycursor = conn.cursor()

    print('------ Select Data from award Table ------\n')

    try:
        sql = 'SELECT * FROM award'
        mycursor.execute(sql)

        rows = mycursor.fetchall()

        if rows:
            print("OrganizationName\tspID")
            for row in rows:
                print(f"{row[0]}\t\t{row[1]}")
        else:
            print("Not found in award table")

    except psycopg2.Error as e:
        print(f'Error: {e}')
    exit()
    
def addOrganization():

    mycursor = conn.cursor()

    print('------ Add Data to organization Table ------\n')

    orgID = int(input('Enter organization ID: '))
    name = input('Enter organization name: ')

    sql = 'INSERT INTO organization ("orgID", "name") VALUES (%s, %s)'
    val = (orgID, name)
    mycursor.execute(sql, val)
    conn.commit()
    print('------ SUCCESS------\n')
    exit()
    
def selectOrganization():

    mycursor = conn.cursor()

    print('------ Select Data from organization Table ------\n')

    try:
        sql = 'SELECT * FROM organization'
        mycursor.execute(sql)

        rows = mycursor.fetchall()

        if rows:
            print("orgID\tname")
            for row in rows:
                print(f"{row[0]}\t{row[1]}")
        else:
            print("Not found in organization table")

    except psycopg2.Error as e:
        print(f'Error: {e}')
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
