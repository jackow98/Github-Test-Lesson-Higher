teamName = ""
highScore = 0
highTeam = ""
while teamName != "stop":
    teamName = input("Enter team name or stop")
    if teamName !="stop":
        score = int(input("Enter score"))
        if score > highScore:
            highScore = score
            highTeam = teamName
print("Winner is " + highTeam + " with score " + str(highScore))

