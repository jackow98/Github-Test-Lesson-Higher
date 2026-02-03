highestScore = 0
highestTeam = ""
teamName = ""
while teamName != "stop":
    teamName = input("Enter team name or stop to stop")
    if teamName !="stop":
        teamScore = int(input("Enter team score"))
        if teamScore > highestScore:
            highestScore = teamScore
            highestTeam = teamName
print(highestScore)
print(highestTeam)