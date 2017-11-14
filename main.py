import json
username = input("Please enter your username: ")
password = hash(input("Please enter your password: "))

f = open('database.json', 'r')
data = f.read()
jsondata = json.loads(data)

def lookup(un, hashedpass):
    #this function looks in the dictionary to see if username
    #is registered in the program
    if(un not in jsondata):
        #write the username plus hashed password to the database
        w = {un: hashedpass}
        with open('database.json', 'w') as outfile:
            jsondata.update(w)
            json.dump(jsondata, outfile)
        print("new user registered in the database")
    else:
        authenticate(un, hashedpass)

def authenticate(user, code):
    #this function looks if the hashed password equals username value
    if(jsondata[user] == code):
        print("login succesful")
    else:
        print("fail")
lookup(username, password)

def attack(mess):
    start = 0
    #number of times to iterate through trying different brute force options
    #this is not a good way of doing it but it works as an example
    for i in range(10000000):
        #print(hash(start))
        if(hash(str(start)) == mess):
            print("found")
            return(start)
        else:
            start+= 1

    #this function takes a given hashed password and then cracks it
print(jsondata[username])
print(attack(jsondata[username]))

