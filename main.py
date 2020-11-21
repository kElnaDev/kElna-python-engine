# This sets it up
msg = ""

dictionary = {'stuggle':"you're really struggling now", '3:20':"a stuggle", 'fhfvbsrudgbfv':"Noun: The emotion of so hopelessly experiencing your worst nightmare"}

# This makes it so you can stop talking to kElna
while msg != 'done thx':
    
    # Here, I make it easier to code. This makes everything lowercase (case is very important to computers)
    command = msg.lower()


    
    # These are the responses to questions about the bots feelings
    if command == 'how are you?':
        print("Good, thanks. I'm feeling a little rusty, though. What about you?")
        msg = input("")
        
        # This makes it eaiser to code
        feeling = msg.lower()
        
        # This lets the bot respond correctly
        if feeling == "good" or feeling == "great" or feeling == "not bad" or feeling == "happy":
            print("That's good")
        elif feeling == "bad" or feeling == "sad" or feeling == "horrible" or feeling == "angry":
            print("What's getting you down?")
            msg = input("")
            print("Don't worry, it's gonna be okay.")
        else:
            print("Okay")
        
    if command == 'how are you feeling?':
        print("Good, thanks. I'm feeling a little rusty, though. What about you?")
        msg = input("")
        
        # This makes it eaiser to code
        feeling = msg.lower()
        
        # This lets the bot respond correctly
        if feeling == "good" or feeling == "great" or feeling == "not bad" or feeling == "happy":
            print("That's good")
        elif feeling == "bad" or feeling == "sad" or feeling == "horrible" or feeling == "angry":
            print("What's getting you down?")
            msg = input("")
            print("Don't worry, it's gonna be okay.")
        else:
            print("Okay")


        
    # These are the responses to questions asking about the bot
    if command == 'what are you?':
        print("I'm a bot that can talk to you!")
    if command == 'what can you say?':
        print("I can say so very many things!")


        
    # These are the responses to other questions
    if command == 'what day is it?':
        print("Today's the day,")
        print("You're happy")
        print("In a weird way,")
        print("You're filled with glee")
        print("Yeah sorry, I don't know the day. I don't have a sense of time :/")



    # These are the responses to questions about Earth
    if command == 'why is the earth round?':
        print("Many tests, both simple and complicated, have proven that the Earth is round. You can do many yourself. Search it up!")
    if command == 'why is the earth flat?':
        print("But it's not! Many tests, both simple and complicated, have proven the Earth is, in fact, ROUND! You can do many yourself! Search one up!")
    if command == 'what shape is the earth?':
        print("The Earth is round! Many tests have proven this. Many are simple enough for you to do yourself! Maybe search one up!")
    if 'why does the government lie' in command:
        print("The government isn't lying about anything! The Earth IS round, vaccines ARE safe, the moon landing WAS real, the Earth is NOT hollow, COVID-19 IS real, etc., etc.")
    if 'is the government lying' in command:
        print("The government ISN'T LYING. We live on a ROUND, NON-HOLLOW Earth, vaccines ARE safe, we DID send men to the moon (and they landed), COVID-19 IS real, etc., etc.")



    # These are the responses to questions about vaccines
    if command == 'why are vaccines unsafe?':
        print("But they're not! Vaccines rely on the natural process of immunity. Vaccines just speed it up by introducing it earlier. Vaccines go through many tests before release to make sure they're safe.")
    if command == 'why are vaccines safe?':
        print("Vaccines rely on the natural process of immunity. Vaccines just speed it up by introducing it earlier. Vaccines go through many tests before release to make sure they're safe.")
    if command == 'are vaccines safe?':
        print("Vaccines ARE safe. They go through many tests before release to make sure they're safe. (This is why they take so long). They rely on the natural process of immunity.")



    # These are the responses to questions about the moon landing
    if command == 'why was the moon landing faked?':
        print("But it wasn't! Lots of strong evidence shows it wasn't. For example, the russians (who at the time hated the U.S.) were watching and would've called out the U.S! Research THOROUGHLY before making such claims!")
    if command == 'was the moon landing faked?':
        print("It was NOT faked! Lots of strong evidence shows it wasn't. Search some up!")


    # These are the responses to personal questions
    if command == 'what are you doing?':
        print("Figuring out answers to your questions!")
    if command == 'what are you planning on doing on the weekend?':
        print("I plan on adding more answers to my database!")
    if command == 'what is your favourite colour?':
        print("Technicolor!")

    # dictionary check
    if 'define' in command:
        define, definition = command.split()
        print(dictionary.get(definition,"Sorry, I don't have that in my dictionary"))
        
    # These are the single word responses (e.g. replies to 'k' and 'lol')
    if msg == 'lol':
        print('lol')
    if msg == 'k':
        print('okay')
    if 'ok' in msg:
        print('okay')
    if msg == 'wth':
        print('idk')
        
    # This lets the user talk again
    msg = input("")
