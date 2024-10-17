# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define w = Character("Pie Wizard")
define d = Character("Pie Demon")

# The game starts here.

label start:

    "It’s finally the day."

    "You’ve trained for so long, studied the arcane arts, honed your skills..."

    "And now you must put them to the test."

    "Your continued apprenticeship under the (Great Wizard) depends on it!"

    "The (Wizard’s) test for you…"
    
    # All the comments below came from creating the file, and they're correct, so I'm not deleting them, but we probably can later on. -V
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room
    with fade # Saw this in The Question so I'm doing it here -V

    "...is to successfully bake a pie!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show eileen happy

    # These display lines of dialogue.
    w "Up bright and early today, I see! Are you ready for your final test?"
    
    "You push down any doubts. You have to be ready."

    y "Yes I am, Great Pie Wizard!"

    w "Well, go ahead then. Show me how you’ll bake this pie!"

    y "I won’t disappoint you!"

    "You studied the cookbooks and summoning rituals fervently for the past week."

    "You should have all the materials you need, but..."



    # This ends the game.
    return
