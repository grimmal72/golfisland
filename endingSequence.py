
def endingSequence(shots, par):
  scoreNames = ["Hole-in-one!", "Albatross.", "Eagle.", "Birdie.", "Par.", "Bogey.", "Double Bogey...", "Triple Bogey...", "Worse than Triple Bogey... Basically, really bad!"]

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
  return fancyScoreWord

# Example usage:
shots = 4
coursePar = 3
result = endingSequence(shots, coursePar)
print(result)

# Note: this is imported but is not actually in use right now. I'll use it when I've written the game loop.
