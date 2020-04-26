import os
virtueslist = [
{"virtue":"Production", "definition" : " to work ceaselessly to create one's values.", "value": 1},
{"virtue":"Pride", "definition" : " Related to confidence and self-esteem.", "value": 1},
{"virtue":"Ambition", "definition" : " to pursue one's own goals and desires.", "value": 1},
{"virtue":"Self-restraint", "definition" : "Moderation or voluntary self-control.", "value": 1},
{"virtue":"Wisdom", "definition" : " Used as tools to navigate life", "value": 1},
{"virtue":"Order/Aesthetics", "definition" : "is the commitment to beauty and harmony", "value": 1},
{"virtue":"Integrity", "definition" : "Consistent application of reason.", "value": 1},
]

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

