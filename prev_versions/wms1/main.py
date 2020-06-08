import os
#import datetime
#from datetime import date
from datetime import datetime
#from dateutil.parser import parse
#import pandas as pd
from operator import itemgetter

#list containing months and dates
#FIFO - First-In, First Out
#SJF- (i.e. highest priotity to shortest task
#PS -Estimate priority using metrics and assign (preemptive and non-premptive)
#RR- (e.g. run tasks FIFO but preempt every 25 minutes)
#EDD - (sort tasks by earliest deadline)

months = ["Unknown", "January", "Febuary", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]
date = ["th", "st" , "nd", "rd"]
estime =["1-10 minutes", "10-30 minutes","30-60 minutes", "1-2 hours","2-4 hours", "4+ hours"]
now = datetime.now()
month = (months[now.month])
day = (now.day)
suffix = ""
newtasks = ""
moral = ""
curdate = now.strftime("%m" +"/"+ "%d"+ "/" + "%Y")

#print(estdate)

def diff_dates(curdate, deadline):
    return abs(deadline-curdate).days

def calculateRemainingDays():
    d1 = date(deadline[0:3],deadline[5:6],deadline[7:8])
    d2 = date(now.year,now.month, now.date)
  #  d2 = date(now.year, now.month, now.day)
    result1 = diff_dates(d2, d1)
  #  print('{} days between {} and {}'.format(result1, d1, d2))
  #  print("Happy programmer's day!")



tasklist = []
	#	{"task": "Write PPD", "importance": "H!", "urgency":"H!", "estime": "50", "deadline": "31/10/18", "status": "PENDING"},
		#{"task": "Join mastadon", "importance": "H", "urgency":"H!", "estime": "30", "deadline": "23/10/18", "status": "IN-PROG"},
	#	{"task": "Arrange a meetup with a friend","importance": "M", "urgency":"H!", "estime": "24", "deadline": "24/10/18", "status": "PENDING"},
		#{"task": "Add current time", "importance": "L", "estime": "43", "deadline": "01/11/18", "status": "PENDING"},
		#{"task": "Add todo/in-progress/complete", "importance": "L", "estime": "99", "deadline": "26/10/18","status": "PENDING"},
#	{"task": "3", "importance": "L", "estime": "1", "deadline": "21/10/18"},
	#{"task": "4", "importance": "L", "estime": "15", "deadline": "22/05/18"},
	#{"task": "5", "importance": "L", "estime": "15", "deadline": "14/05/18"},
	#{"task": "6", "importance": "L", "estime": "15", "deadline": "14/05/18"},
	#{"task": "7", "importance": "L", "urgency": "Y", "estime": 15}
#]

virtueslist = [
{"virtue":"Production", "definition" : " to work ceaselessly to create one's values.", "value": 1},
{"virtue":"Pride", "definition" : " Related to confidence and self-esteem.", "value": 1},
{"virtue":"Ambition", "definition" : " to pursue one's own goals and desires.", "value": 1},
{"virtue":"Self-restraint", "definition" : "Moderation or voluntary self-control.", "value": 1},
{"virtue":"Wisdom", "definition" : " Used as tools to navigate life", "value": 1},
{"virtue":"Order/Aesthetics", "definition" : "is the commitment to beauty and harmony", "value": 1},
{"virtue":"Integrity", "definition" : "Consistent application of reason.", "value": 1},
]

friendslist = [
{"friend":"Baljinder Bains", "Admiration": 10, "Affection": 10, "Enjoyment":10,"TimeKnown":10}
]

wellbeinglist = []
# goals =[
# {"goal" : "Cardiovascular Exercise", "reason" : "energy, health", "instantiation" : "3x running"},
# {"goal" : "Improve diet", "reason" : "health, energy", "instantiation" : "cook own meals, forgo sugar/sat fat/oil"},
# {"goal" : "Resistance Training", "reason" : "strength, confidence", "instantiation" : "3x running"},
# {"goal" : "Knowledge & Wisdom", "reason" : "improved decision-making", "instantiation" : "Reading etc"}
# ]

#journallist = [
#{"timestamp" : "2018/10/30", "title" : "Went to the striip clubs", "content" : "So today was...", "wellbeing" : "12"},
#{"timestamp" : "2018/10/29", "title" : "Went to the striip clubs", "content" : "So today was...", "wellbeing" : "12"},
#{"timestamp" : "2018/10/28", "title" : "Went to the striip clubs", "content" : "So today was...", "wellbeing" : "12"},
#{"timestamp" : "2018/10/27", "title" : "Went to the striip clubs", "content" : "So today was...", "wellbeing" : "12"},
#]
donebucket = []

def readtxt():
	with open("test.txt", "r") as file:
		data2 = eval(file.readline())
	tasklist=data2
#	print(tasklist)

def writetxt():
	with open("test.txt", "w") as file:
		file.write(str(tasklist))


def printTasks():
	with open("test.txt", "r") as file:
		data2 = eval(file.readline())
	tasklist=data2
	#print(tasklist)

	print("|          Current Task            | IMP | URG |  TIME  | DDL (yyyy/mm/dd)|     STATUS    | PROD | ETC |")
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
	with open("test.txt", "r") as file:
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
	switchViews()
	#todo = input("\n")

def virtues():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("ABOUT THE VIRTUE SYSTEM")
	print("=======================")
	print("This program is inspired by the Objectivist ethical system. To summarise:\n")
#	print("  - That man is a heroic being, with his own happiness as the moral purpose of his life, \n    with productive achievement as his noblest activity, and reason as his only absolute")
	#print("  - The basis of all virtue is self-interest:\n")

	i=1
	for x in virtueslist:
		print(""+str(i) + ") "+ x.get("virtue") + ":" + x.get("definition"))
		i +=1
	print("8) Rationality: The cardinal virtue that embodies following reason (and rejecting emotion)")



def goals():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("T - Back to task view")
	print("Your goals are as follows:")
	print("")
	print(goals)
	#i = 1
	#for x in goals:
		#print(str(i) +". " + x.get("goal") + " | " + x.get("reason") +" | " + x.get("instantiation"))

#	i+=1
	print("\n")
	print("----------------")
	print("What would you like to do?")
	print("1 - Add Goal")
	print("2 - Remove Goal")
	print("3 - Update Goal")


def changeSA():
	algorithm = input("What sorting algorithm would you like to use? (FIFO, SJF, PS, EDF, RR)")
	if(algorithm == "FIFO"):
		print("The scheduling algorithm will remain on FIFO")
	if(algorithm == "SJF"):
		sortingalgorithm = "SJF"
		sorttasklist()

def markComplete():
	with open("test.txt", "r") as file:
		data2 = eval(file.readline())
	tasklist=data2

	os.system('cls' if os.name == 'nt' else 'clear')
	printTasks()
	print("COMPLETE A TASK")
	print("==============")
	mark = input("which task do you want to mark as complete?\n")
	tasklist[int(mark)-1]["status"] = "COMPLETE"
	with open("test.txt", "w") as file:
		file.write(str(tasklist))
	start3()

def deleteTask():
	with open("test.txt", "r") as file:
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
	with open("test.txt", "w") as file:
		file.write(str(tasklist))
#	start3()
	start3()

def addSubTasks(subtasks):
	finaltasks = ""
	while(subtasks == "Y" or subtasks =="y"):
		stasks = input("what do you want to add as your subtasks?")
		finaltasks +="\n ---- " + stasks
		subtasks = input("do you want to add a new task?")
		if(subtasks == "n"):
			break
	return finaltasks

def createTask():
	with open("test.txt", "r") as file:
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
		deadline = input("What is the deadline (yyyy/mm/dd) \n")
		pdeadline = datetime.strptime(deadline, "%Y/%m/%d")
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
	with open("test.txt", "w") as file:
		file.write(str(copytasklist))
	start3()


def personalProfile():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("----PERSONAL PROFILE-----")
	print("Name: Patrick")

	with open("journallist.txt", "r") as file:
		data2 = eval(file.readline())
	journallist = data2

	with open("test.txt", "r") as file:
		data3 = eval(file.readline())
	tasklist = data3

	#L = [int(n) for n in wellbeinglist if n]
	#ave = sum(L)/float(len(L)) if L else '-'
	#L = [int(n) for n in wellbeinglist if n]
#	ave = sum(L)/float(len(L)) if L else "-"
	#average = round(ave,0)
	total = 0
	for x in journallist:
		total += int(x.get("wellbeing"))

	#print(total)
	count = len(journallist)
	#print(count)

	wellbeingindex = round(total/count,0)


	#To be implemented
	print("Wellbeing index (-2 to 3): " + str(wellbeingindex))
	print("Inner Circle: 2")
	print("Outer Circle: 3")

	print("\n========")
	print("VIRTUES")
	print("========")
#	rationality = 0
	#for i in virtueslist:
		#rationality += i.get("value")

	#i=0
	#for x in virtueslist:
#		print(x.get("virtue")+":",x.get("value"))
#	print("Rationality :"+rationality)

	productionvalue = 0
	for x in tasklist:
		if(x.get("status") == "COMPLETE"):
			productionvalue += int(x.get("production"))
	print("Production: " + str(productionvalue))

#	print("---------------")
	#print("Rationality: ", rationality)
	#print("---------------")


def viewFriends():
	print("----FRIENDS-----")
	print("INNER CIRCLE")
	print("OUTER CIRCLE")

def Journal():
	os.system('cls' if os.name == 'nt' else 'clear')
	with open("journallist.txt", "r") as file:
		data2 = eval(file.readline())
	journallist=data2

	print("Welcome to my journal! \n")
	print("View current entries")
	for x in journallist:
		print(str(journallist.index(x) + 1) + " " + x.get("timestamp") + " " + x.get("title") +  " " +x.get("wellbeing"))
	print("\n")
	#Read wellbeing
#	with open("wellbeing.txt", "r") as file:
#		data2 = eval(file.readline())
#	wellbeinglist=data2
	#print(wellbeinglist)
	#wellbeing

	print("(1) - Add an entry for today")
	print("(2) - View previous entry")
	print("(3) - Modify previous entry")
	
	print("")
	print("Switch views")
	print(" (A)chievements log | (D)iet Planner   |")
	print(" (H)abits tracker   | (F)riends        | (T)odo")
	print(" (J)ournal          | (P)rofile")

	check = input("What would you like to do? \n \n")
	if(check == "1"):
		strtimestamp = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
		#catch date
		#for x in journallist:
		#	if(strtimestamp == x.get("timestamp")):
			#	catch = input("failed")
		title = input("What is the title for today's entry?: ")
		lines = []
		index  = 0
		suffix =""
		while True:
			if 4 <= index <= 20 or 24 <= index <= 30:
				suffix = "th"
			else:
				suffix = ["st", "nd", "rd"][index % 10 - 1]
			index +=1
			if(index == 1):
				line = input("What did you do today? \n")
			else:
				
				line = input(str(index) + suffix +" paragraph \n")
			if line:
				lines.append(line)
			else:
				break
		content = "\n".join(lines)	
		wellbeing = input("How did you feel today? \n (-3 Severe Depression -2 Moderate Depression 1-Borderline Depression 0- Neutral 1-Content 2-Happy 3-Eastatics ")
		comb = {"timestamp": strtimestamp, "title": title, "content": content, "wellbeing": wellbeing }
		print(comb)

		journallist.append(dict(comb))
		copyjournallist= journallist
		os.system('cls' if os.name == 'nt' else 'clear')
		with open("journallist.txt", "w") as file:
			file.write(str(copyjournallist))
		Journal()


	if(check == "2"):
		print("View current entries")
		for x in journallist:
			print(str(journallist.index(x) + 1) + " " + x.get("timestamp") + " " + x.get("title") +  " " +x.get("wellbeing"))
		print("\n")
		picklist = input("which one do you want to view")
		for idx,val in enumerate(journallist):
			if(str(idx + 1) == picklist):
				print(val.get("title") + "\n\n" + val.get("content"))
				
	if(check == "b" or check == "B"):
		booklog()
	if(check == "j" or check == "J"):
		Journal()
	if(check == "f" or check =="F"):
		viewFriends()
	if(check == "p" or check == "P"):
		personalProfile()
	if(check == "v" or check == "V"):
		virtues()
	if(check == "H" or check == "h"):
		habittracker()
	if(check == "a" or check == "A"):
		achievements()
	if(check == "spec" or check == "SPEC"):
		specification()
	if(check == "T" or check == "t"):
		start3()	

def habittracker():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("\nExcellence is not an act, but a habit' ~ Socrates" )
	print("==================================================")
	print("BASIC HYGIENE & APPEARANCE ")
	print("==================================================")
	print(" - Brush teeth, floss & mouthwash, Frequency: Daily")
	print(" - Bathe, Moisturise & Vaseline (+fragrance)")
	print(" - Shave")
	print(" - Trim Nails")
	print(" - Haircut")
	print("==================================================")
	print("HEALTH & WELLBEING")
	print("==================================================")
	print(" - Sleep (11:00 - 06:30)")
	print(" - Exercise")
	print(" - Mindfulness")
	print("==================================================")
	print("WISDOM & KNOWLEDGE")
	print("==================================================")
	print(" - Self-help")
	print(" - Programming")
	print(" - Textbook")
	print("==================================================")
	print("SOCIAL INTERACTION")
	print("==================================================")
	print(" - Self-help")
	print(" - Programming")
	print(" - Textbook")
	print("")
	switchViews()

	#This method will need to be remade with tables
def achievements():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("					|  ACHIEVEMENTS  |\n 	 			        ==================")
#	print("                	   This will need to be remade as tables")
	print("               PERSONAL PROJECTS")
	print("==============================================")

	print(" - Finish WATERBUFFALO MICROMANAGEMENT SYSTEM")
	print(" - Start WATERBUFFALO EDUCATIONAL TOOLS (LONG DIVISION)")
	print(" - Start DATABASE ")
	print("")
	#print("----------------------------------------------")
	print("               ACADEMIA AND WORK-LIFE")
	print("==============================================")
	print(" - Finish WORLDBOOKS")
	print(" - Become junior python developer/data analyst")
	print("")
#	print("----------------------------------------------")
	print("               LIFESTYLE")
	print("==============================================")
	print(" - Get a pet (cat/dog)")
	print(" - Add a new member into the inner circle")
	print(" - Go travelling with friends")
	print(" - Memorable experience X,Y,Z")
	print(" - Live with friends")
	print("")
#	print("----------------------------------------------")
	print("            SOCIAL AND RELATIONSHIPS          ")
	print("==============================================")
	print(" - Full Inner circle")
	print("")
	switchViews()


def specification():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("					|  ACHIEVEMENTS   |\n 	 			        ===================")
	print("               PERSONAL PROJECTS")
	print("----------------------------------------------")
	print(" - WATERBUFFALO MICROMANAGEMENT SYSTEM")
	print("==============================================")
	print(" Main features")
	print("  - Goals list (75%)")
	print("  - Habits log (50%)")
	print("  - Achievements log (50%)")
	print(" Further micromanagement")
	print("  - Dynamic timeline (0%)")
	print("  - Profile - Statistics tracker (50%)")
	print("  - Journal and wellbeing tracker (25%)")
	print("  - Diet planner & Calorie counter (0%)")
	print("  - Calendar (0%)")
	print("  - Weight tracker (0%) \n")

	print("----------------------------------------------")
	print(" - WORLDBOOKS")
	print("==============================================")


def booklog():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("					|  READINGLIST   |\n 	 			        ===================")
	print("IN-PROGRESS")
	print("Title            | Progress  | %   | Days to finish book at current rate")
	print(" Atlas Shrugged  | (494/1054)| 46% | booksize * days - finaldays  ")
	print("PENDING")
	print("Mindfulness book\n Python book")
	print("READING LIST")
	print("1 - Add book to list")
	print("2 - Update progress")
	print("3 - Mark book as complete")
	print("4 - Add book to reading list")
	print("5 - Start book progress")
	print("6 - Delete book")

def viewDoneTasks():
	os.system('cls' if os.name == 'nt' else 'clear')
	with open("test.txt", "r") as file:
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
def switchViews():
	print("")
	print("Switch views")
	print(" (A)chievements log | (D)iet Planner   |")
	print(" (H)abits tracker   | (F)riends        | (T)odo")
	print(" (J)ournal          | (P)rofile")
	todo = input("what do you want to do?")
	if(todo == "b" or todo == "B"):
		booklog()
	if(todo == "j" or todo == "J"):
		Journal()
	if(todo == "f" or todo =="F"):
		viewFriends()
	if(todo == "p" or todo == "P"):
		personalProfile()
	if(todo == "v" or todo == "V"):
		virtues()
	if(todo == "H" or todo == "h"):
		habittracker()
	if(todo == "a" or todo == "A"):
		achievements()
	if(todo == "spec" or todo == "SPEC"):
		specification()
	if(todo == "T" or todo == "t"):
		start3()
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
		
def switchViewsMany():
	print("Switch views")
	print(" (A)chievements log | (D)iet Planner   |")
	print(" (H)abits tracker   | (F)riends        | (T)odo")
	print(" (J)ournal          | (P)rofile")
	todo = input("what do you want to do?")
	if(todo == "b" or todo == "B"):
		booklog()
	if(todo == "j" or todo == "J"):
		Journal()
	if(todo == "f" or todo =="F"):
		viewFriends()
	if(todo == "p" or todo == "P"):
		personalProfile()
	if(todo == "v" or todo == "V"):
		virtues()
	if(todo == "H" or todo == "h"):
		habittracker()
	if(todo == "a" or todo == "A"):
		achievements()
	if(todo == "spec" or todo == "SPEC"):
		specification()
	if(todo == "T" or todo == "t"):
		start3()
		
def start3():
	opening()
	todo = input("\n")
	switchViews()

start3()
#readtxt()