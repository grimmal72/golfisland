class Course:

  def __init__(self, name, holedistance, description, par):
    self.name = name
    self.holedistance = holedistance
    self.description = description
    self.par = par


rollingHills = Course("Rolling Hills", "2321", "A very hilly golf course.",
                      "8")

seaweedCove = Course("Seaweed Cove", "1819", "Watery.", "7")

hauntedMansion = Course(
    "Haunted Mansion", "1538",
    "Whose idea was it to turn a kilometer long mansion into a golf course?!",
    "6")


class Character:

  def __init__(self, name, swingstats, motive, franchise, startquote,
               afterswingquote, endquote, swingpower):
    self.name = name
    self.swingstats = swingstats
    self.motive = motive
    self.franchise = franchise
    self.startquote = startquote
    self.afterswingquote = afterswingquote
    self.endquote = endquote
    self.swingpower = swingpower


dickDastardly = Character(
    "Dick Dastardly", "Unknown",
    "To melt the gold cup and sell its precious metal.", "Wacky Races", [
        "Dick Dastardly: Hahahaha! Maybe I can set a booby trap to funnel the ball underground towards the hole! Then I'll win for sure! Oop... Drats... the ref's watching.\n",
        "Muttley: *Evil laugh* // Dick Dastardly: Haha, that's right, Muttley, if we win this tournament, we'll melt the cup down and be rich!\n",
        "Dick Dastardly: Can I bring my car on the course? *whispers* Muttley, get me the car. I'll drive the ball and get a hole in one. Drive! Get it? Hahahahahahahaha.\n",
        "Dick Dastardly: Muttley, why are you snickering? I'm limber as a... Yow! My back! Drats... I can't swing! Argh... get me the cannon, boy! We'll shoot the ball from here!\n",
        "Dick Dastardly: Muttley, my boy, fetch me my lucky putter. We're going to win this cup fair or foul!\n",
        "Dick Dastardly: I'll show these amateurs how a true villain fairs in competition. Watch and learn, fools!\n"
    ], [""], [""], "160")

tweetyBird = Character(
    "Tweety Bird", "Unknown", "Wants to make Sylvester the Cat jealous.",
    "Looney Tunes", [
        "Tweety Bird: Did I just see a puddy tat?",
        "Yosemite Sam: Haha, little bird, how do you reckon you're going to swing that club, being, what, 4 inches tall? *BONK!* // Tweety Bird: What were you saying?",
        "Bugs Bunny: Ahhhh... Keep your chin up, doc. // Tweety Bird: *Takes out his shiny new golf club*",
        "Tweety Bird: Oh my, what a wuvwy day for a game of gowf."
    ], [""], [""], "45")

scoobyDoo = Character(
    "Scooby Doo", "Unknown", "Money for Scooby Snacks",
    "Scooby Doo by Hanna Barbera", [
        "Scooby Doo: Ruh roh Raggy! How many shots is ris course?\n",
        "Scooby Doo: Reah Raggy, rou're right, ris course is rearry rough. But I'll try my best!\n",
        "Scooby Doo: Roinks! Was that a ghost?\n",
        "Scooby Doo: Ret's get ready to sink some raskets. Er, I mean... sring some shots!\n",
        "Velma: Scoob! You can't eat the golf ball!\n"
    ], ["Shaggy: Zoinks! Watch out for that lake, Scoob!\n"], [""], "280")

spiderMan = Character(
    "Spider-Man", "A break from heroics",
    "Superhuman, but with a chance of abandoning the game to fight crime.",
    "The Avengers", [
        "Spider-Man: My spider senses tell me there's a... bird with a golf club... behind me. Uh... Back off, little bird.",
        "Spider-Man: I'll have you all stuck to your seats in awe. *poses for the camera*",
        "Spider-Man: Looks like we're about to swing into action. Aunt May, Uncle Ben, wish me luck.",
        "Spider-Man: Welcome to the Spider-Man Invitational. I could just swing from some trees and dunk the ball, but I'll go easy on you guys."
    ], [""], [""], "600")

GLaDOS = Character(
    "GLaDOS",
    "Able to calculate exactly how to get a hole in one, but lacks the strength.",
    "To watch mortals get frustrated when they lose at sports.", "Portal", [
        "GLaDOS: Don't worry if you miss your shot. It's not like anyone will remember your performance anyway.",
        "GLaDOS: I hope you're enjoying this golf competition. It's not like you have much else to do with your meaningless existence.",
        "GLaDOS: Oh, how delightful, a group of mortals wiling away their limited time on Earth. Try to actually hit the ball."
    ], [""], [""], "800")

yosemiteSam = Character(
    "Yosemite Sam",
    "Shoots the ball with his handguns, which is actually pretty inaccurate, but sometimes he can shoot it in midair, too.",
    "No stranger to a gold rush, Sam wants the gold from the cup to fashion himself some gold pistols too.",
    "Looney Tunes", [
        "Yosemite Sam: I reckon this here green ain't big enough for the both of us!",
        "Yosemite Sam: Golf club? Dagnabbit, I'll shoot my way to the cup!",
        "Yosemite Sam: Saddle up! Yarharharharharhar!",
        "Yosemite Sam: I'm 'bout to wrangle me a trophy today, I reckon! Yeehaw!"
    ], [
        "Yosemite Sam: Yeehaw! That ball's headin' straight for the hole like a bat outta Hell!",
        "Yosemite Sam: Git along, little ball, git along!"
    ], [""], "250")
