from datetime import datetime
import os
import booklog
import friends
import habits
import profile
import virtues
import achievements
import spec
import task
import journal
import schedule


date = ["th", "st" , "nd", "rd"]
estime =["1-10 minutes", "10-30 minutes","30-60 minutes", "1-2 hours","2-4 hours", "4+ hours"]
months = ["Unknown", "January", "Febuary", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]
now = datetime.now()
month = (months[now.month])
day = (now.day)
suffix = ""
newtasks = ""
moral = ""
curdate = now.strftime("%m" +"/"+ "%d"+ "/" + "%Y")

def diff_dates(curdate, deadline):
    return abs(deadline-curdate).days

def calculateRemainingDays():
    d1 = date(deadline[0:3],deadline[5:6],deadline[7:8])
    d2 = date(now.year,now.month, now.date)
    result1 = diff_dates(d2, d1)


def printTasks():
	with open("savefiles/test.txt", "r") as file:
		data2 = eval(file.readline())
	tasklist=data2
	#print(tasklist)

	print("|          Current Task            | IMP | URG |  TIME  | DDL (dd/mm/yyyy)|     STATUS    | PROD | ETC |")
	print(" =================================== ===== ===== ======= =================== ============== ===== =====")
	i = 1
	for line in tasklist:
		#str(i)
		if(line.get("status") != "COMPLETE"):
			print(str(tasklist.index(line) + 1) +".",line.get("task")," "*(30-len(line.get("task"))),"|","",line.get("importance")+" "*(3-len(line.get("importance")))+"|","",line.get("urgency")+" "*(3-len(line.get("urgency")))+"|",line.get("estime")+" "*(6-len(line.get("estime")))+" |"," ",line.get("deadline")+"  "*(12-len(line.get("deadline")))+"|","  ",line.get("status")+" "*(11-len(line.get("status"))) + "| " + line.get("production") + " "*(5-len(line.get("production"))) + "| " + str(line.get("daysleft")) +line.get("subtasks") + "")
			i +=1

	print("")

def sorttasklist():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Things to do: \n -----------------------------------------------------------------------------------------")
	newlist = sorted(tasklist, key=itemgetter('estime'), reverse=False)
	i=1
	#print(newlist)
	print("|          Current Task             | IMP | URG |    EST   | DDL (dd/mm/yy) |     STATUS    | ")
	print(" =================================== ===== ===== =========== ================ ===============")
	for line in newlist:
		print(str(i) +".",line.get("task")," "*(31-len(line.get("task"))),"|","",line.get("importance")+" "*(3-len(line.get("importance")))+"|","",line.get("urgency")+" "*(3-len(line.get("urgency")))+"|","  ",line.get("estime")+" "*(6-len(line.get("estime")))+"|","  ",line.get("deadline")+" "*(12-len(line.get("deadline")))+"|","  ",line.get("status")+" "*(11-len(line.get("status"))) + "|" + line.get("production"))
		i +=1
	print("")
	#printTasks()

def opening():
	os.system('cls' if os.name == 'nt' else 'clear')
	#testmodule.printTestModule()
	with open("savefiles/test.txt", "r") as file:
		data2 = eval(file.readline())
	tasklist=data2
	#print(tasklist)
	if 4 <= day <= 20 or 24 <= day <= 30:
		suffix = "th"
	else:
		suffix = ["st", "nd", "rd"][day % 10 - 1]
	print("==========================================================")
	print("-----(C)-WATERBUFFALO MICROMANAGEMENT SYSTEM-(C)-2018-----")
	print("==========================================================")
	print("Welcome to your To-Do list! \nThe current date is: " + now.strftime("%d" +suffix +" "+ month+" %Y | %H:%M")+"\n")
	if(len(tasklist) == 0):
		print("Your list is currently empty")
		print("")
	else:
		print("Things to do: \n ----------------------------------------------------------------------------------------")
		printTasks()
	print("What do you want to do today? \n")
	print("1 - Create a task ")
	print("2 - Delete a task")
	print("3 - Mark a task complete")
	print("4 - Change sorting algorithm")
	print("5 - Save tasks")
	print("6 - Import tasks")
	print("7 - View done tasks")
	print("")
	#switchViews()
	#todo = input("\n")


def changeSA():
	algorithm = input("What sorting algorithm would you like to use? (FIFO, SJF, PS, EDF, RR)")
	if(algorithm == "FIFO"):
		print("The scheduling algorithm will remain on FIFO")
	if(algorithm == "SJF"):
		sortingalgorithm = "SJF"
		sorttasklist()

def markComplete():
	with open("savefiles/test.txt", "r") as file:
		data2 = eval(file.readline())
	tasklist=data2

	os.system('cls' if os.name == 'nt' else 'clear')
	printTasks()
	print("COMPLETE A TASK")
	print("==============")
	mark = input("which task do you want to mark as complete?\n")
	tasklist[int(mark)-1]["status"] = "COMPLETE"
#	print(tasklist)

	with open("savefiles/test.txt", "w") as file:
		file.write(str(tasklist))
	
	#printTasks()
	start3()

def deleteTask():
	with open("savefiles/test.txt", "r") as file:
		data2 = eval(file.readline())
	tasklist=data2

	os.system('cls' if os.name == 'nt' else 'clear')
	printTasks()
	print("DELETE A TASK")
	print("==============")
	delete= input("which task would you like to delete\n")
#	print("Are you sure you want to delete task" + delete + str(tasklist.get(delete)+"?")
	del tasklist[int(delete) - 1]
	os.system('cls' if os.name == 'nt' else 'clear')
	with open("savefiles/test.txt", "w") as file:
		file.write(str(tasklist))
#	printtasks()
	start3()
	#start3()

def addSubTasks(subtasks):
	finaltasks = ""
	while(subtasks == "Y" or subtasks =="y"):
		stasks = input("what do you want to add as your subtasks?")
		finaltasks +="\n   - " + stasks
		subtasks = input("do you want to add a new task?")
		if(subtasks == "n"):
			break
	return finaltasks

def createTask():
	with open("savefiles/test.txt", "r") as file:
		data2 = eval(file.readline())
	tasklist=data2
	os.system('cls' if os.name == 'nt' else 'clear')
	printTasks()
	print("")
	print("CREATE A TASK")
	print("==============")
	#print("\nAdding a task:")
	task = input("What is the name of the task you would like to add? \n")
	while True:
		#try:
		importance: str = input("How important is this task? (L) Low, (M) Medium, (H) High, (H!) Highest \n").upper()
			#if (importance == "L" or importance == "M" or importance == "H" or importance == "H!"):
			#	print("valid input")
			#else:
			#	print("invalid output")
			#continue
		urgency = input("How urgent is this task?").upper()
		estime = input("How long do you think this task will take? (mins)\n")
		deadline = input("What is the deadline (dd/mm/yyyy) \n")
		pdeadline = datetime.strptime(deadline, "%d/%m/%Y")
		print("pdeadline: " +str(pdeadline))
		d2 = datetime(now.year, now.month, now.day)
		print("currdate: " + str(d2))
		#pdeadline = date(deadline[:3],deadline[5:6],deadline[7:8])

		daynumber = abs(pdeadline-d2).days
		print(daynumber)

		status = input("what is the status?  (PENDING, IN-PROG)\n")
		production = input("how productive do you think you have been?")

		subtasks = input("do you want to add a new task?")
		stasks = addSubTasks(subtasks)


		break
		#except:
		#	print("try valid")
	#prioity = "some calculation of importance, urgency and estimated time"
	#"subtasks" : subtasks
#	collectTasks(newtasks)
	#subtasks = newtasks
	comb = {"task": task, "importance": importance, "urgency": urgency, "estime": estime, "deadline": deadline, "status" : status, "production" : production, "subtasks": stasks, "daysleft" : daynumber}
	print(comb)
#	"task": "6", "importance": "L", "estime": "15", "deadline": deadline
	tasklist.append(dict(comb))
	copytasklist= tasklist
#	os.system('cls' if os.name == 'nt' else 'clear')
	with open("savefiles/test.txt", "w") as file:
		file.write(str(copytasklist))
	start3()
	
def viewDoneTasks():
	os.system('cls' if os.name == 'nt' else 'clear')
	with open("savefiles/test.txt", "r") as file:
		data2 = eval(file.readline())
	tasklist=data2
	#print(tasklist)

	print("|          Current Task             | IMP | URG |  TIME  | DDL (yyyy/mm/dd)|     STATUS    | PROD | ETC |")
	print(" =================================== ===== ===== ======= =================== ============== ======= =====")
	i = 1
	for line in tasklist:
		if(line.get("status") == "COMPLETE"):
			#str(i)
			print(str(tasklist.index(line) + 1),line.get("task")," "*(30-len(line.get("task"))),"|","",line.get("importance")+" "*(3-len(line.get("importance")))+"|","",line.get("urgency")+" "*(3-len(line.get("urgency")))+"|",line.get("estime")+" "*(4-len(line.get("estime")))+" |"," ",line.get("deadline")+"  "*(12-len(line.get("deadline")))+"|","  ",line.get("status")+" "*(11-len(line.get("status"))) + "| " + line.get("production") + " "*(4-len(line.get("production"))) + "| " + str(line.get("daysleft")) +line.get("subtasks") + "")
			i +=1
	print("")
	
def switchViewsMany():
	print("Switch views")
	print(" (A)chievements log | (D)iet Planner   |")
	print(" (H)abits tracker   | (F)riends        | (T)odo")
	print(" (J)ournal          | (P)rofile")
	todo = input("what do you want to do?")
	if(todo == "b" or todo == "B"):
		booklog.booklog()
		switchViewsMany()
	if(todo == "j" or todo == "J"):
		journal.Journal()
	if(todo == "f" or todo =="F"):
		friends.viewFriends()
		
	if(todo == "p" or todo == "P"):
		profile.personalProfile()
		switchViewsMany()
	if(todo == "v" or todo == "V"):
		virtues.virtues()
		switchViewsMany()
	if(todo == "H" or todo == "h"):
		habits.habittracker()
		switchViewsMany()
	if(todo == "a" or todo == "A"):
		achievements.getAchievements()
		switchViewsMany()
	if(todo == "spec" or todo == "SPEC"):
		spec.specification()
		switchViewsMany()
	if(todo == "T" or todo == "t"):
		start3()
		
def switchViews():
	print("")
	print("Switch views")
	print(" (A)chievements log | (D)iet Planner   | Schedule")
	print(" (H)abits tracker   | (F)riends        | (T)odo")
	print(" (J)ournal          | (P)rofile        |")
	todo = input("what do you want to do?")
	if(todo == "b" or todo == "B"):
		booklog.booklog()
		switchViewsMany()
	if(todo == "j" or todo == "J"):
		journal.Journal()
	if(todo == "f" or todo =="F"):
		friends.viewFriends()
		switchViewsMany()
	if(todo == "p" or todo == "P"):
		profile.personalProfile()
		switchViewsMany()
	if(todo == "v" or todo == "V"):
		virtues.virtues()
		switchViewsMany()
	if(todo == "H" or todo == "h"):
		habits.habittracker()
		switchViewsMany()
	if(todo == "a" or todo == "A"):
		achievements.getAchievements()
		switchViewsMany()
	if(todo == "spec" or todo == "SPEC"):
		spec.specification()
		switchViewsMany()
	if(todo == "T" or todo == "t"):
		start3()
	if(todo == "S" or todo == "s"):
		schedule.sched()
	# if(todo == "g" or todo == "G"):
		# goals()
	if(todo == "5"):
		writetxt()
	if(todo == "6"):
		readtxt()
	#Change scheduling algorithm (FIFO, SJF, PS, EDF, RR)
	if(todo == "4"):
		changeSA()
	#Mark complete
	if(todo == "3"):
		markComplete()
	#Delete a task
	if(todo =="2"):
		deleteTask()
	#Create a task
	if(todo == "1"):
		createTask()
	if(todo == "7"):
		viewDoneTasks()

def start3():
	opening()
	switchViews()
	todo = input("\n")