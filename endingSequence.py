def endingSequence(shots, par):
  scoreNames = [
      "Hole-in-one!", "Albatross.", "Eagle.", "Birdie.", "Par.", "Bogey.",
      "Double Bogey...", "Triple Bogey...",
      "Worse than Triple Bogey... Basically, really bad!"
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

  fancyScoreWord = golfScore(shots, par)





  selectedUserCharacter_score = golfScore(selectedUserCharacter.numofshots, coursePar)
  selectedEnemyCharacter1_score = golfScore(selectedEnemyCharacter1.numofshots, coursePar)
  selectedEnemyCharacter2_score = golfScore(selectedEnemyCharacter2.numofshots, coursePar)

  # Find the minimum score among the players
  minScoreBetweenPlayers = min(selectedUserCharacter.numofshots, selectedEnemyCharacter1.numofshots, selectedEnemyCharacter2.numofshots)

  # Determine which player had the minimum score
  if selectedUserCharacter.numofshots == minScoreBetweenPlayers:
      print("Congratulations to Player 1!")
  elif selectedEnemyCharacter1.numofshots == minScoreBetweenPlayers:
      print("Congratulations to Player 2!")
  else:
      print("Congratulations to Player 3!")

  return fancyScoreWord


# Example usage:
shots = 4
coursePar = 3
result = endingSequence(shots, coursePar)
'''
print(result)
'''


# test area below


  
