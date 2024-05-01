# type: ignore

import random
import time

from endingSequence import endingSequence
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
        f"{i + 1}.\n{courses[i].name}.\n{courses[i].holedistance} feet from start to finish.\n{courses[i].description}\n"
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

# I may add in the direction that the hole points from the tee as a cardinal direction within the course objects, and then based on the wind speed it will affect the ball placement. But I'll come back to that later.

if windSpeed == 0:
  print("There's no wind! Fantastic weather for a game!\n")
else:
  print(
      f"The wind is moving at {windSpeed} miles per hour, {windDirection.lower()}. \n"
  )

print(
    f"The hole is {selectedCourse.holedistance} feet away. Par is {selectedCourse.par}. You tee up.\n"
)


def shotCycle(player, hole_distance):
  if player.position == hole_distance:
    # If the player has already reached the hole, ignore them
    return
  # Player takes a shot
  swingMagnitude = random.randrange(0, int(player.swingpower))
  # Update player's position based on the number recieved from the randrange.
  print(f"{player.name} just struck the ball {str(swingMagnitude)} feet!")

  # Pause to simulate turn
  time.sleep(1)  # Adjust the time as needed

  player.position += swingMagnitude
  # Assuming a shot reduces the distance to the hole
  # Check if the player has reached the hole

  # Print current distance from hole
  distance_to_hole = hole_distance - player.position
  if distance_to_hole > 0:
      print(f"{player.name} is {distance_to_hole} feet away from the hole.")
  elif distance_to_hole == 0:
      print(f"{player.name} has reached the hole!")
  else:
      print(f"{player.name} has overshot the hole by {-distance_to_hole} feet!")
  
    # You can trigger any necessary actions here when a player reaches the hole

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
  endingSequence()

  # *this is the end of gameLoop*


gameLoop(players, selectedCourse.holedistance)
