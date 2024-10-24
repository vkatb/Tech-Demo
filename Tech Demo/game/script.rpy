# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define w = Character("Pie Wizard")
define d = Character("Pie Demon")

default normalEnd = False # variable for what ending you get

# The game starts here.
label start:

    scene black
    
    "It's finally the day."

    "You've trained for so long, studied the arcane arts, honed your skills..."

    "And now you must put them to the test."

    "Your continued apprenticeship under the Great Wizard depends on it!"

    "The Wizard's test for you..."

    scene bgroom # REPLACE WITH FIRST BACKGROUND
    with fade # Saw this in The Question so I'm doing it here

    "...is to successfully bake a pie!"

    show piewizardneutral
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
 
    $ normalEnd = True # Sets normal ending variable to true
    hide piewizardneutral
    with dissolve
    
    "You recall an ancient recipe book, one that has been passed down through generations of your family."
    
    "Yes, that's what you need! Your recipe book! then you can make a pie for the Wizard!"
    
    "You rush off to find the book, then head for the kitchen..."

    scene bgkitchen # shows kitchen
    with fade
    
    "With the book in hand, you flip through the pages, and..."
    
    y "Wow, it's so convenient I have all the ingredients in this kitchen fridge!"
    
    # ((pie crust.jpg flies in from bottom of screen and fades out shortly after))
    
    "You place one pie crust in the bottom of a 9-inch pie plate and crimp to your desire."
    
    show lemoningredient
    with dissolve
    play sound "CuttingFood.mp3" fadein 0.5 fadeout 0.5

    "You juice your lemons until you have 15mL exactly of lemon juice."
    
    #((raspberries.jpeg flies in from bottom of screen and fades out shortly after))
    #((sugar.jpeg flies in from bottom of screen and fades out shortly after))
    #((cornstarch.jpeg flies in from bottom of screen and fades out shortly after))
    hide lemoningredient
    show ourpowerscombined
    with dissolve
    
    "You mix your raspberries, sugar, lemon juice, and cornstarch together and pour the mixture into your pie plate."
    
    y "Wow, this is really starting to come together..."
    
    #((pie crust.jpg flies in from bottom of screen and fades out shortly after))
    
    hide ourpowerscombined

    "You top the pie with a second crust."
    
    y "Hmm... I need to put holes in the top so it doesn't explode in the oven."
    
    "You use a knife to carve vents into the pie."
    
    y "Into the oven it goes!"
    
    "You place the pie in the oven, conveniently preheated to 425°F."
    
    "And after you bake for 10 minutes at 425°..."
    
    "Then lower the temperature to 350°F and bake for about 30-40 minutes, or until crust is baked through and golden..."

    show applepie
    with dissolve
    
    y "Yay! A pie!!!!!!!!!"

    "Now it's time to show your wonderful creation to the Wizard..."

    "Even if you like how it looks, you feel a little nervous about his judgement."

    jump ending



label magical:

    hide piewizardneutral # Removes wizard from screen
    with dissolve
    
    "You recall an ancient spellbook that speaks of a being that may assist you in this."
    
    "That's what you need! The summoning ritual spellbook!"
    
    "You rush off and find the tome, then head to the kitchen..."
    
    scene bgkitchen # Shows the kitchen
    with fade

    "With the ancient spellbook in hand, you flip through the pages, and recite the incantation..."
    
    y "In shadows deep where secrets lie, I call upon the pie demon nigh."
    
    y "With crust so golden, filling divine, Come forth, oh spirit, make your presence mine!"
    
    show piedemonconfused #((...appearing on screen with a bounce, confused))
    play music "DemonMusic.mp3" loop fadein 1.0
    with dissolve
    
    d "Hey! Whoa, whoa, whoa! You summoned me? A pie demon? You think I'm just gonna pop up and serve you dessert? This ain't no bakery, sweetheart!"
    
    "The Pie Demon has a New York accent???"
    
    y "I just need some help in baking this pie, sir. Maybe some evil power on the side."
    
    show piedemonneutral
    hide piedemonconfused
    
    y "Evil power? You think I got that cookin' in my oven? I'm here for the pies, capisce?"
    
    "You try not to fluster at your mistake, and give him a thumbs up."
    
    y "Capisce."
    
    d "You want pie? How about I whip up a raspberry pie that for ya?"
    
    d "But first you gotta show me a little respect!"
    
    y "R-respect...?"
    
    show piedemonhappy #originally this was confused, but we don't have a focused pose so I swapped it around a bit.
    hide piedemonneutral

    d "Yeah! I'm not just some run-of-the-mill pastry chef, okay? I make the best pie in the whole underworld! You treat me right, and I'll treat you right."
    
    show piedemonconfused #this pose looks the most like a focused pose, so I swapped it. See above!
    hide piedemonhappy
    
    d "Now, where's a focus? I can't just make magic happen without a focus, ya know?"
    
    y "Oh! Uh, I think it's over here..."
    
    "You grab your magical cookware over, and he takes out of your hands in an eager motion."
    
    "After some chanting and with a bright flash of light..."
    
    hide piedemonconfused
    with dissolve
    show applepie
    with dissolve

    d "One magic pie, complete!" 
    
    hide applepie
    with dissolve
    show piedemoncelebratory #Not sure how to show pie yet so I'm just showing the demon

    d "But listen, this pie's got a mind of its own. I mean, look at it! It's glistening like it's ready for a Broadway show."
    
    d "Plus, I put a little extra spice in there."
    
    y "Thank you so much Pie Demon, sir."

    "The Pie Demon grins wordlessly, then dissappears from sight."
    
    hide piedemoncelebratory
    with dissolve
    stop music fadeout 1.0

    "Now it's time to show this demonic pie you have off to the Wizard..."

    "Even if you like how it looks, you feel a little nervous about his judgement."

    scene black

    "..."

    jump ending

label ending:

    if normalEnd: # Shows ending for physical end

        scene bgkitchen
        with fade
        show piewizardneutral

        w "From the sounds and smell of it, you appear to have been hard at work! Let's see if this pie is up to snuff."

        "The Great Wizard takes the pie, and gives it a drawn-out sniff. His nose wrinkles at the stench of it."

        hide piewizardneutral
        show piewizardscrutinizing
        with dissolve
        
        w "Eeeuugh!"
        
        "You wince at his comment, but wait for him to try it."
        
        hide piewizardscrutinizing
        show piewizardneutral
        with dissolve
        
        "The wizard takes a single bite, tearing the half-burnt, half-undercooked piece from the rest of the pie."
        
        hide piewizardneutral
        show piewizardscrutinizing
        with dissolve
        
        w "Hmmm... the texture is all over the place... a bit crunchy, yet a bit runny..."
        
        y "Is... is that so? I was sure I put the oven at the right temperature..."
        
        "The wizard swallows the bite, and he winces as it hits his stomach."
        
        hide piewizardscrutinizing
        show piewizardapproving
        with dissolve
        
        w "Er-hem! Well, dear apprentice, I wasn't expecting you to go for a Helmshire Pie!"
        
        y "...A what now."
        
        w "Why, a Helmshire Pie! The Helmsmen love everything stinky, from their cheeses to their pies, and it adds quite the flavor."
        
        w "And the texture! You got it perfectly, the runny filling complementing the tack-like crust is impressive."
        
        "You remember back to the early days of your training, glossing over an encyclo-pie-dia..."
        
        "...and laughing at the picture of a Helmshire pie factory. The whole setup looked so cartoonish."
        
        y "...Ah, yes! I'm, er, glad you could tell what I was going for!"
        
        hide piewizardapproving
        show piewizardneutral
        with dissolve
        
        w "Either way, it's suffice to say that you have passed your trial. Good work!"
    else: # Shows the magic ending
        
        scene bgkitchen
        with fade
        show piewizardneutral
        
        "The Great Wizard walks up and inspects you pie, smirking a little."

        w "Aren't you a little young to be working with devils?"

        "Your eyes immediately shoot down, feeling a tinge of embarrassment as your wizarding master stares down at you.  But you snap out of it as he lets out a little laugh."

        hide piewizardneutral
        show piewizardapproving
        with dissolve

        w "No need to be that worried. In fact, I am impressed. Not every day one of my apprentices manage to summon a demon and not get torn to pieces."

        y "Oh?! Why, thank you!"

        w "Now, I did say I was impressed, but..."

        hide piewizardapproving
        show piewizardscrutinizing
        with dissolve

        w "...you need to learn to listen to instructions better!"

        w "I told you to bake me a pie, not summon me one!"

        "The Great Wizard looks away for a moment, before calming down again"

        hide piewizardscrutinizing
        show piewizardneutral
        with dissolve

        w "Though I can't stay mad I suppose. You have done far greater magic than many before you, so still, good job."

    
    "You beam back at him. Either way, it seems all your training paid off well!"

    # This ends the game.
    return
