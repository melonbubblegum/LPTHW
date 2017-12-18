from random import randint
# -*- coding: utf-8 -*-

# add and define enter, also textual fun
class Scene(object):

	def add(other):
		other.health += randint(0, 20)

	def take(other):
		other.health -= randint(0, 20)

	def overworked(other):
		other.health -= randint(15, 20)

	def breaktime(other):
		other.health -= randint(15, 20)

class Life(Scene):
	def __init__(self, health):
		self.health = health

class Startover(Scene):
	def workmore(self):
		new_game = raw_input("Work another shift? YES/NO\n> ")

		if new_game == "YES":
			print "GOOD"
			# return 
		elif new_game == "NO":
			print "OK BYE THEN!"

		else:
			return 'anew'

# add returns and textual fun
class Feierabend(Scene):
	def how_r_u(self, other):
		if other.health >= 50 and other.health <= 100:
			print "you're still alive"
			# return 'anew'
		elif other.health <= 50 and other.health >= 0:
			print "you collapse bc of exhaustion"
			# return 'anew'
		else:
			print "Uh. This actually shouldn't be possible?!"
			# return 'closed'

# add returns
class Entrance(Scene):
	def start(self):
		print "You've started an odd job sometime ago. Not too long, to be used to it,"
		print "but also not too short to be overwhelmed with the novelty of it."
		print "\nYou've taken up the position of waiting staff at a new eatery near your"
		print "apartement, and although it seemed normal at first, you do have some weird"
		print "stories to tell about it. Either way, you actually do feel quite well welcomed."
		print "Once again, you start your Friday shift today."
		print "Was your week GOOD or BAD until today?"
		energy = raw_input("> ")

		if energy == "GOOD":
			print "Nothing you couldn't handle, anyway."
			#
		elif energy == "BAD":
			print "You kinda think you pissed Karma or some deity off,"
			print "and you feel accordingly."
			Scene.take(Me)
			#
		else:
			print "You don't want to think about it - only gibberish resides in your head."
			Scene.overworked(Me)
			print Me.health
			#

# add returns
class Hipster(Scene):
	def instagrammable(self):
		print "You're relieved to have had only nice customers this afternoon."
		print "That is, until you meet... this guy sitting in the corner."
		print "His seating location gives him the privilege of quiet and"
		print "the window row besides him illuminates his table with clear"
		print "natural sunlight. He wears a t-shirt and open flannel combo" 
		print "with a beanie over a low manbun and, man, is his hair more luscious than yours."
		print "When you approach him, he's curtly asking for your signature item\nbut you have no idea about that."
		print "You tell him the usual simple stuff \n(because, really: everyone else just gets what they actually wanna drink.)"
		print "He snorts condescendingly. 'Then what do you recommend?'\n You feel like you've been posed the 1 Million Dollar question."
		print "\nA quick look at the menu on the wall gives you a few options."
		print "From the top of your head, you think of the usuals:"
		print "You like to rec the extra foamy caramel and hazelnut LATTE "
		print "or a HOMEBLEND of either tea or coffee."
		print "There's also mermaid superfruit black SMOOTHIE"
		print "or you could confuse him with an ultra evasive allusion to some nonexistent SECRET MENU"

		rec = raw_input("> ")

		if rec == "SMOOTHIE" or rec == "SECRET MENU":
			print "HM YEAH"
			Scene.take(Me)
		elif rec == "HOMEBLEND" or rec == "LATTE":
			print "NAH"
			Scene.take(Me)
		else:
			print "You're doing a terrible job, sweetie."
			print "One of your colleagues thankfully saves you from further escapades"
			print "and takes over. You see Mr. Flannel roll his eyes at you, and you"
			print "obnoxiously roll your eyes right back."
			Scene.overworked(Me)
			# return

# add returns 
class Waitress(Scene):
	def take_a_break(self):
		print "You decide to take a break, far away from your ridiculous customers."
		print "Your coworker Molly is also in the breakroom. She smiles as you come in."
		print "She can tell you a story. Would you like to hear it?"
		print "With a mischievous voice, she says that you can even influence some of it."
		print "Like, y'know, in a real computer game. Only that, of course,\n\nthis is reality.\n\nDAM DAM DAAAAAAAA!\n"
		print "Anyway. She looks at you expectantly. 'Think of it as a fun sidequest in the game of life!', she quips."
		print "You do have time for a short chat with her, don't you?"

		storytime = raw_input("YES/NO > ")

		if storytime == "YES":
			print "Molly cheers. 'Swell! Ok, so here goes: Imagine you live in a beautiful town, full of history..."
			print "The quaint streets and the rural atmosphere brims with legends. One of them is at the core this story."
			print "And! You're the main character!' She winks at you, before going on with her storytelling..."
			import firstgame
			print "After you played through her story, she looks expectant again.'Whaddaya think about it?\nIt's nice, right?"

			dis_likey = raw_input("YES/NO\n> ")

			if dis_likey == "YES":
				print "\nYou decide to answer in the positve."
				print "\nOut of politeness, or even real enjoyment - why ever: whatever."
				print "You only know that you feel kind of energised "
				Scene.add(Me)
				#
			else:
				print "\nAw, Man. Whatever. That's not nice."
				print "\nMolly doesn't think so either. You both leave the room"
				print "(she does so earlier than you) and to your added stress from your"
				print "eccentric customers, you feel tense."
				Scene.take(Me)
				print Me.health
				#
		else:
			print "She shrugs her shoulders at your dumb answer. 'I have to get to work soon, anyway,' she says nonchalantly."
			print "Winsome waitress smile on her face, she leaves the room."
			print "Afterwards, you kinda feel tense. And it is with this feeling, you return to duty."
			Scene.take(Me)
			#

class Cook(Scene):
	pass

class Waiter(Scene):
	pass

class TheCafe(object):

	tables = {
		'open': Entrance()
		'kitchen': Cook(),
		'breakroom': Waitress(),
		'bar': Waiter()
		'table1': Hipster(),
		'table2': Diva(),
		'table3': BFF(),
		'closed': Feierabend.enter(),
		'anew': Startover.workmore()
	}

	def __init__(self, start_scene):
		self.start_scene = shift_starts

	def wait_table(self, client):
		val = TheCafe.tables.get(client)
		return val

	def new_shift(self):
		return self.wait_table(self.shift_starts)

class Player(object):
	def __init__(self, the_cafe):
		pass

	def play(self):
		pass


Me = Life(100)
the_cafe = TheCafe('open')
an_odd_job = Player(the_cafe)
an_odd_job.play() 
