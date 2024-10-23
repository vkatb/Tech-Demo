# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define w = Character("Pie Wizard")
define d = Character("Pie Demon")

# The game starts here.
label start:

    scene black
    
    "It's finally the day."

    "You've trained for so long, studied the arcane arts, honed your skills..."

    "And now you must put them to the test."

    "Your continued apprenticeship under the (Great Wizard) depends on it!"

    "The (Wizard's) test for you…"

    scene bg room # REPLACE WITH FIRST BACKGROUND
    with fade # Saw this in The Question so I'm doing it here

    "...is to successfully bake a pie!"

    show eileen happy # REPLACE WITH WIZARD NEUTRAL FACE (or excited?)
    with dissolve

    w "Up bright and early today, I see! Are you ready for your final test?"
    
    "You push down any doubts. You have to be ready."

    y "Yes I am, Great Pie Wizard!"

    w "Well, go ahead then. Show me how you'll bake this pie!"

    y "I won't disappoint you!"

    "You studied the cookbooks and summoning rituals fervently for the past week."

    "You should have all the materials you need, but..."

    "You still need to decide."

    menu:
            
            "Are you going to bake this pie with your own hands or use your magic to help you?"

            "Use your own hands":

                jump physical # Goes to the section labelled physical, aka the no magic section.
            
            "Use your magic":

                jump magical # Goes to the section labelled magical, aka the magic section.

label physical:

    hide eileen happy # REPLACE WITH WIZARD. Removes wizard from screen
    with fade
    
    "You recall an ancient recipe book, one that has been passed down through generations of your family."
    
    "Yes, that's what you need! Your recipe book! then you can make a pie for the Wizard!"
    
    "You rush off to find the book, then head for the kitchen..."

    scene bg room # REPLACE WITH KITCHEN!
    with dissolve
    
    "With the book in hand, you flip through the pages, and..."
    
    y "Wow, it's so convenient I have all the ingredients in this kitchen fridge!"
    
    # ((pie crust.jpg flies in from bottom of screen and fades out shortly after))
    
    "You place one pie crust in the bottom of a 9-inch pie plate and crimp to your desire."
    
    #((lemons.jpeg flies in from bottom of screen and fades out shortly after))
    
    "You juice your lemons until you have 15mL exactly of lemon juice."
    
    #((raspberries.jpeg flies in from bottom of screen and fades out shortly after))
    #((sugar.jpeg flies in from bottom of screen and fades out shortly after))
    #((cornstarch.jpeg flies in from bottom of screen and fades out shortly after))
    
    "You mix your raspberries, sugar, lemon juice, and cornstarch together and pour the mixture into your pie plate."
    
    y "Wow, this is really starting to come together…"
    
    #((pie crust.jpg flies in from bottom of screen and fades out shortly after))
    
    "You top the pie with a second crust."
    
    y "Hmm... I need to put holes in the top so it doesn't explode in the oven."
    
    "You use a knife to carve vents into the pie."
    
    y "Into the oven it goes!"
    
    "You place the pie in the oven, conveniently preheated to 425°F."
    
    "And after you bake for 10 minutes at 425°..."
    
    "Then lower the temperature to 350°F and bake for about 30-40 minutes, or until crust is baked through and golden..."

    #((pie.jpeg appears on screen))
    
    y "Yay! A pie!!!!!!!!!"

    "Now it's time to show your wonderful creation to the Wizard..."

    "Even if you like how it looks, you feel a little nervous about his judgement."

    jump ending



label magical:
    
    hide eileen happy # REPLACE WITH WIZARD. Removes wizard from screen
    with fade
    
    "You recall an ancient spellbook that speaks of a being that may assist you in this."
    
    "That's what you need! The summoning ritual spellbook!"
    
    "You rush off and find the tome, then head to the kitchen..."
    
    scene bg room # REPLACE WITH KITCHEN!
    with dissolve

    "With the ancient spellbook in hand, you flip through the pages, and recite the incantation..."
    
    y "In shadows deep where secrets lie, I call upon the pie demon nigh."
    
    y "With crust so golden, filling divine, Come forth, oh spirit, make your presence mine!"
    
    show piedemon confused #((...appearing on screen with a bounce, confused))
    with fade # May delete this.
    
    d "Hey! Whoa, whoa, whoa! You summoned me? A pie demon? You think I'm just gonna pop up and serve you dessert? This ain't no bakery, sweetheart!"
    
    "The Pie Demon has a New York accent???"
    
    y "I just need some help in baking this pie, sir. Maybe some evil power on the side."
    
    show piedemon neutral
    with dissolve
    
    y "Evil power? You think I got that cookin' in my oven? I'm here for the pies, capisce?"
    
    "You try not to fluster at your mistake, and give him a thumbs up."
    
    y "Capisce."
    
    d "You want pie? How about I whip up a raspberry pie that for ya?"
    
    d "But first you gotta show me a little respect!"
    
    y "R-respect…?"
    
    show piedemon happy #originally this was confused, but we don't have a focused pose so I swapped it around a bit.
    with dissolve 
    
    d "Yeah! I'm not just some run-of-the-mill pastry chef, okay? I make the best pie in the whole underworld! You treat me right, and I'll treat you right."
    
    show piedemon confused #this pose looks the most like a focused pose, so I swapped it. See above!
    with dissolve
    
    d "Now, where's a focus? I can't just make magic happen without a focus, ya know?"
    
    y "Oh! Uh, I think it's over here..."
    
    "You grab your magical cookware over, and he takes out of your hands in an eager motion."
    
    "After some chanting and with a bright flash of light..."
    
    #((Show pie.jpeg, switch to pie demon’s celebratory pose))
    show piedemon celebratory #Not sure how to show pie yet so I'm just showing the demon
    with dissolve

    d "One magic pie, complete!" 
    
    d "But listen, this pie's got a mind of its own. I mean, look at it! It's glistening like it's ready for a Broadway show."
    
    d "Plus, I put a little extra spice in there."
    
    y "Thank you so much Pie Demon, sir."

    "The Pie Demon grins wordlessly, then dissappears from sight."
    
    hide piedemon celebratory
    with dissolve

    "Now it's time to show this demonic pie you have off to the Wizard..."

    "Even if you like how it looks, you feel a little nervous about his judgement."

    jump ending

label ending:
    
    "End game here! Planning to add an if statement or maybe just separate these into physical and magical ending labels."

    # This ends the game.
    return
