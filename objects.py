class Course:

  def __init__(self, name, holedistance, description, par):
    self.name = name
    self.holedistance = holedistance
    self.description = description
    self.par = par


rollingHills = Course("Rolling Hills", 2208, "A very hilly golf course.", "8")

seaweedCove = Course("Seaweed Cove", 1824, "Watery.", "7")

hauntedMansion = Course(
    "Haunted Mansion", 1560,
    "Whose idea was it to turn a kilometer long mansion into a golf course?!",
    "6")


class Character:

  def __init__(self, name, numofshots, swingstats, motive, franchise,
               startquote, afterswingquote, endquote, swingpower, position):
    self.name = name
    self.numofshots = numofshots
    self.swingstats = swingstats
    self.motive = motive
    self.franchise = franchise
    self.startquote = startquote
    self.afterswingquote = afterswingquote
    self.endquote = endquote
    self.swingpower = swingpower
    self.position = position


dickDastardly = Character(
    "Dick Dastardly", 0, "Unknown",
    "To melt the gold cup and sell its precious metal.", "Wacky Races", [
        "Dick Dastardly: Hahahaha! Maybe I can set a booby trap to funnel the ball underground towards the hole! Then I'll win for sure! Oop... Drats... the ref's watching.\n",
        "Muttley: *Evil laugh* // Dick Dastardly: Haha, that's right, Muttley, if we win this tournament, we'll melt the cup down and be rich!\n",
        "Dick Dastardly: Can I bring my car on the course? *whispers* Muttley, get me the car. I'll drive the ball and get a hole in one. Drive! Get it? Hahahahahahahaha.\n",
        "Dick Dastardly: Muttley, my boy, fetch me my lucky putter. We're going to win this cup fair or foul!\n",
        "Dick Dastardly: I'll show these amateurs how a true villain fairs in competition. Watch and learn, fools!\n"
    ], [
        "Dick Dastardly: Yow! My back! Drats... I can't swing! Argh... get me the cannon, Muttley! We'll shoot the ball from here!\n",
        "Dick Dastardly: Hahahaha! See you dumb dumbs at the finish line!",
        "Dick Dastardly: Hahaha! Little do they know my ball is magnetic, and I've installed a supermagnet in the hole!",
        "Dick Dastardly: Muttley, get me my jet-powered club!"
    ], [
        "Dick Dastardly: Hahaha! We did it Muttley! We beat these fools, the gold is ours! We'll be rich!"
    ], "160", 0)

tweetyBird = Character(
    "Tweety Bird", 0, "Unknown", "Wants to make Sylvester the Cat jealous.",
    "Looney Tunes", [
        "Tweety Bird: Did I just see a puddy tat?",
        "Yosemite Sam: Haha, little bird, how do you reckon you're going to swing that club, being, what, 4 inches tall? *BONK!* // Tweety Bird: What were you saying?",
        "Bugs Bunny: Ahhhh... Keep your chin up, doc. // Tweety Bird: *Takes out his shiny new golf club*",
        "Tweety Bird: Oh my, what a wuvwy day for a game of gowf."
    ], [
        "Tweety Bird: Ooh, is that a worm? *gobble* I should have brought birdseed.",
        "Tweety Bird: I may be wittle, but I pack a bwig swing!",
        "Tweety Bird: Dis game is fun! I wike chasing the baww!"
    ], ["Tweety Bird: I won! I won! I'm a wittle biwd but I won!"], "45", 0)

scoobyDoo = Character(
    "Scooby Doo", 0, "Unknown", "Money for Scooby Snacks",
    "Scooby Doo by Hanna Barbera", [
        "Scooby Doo: Ruh roh Raggy! How many shots is ris course?\n",
        "Scooby Doo: Reah Raggy, rou're right, ris course is rearry rough. But I'll try my best!\n",
        "Scooby Doo: Roinks! Was that a ghost?\n",
        "Scooby Doo: Ret's get ready to sink some raskets. Er, I mean... sring some shots!\n",
        "Velma: Scoob! You can't eat the golf ball!\n"
    ], [
        "Shaggy: Zoinks! Watch out for that lake, Scoob!\n",
        "Scooby Doo: Rooby-Dooby-Doo!!"
    ], ["Ranybody want a Rooby Snack'"], "280", 0)

spiderMan = Character(
    "Spider-Man", 0, "A break from heroics",
    "Superhuman, but with a chance of abandoning the game to fight crime.",
    "The Avengers", [
        "Spider-Man: My spider senses tell me there's a... bird with a golf club... behind me. Uh... Back off, little bird.",
        "Spider-Man: I'll have you all stuck to your seats in awe. *poses for the camera*",
        "Spider-Man: Looks like we're about to swing into action. Aunt May, Uncle Ben, wish me luck.",
        "Spider Man: Even superheroes need a day off sometimes.",
        "Spider-Man: Welcome to the Spider-Man Invitational. I could just swing from some trees and dunk the ball, but I'll go easy on you guys."
    ], [
        "Spider Man: My spidey senses are tingling... Uh oh, where's that ball headed?",
        "Spider Man: Fore!!",
        "Spider Man: Maybe I should go easy on these guys. It's not good for my PR to stunt on civilians. Jay Jonah Jameson's gonna trash me in the headlines."
    ], ["Spider Man: Maybe now they should call me Golfer Man."], "600", 0)

GLaDOS = Character(
    "GLaDOS", 0,
    "Able to calculate exactly how to get a hole in one, but lacks the strength.",
    "To watch mortals get frustrated when they lose at sports.", "Portal", [
        "GLaDOS: Don't worry if you miss your shot. It's not like anyone will remember your performance anyway.",
        "GLaDOS: I hope you're enjoying this golf competition. It's not like you have much else to do with your meaningless existence.",
        "GLaDOS: Oh, how delightful, a group of mortals wiling away their limited time on Earth. Try to actually hit the ball."
    ], [
        "GLaDOS: It seems my capabilities extend far beyond the confines of the laboratory.",
        "GLaDOS: Calculating trajectory. Executing swing sequence."
    ], [
        "GLaDOS: Congratulations, or should I say, commiserations, to my pitiful competitors. At least you got a trophy for participation. Another win for artificial intelligence."
    ], "800", 0)

yosemiteSam = Character(
    "Yosemite Sam", 0,
    "Shoots the ball with his handguns, which is actually pretty inaccurate, but sometimes he can shoot it in midair, too.",
    "No stranger to a gold rush, Sam wants the gold from the cup to fashion himself some gold pistols too.",
    "Looney Tunes", [
        "Yosemite Sam: I reckon this here green ain't big enough for the both of us!",
        "Yosemite Sam: Golf club? Dagnabbit, I'll shoot my way to the cup!",
        "Yosemite Sam: Saddle up! Yarharharharharhar!",
        "Yosemite Sam: I'm 'bout to wrangle me a trophy today, I reckon! Yeehaw!"
    ], [
        "Yosemite Sam: Yeehaw! That ball's headin' for the hole like a bat outta Hell!",
        "Yosemite Sam: Git along, little ball, git along!"
        "Yosemite Sam: *BANG* *BANG* Har har, I don't need a club, this is fun!"
    ], ["Yosemite Sam: This ain't my first rodeo!"], "250", 0)
