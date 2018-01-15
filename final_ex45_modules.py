# I tried:
# import firstgame
# then:
# from firstgame import *
# but both just ... play out right at the start if I 
# write them at the beginning ...
# So I nested the import inside the if-else in Waitress() again.
from sys import exit
from random import randint

class Scene(object):
	def add(self, other):
		other.health += randint(0, 20)

	def take(self, other):
		other.health -= randint(0, 20)

	def overworked(self, other):
		other.health -= randint(15, 20)

	def breaktime(self, other):
		other.health -= randint(15, 20)

class Player(object):
	kitchenvisit = 5
	SeenThisAlreadyRollsEyes = False

	def __init__(self, health):
		self.health = health
		self.table = table

	def play(self):
		current_table = self.table.new_shift()
		last_table = self.table.next_table('closed')

	while current_table != last_table:
		next_client = current_table.enter()
		current_table = self.table.next_table(next_client)

	current_table.enter()

class Entrance(Scene):
	def start(self):
		print """
		You've started an odd job sometime ago. Not too long, to be used to it,
		but also not too short to be overwhelmed with the novelty of it.

		You've taken up the position of waiting staff at a new eatery near your
		apartement, and although it seemed normal at first, you do have some weird
		stories to tell about it. 

		Either way, you actually do feel quite well welcomed and once again, 
		you start your Friday shift this today.

		Was your week GOOD or BAD until today?
		"""
		energy = raw_input("> ")

		if energy == "GOOD":
			print "Nothing you couldn't handle, anyway."
		elif energy == "BAD":
			print "You kinda think you pissed Karma or some deity off. So, you feel accordingly."
			Scene.take(Me)
		else:
			print "You don't want to think about it - only gibberish resides in your head."
			Scene.overworked(Me)

		print """
		You arrive, get dressed, then head down to ... well, actually, where to first? 

		Worry not, here are the options: Go handle some GUEST first, or go goof off with
		your COLLEAGUES in the breakroom?
		"""

		begin = raw_input("(There are no other options. I'm honestly a little sorry.) > ")

		if begin == COLLEAGUES:
			print """"
			You're a lazy one, and that's fine. In-game, you're working a little first,
			anyway. But here you go: Have a break first. 

			It's not a wise decision, let's be honest. Pausing right off the start? As you're
			the player, I can only say: power to you. 
			"""
			return 'breakroom'
		elif begin == GUEST:
			print """
			Gutsy! Or the normal, level-headed, sensible choice, anyway. 

			So you work your shift first. There are a lot of uncomplicated,
			friendly customers today. Did something good happen, recently? 
			You don't know. 

			Working on unbothered, you eye your next guest...
			"""
			Scene.add(Player.Health)
			return 'table1'
		else:
			print "BOOM! Magic option! Return to square one."
			Scene.take(Player.health)
			return 'open'

class Waitress(Scene):

	if Player.kitchenvisit >= 2:
		print "You have visited the kitchen and breakrooms %d times today. Which makes this visit Number %d." % (Player.kitchenvisit, Player.kitchenvisit + 1)
		Player.kitchenvisit = Player.kitchenvisit + 1

		print """
		You've clearly exceeded your amount of breaks for a day. 
		No matter how bad the day went, your boss would fire you
		for this many breaks in a single afternoon shift.

		Annoyed, you turn back from your trudge to the kitchen doors, 
		lingering around there for a while (which is totally not a break),
		then head back into the crazy battlefield that is your waitressing
		job.

		...

		...

		When the clock strikes eight, you have to reign in the burst of 
		happiness about to spill from your lips. What a day! 
		"""

		return 'closed'
	elif Player.kitchenvisit <= 1:
		def take_a_break(self):

			if Player.kitchenvisit == 0:
				print """
				Ah, the breakroom. It's very easy to find - just weasel through the public salon
				and then right through the kitchen, past the grumpy chef who eyes you glaringly.
				Luckily for you, I didn't code this exhausting encounter, so let's just skip to the 
				good parts, amirite?

				You find the room just as it was last week: neat and cozy, albeit small and a little
				barren. At the tiny table, you spot your coworker Molly who just took the final bite
				of an absolutely delicious sandwich. (This reminds you that you forgot to pack your
				own at home in your hurry to rush here on time. Curse you, Shop Manager! If you die of
				malnutrition, it surely is their fault! Or at least that's what your documents are going
				to state if you have any say in it.) 
				"""
			else:
				print """ 
				Molly smiles as you come in. She takes a sip from her soda. (Does she have an endless supply
				of melon soda? You never see her drink anything else.) With a mischievous voice, she offers to 
				tell you a story, decorating it with big words like escapism, mellifluous and avantgarde. 

				You know the story already, of course. It's that one, the same one as always, but she just 
				doesn't get tired of it.

				As always, she says that you can even influence some of it.
				'Like, y'know, in a real computer game. Only that, of course...

				this is reality.' She nudges you. 

				(You could've sworn you heard dramatic piano punching in the background just now. Somebody 
				has great timing and either a jukebox or a real piano. Allegro!)

				Anyway. 

				She looks at you expectantly. 

				'Think of it as a fun sidequest in the game of life!', she quips.

				You do have time for a short chat with her, don't you?
				"""

				storytime = raw_input("YES/NO > ")

				if storytime == "YES":
					print """
					Molly cheers. 'Swell! Ok, so here goes: Imagine you live in a beautiful town, full of history...
					The quaint streets and the rural atmosphere brims with legends. One of them is at the core this story.
					And! You're the main character!' 

					She winks at you, before going on with her storytelling... taking a deep breath and clearing her throat...

					"""
					import firstgame

					print "After you played through her story, she looks expectant again.'Whaddaya think about it? Nice, right?"

					dis_likey = raw_input("YES/NO > ")

					if dis_likey == "YES":
						print """
						You decide to answer in the positve.
						Out of politeness, or even real enjoyment - why ever, whatever.
						You only know that you feel kind of energised now, so good for you!

						You bid her adieu, to go back to the job...
						"""

						Scene.add(Player.health)
						
						if Player.SeenThisAlreadyRollsEyes == True:
							print "Ah. As you make your way back, you sense your shift ending. A quick glance at the clock proves true."
							return 'closed'
						elif Player.SeenThisAlreadyRollsEyes == False:
							return 'table1'
						else:
							print "MAGIC OPTION! Return to square one."
							return 'open'
					elif dis_likey == "NO":
						print """
						Wow, first off, as the narrator of this AMAZING STORY: Rude af. 
						You could've also just say something vaguely polite to keep the peace. 
						Ever heard of a white lie?

						Molly is shocked, also. 'Oh,' she whispers, eyes downcast. 'I-I guess I'll
						do a better job of making it exciting next time..." She dejectedly fiddles 
						with the drinking straw.

						You know that she will recover very, very soon, but the fatal puppy dog
						eyes still hit you hard. Kidney function is not a right - it's a privilege.
						A privilege that you've felt like you've given it right up for a second,
						poison infusing your system.

						You meekly leave the room...
						"""

						if Player.kitchenvisit <= 1:
							Scene.take(Player.health)
						else:
							Scene.overworked(Player.health)

						if Player.SeenThisAlreadyRollsEyes == True:
							return 'closed'
						elif Player.SeenThisAlreadyRollsEyes == False:
							print """
							As you get into the swing of things again, you spot a customer whose face is 
							hidden by a menu card. You can't remember if he's ordered already, and a quick
							glance at the other waiters tells you they don't think so either. (Magical waiter
							telepathy ftw.)

							You head over... It's table #12. Totally a lucky number. 
							"""
							return 'table1'
						else:
							print "MAGIC OPTION! Return to square one."
							return 'open'
					else:
						print """
						Aw, Man. Whatever. That's not nice, to just outright ignore someone like that. 

						Molly doesn't think so either. You both leave the room, (she does so earlier than you)
						and to your added stress, you feel extremely tense. 

						Why couldn't you just have said something... no, anything else? What were you even
						saying? Nevermind. 

						You're on the lookout for the next task now, fleeing the scene towards the customers. 
						"""
						Scene.take(Player.health)
						Scene.overworked(Player.health)
						
						if Player.SeenThisAlreadyRollsEyes == True:
							print """
							You actually don't feel like working anymore. Which is, in fact, good: when you
							listlessly turn your head toward the stylish brass clock mounted on the wall over 
							by the cashier and counter, you see it's already five o'clock!

							It's over! You scramble towards your Feierabend like a loonatic... 
							"""
							return 'closed'
						elif Player.SeenThisAlreadyRollsEyes == False:
							print """
							As you get into the swing of things again, you spot a customer whose face is 
							hidden by a menu card. You can't remember if he's ordered already, and a quick
							glance at the other waiters tells you they don't think so either. (Magical waiter
							telepathy ftw.)

							You head over... It's table #12. Totally a lucky number. 
							"""
							return 'table1'
						else:
							print "MAGIC OPTION! Return to square one."
							return 'open'
				else:
					print """"
					She shrugs her shoulders at your dumb answer, her forehead in folds. 

					'I have to get to work soon, anyway,' she says nonchalantly, dropping the empty soda can,
					drinking straw inclusive, into the pastel minimalist wastebin that she brought solely for her
					soda trash. (It's sitting right next to the garbage can for mortal people, rusted iron.) 

					Winsome waitress smile on her face, she leaves the room. You're sure she'll be back, soon though. 
					Afterwards, you kinda feel sad. Wasted a perfectly good decision with your incoherent blarghle. 

					And it is with this feeling, you return to duty.
					"""
					Scene.take(Player.health)

					if Player.SeenThisAlreadyRollsEyes == True:
						print """
						As soon as you return, you find your shift ending.
						Can I get a hooray for cool coincidences?

						None? 

						Good, less to code for me. 

						You file out of the room, sighing out of relief. Finally,
						finally, finally, it's over with.
						"""
						return 'closed'
					elif Player.SeenThisAlreadyRollsEyes == False:
							print """
							As you get into the swing of things again, you spot a customer whose face is 
							hidden by a menu card. You can't remember if he's ordered already, and a quick
							glance at the other waiters tells you they don't think so either. (Magical waiter
							telepathy ftw.)

							You head over... It's table #12. Totally a lucky number. 
							"""
							return 'table1'
					else:
						print "MAGIC OPTION! Return to square one."
						return 'open'
	else:
		print "Huh. This is a dead end? It's not supposed to be, that's for sure."
		print "The only logical solution is to restart ... from the very beginning!"
		return 'anew'

class Hipster(Scene):
	def instagrammable(self):
		Player.SeenThisAlreadyRollsEyes = True

		print """
		You're relieved to have had only nice customers this afternoon. Naively,
		there's no shred of doubt in you that questions this status quo. Oh, don't
		they teach you this in university, my sweet summer child? 
		
		Past one oddly relieved-looking colleague, you approach ... this guy sitting 
		in the corner table #12. Right now. 

		His seating location gives him the privilege of quiet and the window row besides 
		him illuminates his table with clear, natural sunlight. He wears a t-shirt and open 
		flannel combo with a beanie over a low manbun and, man, is his hair more luscious than 
		yours. (That's probably also because he does not work here part-time. Wise decisions...)

		When you approach him, he's curtly asking for your signature item. Do you have no idea 
		about that, or what. Signature item ... Me? Oh, I don't know either. So you tell him the 
		usual simple stuff. (Because, really: everyone else just gets what they actually wanna drink.)

		He snorts condescendingly. 'Then what do you recommend?'

		You feel like you've been posed the 1 Million Dollar question.
	
		From the top of your head, you think of the usuals:
		You like to rec the extra foamy caramel and hazelnut LATTE 
		or a HOMEBLEND of either tea or coffee. 
		(Both very good - or at least the aficionados tell you so. But isn't that
		also what makes them aficionados of something...?)
			
		A quick look at the menu on the wall provides you with a very decent option:
		Some fashionable barista had recently added mermaid superfruit black 
		SMOOTHIE with vanilla honey fluff and almond-pistachio pate.
		(You wager it's Molly's idea, she loves that stuff. You've never seen her actually eat
		or drink something like that - just melon soda and blueberry tartelettes - but
		her social media accounts all are ... just ... incredible.)
		
		... You could also simply confuse him with an ultra-evasive allusion to some 
		nonexistent SECRET MENU. (Tempting! Very tempting! You did that with the last
		overly self-conscious customer.)
		"""

		rec = raw_input("What do you think will pacify the man-bunned nitpick? > ")

		if rec == "SMOOTHIE":
			print """
			You go wild. Not sure about what the smoothie is about or what's inside, 
			you rave on and one about it. The word exclusive might have fallen numerous
			times, as well as unique and it's best friends 'trending on instagram'. Thank
			God you listen to Molly ramble sometimes - it's super useful. You swear she 
			knows everything and can probably do everything, also. As for you? Copying her 
			works, at least. 

			Mr. Flannel's eyes twinkle. It makes you think to ensure he gets the most extravagant
			thing this entire caf- no, scratch that: universe has ever laid eyes upon. It's gonna
			be mermaid as all high water can be, and darker black than actual vulcano ash. 

			When you bring back his order (giving Devlynn, your local barista and general enthusiast
			exact instructions on how to build this gargantuan thing), he actually smiles. Not any kind
			of smirk, no: he smiles. 

			Wow, so he's only human, too, you think, serving his super smoothie with a super smile. 

			You cannot believe it, but he's really happy. Props to you. Turning away to other clients,
			you resume your job, feeling lighter than before. 
			"""
			Scene.breaktime(Player.health)

			if Player.kitchenvisit >= 3: 
				print "Aren't you a lucky one? Your shift is over in the blink of an eye."
				return 'closed'
			else:
				print "You decide to pamper yourself with a break."
				return 'breakroom'
		elif rec == "HOMEBLEND" or rec == "LATTE":
			print """
			Wow. You feel like you've tamed a beast. 

			He accepts your recommendation quietly. Just like that. Baffled, you ask
			if that would be all? No sneer, no scoff, just a nod. 

			You relay his order back to the kitchen and bring him back an exquisitely 
			warm beverage. He mumbles a thanks distractedly as he sets up his camera 
			and works.

			You're not sure how to feel about this, but you're no Trojan, so you don't
			worry about a gift horse. Soon enough, a new customer arrives and you 
			go to entertain their wiles.
			"""
			Scene.take(Player.health)
			Scene.add(Player.health)

			if Player.kitchenvisit >= 3:
				print """
				After a while, you look up at the clock. 
				
				It's 5pm! 
				
				Which means you're free to leave. Oh, how absolutely free you feel to
				do so. You scramble towards in the hallway before the breakroom
				to hang your apron away, then hastily make to exit this ... eatery.
				"""
				return 'closed'
			else:
				print """
				After a while, you figure you could use a break. 

				So that's exactly what you do. Don't forget to hang your apron on the hooks in 
				the hallway between kitchen and breakroom! The last time you brought your uniform 
				there, you left with a nasty coffee spill. How does that happen in your break, anyway?
				Now, that's another story.

				When you enter, there's a familiar sight awaiting you. 
				"""
				return 'breakroom'
		elif rec == "SECRET MENU":
			print """
			Oh snap. Look at his eyes: He sees right through your lies.

			'Dude,' he says, totally assuming your gender which should infuriate him
			the most, actually. Or is dude a neutral term? Are we all dudes in the end
			of our long (or in your case: about to be drastically shortened) life? 'If
			there's nothing decent here, just tell me. I'm not buying this.'

			He leans over to you, like fashion critics at the NY Fashion Week runways. 
			As if spilling secrets about the latest gossip about Anna Wintour's new
			hair (which will not happen, I tell you!) or another Westwood work 
			having the world of couture agasp.

			'The interior design here is icky anyway...' He stroked the table, disgusted 
			with the regular oak wood. 'Can't catch any good pictures with bad backgrounds
			anyway.'

			You try your hardest to convince him to stay (how did you manage NOT to rip-off
			a guy like that? Look at him! He's a walking money bag! What a shame...), but 
			he saunters off, eyes rolling. 

			He leaves you a tip. And that tip is: 'The boutique patisserie around the corner
			also has some cheap sweets options. You look like you need some. One macaron for 4
			bucks, I tell ya.'

			You just nod your non-descript answer to that.
			"""
			Scene.overworked(Player.health)

			if Player.kitchenvisit >= 2:
				print "When you watch the clock strike five, you manage a meagre sigh. Shift: ended. Time to file out!"
				return 'closed'
			else:
				print "You're desperately in need of a break. Trudging towards the breakrooms, you're greeted by a familiar sight."
				return 'breakrooms'
		else:
			print """
			With one single input, you're unstoppable: 
			As if out of your control, your mouth starts babbling off.
			You string sentences together out of a nonsensical amalgam of words. If one 
			were a very kind person, the things you spout might be described with
			neologisms inspired by an avantgarde sense of spirituality, or genius 
			untamed by mankind.

			But as it is, you're just grumble-growling, hiss-howling, splutter-saying
			utter nonsense. Your eyes glaze over, your mouth foams - you turn into a
			beast of idiocy, convulsing with spiteful sounds. 

			Oh, what are you even doing?

			May I be honest with you? 

			You're doing a terrible job, sweetie.

			One of your colleagues thankfully saves you from further escapades
			and takes over. A calm hand on your shoulder, he soothes you from 
			your borderline supernatural wrath and you slump down, exhausted.

			You see Mr. Flannel roll his eyes at you, inconvenienced but unbothered.
			You know - just like you know that he's gonna be making a post on any of 
			his worn social media accounts out of this event, tagging it with #crankywaitress
			or #coffee, #chill, #avocado - that you'll meet again and when that happens,
			he will pay.

			Though right now all you can do is obnoxiously roll your eyes right back.

			Your coworker shushes you into the kitchen, convincing you to take a break.
			Of course, you know it's to limit the wildfire, that is your grandiose self. 
			As he pushes you away, he mutters:

			'Why does the boss always have to take a liking to the weird ones...'
			"""
			Scene.overworked(Player.health)
			Scene.overworked(Player.health)
			return 'breakroom'

class Feierabend(Scene):
	def end_shift(self):
		print """
		Leaving your work place, you can't help but ponder about it. 
		You'd rate day as ... %d out of 100.
		""" % Player.health
		print
		if health >= 50:
			print """
			That's decent.

			Can't believe you're still alive after that ordeal? Me neither. But
			here we are, anyway. Sometimes life can be just that sweet. You skip
			down the sidewalk, ready and rested for the weekend. 
			"""
			return 'anew'
		elif health <= 50:
			print """
			That's ... you're feeling awful. Yes. That's it. 

			It's been a hard week for you, and it's been an even harder shift to beat.
			What a time to be alive? Cough, sarcasm, cough, cough. (Or are you coughing
			because you just feel that unwell? Yikes. Either or both likely true.)

			You sluggishly drag yourself home... just don't think about this week's
			assignments, or the deadlines. Ugh. I feel you, sweetheart.
			"""
			return 'anew'
		else:
			print """
			Uh. This actually shouldn't be possible?!

			How did you land here? 

			You deserve a haiku. I call it:
			'Please have mercy! Though I'm a snake, I don't understand Python too well!'

			I beg of you mercy,
			Though a snake I am, Python
			I don't understand. 

			...


			...

			Let's just restart, alright?
			"""
			return 'open'

class Startover(Scene):
	def workmore(self):
		print """
		Congratulations, you've reached the end of this little slice of hell game!
		That's nice because that means you didn't encounter any bugs. Or at least 
		unsignificant ones. 
		"""
		new_game = raw_input("Do you have the nerves to work another shift? YES/NO > ")

		if new_game == "YES":
			print "That's incredible. But all the power to you! So here goes, again:"
			Player.kitchenvisit = 0 
			Player.SeenThisAlreadyRollsEyes = False
			return 'open' 
		elif new_game == "NO":
			print """
			A sensible decision. Here a goodbye haiku.
			I call it 'Goodbye Haiku':

			the season's pass like this
			game right here. Stopping
			is the right choice.

			THE END
			"""
		else:
			print "Hey! The options clearly state YES or NO. As punishment... well, nothing. BYE!"
			

# I dropped the other scenes because I would need
# more print "story-telling etc." if I kept them.
# But that would take too much of my time
# I tend to get really into the writing... 
# and cannot stop myself. They would essentially 
# work the same as Hipster()/Waitress().
class TheCafe(object):

	tables = {
		'open': Entrance(),
		#'kitchen': Cook.function(),
		'breakroom': Waitress(),
		#'bar': Waiter.function(),
		'table1': Hipster(),
		#'table2': Diva.function(),
		#'table3': BFF.function(),
		'closed': Feierabend(),
		'anew': Startover()
	}

	def __init__(self, first_table):
		self.first_table = first_table

	def wait_table(self, client):
		val = TheCafe.tables.get(client)
		return val

	def new_shift(self):
		return self.wait_table(self.first_table)

