define a = Character("Aurora")
define s = Character("Stella")

define config.default_text_cps = 45

define x = [0, 0, 0, 0]
define fantasypoints = 0
define realitypoints = 0

label start:

    scene background

    show aurora_test
    #DELETED TEST LINES

    "You wake up in a lush green field, unfamiliar flowers and scents surrounding you. The gentle sunlight, speckled by the trees, dances on your face."
    "You blink awake, and as you turn your head to the side you spot a girl sitting next to you. She looks uninterested, spacing out, she traces the horizon with her eyes."

    "She notices your subtle movements and turns to look at you."

    s "You're awake. You usually sleep for a little longer."
    "She looks at you blankly as she tucks a strand of her thick hair behind her long pointed ears."

    menu:
        "Who are you?":
            s "Did you forget my name again? (She says with a sympathetic smile)."
            s "It's Stella."
            "Before you have time to ask any other questions, Stella gets up, brushing off her legs."
            s "Come on, it'll get dark soon. You said you would help me gather the ingredients for that potion I wanted to make."
            menu:
                "Right...":
                    jump goToGrove
                "Of course.":
                    jump goToGrove

label goToGrove:
    "You get up, but before you meet her eyes she turns over her shoulder and starts walking toward the crowd of fruit trees."
    "She walks proudly and quickly, her hair swinging back and forth, her shoulders rolled back."
    s "Come on, slowpoke (she says with a teasing grin)"
    "You jog a few steps to catch up until you are walking with her side by side"
    menu:
        #"You try and talk to her some more"
        "What kind of potion are you going to make?":
            s "Hmm..... now you care? When I first told you about it you didn't seem that interested."
            a "Well I want to know now."
            s "I forgot the name, it's just this thing I wanted to try. It's not like you're doing anything else today, so I made you come along."
        "Your hair looks nice today":
            s "Ughhh...(she groans)"
            s "If you're going to compliment me at least make it better than /that/."
            menu:
                "I'm taking it back then!":
                    "She lets out a laugh, raising her hand to ever so slightly cover her lips"
                "Sorry":
                    a "I'm sorry, I guess I run out of words when I'm around such a pretty girl."
                    #show stella blushing
                    "She nudges you on the arm playfully"
            s "Stop messing around, we're almost at the orchard."

#insert transition to orchard
s "Here, take this"
"She hands you a redish-orange fruit, then another, and another."
a "Do you really need this many?"
s "Hey, why did you come along if you're just going to complain?"
s "Obviosly I don't need this many for just one potion (she rolls her eyes)"
"She sets another fruit on top of your hands"
s "Pick one! The best one!"
menu:
    "Which one should Stella use for her potion?"
    "First fruit":
        "Stella takes it from your stack and palms the fruit in her hands, looking at it from all sides with the gaze of a connosieur"
        s "Yup! This is a good one."
        jump makePotion
    "Second fruit":
        "Stella takes it from your stack and palms the fruit in her hands, looking at it from all sides with the gaze of a connosieur"
        s "Yuck! This one has a weird... gushy spot."
        s "Pick another one..."
        menu:
            "First fruit":
                "You hand her the first fruit and she looks at it very carefully."
                s "Yup! This is a good one"
                jump makePotion
            "Third fruit":
                "She holds the fruit up to her face and sniffs it."
                s "Perfect! This is exactly what I needed."
                jump makePotion
            "Fourth fruit":
                "She holds the fruit up to her face and sniffs it."
                s "Ew! This one's rotten... what is it doing with the rest of these?"
                s "Pick a different one."
                menu:
                    "First fruit":
                        s "Yup! This is a good one."
                        jump makePotion
                    "Third fruit":
                        s "Perfect! This is exactly what I needed."
                        jump makePotion
    "Third fruit":
        "Stella takes it from your stack and palms the fruit in her hands, looking at it from all sides with the gaze of a connosieur"
        s "Perfect! This is exactly what I needed."
        jump makePotion
    "Fourth fruit":
        "Stella takes it from your stack and palms the fruit in her hands, looking at it from all sides with the gaze of a connosieur"
        "She holds it up to her face and sniffs it."
        s "Ew! This one's rotten... what is it doing with the rest of these?"
        s "Pick a different one."
        menu:
            "First fruit":
                "You hand her the first fruit and she looks at it very carefully."
                s "Yup! This is a good one"
                jump makePotion
            "Second fruit":
                s "Yuck! This one has a weird... gushy spot."
                s "Pick another one..."
                menu:
                    "First fruit":
                        s "Yup! This is a good one"
                        jump makePotion
            "Third fruit":
                s "Perfect! This is exactly what I needed."
                jump makePotion  

label makePotion:
    #make potion in here.... onl y happens after first or third fruit is chosen.
    "Stella crouches on the floor and pulls out an assortment of containers"
    "She rips open the fruit with her hands, pomegranate seeds pouring out and sprawling all over her lap, a few small drops of red forming on her clothes."
    "She takes three small pomegranete seeds out of the hundreds and drops them one at a time inside the bottle. With a small pestle from her bag she crushes the seeds into
    a hard pulp inside the bottle, then takes out a small powder satchet and pours it in as well."
    "It turns an ominous, dark-red and murky color, and the sweet smell of the fruit is gone. Then she takes another container and pours its liquid inside the bottle, swirling
    the mixture around gently."
    "She smells it and makes a face, but hides her disgust with a mischevious smile."
    s "Here!"
    s "Drink it!"
    a "What? You want me to drink that?"
    s "Yeah that's what I just said."
    "She pushes the bottle right in front of your face, her smile bright. You haven't seen her smile like that before. She looks at you with pleading eyes"
    s "Come on, drink it! Be my test subject."
    menu:
        "Will you drink Stella's potion?"
        "Drink it":
            jump drinkPotion
        "Don't drink it":
            jump dontDrinkPotion

label drinkPotion:
    $ fantasypoints += 1
    "You take the bottle and bravely chug it as Stella watches with wide eyes."
    a "*Burp*"
    s "Hahahaha"
    "You try and ignore that burning sensation in your throat as Stella laughs, rolling around in the dirt with amusement."
    "It takes her a while to calm down as you chug water that she conveniently laid out before you drank the potion."
    s "I can't believe you actually did it! You're crazy."
    menu:
        "Crazy for you":
            #show stella flushed
            s "Hey! Stop that!"
            s "You better not expect anything out of complimenting me, you got that?"
            s "Geez..."
        "I regret everything":
            "She continues laughing."
            s "Aw man, I knew it was gonna be bad, but I didn't know it would be *that* bad!"
            a "The things I do for you..."
            "Stella gives you a solemn look and a slight smile."
        "That tasted awful!":
            "She continues laughing."
            s "Aw man, I knew it was gonna be bad, but I didn't know it would be *that* bad!"
            a "The things I do for you..."
            "Stella gives you a solemn look and a slight smile."
    s "Come on!"
    "She stands up, throwing all her leftover containers halfhazardly back into her bag."
    s "There's another place I want to check out today before it gets dark!"
    menu:
        "What place?":
            s "The rose garden!"
    s "You know how much I like roses. I keep walking by this garden on my way back to town, but I never have time to go inside and take a closer look."
    s "That's why I'm dragging you with me today!"
    menu:
        "Stella wants you to go to the rose garden with her"
        "With pleasure":
            "She rolls her eyes at you and pulls you up."
            s "Ok, Cassanova, let me lead the way!"
        "Fine...":
            s "It seems like you're getting a little tired of me, but that's fine!"
            s "It's not like you're my only friend around here anyway."
    "The two of you gather yourselves and make your way to town to view the rose garden"
    jump event2

label dontDrinkPotion:
    $ realitypoints += 1
    a "No way! I'm not drinking that! What is it supposed to do anyway?"
    s "Tch..."
    s "Come onnnn you're no fun."
    menu:
        "Never in a million years!":
            s "Tch..."
        "Don't even think about it":
            s "Tch..."
    "Stella scoffs, but doesn't try to convince you any more."
    s "You never really liked my cooking anyway."
    a "Is this considered cooking?"
    "She frowns but only for a second before She takes the potion bottle and throws it a few feet away. You watch the glass shatter and the suspicious-looking
    liquid seep into the dry dirt."
    s "Well, I wasn't gonna drink it."
    "She stands up, throwing all her leftover containers halfhazardly back into her bag."
    s "There's another place I want to check out today before it gets dark!"
    menu:
        "What place?":
            s "The rose garden!"
    s "You know how much I like roses. I keep walking by this garden on my way back to town, but I never have time to go inside and take a closer look."
    s "That's why I'm dragging you with me today!"
    menu:
        "Stella wants you to go to the rose garden with her"
        "With pleasure":
            "She rolls her eyes at you and pulls you up."
            s "Ok, Cassanova, let me lead the way!"
        "Fine...":
            s "It seems like you're getting a little tired of me, but that's fine!"
            s "It's not like you're my only friend around here anyway."
    "The two of you gather yourselves and make your way to town to view the rose garden"
    jump event2

label event2:
    #scene rose garden
    "You both walk into the garden, the sweet floral smells almost overwhelming your senses, stinging your eyes."
    s "Wow! It's so much prettier than I imagined."
    "You watch by her side as she skips around the enclosed area, walking beneath floral arches and in between small fountains and benches. The entire garden is 
    made up of only two colors of roses: red and white. "
    "She picks a white rose off of one of the bushes, cutting the thick stem with her long, dagger-like nails."
    
    "She presses her thumb firmly on one of the rose's thorns, her gaze low and uninterrupted. She looks lost in thought, as if she's forgotten that you are there too."
    s "I prefer the white ones over the red. I think red roses are too cliche..."
    "She continues gripping the thorns, twirling the untamed rose in her bare hand."
    s "These flowers are beautiful."
    menu:
        "I think you're more beautiful":
            #show stella flushed
            s "How can you say things like that with a straight face?"
            s "Stop it..."
            a "It's true."
            "She glances at you, her grip on the rose weakening."
            s "Geez... hahah"
        "Yes they are":
            s "I'm glad we're agreeing on something!"
    s "Which ones do you think are better? The red or white roses?"
    menu:
        "Which roses do you prefer?"
        "Red":
            jump redRoses
        "White":
            jump whiteRoses
        "Pink":
            jump pinkRoses

    label redRoses:
        s "The red ones?" #show stella disgusted
        s "Ugh, I bet you don't even have a preference, you just want to go against what I say."
        a "No, I love red roses. They're the classic symbol of romantic love."
        s "Gross! Don't talk about romance with me!"
        s "White roses are so much better! They're pure and simple. Plus, they're not purely romantic. They're about remembrance and respect. Something that you should
        have for me!"
        menu:
            "I respect you":
                $ fantasypoints += 1
                a "Oh, beautiful Stella, I have so much respect for you. You have made me see the error of my ways."
                a "You're right, white roses are much better."
                #show stella happy
                s "Mhm! That's what I thought."
                jump event2End
            "Let's agree to disagree":
                $ realitypoints += 1
                a "Let's agree to disagree."
                s "Fine by me... If you're fine with being wrong!"
                "You both laugh and continue to look around the garden together, Stella now loosely holding the white rose between her reddened fingers."
                jump event2End
            "Red roses are more popular for a reason":
                $ realitypoints += 1
                a "Well, the red ones are more popular for a reason."
                s "Yeah... you would think that."
                "She laughs and you both continue to look around the garden together. Stella's white rose now being loosely grasped between her reddened fingers."
                jump event2End
    label whiteRoses:
        $ fantasypoints += 1
        a "Of course I agree with you. The red roses are too cliche, white ones are much better. It's not even a competition."
        s "Exactly!"
        s "Wait..."
        s "You're not just agreeing with me right?"
        menu:
            "Of course not!":
                a "No not at all! Your opinion is simply the correct one."
                s "Hahaha, good to know."
                jump event2End
            "Yes I am":
                a "Yeah, I am. I don't care too much about roses, I just like seeing you happy."
                "Her cheeks flush as red as the flowers around her."
                s "You shouldn't try so hard... It's not going to get you anywhere!"
                a "Sorry, sorry. I can't help myself."
                jump event2End
                

    label pinkRoses:
        s "Oh come one! Be serious. There's no pink roses here."
        a "You didn't say I had to choose a rose that was in this garden."
        s "Nooo, I asked you if red or white roses were better."
        a "Well I like them both, and I think they can coexist in one rose."
        s "Tch... Come on. You have to pick one!"
        menu:
            "Which roses do you prefer?"
            "White roses":
                jump whiteRoses
            "Red roses":
                jump redRoses

    label event2End:
        #end event 2
        "The sun is starting to set, turning the white roses into a light orange. It feels like hardly any time had gone by, but its already dawn."
        "Stella notices this and turns to make her way toward the exit."
        "She lets go of the white rose she was holding, letting fall onto the dirt."
        a "You're not taking it with you?"
        s "Nope... Everything must go back to where it came from , right?"
        "You notice the sun setting far behind the arch of roses."
        "Stella continues walking forward, a small skip in her step. You both have seen all there is to see at the rose garden, and make your way back to town to rest."


    # Event 3
    "..."
    "It's dusk, the sun is going down slowly on the horizon."
    a "Oh..."
    a "Is it already this late...?"
    "It's a normal day, but it's not normal that I wake up when the sun is already going down."
    a "Stella"
    "..."
    a "Stella?"
    "......"
    s "Stella!"
    "........."
    "It's so slient. She doesn't seem to be here."
    "............."
    "Stella is not home."
    "Looking aroud, you realize there is a photo of Stella in your pocket."
    "You took it out and lifted up to your vision."

    menu:
        "She's beautiful":
            a "I should head out to look for her. It's getting late."
        "WHERE IS SHE":
            a "I should head out to look for her. It's getting late."
    
    a "There is just one path stretching out from my home."
    a "I just need to follow along -- there's no other way Stella could go."
    "..."
    "......"
    "........."
    "........................"
    "You have no idea how long it has been."
    "It's always the same path."
    "It's leading me to nowhere."
    a "Why can I still see my house...?"
    a "Why is still dusk...?"
    "You sit down paralyzed on the dirt ground."
    "..."
    s "Aurora"
    "!!!"
    a "Is that you?!"
    "......"
    "I turn around, and around, and Stella is just in front of me."
    s "Hey Aurora."
    "Her voice sounds unfamiliar."
    a "What do you mean \"hey\"? Where have you been? It\'s late!"
    s "I think this should be the end."
    a "...?"
    s "Like anything, including life, there's the end of you and me."
    a "Wait... what on earth are you talking about?"
    "In a blink of an eye. Stella disappeared."
    "Her soft voice remained and echoed profoundly."
    
    menu:
        "No. Our story is IMMORTAL.":
            jump bad
        "What's this end... Is it really the end?":
            if fantasypoints >= 2:
                jump bad
            else: 
                jump true

label bad:
    "......"
    "Birds are chirping."
    "It's dawn."
    "......"
    a "So... that was a dream."
    a "What a dream..."
    "You managed to get up from the soft pillow."
    "(Szzzzzzzzz~)"
    "The familiar and appetizing sound of Stella frying eggs comes from the kitchen."
    "It's just another day."
    a "And there'll be infinitely many other days just like today."
    "Stella comes over, taking off the warm-colored apron."
    s "Breakfast's ready!"
    a "You looks happier than normal."
    "And you don't know why -- she also looks sadder than ever before."
    "Stella makes a puzzled face to your words, and then smiles and moves away, which tells you to hurry up."
    a "Yeah, I'm not letting her go. NEVER"
    "......"
    "Bad Ending: Forever and Ever"

    return

label true:
    "......"

    a """
    Where am I?

    My head hurts...
    """

label find:
    menu :
        "There're something overthere..."
        "Garnet earrings":
            a """
            It’s a pair of beautiful garnet earrings.

            These are not mine…

            These are...
            """
            $ x[0] = 1

        "A notebook":
            a """
            There\’s a dried white rose petal between the pages.

            The fragrance of the rose has almost worn off.

            There\'s... someone\'s funeral...
            """
            $ x[1] = 1
            
        "A poem by Dylan Thomas":
            a """
            This line says... \"Do not go gentle into that good night\".

            She... she loved this poem, didn't she?
            """
            $ x[2] = 1
        
        "Old Card Deck":
            a """
            The title of the game is printed on the back of the card.
            
            \"Spell Dual\".

            ...

            \"Spell Dual\"...

            ...
            """
            $ x[3] = 1
        
    if x[0] == 1 and x[1] == 1 and x[2] == 1 and x[3] == 1:
        jump found
    else:
        jump find

label found:
    a """
    I remember now...

    Stella, my one and only friend...

    I didn't... get to tell you...

    I used to play pretend in a treehouse with Stella.

    We would dress up as little witches, and play that card game together...

    In retrospect, my love started to grow away back then...

    Then, that night, the prom...

    The funeral...

    The day I had to sort out her things...
    """

    "Stella shows up in her prom dress."

    s """
    It has been too long since then, Aurora...

    You know our fantasy world is not real.

    You know you are no longer 17.

    You can't live like this anymore.

    Daydreaming is fun when we were together. But you should not throw away your life like this.
    """

    menu:
        "I didn't get to tell you how I feel about you.":
            s """
            I know. I always know.

            That is why it hurts so much for me to see you like this.

            Go back to school.

            Find a job...

            For me, please?

            I am your memory.

            Stella would have wanted you to move on.

            And deep down in your heart, you know that.

            She wouldn't want you to escape from reality. She doesn't wnat you to escape from anything!

            I am distant because you knew deep down that she would want this for you.
            """
        
        
        "Is that why you were so distant to me?":
            s """
            I am your memory.

            Stella would have wanted you to move on.

            And deep down in your heart, you know that.

            She wouldn't want you to escape from reality. She doesn't wnat you to escape from anything!

            I am distant because you knew deep down that she would want this for you.
            
            I know. I always know.

            That is why it hurts so much for me to see you like this.

            Go back to school.

            Find a job...

            For me, please?
            """
    
    a """
    It's scary to live in a reality without you.

    I don't want to leave you...
    """

    s """
    You have to venture on.

    Without me.

    Be brave, Aurora!

    I'm always with you.

    In the fantasy we made together, in the worlds we built together.

    In those silly witch stories we wrote together
    """

    a "I love you."
    s "I love you too."

    "True Ending: Venture On"

    return