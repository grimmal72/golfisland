# type: ignore

import math
import random
import time

from objects import dickDastardly, GLaDOS, scoobyDoo, spiderMan, tweetyBird, yosemiteSam
from objects import hauntedMansion, rollingHills, seaweedCove

courses = [rollingHills, seaweedCove, hauntedMansion]

characters = [
    dickDastardly, GLaDOS, scoobyDoo, spiderMan, tweetyBird, yosemiteSam
]

print("GOLF ISLAND - A GAME BY JORDAN MALMGREN\n")

startTheGame = " "
while startTheGame != "y":
  startTheGame = input("Enter 'y' to start the game.\n")
  if startTheGame.lower() == "y":
    break
  else:
    print("Incorrect input. Enter 'y' when you'd like to start the game.\n")
    continue
#this line is supposed to be where the loop ends/repeats

# The game is of course started based on the input of the startTheGame variable.
# What it contains will lead to starting the game or not starting the game.

#After the game has been started:
print(
    "It's a sunny day on Golf Island. Golf Island is a prestigious golf tournament that happens once a year on a series of islands in the middle of the Pacific Ocean.\nYou're vying for the gold cup, which is made of real gold! Pick your stage:\n"
)


def displayCourses():
  for i in range(len(courses)):
    print(
        f"{i + 1}.\n{courses[i].name}.\n{str(courses[i].holedistance)} feet from start to finish.\n{courses[i].description}\n"
    )


# That above loop just lists out the stages. It isn't how the numbers are determined, by the way. The stages' numbers were already determined by the items' positions in the "courses" list.
# The below loop is just about trying to get a number key input that corresponds to the available options.


def selectCourse():
  while True:
    userCourseChoice = input(
        "Enter the number of the course you'd like to play.\n")
    try:
      choice = int(userCourseChoice)
      if 1 <= choice <= len(courses):
        #Then the inputted course will be chosen. Except, as it turns out, the Haunted Mansion is old and collapses when you try to pick it.
        if choice == 3:
          print(
              "Uh oh... Breaking news. The haunted mansion golf course just collapsed in on itself. Guess we won't be able to play there.\n"
          )
        else:
          return courses[choice - 1]
      else:
        print(
            "Invalid choice. Please enter a number within the range of courses available, using a number key.\n"
        )
        continue
    except ValueError:
      print(
          "Invalid input. Please enter a number corresponding to the available stages, using a number key.\n"
      )
      continue


displayCourses()
selectedCourse = selectCourse()

print(f"You picked {selectedCourse.name}!\n")


def displayCharacters():
  for i in range(len(characters)):
    print(
        f"{i + 1}.\n{characters[i].name}.\nFranchise: {characters[i].franchise}.\nMotive: {characters[i].motive}\nSwing stats: {characters[i].swingstats}\n"
    )


# These two loops work the same way as the stage selection loops.


def selectCharacter():
  while True:
    userCharacterChoice = input(
        "Enter the number of the character you'd like to choose:\n")
    try:
      choice = int(userCharacterChoice)
      if 1 <= choice <= len(characters):
        # Return the chosen character
        return characters[choice - 1]
      else:
        print(
            "Invalid choice. Please enter a number corresponding to the available characters, using a number key."
        )
        continue
    except ValueError:
      print("Invalid input. Please enter a number, using a number key.")
      continue


print(
    "Pick your player! Choose who you'd like to play as. Use the number key.\n"
)

displayCharacters()

selectedUserCharacter = selectCharacter()

print(
    f"You selected {selectedUserCharacter.name}! You'll play as {selectedUserCharacter.name}."
)

print("Select who will be opponent 1.")

selectedEnemyCharacter1 = selectCharacter()

while True:
  if (selectedUserCharacter == selectedEnemyCharacter1):
    print(
        "That character is already in use! You'll have to pick a different character"
    )
    selectedEnemyCharacter1 = selectCharacter()
    continue
  else:
    break

print(
    f"You selected {selectedEnemyCharacter1.name}! Opponent 1 will be {selectedEnemyCharacter1.name}! Now pick opponent 2!"
)

selectedEnemyCharacter2 = selectCharacter()

while True:
  if (selectedEnemyCharacter2
      == selectedEnemyCharacter1) or (selectedEnemyCharacter2
                                      == selectedUserCharacter):
    print(
        "That character is already in use! You'll have to pick a different character"
    )
    selectedEnemyCharacter2 = selectCharacter()
    continue
  else:
    break

#The thirty or so lines above this are the last major revision I made to this code before going to sleep last night, April 28th 2024

print(
    f"You selected {selectedEnemyCharacter2.name}! Opponent 2 will be {selectedEnemyCharacter2.name}!"
)

print(
    "You take a look around the green. A crowd cheers on the bleachers. A blimp passes by, and camera drones buzz around, filming the event. It's certainly a major festival. You look over at your competition.\n"
)

print(
    f"Your opponents {selectedEnemyCharacter1.name} and {selectedEnemyCharacter2.name} stand in front of the tee.\n"
)


def randomEnemyQuote1ForStart():
  enemyQuote1 = random.choice(selectedEnemyCharacter1.startquote)
  print(enemyQuote1)


def randomEnemyQuote2ForStart():
  enemyQuote2 = random.choice(selectedEnemyCharacter2.startquote)
  print(enemyQuote2)


randomEnemyQuote1ForStart()
randomEnemyQuote2ForStart()

#As you can imagine, these two quote functions pull from the two above lists of potential enemy character phrases.

players = [
    selectedUserCharacter, selectedEnemyCharacter1, selectedEnemyCharacter2
]

windSpeed = random.randrange(0, 25)
# According to my Googling, wind above 40mph is a gale, and 74mph is a hurricane, so I'm not going to go that high.

cardinalDirections_List = [
    "North", "North East", "East", "South East", "South", "South West", "West",
    "North West"
]

windDirection = random.choice(cardinalDirections_List)

holeDirection = selectedCourse.holedirectionfromtee

# I may add in the direction that the hole points from the tee as a cardinal direction within the course objects, and then based on the wind speed it will affect the ball placement. But I'll come back to that later.

if windSpeed == 0:
  print("There's no wind! Fantastic weather for a game!\n")
else:
  print(
      f"The wind is moving at {windSpeed} miles per hour, {windDirection.lower()}. The hole is {selectedCourse.holedirectionfromtee.lower()} of the tee. \n"
  )

print(
    f"The hole is {str(selectedCourse.holedistance)} feet away. Par is {str(selectedCourse.par)}. You tee up.\n"
)


# Calculate the angle between two cardinal directions
def calculateAngle(direction1, direction2):
  directions = cardinalDirections_List
  angle = (directions.index(direction1) - directions.index(direction2)) * 45
  if angle > 180:
    angle -= 360
  elif angle < -180:
    angle += 360
  return angle


# Calculates the angle between windDirection and holeDirection
angle = calculateAngle(windDirection, holeDirection)

# Determine swing magnitude adjustment based on angle
if angle == 0:
  swingAdjustment = 1  # No adjustment if wind and hole direction are the same
elif angle == 180 or angle == -180:
  swingAdjustment = -1  # Detract from swing if wind and hole direction are opposite
elif abs(angle) < 90:
  swingAdjustment = 1 - abs(
      angle) / 90  # Boost or detract slightly based on angle
else:
  swingAdjustment = -(abs(angle) -
                      90) / 90  # Boost or detract slightly based on angle

# Apply wind speed to swing magnitude adjustment
# The randrange was 0 to 25, but we want swingAdjustment to be 0 to 1 and potentially negative.
swingAdjustment *= windSpeed / 25

# How this works is a swingMagnitude multiplied by one is a normal swing. swingAdjustment can be negative, and can cause us to be blunting our swing with something like a 0.78 * swingMagnitude that slightly dulls the swing. Alternatively, you can have like a 1.98 * swingMagnitude that almost doubles the power of the swing. But it can go no lower than a swingMagnitudeMultiplier of 0 and no higher than a swingMagnitudeMultiplier of 2.
swingMagnitudeMultiplier = 1 + swingAdjustment

swingMagnitudeMultiplier = round(swingMagnitudeMultiplier * 10000) / 10000

print(
    f"Due to the wind, your swing multiplier is: {str(swingMagnitudeMultiplier)}x."
)
# I was getting numbers like 0.040000000000000036x in the above print statement which is why I instituted the rounding function above it.

def endingSequence(players):
  scoreNames = [
      "Hole-in-one!", "Albatross.", "Eagle.", "Birdie.", "Par.", "Bogey.",
      "Double Bogey...", "Triple Bogey...",
      "Worse than Triple Bogey... Basically, really bad! But hey, at least they still won!"
  ]

  def golfScore(shots, par):
    if shots == 1:
      return scoreNames[0]
    elif shots == par - 3:
      return scoreNames[1]
    elif shots == par - 2:
      return scoreNames[2]
    elif shots == par - 1:
      return scoreNames[3]
    elif shots == par:
      return scoreNames[4]
    elif shots == par + 1:
      return scoreNames[5]
    elif shots == par + 2:
      return scoreNames[6]
    elif shots == par + 3:
      return scoreNames[7]
    else:
      return scoreNames[8]

  # Initialize an empty list to store the fancyScoreWord for each player
  fancyScoreWords = []

  for player in players:
    player.fancyscoreword = golfScore(player.numofshots, selectedCourse.par)
    fancyScoreWords.append(player.fancyscoreword)

  # Determine the player(s) with the best score
  best_score = min(player.numofshots
                   for player in players)  # Find the minimum score
  second_best_score = sorted(set(
      player.numofshots
      for player in players))[1]  # Find the second best score
  third_best_score = sorted(set(player.numofshots for player in players))[2]
  # Find the third best score

  # The above three variables contain the numofshots attributes of the winning players, but we actually can't tell who the players even are. Below this comment is a way to make it clear who the player was who was in which place. Eg. 1st, 2nd, 3rd.
  for player in players:
    if player.numofshots == best_score:
      bestScorePlayer = player
    elif player.numofshots == second_best_score:
      secondBestScorePlayer = player
    elif player.numofshots == third_best_score:
      thirdBestScorePlayer = player

  winningPlayers = []  # Create an empty list to store the winners

  # Check each player's score
  for player in players:
    if player.numofshots == best_score:  # If player's score matches the best score
      winningPlayers.append(player)  # Add them to the list of winners

  # Check if there's a single winner or a tie
  if len(winningPlayers) == 1:
    print("Congratulations to the winner!")
    # Say who the single winner is and let them speak their endquote.
    print(
        f"Player {winningPlayers[0].name} is the champion with {bestScorePlayer.numofshots} shots!"
    )
    if winningPlayers[0].name == dickDastardly.name:
      print(f"{dickDastardly.endquote}")
    elif winningPlayers[0].name == GLaDOS.name:
      print(f"{GLaDOS.endquote}")
    elif winningPlayers[0].name == scoobyDoo.name:
      print(f"{scoobyDoo.endquote}")
    elif winningPlayers[0].name == spiderMan.name:
      print(f"{spiderMan.endquote}")
    elif winningPlayers[0].name == tweetyBird.name:
      print(f"{tweetyBird.endquote}")
    elif winningPlayers[0].name == yosemiteSam.name:
      print(f"{yosemiteSam.endquote}")

    print(
        f"In second place is {secondBestScorePlayer.name} with {secondBestScorePlayer.numofshots} shots."
    )
    print(
        f"In third place is {thirdBestScorePlayer.name} with {thirdBestScorePlayer.numofshots} shots."
    )

  else:
    print("It's a tie between:")
    for p in winningPlayers:
      print(f"Player {p.name} is tied for the win!")
      print(f"In third place is {third_best_score}")


zone1 = "zone1"
zone2 = "zone2"
zone3 = "zone3"
zone4 = "zone4"
zone5 = "zone5"
zone6 = "zone6"
zones = [zone1, zone2, zone3, zone4, zone5, zone6]
currentZone = zone1

driver = 1.3
threewood = 0.8
iron = 0.5
wedge = 0.25
putter = 0.1
putterwithin10ft = 0.01
clubs = [driver, threewood, iron, wedge, putter, putterwithin10ft]
currentClub = driver
# Since this line is never revisited, it isn't an issue that we are seting currentClub to driver, as it will just be reassigned later.

def shotCycle(player, hole_distance):
  if player.position == hole_distance:
    # If the player has already reached the hole, ignore them
    return

  # The next three conditional blocks are used to check what zone we're in and what club we're using. The reason I get that sorted before taking a swing is so that we pick the right club for the current position BEFORE swinging each time, instead of after, which wouldn't make much sense.

  if player.position >= 0 and player.position <= (hole_distance *
                                                                0.30):
    currentZone = zone1
  elif player.position > (hole_distance *
                          0.30) and player.position <= (hole_distance * 0.50):
    currentZone = zone2
  elif player.position > (hole_distance *
                          0.50) and player.position <= (hole_distance * 0.70):
    currentZone = zone3
  elif player.position > (hole_distance *
                        0.70) and player.position <= (hole_distance * 0.85):
    currentZone = zone4
  elif player.position > (hole_distance - 10) and player.position < (hole_distance + 10):
    currentZone = zone6
  else:
    currentZone = zone5

  if currentZone == zone1:
    currentClub = driver
  elif currentZone == zone2:
    currentClub = threewood
  elif currentZone == zone3:
    currentClub = iron
  elif currentZone == zone4:
    currentClub = wedge
  elif currentZone == zone5:
    currentClub = putter
  else:
    currentClub = putterwithin10ft

  swingPowerBasedOnClub = player.swingpower # Despite the finality that this line seems to have, the variable is about to have a different value.
  # By the way, the reason I use this variable instead of player.swingpower is that with player.swingpower it was taking the assigned multiplied value into the next loop, after which it would multiply to be even bigger the next turn, growing or shrinking exponentially.
  
  if currentClub == driver:
    swingPowerBasedOnClub *= driver
  elif currentClub == threewood:
    swingPowerBasedOnClub *= threewood
  elif currentClub == iron:
    swingPowerBasedOnClub *= iron
  elif currentClub == wedge:
    swingPowerBasedOnClub *= wedge
  elif currentClub == putter:
    swingPowerBasedOnClub *= putter
  else:
    swingPowerBasedOnClub *= putterwithin10ft

  # Player takes a shot
  if player == selectedUserCharacter:  # If it's the user's turn
    while True: # Loop doesn't end until you properly input a number key
      try:
        swingMagnitude = " "
        swingMagnitudeInput = int(input(f"Enter your shot with the number key: "))
        if 1 <= swingMagnitudeInput <= 25:
          swingMagnitude = swingMagnitudeInput * int(swingPowerBasedOnClub)
          break
        else:
          print("Select a number key from 1 to 25.")
          continue
      except ValueError:
        print("Invalid input. Please enter a number using the number key.\n")
        continue
  else:
    swingMagnitude = random.randrange(1, int(swingPowerBasedOnClub))

  # Update player's position based on the number recieved from the randrange.
  print(f"{player.name} just struck the ball {str(swingMagnitude)} feet!")
  print(f"They are in {currentZone}. They've currently equipped the {currentClub}.")
  # Pause to simulate turn
  time.sleep(0)  # Adjust the time as needed

  # Save player position before the swing, so we can reference it if we sink the ball by accident
  lastSavedPlayerPosition = player.position

  # Whether or not we're shooting towards the hole, adding to them sum, or shooting down towards the hole, subtracting from the total.
  #swingMagnitudeMultiplier was defined based on the wind, that's it.
  if (player.position < hole_distance):
    player.position += math.ceil(swingMagnitude * swingMagnitudeMultiplier)
  else: #  (player.position > hole_distance)
    player.position -= math.ceil(swingMagnitude * swingMagnitudeMultiplier)

  # I believe that the ceil function is being used such that it will be impossible to get the number 0 as a swing. I use ceil to have round numbers. But there was a time when I was getting infinite zero shots because the putter shots kept flooring to zero. That's why I'm not using floor.
  
  # Each character's number of shots starts at 0, but after a shot, it goes up by one. If the ball goes in the lake, it still goes up by one. This is the only line of code we need to do this.
  player.numofshots += 1

  # Chance of ball falling in lake
  def isBallInLake():
    probability = 1
    if random.randrange(0, 10) < probability:
      print(
          "Uh oh! The ball fell in a lake! They'll have to shoot from where they were last positioned."
      )
      player.position = lastSavedPlayerPosition
    else:
      return None

  isBallInLake()

  # Check if the player has reached the hole, or print current distance from hole, or print how much they overshot it by.
  feetRemaining = hole_distance - player.position
  if feetRemaining > 0:
    print(f"{player.name} is {feetRemaining} feet away from the hole.")
  elif feetRemaining == 0:
    print(f"{player.name} has reached the hole!")
  else:
    print(f"{player.name}'s ball is {-feetRemaining} feet further than the hole! They'll need to backtrack a bit.")

  # You can trigger any necessary actions here when a player reaches the hole
  
  def afterSwingSpeakChance(player):
    probability = 1
    if random.randrange(0, 10) < probability:
      afterSwingQuote = random.choice(player.afterswingquote)
      print(f"{afterSwingQuote}")
    else:
      return None
  
  afterSwingSpeakChance(player)
  # *this is the end of shotCycle*


def gameLoop(players, hole_distance):
  allBallsInHole = False
  while not allBallsInHole:
    for player in players:
      shotCycle(player, hole_distance)

      # Check if all balls are in the hole
      allBallsInHole = all(player.position == hole_distance
                           for player in players)
  # If all the characters' balls have reached the holes, the while not loop will be broken, and allBallsInHole will be permanently set to True, at least within the scope of the gameLoop function.
  endingSequence(players)

  # *this is the end of gameLoop*


gameLoop(players, selectedCourse.holedistance)

# May 3rd: Notes for next time I code this.
# Some features I still want to add are i want there to be a chance of spiderMan dropping from the roster (maybe by being deleted from the list?), i want there to be a chance of landing in the rough, and i want glados to have a chance of an auto hole in one.
# lastly, i just need to add the 2nd and third quotes to endingSequence().
# I may add \n to every sentence in the program.
# Lastly, something needs to be done about the zones. Maybe instead of 4 clubs for 4 zones, there can be 10 zones with 10 clubs, or 20 zones with 20 clubs. And I may institute a variable called powerGradient, where the weak clubs aren't nerfed as bad for the weak characters, and the strong clubs aren't as overpowered for the strong characters.
# The problem is that par should be like 7, but these characters are legitimately having 5000 shot games, which is unreasonable.

