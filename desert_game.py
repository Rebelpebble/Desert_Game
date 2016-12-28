def at_the_well(drink):
    if drink == "1":
        print """
You pull up the bucket to find that the well is dried up.
Marching on, you finally collapse and die due to fatigue and thirst."""
    elif drink == "2":
        print """
You march on knowing that there is no way the well hasn't dried up.
You stumble upon some merchants that just happen to be passing by.
Merchant: \"You look tired. Come and rest at our camp.\""""
        print "1. Go with the merchants to their camp."
        print "2. Refuse, but ask for some water to quench your thirst."

        camp = raw_input("> ")
        going_camping(camp)
    else:
        print "\nYou killed yourself."


def going_camping(camp):
    if camp == "1":
        print """
The merchants take you back to their camp.
They give you a tent to sleep in.
In the middle of the night the merchant takes a knife to your neck.
You bleed out and the group of merchants feasts on your body.
You should have known:
\"Never trust a stranger.\""""
    elif camp == "2":
        print """
The merchants agree and give you a water sack and send you on your way.
You walk for a couple of hours and finally stumble across a river.
The river seems to be flowing quickly."""
        print "1. Try to swim across."
        print "2. Keep walking around aimlessly."

        river = raw_input("> ")
        down_the_river(river)
    else:
        print "\n You killed yourself"


def at_the_tree(nap):
    if nap == "1":
        print """
You take a nap and wake up a few hours later.
The sun has gone down and it is now dusk.
The temperature is much more pleasant."""
        print "1. Climb the tree."
        print "2. Walk towards the sunset."

        sunset = raw_input("> ")
        walking_toward_the_sun(sunset)
    elif nap == "2":
        print """
You continue on your way westward.
You walk and walk and walk for what seems like forever.
A snake finds itself under your foot and bites you.
Within minutes you start to loose your vision.
You take your last breath and fall, never to get up again."""
    else:
        print "\nYou killed yourself."


def walking_toward_the_sun(sunset):
    if sunset == "1":
        print "\nYou climb to the top of the tree and *SNAP*, you fall to your death."
    elif sunset == "2":
        print """
You walk toward the sunset over a large sand dune.
Once at the top, you slip and start tumbling down.
You finally come to a stop at the edge of a river.
You bury your face in the refreshing water drinking to your hearts content.
The river seems to be flowing quite rapidly."""
        print "1. Try to swim across."
        print "2. Keep walking around aimlessly."

        river = raw_input("> ")
        down_the_river(river)


def down_the_river(river):
    if river == "1":
        print """
You try to swim across the river. The current is just too strong.
You get swept away and finally wash up on the bank...
RIGHT NEXT TO AN ALLIGATOR!"""
        print "1. Attack the alligator."
        print "2. RUN AWAY!"

        action = raw_input("> ")
        fight_or_flight(action)
    elif river == "2":
        print """
The river was much too fast to cross.
The safe thing to do is to walk around aimlessly some more.
It got you this far!
Unfortunately, you stumble upon an aggressive camel and it stomps you to death."""
    else:
        print "\nYou killed yourself."


def fight_or_flight(action):
    if action == "1":
        print "\nHa! An alligator is no match for your might!"
        print "How shall you attack?"

        attack = raw_input("> (Be colorful) ")
        alligator_attack(attack)
    elif action == "2":
        print """
You fool! The alligator slaps you to the ground with his tail.
The wind is knocked out of you and you're laying on the ground.
The alligator puts it's mouth around your head.
You close your eyes and the alligator crushes your head between it's jaws.
OUCH!"""

def alligator_attack(attack):
    attack_power = len(attack)
    alligator_defense = 25

    if attack_power >= alligator_defense:
        print "You defeated the alligator! You win the game!"
    else:
        print "What a wimpy attack! The alligator bites you in half."


########################## Beginning of the journey. ##########################
print """
You wake up in a desert.
The sun beats down hard on your face as your eyes adjust to the light.
There is an object to the east and another to the west.
Which way do you choose to go?"""

direction = raw_input("> ")

if direction == "east":
    print "\nYou trudge on eastward and stumble upon a well."
    print "1. Lower the bucket to drink from the well."
    print "2. Continue eastward."

    drink = raw_input("> ")
    at_the_well(drink)

elif direction == "west":
    print "\nYou make your way westward to find a beautiful tree."
    print "1. Take a nap in the shade of the tree."
    print "2. Continue westward."

    nap = raw_input("> ")
    at_the_tree(nap)

else:
    print "\nYou killed yourself."
