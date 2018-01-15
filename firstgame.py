from sys import exit

def fairy_walk():
    print """
It gets late - you see the sky through the leaves of the forest's trees darken from pink to magenta
to red to purple. You remember that your friend is a little fearful of the dark, so you unpack your bag before the sky turns indigo and the forest turns full of shadows. 
\nYour LUNCH is untouched, your WATER BOTTLE empty, your FIRST AID KIT unused, and buried deep you find your FLASHLIGHT.
Turning it on gives the both of you a huge shock! Not that it doesn't work or that it gave you an electric jolt, but it seems that the forest also lit up in canon with it.
A thousand tiny lights hide in the crowns of the trees and suddenly it doesn't seem like night anymore. Only the cool breeze reminds you that it is indeed short after sundown.
One light approaches you...
"""    
    greet = raw_input("What do you do?\nPoint at it with your FLASHLIGHT?\nMeekly greet HELLO?\n")
    
    if greet == "FLASHLIGHT":
        print """
The light shrieks as you point the lamp at it, then falls to the ground.
Oh no! What lies on the ground before you is a small, small fairy with delicate transparent wings reminiscent of dragonflies.
Your friend nudges you to do something quick! The other fairies seem to be abuzz with scandalous gasps, but to your ears it sounds like musical bells ringing.
You don't expect it to glow all over though, so the both of you just cower, as the other fairies even join in.
Soon, the whole forest is filled with white light that painfully remind you of concert flood lights. Your flashlight hits the ground- and you wake in bed, drenched in sweat. 
What a vivid dream! Nonsensical, but ... 
"""
        print "\t"*6, "THE END",
        restart()
    elif greet == "HELLO":
        print """
The fairy shakes its head as it flies right in front of your face. As if in trance, you offer it a hand to land on which it gracefully accepts and stands upon. Its language sound just as adorable as the flickering soft colors its kin change into as they excitedly chatter. You don't understand muc, neither does your companion, but the last thing you catch is a sorry as it touches your eye-lids - and you find yourself in the town square, arms linked with your friend. 
\nYou share a secretive look with each other that spoke of both angst and excitement. As if spoken through telepathy, you seem to agree to keep this your little mystery. As you look at your phone clock, you realise it is still just barely evening. Led by your hungry rumbles, you both enjoy a dinner in town, excitedly talking about your adventure.
\nThe myth of the haunted shrine entirely exchanged with the very surreal experience of finding real fairies! WHOOOOHOOO!
"""
        print "\t"*6, "THE END",
        restart()
    else:
        print """
You stumble!run away through the forest, a music of twinkling following you from the fairy lights into the dark when- 
you wake up. 
\nIt was all just a dream.
"""
        print "\t"*6, "THE END",
        restart()

def water_way():
    print """
It feels like a long time since you've started out from your small village home, but nonetheless you walk on.
After passing the fifth bridge, the vegetation seems to thin out, until you find yourself by the beach of the river the forest creek is crossing into. You hear a mumbled 'Oh, great...' coming from beside you. 
You turn towards your traveling companion with a frown, but neither of you can keep it in for long, and laughter spills out of you. Of course, it just so happens that you went the complete wrong way: instead of //into// the forest, you followed the creek out of the forest. No wonder it got larger.
Fed up with walking, your friend suggests a little game: If you guess their zodiac sign's element right, you can lead on. 
If you are wrong, you'll both do what they want. Judging from their huffs during the hike and their twinkle at seeing the shallow river, you guess that would mean you're gonna playing at the beach until sunset.
\nYou only remember that you had a bbq and went swimming on their last birthday party, so it must be a summer birhtday.
"""
    element = raw_input("So is your friend a FIRE, EARTH, WATER, or AIR sign?\n")
    
    if element == "WATER":
        print """
It was easily one of the easiest deals in history. Of course you guessed correctly. friend grumbles, as they less willingly get dragged back by you towards the forest road. With a longing sigh, they wave rest and beach fun goodbye. You resume your hike!
"""
        fairy_walk()
    elif element == "FIRE":
        print """
Your friend gasps at your wrongest of wrong guesses and explodes, sharply, into a million small bits. Slack-jawed, you cannot help but do nothing as the sky cracks into two pieces and purple rain descends upon the earth, turning the trees pastel-colored. The remnants of your friend diffused through the air! The HORROR!
You jolt awake from the dream! 
Of course you know your every single friend's birthdate!
The audacity your brain had to even //imply// that you would fail such a basic question! 
And the ending! Terrible!
You lay back into your bed, shaking your head at it angrily. 
As if gone with that motion, the details of your dream pass... and after calming down, you fall asleep again...
"""
        print "\t"*6, "THE END"
        restart()
        
    elif element == "EARTH" or element == "AIR":
        print """
You jolt awake from the dream! 
What kind of nonsense was that! 
Of course you know your every single friend's birthdate! And zodiac sign, their planetary houses, their north node and moon sign, their mercury- their- every single detail of their natal chart! 
The audacity your brain had to even //imply// that you would fail such a basic question!
You lay back into your bed, shaking your head at it angrily. 
As if gone with that motion, the details of your dream pass... and after calming down, you fall asleep again...
"""
        print "\t"*6, "THE END"
        restart()
        
    else:
        print """
You jolt awake from the dream! 
What kind of nonsense was that! 
Of course you know your every single friend's birthdate! And zodiac sign, their planetary houses, their north node and moon sign, their mercury- their- every single detail of their natal chart! 
The audacity your brain had to even //imply// that you would fail such a basic question!
You lay back into your bed, shaking your head at it angrily. 
As if gone with that motion, the details of your dream pass... and after calming down, you fall asleep again...
"""
        print "\t"*6, "THE END"
        restart()


def forest_path():
    partner2 = raw_input("Ah. What's your friend's name again? Sorry, I'm quite forgetful...\n")
    print "%s? Hm? Ok." % partner2
    
    print """
So you and %s wander deep into the forest... you make easy conversation and wonder about how weird of a bonding experience this is - it's not every day you venture into a haunted shrine, after all. Around an hour into the forest, you come to a fork in the road.
You can go LEFT and walk the darker path into the bushes, 
RIGHT over the bridge to the other side of the creek or 
go STRAIGHT forward to continue following the clear body of water that winds its way through the woods. 
You could even go BACK, and spend day the with %s otherwise!
""" % (partner2, partner2)

    roads = raw_input("What would you like?\n")
    
    if roads == "LEFT":
        print "You go left!"
        fairy_walk()
    elif roads == "RIGHT":
        print "You go right!"
        water_way()
    elif roads == "BACK":
        print """
You romance %s for the day and end up marrying each other in the future due to this successful date! Incredible!
Your white picket fence could not look cuter, neither could your one point five kids!
Or so you think. In reality, you come to dressed in your pjs, curled up in your bed. It is three am. That dream sure felt real, huh?
You wander towards the window and look into the november night. No sight of any red-roofed forest shrines anywhere. 
Sighing, you drop back into bed, pull the covers up. For a while, you wonder if you've been harboring a little crush on your friend %s that you'd even dream of this- but soon enough you slip into a sweet, dreamless, sleep...
""" % (partner2, partner2)
        restart()
    elif roads == "STRAIGHT":
        print """
Whatever you may want to decide, %s was faster, and pulls you towards the bridge. Looks like you ended up RIGHT anyway...
"""
        water_way()
    else:
        print """
Suddenly, you come to dressed in your pjs, curled up in your bed. It is three am. That dream sure felt real, huh?
You wander towards the window and look into the november night. No sight of any red-roofed forest shrines anywhere. 
Sighing, you drop back into bed, pull the covers up, and soon slip into a sweet, dreamless, sleep...
"""
        restart()  


def prepare():
    print """
\nNow, are you naive or courageous, I wonder?
\nFact is: you don't believe in groundless rumors masquerading as truth, much like your peers.
You decide to venture out on your own to the shrine complex that no one is willing to check on.
Despite any reassuring arguments, you only manage to convince one of your friends to brave this little adventure with you.
"""
    partner = raw_input("What's their name?\n")
    
    print "%s it is? Nice. Here would be the part in which you're asked how deep your friendship goes, but we only have a short amount of time and nerves, so..." % partner
    
    print """
Anyway. You both decide it is wise to meet up early in the morning, so the next day you rise even earlier than the sun. You've already packed your BACKPACK yesterday, filled with only the necessities:
\na WATER BOTTLE to quench your thirst on the hike,
your lunchbox in which you carry your LUNCH of simple sandwiches with cucumber and cheese,
a small FLASHLIGHT to light up dark rooms and an equally small FIRST AID KIT.
\nYou're pretty sure you'll be back by dinnertime
\nBefore you depart - dressed appropiately, freshly showered - you're having breakfast...  
""" 
    
    breakfast = raw_input("What will it be?\nA SHORT breakfast, such as a buttered toast, some cereals or the likes,\nor SWEET and decadent breakfast of pancakes\nor SIMPLE leftovers?\n")
    
    if breakfast == "SIMPLE":
        print """
You quickly stuff yourself with some leftovers you have in your fridge, then meet up with your friend at the determined meeting point.
%s looks at you funny, but is quick to dismiss the weird look with a welcoming smile, greeting you. 
You smile back and as you begin your walk into the forest, the both of you fall into easy conversation, though you can't get over your awkward meet-up. What were they thinking of? You may never know.
\nBut as you near the quiet creek near that the forest path winds along, you're overcome with a sense of sickness. 
You stumble, suddenly very dizzy, and as soon as you open your mouth to answer the joke your companion just made, you run for the creek and hurl your breakfast out with alarming sounds.
\nAfter... well, after //that//, %s convinces you to get back and consult a doctor. Health before adventures, you know.
The doctor for his part, prescribes you some rest and notes you another appointment at a specialised clinic.
Apparently, you have a mild allergy for whatever was in your breakfast. 
\n%s will never let you live this down, but at least your friendship is deep enough to overcome this and you spend the rest of the day lounging around your home. Thoughts of the shrine myth forgotten.
""" % (partner, partner, partner)
        print "\t"*6, "THE END",
        restart()
    elif breakfast == "SWEET":
        print """
You enjoy a scrumptious meal of buttery, fluffy pancakes with your preferred toppings, a glass of milk, and fresh fruits.
It's a meal you now rarely had since you've moved out of your childhood home, but it doesn't fail to bring back happy memories of Sundays spent lazying around home and just doing nothing. Ah. With a satisfied and melancholic sigh, you take care of the dishes, then leave your cozy apartment to meet up with %s.
""" % partner
        forest_path()
    elif breakfast == "SHORT":
        print """
You're usually not the breakfast type. If you eat anything at all in the morning, it's something light. 
Today is no different. You clear the table off of any crumbs and dirty dishes, then stroll out of your home to meet up with your friend...
"""
        forest_path()
    else: 
        print """
Apparently, you don't want breakfast. You are caught in a dizzy spell, and fall unconscious...
Or so you think. In reality, you come to dressed in your pjs, curled up in your bed. It is three am. That dream sure felt real, huh?
You wander towards the window and look into the november night. No sight of any red-roofed forest shrines anywhere. 
Sighing, you drop back into bed, pull the covers up, and soon slip into a sweet, dreamless, sleep...
""" 
        print "\t"*6, "THE END",
        restart()


def restart():
    restart = raw_input("\nRestart? YES/NO\n")
        
    if restart == "YES":
        print "\nVery well. Here we go again:\n"
        start()
    else:
        print "\nWell... Goodbye. Thank you for playing."

                  
def start():
    print """
\nYou've heard of a legend surrounding the abandoned shrine near your hometown.
They say, that not only is it dangerous, hidden deep in the forest, but-
\tsometimes it swallows the rare curious visitor whole, never to be seen again.
\nNobody really knows what it looks like, if it even truly exists
\tor if it is illusion or fata morgana
\nOnly when winter comes, pulling autumn's lush red leaves to the ground, do the red roofs of it fully emerge out of the tree crowns. It's not eerie at all, no. Quite beautiful, even. But you're sadly not here to marvel at textual landscapes, aren't you?
\nThe real question now is, is it haunted?\n... Perhaps.
"""

    believe = raw_input("\nYour friends don't believe in any myths. Do you? YES/NO\n")
    
    if believe == "YES":
        print """
Of course, you do. You're not sure why. There's actually no real reason behind the story.
No spooky incidents or disappearances, none that you know of, except for hushed rumors and fantasies.
But the feeling of dread persists at the idea of digging deeper. 
Eventually, you turn away from the sight of the temple's gold-ornamented roof. Life goes on.
            """
        print "\t"*6, "THE END",
        restart()
    elif believe == "NO":
        prepare()
    else:
        print "\nIf you don't answer seriously, then shoo!"
        restart()

start()