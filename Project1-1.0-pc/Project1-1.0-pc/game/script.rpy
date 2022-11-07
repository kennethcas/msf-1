define a = Character("Aurora") #the player character
define s = Character("Stella") #the love interest

define config.default_text_cps = 45

define x = [0, 0, 0, 0]
define fantasypoints = 0
define realitypoints = 0

define canchoosereality = 0
define canchoosefantasy = 0



label start:
  
    scene white
    #scene cutscene: stella casting spell
    #with fade
    play music "audio/duel.wav" fadein 1.0 fadeout 1.0 
    s "You are going down! "
    #scene cutscene: aurora casting spell
    #with fade
    a "In your dreams!"
    scene white
    with dissolve
    "\"Hahahaha...\""
    "\"That was a good round.\""
    scene bcstart
    with fade
    play music "audio/datingsim.wav" fadein 1.0 fadeout 1.0 
    show aurora_test

    """
    I wake up from that familiar dream, fluttering my eyelashes as the speckles of 
    sunlight dance on my face.

    My eyes open and I look at a figure sitting on the ledge of the window, 
    sorting through books and pages and little knick-knacks.
    """
    s "Finally you're awake. I was starting to get worried."

    "So she says, with an all-too-obviously sarcastic grin on her face."

    a "You sound like someone who's still mad about always losing to me in Spell Duel."
    s """
    Spell Duel? That silly childhood game?

    Why are you bringing this up all of a sudden. Did that nap mess with your cognitive function?

    Haha, you're still the same as when we were kids.
    """
    "Stella softly chuckles, glancing away."

    a "Was it really that long ago?"
    "That vivid dream made it seem like it was yesterday. A strange feeling is burning in my chest."
    
    s "Seriously, Aurora. That was so long ago. Move on and get a life. "
    """
    She comes closer and reaches out to playfully hit me on the shoulder.

    The small physical contact shocks me back into reality.

    I can hear the comforting bubbling, fizzling, and whistling of pots, potions, and cauldrons
    in the humble cabin. 

    In every nook and cranny there is some kind of whimsical device. 

    Every shelf is full of large spell books and every bottle is teeming with all kinds of colorful
    and strange liquids. 

    Two witch hats hang on the wall.

    Stella stands by the door, putting garden pruners and some elixir bottles into her bag.
    """

    a "Those bottles... are you going to collect the ingredients for that potion today?"

    "Stella's gaze stays on her bag."

    s "Yeah, I can't just wait here all day for you to get ready."

    a "What are the garden pruners for?"

    s "I'm going to do some work in the rose garden later in the afternoon."

    "This means Stella's going to be out all day, and I won't be able to spend as much time with her"

    menu ("", screen = "option"):
        "Let me come with you!":
            a "I want to go with you!"
            s "Are you sure?" #SHOW HER SMIRKING
            s "You seemed pretty tired earlier."
            a "I'm not! I want to go with you. Let's go!"
            jump gettingReadyForPotion
            

        "You're going to leave me here all day?":
            a "You're not going to leave me here all day by myself are you?"
            s "You're free to go out whenever you want! Haha, don't act like I own you or anything."
            s "You realize you can go out and do things without me, right? We're not kids anymore."
            "She gives me a symathetic smile"
            a "Its not I can't go out without you or anything... I just like spending time with you."
            s "Haha, alright. Come on then!"
            jump gettingReadyForPotion

label gettingReadyForPotion:
    "I get up quickly and brush off my dress before rushing to Stella's side by the door." #SHES WEARING A DRESS,, MAKE SURE TO UPDATE

    """
    Stella doesn't seem as enthusiastic as I would like her to be. Instead, she looks a little torn.

    But that expression only lasts a few seconds before she looks at me and smiles.
    """

    s "You really can't live without me can you, Aurora? You don't to follow me around all day like a pet."
    """
    She lightly taps my nose with the tip of her finger.

    She teases me, but I don't think she really understands the extent of my feelings for her.

    Perhaps today I can make those feelings clear to her.
    """
    a "I'm coming with you."
    """
    I repeat my intent in a firmer tone. 
            
    Stella and I have known each other since we were very young, 
    and even though she can appear dismissive sometimes, she's usually just shy.

    Or perhaps there is some other reason why she's so anxious about our relationship.

    We walk out the door.
    """
    jump pomegranatePotion

label pomegranatePotion:
    scene black
    with dissolve
    scene bcevent1
    with fade
    play music "audio/datingsim2.wav" fadein 1.0 fadeout 1.0 
    """
    We walk on the small dirt path through the woods that surrounds our humble cabin,
    making light conversation and laughing like normal.

    The lush green grass pads the ground along the path. Piles of fallen fruits sink into the cushiony foliage and the air smells deep and natural with a hint of sweetness from the fruits.

    Stella's heels make small clouds of dirt as she walks forward with a clear destination in mind.

    We walk along countless trees, their overextending branches and strong trunks providing a protective
    presence, making me feel safe and comfortable within this large and unpredictable forest.

    The fluffy grass climbs up the bases of the trees, and some fallen fruits lay nested in the nooks of the branches.

    Small animals scurry around as if dancing along to the birds' songs. I've always been engrossed in the
    complexity and beauty of this forest.

    I stop my eyes from wandering around at the beautiful environment and focus my attention on Stella once more.
    """

    a "So, what was this potion for again?"
    s "I don't know... that's what we're here to find out."
    a "What do you mean you don't know?"

    s "It's a new innovation I wanted to try. I drew some inspiration from an old mythology book."

    "Stella was always such a bookworm. She's always reading mythology or poetry of some kind or another. I wonder why she didn't just become a literature professor."

    s """
    You know that story about the goddess of spring, Persephone, who was kidnapped and taken to Hades' palace in the underworld where they got married.

    Her absence caused a famine and eternal winter in the world above, but she couldn't return because she had consumed a few pomegranate seeds. Once you consume the fruit of the underworld you are trapped there.

    Eventually, Hades agreed to let her revisit her home above once every nine months.
    """

    a "That... is a really twisted love story."

    s """
    Exactly! I want to find out more about this dark and powerful fruit.
    
    What will happen if I make a potion with pomegranate extract as the main ingredient?

    Aren't you excited to see what will happen if someone drinks that kind of potion?
    """

    a "Wouldn't that just be a less concentrated pomegranate juice?"

    s """
    I knew you would say something like that. Sometimes you can be uncharacteristically realistic...

    I dare you to try it!
    """

    """
    Stella is clearly ecstatic about her new idea. A mischevious smile overtakes her face.

    She has already grabbed a ripe pomegranate off of one of the many fruit trees surrounding us.

    Without waiting for me to agree she slices the fruit in half and starts squeezing the pomegranate juice into an exilir bottle that she had brought from the cabin.
    """

    menu ("", screen = "option"):
        "Are we seriously doing this?":
            s "Are you backing out?"

    """
    Once Stella becomes set on something, it's very hard to convince her any other way.

    The extract is mixed with a few other strange ingredients from Stella's bag and the liquid inside the glass bottle turns into a deep crimson color. It glistens in the sunlight like a rare jewel.

    The way Stella holds it up makes the potion look beautiful and tempting, fleeting and temporary.
    """

    a "Are you trying to trick me into drinking a potion that will also bind me to you forever?"

    "Stella's previously elated expression dims down just slightly, as if trying to hide something."
    
    "Her emotions are so hard to understand. We tease each other all the time, so what's wrong?"

    menu ("", screen = "option"):
        "...":
            "Stella notices your concern and quickly shakes her dimmed expression off of her face. She laughs off the tension."

            s "Haha, of course you shouldn't want to spend eternity with me. Persephone also fell into that fate by accident, what sane person would make that kind of choice?"
             
        "What's wrong?":
            a "What's wrong?"
            "Stella looks away and pouts."
            s "Nothing! I guess you wouldn't want to spend eternity with me, and I wouldn't want to do that with you either!"
        
    "I look into Stella's eyes, her gaze is deep and confusing. Specks glimmer in her cosmic-latte-colored irises, applying even more complexity."

    "It's like I can see galaxies swirling in her eyes, silver clouds spinning in a vast universe of secrets. Her cheeks are flushed, though hardly noticeable under her dark skin."
    "Even after all these years, her emotions can be so difficult to understand."

    stop music
    play sound "audio/majorchoice.wav" fadeout 1.0

    menu ("", screen = "option_major"):
        "Should I drink Stella's underworld potion?"
        "Drink the potion":
            
            jump drinkThePotion
            
        "{glitch=5}\"Miss-Worst-Cook\"{/glitch}":
            
            jump dontDrinkThePotion

label drinkThePotion:
    
    play music "audio/datingsim3.wav" fadein 1.0 fadeout 1.0

    $ fantasypoints += 1
    """
    Without another second to delay, I snatch up the bottle from her hand and start chugging away.

    With each gulp the potion becomes harder to swallow, but I am determined to finish every last drop.

    I pull my lips away from the bottle, a burning sensation in my throat. The aftertaste is even more bitter, something I didn't even think was possible.
    """
    a "*COUGH* *COUGH* *COUGH*"
    s "Aurora! What's wrong with you! I didn't expect you to actually drink it!"

    """
    As I continue with my coughing fit Stella hits me on the back repeatedly with a shy rage, trying to coax out the rest of the liquid trapped in my throat.

    I finally calm down, wiping away the tears that built up on my eyelashes and clearing my throat.

    Stella's eyes, worried and attentive, stare into mine. She's holding her breath waiting for what happens next.

    But apart from the horrible taste in my mouth, I don't feel any different. 
    """

    menu ("", screen = "option"):
        "That was awful!":
            a "Yuck! That tasted awful..."
            s "Why did you drink it! Anyone in their right mind wouldn't try something like that!"
            s "We're lucky it didn't actually do anything... what if you grew a tail or something?"
            a "Then it would've been worth it to aid you in your experiments."
            s "Oh, be serious! You're still so childish." #show her smiling

        "Lie and say it tasted good":
            a "Yummm... this is definetely one of your better potions."
            s "Don't lie to me! You almost just choked to death!"
            a "Hahaha. I would drink it all over again just for you!"
            s "Don't say things like that! It's embarassing..."

    """
    Stella launches herself into my arms, trapping me in a tight embrace.

    I must have really worried her, but judging by the way her usually calm self holds me close, I can tell our bond is even deeper than before.
    """
    jump roseGarden

label dontDrinkThePotion:
    stop sound
    play music "audio/cognitiveerror.wav" fadein 1.0 fadeout 1.0
    $ realitypoints += 1
    a "{glitch=5}\"I'm not eating or drinking anything Miss-Worst-Cook makes.\"{/glitch}"
    s "..."
    "There is an unbearable silence for a few moments. Stella looks at me blankly, as if I have somehow stopped time and frozen her in this moment."
    "Why did I say that?"
    "Where did that come from?"
    a "Stella... I-"
    "The usual soft whistles of the wind traveling through the trees' branches suddenly turns harsh and loud."
    "The strange winds create an almost omniscient resonation within the pomegranate trees. "
    "Leaves fall down from the treetops and swirl like strange musical notes falling off the staff. The foliage dances a strange waltz mid air."
    "I look around, unsure of what caused this interruption. Nothing like this ever happens in this peaceful, quiet world that Stella and I live in. It's unnerving, and I feel myself getting cold and clammy."
    "I turn to Stella, wanting to see her reaction to this strange event... but she just stands there, smiling."
    "Her smile is a familiar one: the kind of smile she gives me when I correctly guess the next ingredient in a potion, or when I bring her something she needs before she asks for it. "
    "...The same smile that she would give me as kids when we had a good round of Spell Duel."
    "Her reaction confuses me, it's as if she's completely unfazed by the sudden change in our environment."
    "But before I can say anything else, she is already walking away, her wild silver waves bouncing slightly behind her."
    "The wind has stopped."
    jump roseGarden

    #a "No way! No matter how much I love you, I'm not drinking that..."
    #a "I don't even know what it's supposed to do."
    #s "I thought so! You've been a bit of a coward ever since we were kids. Haha"
    #"Her concerning expression goes away, and she has immediately gone back to teasing me."
    #a "On second thought, maybe I will take a sip! You'll feel sorry when I become invisible or start to grow extra limbs."

label roseGarden:
    scene black
    with dissolve
    scene bcevent2
    with fade
    play music "audio/datingsim2.wav" fadeout 1.0 fadein 1.0
    #start of rose garden/ event 2
    #INCLUDE TRANSITION FROM EVENT 1 TO EVENT 2
    """
    We walk back to the cabin toward the rose garden that Stella has grown and tended to for years.

    Neither of us speak of what happened in the forest. She hasn't looked back at me.
    """

    if fantasypoints >= 1:
        """
        
        From where I am standing, I can see her ear burning red... 
        
        Oh, Stella, and her cute shyness. 
        """
    elif fantasypoints == 0:
        """
        I really want to talk about that strange gust of wind, but Stella seems caught up in her own thoughts.

        I guess I can only wait until she decides to talk again. 
        """

    """
    It's a good thing that there's only a small walk before we reach the garden in no time. 

    The sunlight reflects off of the pure-white roses and hits me in the eye. Without realizing it, a single tear streams down my face.
    """


    s "What's wrong? Is the state of my garden that bad?" #shes smiling
    "I wipe away the tear and laugh. The usual Stella is back."
    a "It's nothing. It's probably just the pollen."
    s "If you're allergic to the pollen you should just go inside. Don't put yourself in uncomfortable situations for me."
    menu ("", screen = "option"):
        #"What should I do?"
        "Grab the watering can":
            "I grab the nearby watering can and start watering the rose bushes without missing another beat."
            a "It's fine, see? I can still work."
            s "Okay then, as long as you're useful." #smiling
    "I keep watering the bushes, watching the clear dew form on top of the rose petals. The drops of water catch the light beautifully, absorbing the subtle tones of the sky."
    "Stella only grows red and white roses. She doesn't even grow any other flowers unless she needs something for a specific spell or potion. She likes to keep her garden simple, which I find ironic considering the complexity of her emotions."
    "While I water the roses, Stella mixes some of her potions in the soil. A while ago she figured out a way to make a potion that replaces fertilizer."
    "I watch as she takes a loose chunk of her silver hair and swipes it elegantly behind her ear. She looks so natural in a sea of roses, each flower enhancing her natural beauty."
    "The deep floral scent and the classic beauty of the roses combined with incoming sunset make for such a romantic environment."
    "I'll take advantage of this opportunity."
    menu ("", screen = "option"): #COME BACK TO THIS AND FIX IT
        "You look beautiful.":
            a "Even among this sea of roses you manage to be the most beautiful."
    "I pluck a rose from its bush and hold it out toward Stella, motioning her to accept it."
    s "Why are you saying things like this all of a sudden..."
    a "Sorry, but it's true. I can't help myself."
    "She looks away shyly, embarassed by my boldness."
    s "No... it's not true. I don't fit in with these roses."
    a "How come? I think you match their beauty perfectly."
    "She looks down at the rose in my fingers: A vibrant red rose in full bloom."
    s "Haha, the red roses are so bright and full of life. They're bold and their meaning is never questioned."
    s "Meanwhile I'm dull and insecure. And I have a hard time dealing with the kind of passion a red rose brings."
    menu ("", screen = "option"):
        "I like you the way you are.":
            a "I like you exactly the way you are. You don't need to change anything."
        "Good thing I prefer white roses.":
            a "It's a good thing I prefer white roses to red ones, then."
            #stella blushing
    s "Stop that...you're just trying to make me feel better."
    a "Either way, as long as it's working."
    "I watch her as she presses the backs of her hands to her face, trying to cool down her flushed cheeks."
    a """
    Each rose has it's own charm.

    Actually, I remember since we were younger you've always preferred white roses.

    Remember that time we had a fight over which color rose was prettier? Hahah, things used to be so much simpler.
    """
    "Stella brings her face away from her hands and chuckles fondly at the memory."
    s "Yup, you really wanted to be right back then."
    a "I take back what I said back then, white roses are definetely prettier. They look better on you."
    s "Stoppp！All you do is tease me. It's like you enjoy seeing me embarassed."
    "Her smile is much brighter than it was just a few moments before as she pushes me on the shoulder gently."
    a """
    Not only that, but white roses are more elegant, more delicate, harder to care for.
    
    You have to be more careful with them, because the smallest actions can blemish their petals.
    """
    s "Alright, alright, I get it. You can stop teasing me now."
    a """
    Plus, their color reminds me of you.
    
    When I look at a white rose I can only see you, your hair, and your eyes. It makes me smile.
    """
    s "Stop it already!"
    "She finally takes the red rose from my hand and glances away quickly as if trying to shake the blush away from her cheeks."
    "She bends down briefly and plucks a white rose, holding both of our cut flowers in her hand."

    s "Tell me... If you were to pick just one of these flowers, which one would you choose?"
    """
    Intrigued by her question, I take another look at the flowers held within her palms.

    The red rose is being held in her left. It looks fresh, vibrant, lively, and ... oddly familiar despite it being one of hundreds.

    The white rose is being held in her right palm. As my eyes come across it that blinding light stings me once more. It's the same 
    glare that caused me to shed a tear as Stella and I arrived at the garden earlier.

    It's strange. By now the sun's light, which would have been reflected, has dimmed.

    Involuntarily my breathing speeds up, my heart trembling within my chest. My thoughts are suddenly cloudy. My head is spinning.

    Was that blinding light earlier just a coincidence? Either way, something about this white rose unnerves me deeply, although I can't even begin to understand why.

    But there's no time to worry about myself and my racing thoughts, right now all that matters is Stella.
    """
    stop music
    play sound "audio/majorchoice.wav" fadeout 1.0

    menu ("", screen = "option_major"):
        "Which of the roses should I take from Stella's hands?"
        "Take the white rose":
            
            jump takeWhiteRose
        "{glitch=5}I want to- ... -this ... red rose here{/glitch}":
            
            jump takeRedRose

label takeWhiteRose:
    play music "audio/datingsim3.wav" fadein 1.0 fadeout 1.0

    $ fantasypoints += 1
    "I wrap my fingers around hers, taking the white rose in my hand."
    a "What kind of question is that? Of course I'd pick the white rose. The one that reminds me the most of you."
    "The flush in Stella's cheeks comes back in a sharp wave. Her affectionate eyes soften, yet there is a sense of subtle complicated emotions behind her silver irises that I can't quite read."
    "We stand in silence for only a few moments, my hands still wrapped around hers, until she drops her head on my shoulder and whispers."
    s "I'm happy... that you're choosing me like this. But..."
    "But?"
    s "But you shouldn't act like this anymore. When will you understand..."
    "Her soft voice trails off in defeat. I can barely make out what she says."
    "Her strange habit of suddenly speaking in riddles always comes at the worst time. How am I supposed to decipher what she means? How am I supposed to decipher her heart?"
    menu ("", screen = "option"):
        "I choose you.":
            a "I chose the white rose, and I chose you."
    "Her head is still hanging on my shoulder. Her hands are uncharacteristically cold."
    s "Stop talking. You really haven't changed a bit since then..."
    "Among the rose-filled pasture, she is still the only thing I can see."
    jump event3

label takeRedRose:
    stop sound
    play music "audio/cognitiveerror.wav" fadein 1.0 fadeout 1.0
    $ realitypoints += 1
    #JKLFDLJDSF
    "My vision blurs, a throbbing headache appears. I can't think."
    a "{glitch=5}\"I know this might not be the right timing, but I want to- ... -this red rose here.\"{/glitch}"
    "I don't feel my mouth move, but words come out. With my fists I attempt to rub out whatever has overtaken my vision."
    "When I open my eyes I see Stella staring back at me, a dumbfounded expression on her delicate face."
    s "What did you just say?"
    "Wait... was that voice me? Did I say that? I don't know what came over me, or why my head still throbs."
    "Stella's expression softens. She gives me an understanding smile."
    if realitypoints > 1:
        #CHOSE REALITY OPTION BEFORE
        "It's that warm smile again. That familiar, comforting smile."
        "Neither of us say anything more."
        "That same tune that appeared in the forest appears again, the strange wind moving away the clouds from the sky."
        "The harsh light from the sky reflects off of the white roses, blinding me again."
        "The light gets brighter and brighter. I instinctively cover my eyes with my hand. I tear up again, the headache worsening, throbbing even worse than before."
        "The landscape around us seems to distort. The strange song emerges from the previously meek wind as it pushes the clouds away, casting a bright light onto the white rose petals."
        "The harsh light blinds me again and I instincively bring up my hands to shield my eyes. I tear up again. The headache worsens."
        "Rose stems growing and thinning, curling around each other, cutting each other with their thorns."
        "I'm overwhelmed, afraid. Was this all triggered by a single red rose? What does this have to do with the previous event in the forest?"
        "Through blurry and wavering eyes I look at Stella, who has already turned and started walking toward the cabin."
        "She turns her head over her shoulder, silver hair swaying gently."
    elif realitypoints== 1:
        #FIRST TIME CHOOSING REALITY OPTION
        "Her smile is a familiar one: the kind of smile she gives me when I correctly guess the next ingredient in a potion, or when I bring her something she needs before she asks for it. "
        "The same smile that she would give me as kids after a good round of Spell Duel."
        "The harsh light from the sky reflects off of the white roses, blinding me again."
        "The light gets brighter and brighter. I instinctively cover my eyes with my hand. I tear up again, the headache worsening, throbbing even worse than before."
        "A strange song emerges from the previously meek wind as it pushes the clouds away, casting a bright light onto the white rose petals."
        "The harsh light blinds me again and I instincively bring up my hands to shield my eyes. I tear up again. The headache worsens."
        "The landscape around me seems to distort: rose stems growing and thinning, curling around each other, cutting each other with their thorns."
        "I hear sounds and see things I've never experienced before in Stella and I's quiet world."
        "I'm overwhelmed, afraid. Was this all triggered by a single red rose?"
        "Through blurry and wavering eyes I look at Stella, who has already turned and started walking toward the cabin."
        "She turns her head over her shoulder, silver hair swaying gently."

    "Did I make her upset? Should I have chosen the white rose instead? What triggers her strange behavior?"
    "There are too many feelings... too many questions. "
    "But one thing I know for sure. Stella would not do anything to harm me."
    "The wind has gone and the distortion has ceased: reverting back to the world I'm used to. "
    "I go back inside after Stella, deciding to lie down for a while."
    jump event3

label event3:
    scene black
    with dissolve
    scene bcevent3
    with fade
    play music "audio/datingsim4.wav" fadein 1.0 fadeout 1.0
    

    "..."
    "I don't know how long I slept, but the window displays the somber darkness outside. It must\'ve been a considerate amount."
    "Today's events completely exhausted me."
    "The cabin is completely dark except for the flickering flame of a single white candle."
    "I can barely make out Stella's face: one side cast in a warm light, the other completely hidden in the darkness."
    "Stella sits at the windowsill, her nose in yet another book: a small hardcover collection of existing poems that she bound together herself."

    s "You're awake. I have something to tell you."
    "She closes the book and leaves it on the windowsill."
    s "I... have to leave now."

    

    menu ("", screen = "option"):
        "Where are you going?":
            a "Where are you going?"
        "This late?":
            a "You're going out now? It's so dark outside."
    "She doesn't answer. Instead, she looks out the window into the dark night. Her eyes scan the barely recognizable woods and the white stars in the sky."
    a "It's really dangerous to leave at this time... When are you planning on coming back?"
    "Still silent. Now her gaze is fixed onto a specific point, unwavering."
    menu ("", screen = "option"):
        "Are you okay?":
            a "Stella? Is everything alright?"
            s "I'm okay."
            "She has already decided what she wants to do. There's nothing I can say to convince her to stay."
            a "I don't know where you're going... but I want to come with you."
            "I have to go with her. Wherever she goes I have to be by her side. The thought of her leaving gives me a desperate ache in my chest."
        "Can I come with you?":
            a "Stella? Can I at least come with you?"
    s "... I know you need me. I know it's just been us for a long time. But... I have to do this. I've been putting it off for too long. We have been putting it off for too long." #empahses on we
    "She continues staring into the starry night, and I can spot moisture on her cheek."
    s "Goodbye."
    "Without another word she rushes out the door, her long skirt swaying behind her."
    stop music
    play sound "audio/majorchoice.wav" fadeout 1.0
    
    if realitypoints == 2:
        jump firstMenu
    elif fantasypoints == 2:
        jump secondMenu
    else:
        jump thirdMenu


label firstMenu :
    menu ("", screen = "option_onlyreality"): 
        "Run after her":
            #"I can't let her leave like this."T
            jump firstMenu
        "{glitch=5}Do not go gentle into that good night{/glitch}": #only available with 1 reality point
            stop sound
            play music "audio/cognitiveerror.wav" fadein 1.0 fadeout 1.0
            "Softly, to myself, I speak the opening line to a poem that I somehow know."
            "{glitch=5} \"Do not go gentle into that good night. \"{/glitch}"
            "I say as I watch her back, her hat bouncing with every step."
            "She's getting further and further away."
            "The candle in her hand flickers in the night wind. It is so dim compared to the endless night surrounding her. "
            "I'm unsure if she's coming back, but she seemed so certain."
            "An ominous feeling rises in my heart... She... could be gone forever. "
            "Why am I still here? What am I doing? "
            "The headache returns, the twisted tune teasing at my ear. Outside, the wind howls, banging branches across our window."
            "It's all too much. I need to wake up from this dream."
            $ canchoosereality += 1
            jump event3Part2

label secondMenu:
    menu ("", screen = "option_onlyfantasy"): 
        "Run after her":
            stop sound
            play music "audio/shelovesyoulower.wav" fadein 1.0 fadeout 1.0
            "I can't let her leave like this."
            $ canchoosefantasy += 1
            jump event3Part2
        "{glitch=5}\"Do not go gentle into that good night\"{/glitch}": #only available with 1 reality point
            jump secondMenu

label thirdMenu: 
    menu ("", screen = "option_major"): 
        
        "Run after her":
            stop sound
            play music "audio/shelovesyoulower.wav" fadein 1.0 fadeout 1.0
            "I can't let her leave like this."
            $ canchoosefantasy += 1
            #can choose fantasy == true
            jump event3Part2
        "{glitch=5}\"Do not go gentle into that good night\"{/glitch}": #only available with 1 reality point
            stop sound
            play music "audio/cognitiveerror.wav" fadein 1.0 fadeout 1.0
            "Softly, to myself, I speak the opening line to a poem that I somehow know."
            "‘’{glitch=5} Do not go gentle into that good night.‘’{/glitch}"
            "I say as I watch her back, her hat bouncing with every step."
            "She's getting further and further away."
            "The candle in her hand flickers in the night wind. It is so dim compared to the endless night surrounding her. "
            "I'm unsure if she's coming back, but she seemed so certain."
            "An ominous feeling rises in my heart... She... could be gone forever. "
            "Why am I still here? What am I doing? "
            "The headache returns, the twisted tune teasing at my ear. Outside, the wind howls, banging branches across our window."
            "It's all too much. I need to wake up from this dream."
            $ canchoosereality += 1
            jump event3Part2
            #event3Part2

#menu ("", screen = "option_major"): 
    #DONT GO GENTLE INTO THAT GOOD NIGHT OPTIONS INSERT HERE!~~~~
        #"Run after her":
        #    "I can't let her leave like this."
        #"Do not go gentle into that good night": #only available with 1 reality point
        #    $ realitypoints += 1
         #   "Softly, to myself, I speak the opening line to a poem that I somehow know."
         #   "Do not go gentle into that good night."
         #   "I say as I watch her back, her hat bouncing with every step."
         #   "She's getting further and further away."
         #   "She's gone. I'm unsure if she's coming back, but she seemed so certain."
          #  "We've been putting it off for too long."
          #  "The headache returns, the twisted tune teasing at my ear. Outside, the wind howls, banging branches across our window."
         #   "It's all too much. I need to wake up from this dream."
          #  jump realityEnding

label event3Part2:
    
    "Panicking, I pick up the candle that's burning on the windowsill and run out after her."
    "..."
    "She's always been fast and elusive. I sprint after her as best as I can, but it takes me a while before I reach out for her shoulder and force her to stop running."
    
    a "Stella! Please! At least... let me speak."
    "I'm completely out of breath. My chest heaves up and down, our faces illuminated by that dim candle in my hand."
    "Poor Stella, usually so cool and collected, now a sobbing mess. All the emotions she has repressed all this time force their way out and seep from her face."

    menu ("", screen = "option"):
        "What do you mean you \"have\" to do this?":
            a "What did you mean by you \"have\" to do this?"
            a "You \"have\" to leave me? You \"have\" to leave me alone? What kind of sick tragedy have you been planning in your head?" #emphasis on putting this off
            if realitypoints >= 1:
                #look around. do u not see how strange and twisted this world is
                s """
                Look around you. This darkness, that horrible feeling in your chest, the twisted way this world reacts to certain things.

                Surely you've noticed it, too!

                This world isn't normal. Do you have any idea how long it's even been?
                """
                "..."
                s """
                We've been living here, in this world, for years.

                And it doesn't feel that way. Every day is the same. We've been living the same life, doing the same things, visiting the same places. There's never something new.
                
                There's never something new because nothing else exists. Nothing outside of these woods exists.

                What if I don't exist? You don't know me now. The only thing you can really remember are our memories as children. Maybe I'm just another placeholder.

                It would be cruel for me to stay with you, for me to love you the way I do, in this world.
                """

            elif realitypoints == 0:
                #... i cant explain it to you. you dont get it. you wont see the things you dont want to see
                s """
                ... I...

                I can't explain it to you. You can only see the things you want to see.

                You've been completely tricked by this world. And it's my fault.

                I don't want you to be trapped here the way I am. Every day is the same. We've been living the same life, doing the same things, visiting the same places. There's never something new.

                Do you think that kind of life is normal? A life where we're completely stuck in the past and unable to grow in the present?
                """
                a "I... don't understand."
                s "I know you don't. And as long as I'm here, you seem to only see me."
                s "Maybe if I'm gone... If I finally leave... for sure this time. Maybe then you will see the truth."
    #contd 
    s "That's why... I have to leave now."
    a "So that's it? I don't have a say in this?"
    s """
    You always do. I can't stop you, and you can't stop me. I have to walk into that woods, for as long as I can, and I can't come back.
    """
    jump lastchoice

    label lastchoice: 
        #stop music
        #play sound "audio/majorchoice.wav"
        menu ("", screen = "option_branching"):
            "Stella isn't coming back after she walks into that woods."
            "I'm coming with you": #ONLY AVAILABLE WITH AT LEAST 1 FANTASY POINT
                if canchoosefantasy == 1:
                    "Ugly sobs erupt from my mouth."
                    jump fantasyEnding
                elif canchoosefantasy == 0: 
                    a "I'm..."
                    jump toRealityEnding

            "I love you enough to let you go": #ONLY AVAILABLE WITH 1 REALITY POINT AT LEAST
                if canchoosereality == 1:
                    
                    play music "audio/menumusic.wav" fadein 1.0 fadeout 1.0

                    "Ugly sobs erupt from my mouth."
                
                    a "I don't want you to leave. I can't imagine my life without you. But... I know I have to let you go. You have to do what you think is right."
                    "The leaves gently rustle, providing a soothing accompaniment."
                    s """
                    I love you, Aurora.

                    You know I've always loved you.

                    I loved being by your side every second. No matter what world we live in, or how far apart we are, just know that I love you.
                    """

                    "She looks down into her hands and cries softly."
                    s "Honestly... I don't want to leave you either. It's a comforting world, where everything is safe and still. But I'm leaving because I love you." 
                    s "I want you to see the full truth."

                    """
                    Overwhelmed with emotion, I don't answer. I just sob. I get the feeling things will make sense soon.

                    That strange wind's song appears again. The gentle breeze turns harsh. Except this time, it's must stronger than usual.

                    The wind slashes me in every direction, slapping me with my own hair, grabbing me by my clothes, pulling me forwards and backwards.

                    The song gets louder and louder, my headache returns with a rigorous vengeance.

                    There is a pounding in my ears. All of my senses are completely overtaken. I can barely make out Stella who is standing just two feet in front of me, completely unmoved by the vengeful wind.
                    """

                    a "Stella..."
                    """
                    I can barely manage to speak, my throat suddenly numb.

                    I can't hear anything except the slashing of the wind across my face.

                    In front of me, Stella mouths something.

                    \"I love you.\"
                    """
                    jump realityEnding
                elif canchoosereality == 0: 
                    a "I... love you enough to..."
                    jump toFantasyEnding
            
label toFantasyEnding:

    """
    No. 
    
    This is wrong.

    After this day we spent together, after all the things I said to her today... 

    Even if clinging to her is wrong, I am already too far gone. 

    I can't back out now. I can't leave Stella like this. 

    Alone, in the night... She would be so, so lonely. 
    
    Just like me without her. 

    I have to... 
    
    I have to go with her. 

    """

    a "I'm coming with you. "

    "Ugly sobs erupt from my mouth."

    jump fantasyEnding

label toRealityEnding:
    """
    No. 
    
    There is something wrong with... what I am doing.

    After this day we spent together, after all the strange words that popped out of my mouth... 
    
    I can't lie to myself. Deep down I know. 

    I have to do this for both of us. 

    I have to... 
    
    I need to...

    Let her go. 
    """

    a "I... I love you enough to let you go. "

    play music "audio/menumusic.wav" fadein 1.0 fadeout 1.0
    
    "Ugly sobs erupt from my mouth."
    
    a "I don't want you to leave. I can't imagine my life without you. But... I know I have to let you go. You have to do what you think is right."

    "The leaves gently rustle, providing a soothing accompaniment."

    s """
    I love you, Aurora.

    You know I've always loved you.

    I loved being by your side every second. No matter what world we live in, or how far apart we are, just know that I love you.
                    """

    "She looks down into her hands and cries softly."
    s "Honestly... I don't want to leave you either. It's a comforting world, where everything is safe and still. But I'm leaving because I love you." 
    s "I want you to see the full truth."

    """
    Overwhelmed with emotion, I don't answer. I just sob. I get the feeling things will make sense soon.

    That strange wind's song appears again. The gentle breeze turns harsh. Except this time, it's must stronger than usual.

    The wind slashes me in every direction, slapping me with my own hair, grabbing me by my clothes, pulling me forwards and backwards.

    The song gets louder and louder, my headache returns with a rigorous vengeance.

    There is a pounding in my ears. All of my senses are completely overtaken. I can barely make out Stella who is standing just two feet in front of me, completely unmoved by the vengeful wind.
    """

    a "Stella..."
    """
    I can barely manage to speak, my throat suddenly numb.

    I can't hear anything except the slashing of the wind across my face.

    In front of me, Stella mouths something.

    \"I love you.\"
    """

    jump realityEnding

    

label fantasyEnding:
    scene black
    with dissolve
    scene bcend1
    with fade 
    stop music
    play sound "audio/fantasyending.mp3" fadein 1.0 fadeout 1.0
    """
    Stella sniffles, deep pools of tears flooding her silver eyes.

    We both stand there for a moment, our cries echoing off the deep woods that Stella is about to walk into.
    """
    s "I don't want you to make a choice you're going to regret."
    a "If it's you, I don't have anything to regret."

    "Stella wipes her tears away with her sleeve and collects herself. I try and do the same, taking deep breaths."
    "Slowly, she takes the candle from my hand and puts it on the ground. Then, she extends her left hand. It itches closer and closer until her fingers graze my right hand."
    "Timidly, almost unsuredly, she grabs my hand, intertwining her cold fingers with mine."
    s "Ok then. Let's go."
    "Her smile is a sweet and timid one, one backed up with countless emotions. She's complicated, she's hard to understand, but I love her. And this is the version of her that I love."
    "I smile back, blinking away the tears."
    "A headache flushes over me, and somehwere in the distance a distorted flute plays. The wind starts to act up, shaking the tree leaves violently."
    "But none of that matters now. It will all be over soon."
    a "Lead the way."

    scene black
    with dissolve
    "Good Ending"
    "Together Ever After"

    jump endCredits2




label realityEnding:
    play music "audio/birds.mp3" fadeout 1.0 fadeout 1.0
    scene white
    with dissolve
    ". . . . . "
    "Where am I?"
    scene bcend2
    with dissolve
    "My head is still throbbing, my vision still blurry."
    "What happened?"
    "The inside looks like Stella and I's living room... but not quite."
    menu ("", screen = "option_afterwaking"):
        "Have a look around":
            jump find

label true:
    "......"

    a """
    Where am I?

    My head hurts...
    """
    jump find

label find:
    scene bcend2
    menu ("", screen = "option_afterwaking"):
        "There's something over there..."
        "Garnet earrings":
            
            a """
            A pair of earrings with inlaid garnet stones. The dark red color looks almost black.

            These aren\'t mine...

            These are...
            """

            play sound "audio/realitychoice.wav" fadeout 1.0
            #scene cutscene: garnet earing on the ground 
            scene white 
            with dissolve

            a "{glitch=5} \"Stella...\"{/glitch}"
            $ x[0] = 1

        "A notebook":
            a """
            One of those small hardcover bound notebooks with a ribbon bookmark.

            I open it up to the bookmarked page, revealing a pressed white rose.

            The fragrance of the rose has almost worn off.

            A funeral rose...?

            """
            play sound "audio/realitychoice.wav" fadeout 1.0
            scene white 
            with dissolve
            #scene cutscene: aurora putting red rose at funeral
            a "{glitch=5}\"I know this might not be the right timing, but I want to put this red rose here with her… \"{/glitch}"
        
            $ x[1] = 1
            
        "A poem":
            a """
            A poem from an author called Dylan Thomas.

            Stella loves this poem.

            The title reads... 

            """
            play sound "audio/realitychoice.wav" fadeout 1.0
            scene white 
            with dissolve
            #scene cutscene: Stella reading this book 
            a "{glitch=5} \"Do not go gentle into that good night...\"{/glitch}"

            $ x[2] = 1
        
        "Old Card Deck":
            scene spellduel
            with fade
            a """
            An old hand-made card deck. The title of the game is written in water-based marker on the back of every card.
            
            \"Spell Duel\".

            ...

            """
            play sound "audio/realitychoice.wav" fadeout 1.0
            #scene cutscene: spell duel
            scene white 
            with dissolve
            a "{glitch=5}\"Spell Duel\"...{/glitch}"

           

            $ x[3] = 1
        
    if x[0] == 1 and x[1] == 1 and x[2] == 1 and x[3] == 1:
        jump found
    else:
        jump find

label found:

    scene white
    with dissolve

    play music "audio/shelovesyou.wav" fadein 1.0 fadeout 1.0
    
    a """
    I remember now... Stella, my one and only friend. My first love.

    I didn't get to tell her how I felt back then.

    We grew up together, we used to play pretend in my backyard treehouse. We would wear cheap witch hats and play our own card game that no one else knew the rules to: \"Spell Duel\"...

    I've always loved her. Even back then. Although that love bloomed into something new as we got older.

    Then, that one night... she didn't come back.""" 

    "The funeral... "
    a "{glitch=5} \"... \"{/glitch}"
    #scene cutscene：open casket

    "The day I had to sort out her things..."
    a "{glitch=5} \"Do not... go gentle... \"{/glitch}"
    #scene cutscene: stella sorting aurora's things

    "And all the fun memories I had with her even before that fateful night..."
    #scene cutscene: Stella feeding Aurora cookie
    s "I made this by myself! This time it's going to be good, trust me."
    a "{glitch=5} \" You made this? Nah nah nah, I'm not eating or drinking anything Miss-Worst-Cook makes.\" {/glitch} "
    

    scene white
    with dissolve

    "Everything comes flooding back to me in a heartwrenching wave."




    "Before I know it, there she is. Standing in front of me as some kind of ghostly apparition."


    play music "audio/lastgoodbyeslow.wav" fadein 1.0 fadeout 1.0

    s "Hi, Aurora. It's been way too long since you've been back."
    a "Stella? Is it you? The real you?"

    s "You were in that fantasy world for a while. It was destroying you."
    s "But... I didn't have the courage to leave either."
    s "We were both trapped there. I didn't want you to delve deeper into the fantasy."

    "I don't know what to say."
    s "I know it's hard, but we are no longer children. We can't live in a world where Spell Duel was more than just a card game."
    s "You can't live like this anymore."
    s "I'm glad you made the right choice. Even if you didn't know what it meant, or where it would take you. Deep down you had the will to exit that fantasy, to come back, to get over me."
    s "Daydreaming and enjoying our youth is fun when we're together, but you shouldn't throw away your future for me."

    menu ("", screen = "option_afterwaking"):
        "I didn't get to tell you how I feel about you.":
            a "But I never got to tell you how I really feel."
            s """
            You didn't have to. The kind of bond we shared didn't need words. We cared for each other more deeply than anyone else would understand.

            It was very hard for me to be separated from you so suddenly, too. That's why I'm here isn't it? That's why we stayed for so long in our little witch cabin amongst our roses and strange forests.

            Trust me, I understand how you feel. I feel the same way. That's why it hurts me so much to see you this way.

            Please, return fully to the real world. Grow up, build a future for yourself. Remember me, and use me as a reason to move forward instead of a reason to stay in the past.
            """
            "It hurts to hear. This is the end. No more strange potions and mythology stories."
            "The life that we had built for ourselves, or rather the life that I built for ourselves, had come crashing down."
            "I have to face the reality of what happened. I sob, clutching my chest, but I know Stella is right. It's time to move on."
            "She doesn't want me to run away. She wants me to walk forward."
            "All that time trying to win her over, when we were already each others'. Those moments when she acted cold and unsure, she just wanted to help me. She wanted me to look beyond our comfortable fantasy."
        
        
        "Is that why you were so distant to me?":
            a "Is that why you were cold toward me? Why you made it so difficult to win you over?"

            s """
            I'm sorry. Maybe I didn't do it in the best way. I just want you to be healthy.

            But there was no need for you to win me over. You never had to say anything. The kind of bond we shared is special. We cared for each other more deeply than anyone else could understand.

            It was very hard for me to be separated from you so suddenly, too. That's why I'm here isn't it? That's why we stayed for so long in our little witch cabin amongst our roses and strange forests.

            Trust me, I understand how you feel. I feel the same way. That's why it hurts me so much to see you this way.

            Please, return fully to the real world. Grow up, build a future for yourself. Remember me, and use me as a reason to move forward instead of a reason to stay in the past.


            """
            
            "It hurts to hear. This is the end. No more strange potions and mythology stories."
            "There's still so much I have to process, so much I don't understand. I can't bring myself to ask any more. It was just fate. Cruel, twisted fate."
            "The life that we had built for ourselves, or rather the life that I built for ourselves, had come crashing down."
            "I have to face the reality of what happened. I sob, clutching my chest, but I know Stella is right. It's time to move on."
            "She doesn't want me to run away. She wants me to walk forward."
            "All that time trying to win her over, when we were already each others'. Those moments when she acted cold and unsure, she just wanted to help me. She wanted me to look beyond our comfortable fantasy."
            
    
    a """
    It's scary to live in a reality without you.

    I don't want to leave you...
    """

    s """
    I know. It took me too long to gain the courage to walk into those woods. But you have to venture on, and be brave.

    Without me.

    This is our final goodbye, Aurora.

    I'm always with you. In your heart, in your memories. In the worlds you dream about. In those silly pretend games we used to play.
    """
    #scene cutscene: stella and aurora hugging
    "Through tears, I barely manage to choke out my words-"

    a "I love you."

    s "I love you too."

    ""



    scene black
    with dissolve

    "True Ending"
    
    "Venture On"

    jump endCredits1


label endCredits1:
    scene white 
    with dissolve
    play music "audio/memory.wav" fadein 1.0 fadeout 1.0
    scene spellduel
    with dissolve

    "Proof of Concept: Spell Duel" 

    "By Diane, Kenneth and Leo"

    "Diane: \n UI Design and Development, Origiinal Soundtrack, \n Scene Art, Narrative Concept Design and Development. "

    "Kenneth: \n Character Art, Character Design, Narrative Concept Design and Development."

    "Leo: \n Cutscene Art, Narrative Concept Design, and this guy is good at python. "

    "Thank you for playing. "
    return


label endCredits2:
    scene white 
    with dissolve
    scene spellduel
    with dissolve

    "Proof of Concept: Spell Duel" 

    "By Diane, Kenneth and Leo"

    "Diane: \n UI Design and Development, Origiinal Soundtrack, \n Scene Art, Narrative Concept Design and Development. "

    "Kenneth: \n Character Art, Character Design, Narrative Concept Design and Development."

    "Leo: \n Cutscene Art, Narrative Concept Design, and this guy is good at python. "

    "Thank you for playing. "
    return
    #jump main_menu



#########################
label oldThing:
    #a "Oh..."
    #a "Is it already this late...?"
    #"It's a normal day, but it's not normal that I wake up when the sun is already going down."
    #a "Stella"
    #"..."
    #a "Stella?"
    #"......"
    #s "Stella!"
    #"........."
    #"It's so slient. She doesn't seem to be here."
    #"............."
    #"Stella is not home."
    #"Looking aroud, you realize there is a photo of Stella in your pocket."
    #"You took it out and lifted up to your vision."
    #menu:
     #   "She's beautiful":
      #      a "I should head out to look for her. It's getting late."
       # "WHERE IS SHE":
        #    a "I should head out to look for her. It's getting late."
    
    #a "There is just one path stretching out from my home."
    #a "I just need to follow along -- there's no other way Stella could go."
    #"..."
    #"......"
    #"........."
    #"........................"
    #"You have no idea how long it has been."
    #"It's always the same path."
    #"It's leading me to nowhere."
    #a "Why can I still see my house...?"
    #a "Why is still dusk...?"
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

##label bad:
   # scene bcend1
    #"""
    #....

    


    #"""

    #"......"
    #"Birds are chirping."
    #"It's dawn."
    ##"......"
   # a "So... that was a dream."
    #a "What a dream..."
    #"You managed to get up from the soft pillow."
    #(Szzzzzzzzz~)"
    ##"The familiar and appetizing sound of Stella frying eggs comes from the kitchen."
    #"It's just another day."
    #a "And there'll be infinitely many other days just like today."
    #"Stella comes over, taking off the warm-colored apron."
   # s "Breakfast's ready!"
  #  a "You looks happier than normal."
   # "And you don't know why -- she also looks sadder than ever before."
    #"Stella makes a puzzled face to your words, and then smiles and moves away, which tells you to hurry up."
    #a "Yeah, I'm not letting her go. NEVER"
    #"......"
   # "Bad Ending: Forever and Ever"

    #return
##############################################

#################UNUSED EVENT.. i just didnt want to erase it lol
#label pickRedRose:
    #picking a red rose for stella
 ##  "Red roses... the classic symbol of love."
   # "I hold the rose and approach Stella, holding it out for her, expecting her to accept my gift the way she has always accepted my gifts."
    #a "This is for you."
    #s "..." #blushing expression ???
    #a "What's wrong?"
    #"She has never rejected me this way before..."
    #s "Ah... to be honest I'm not too fond of red roses recently."
    #a "How come?"
    #s "They're just... so cliche don't you think?"
    #menu:
     #   "They're not cliche":
      #      a "I don't think they're cliche. They're timeless and romantic."
       #     s "Haha, don't talk about romance with me!"
        #    s "I prefer the white roses. They're less...concrete."
#too vibrant, too alive, nake it obvious that she feels like it doesnt fit her
        #"You're right. White roses are better":
         #   a "Now that I think about it, you're right! The white ones are even more beautiful."
          #  s "Exactly! They're pure and can hold so much meaning beyond just love or romance or passion."

















####################################################END OF NEW VERSION
####################################################THE OLD VERSION!!!!
label start2:

    scene background

    show aurora_test

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
    "She takes three small pomegranete seeds out of the hundreds and drops them one at a time inside the bottle. With a small pestle from her bag she crushes the seeds into a hard pulp inside the bottle, then takes out a small powder satchet and pours it in as well."
    "It turns an ominous, dark-red and murky color, and the sweet smell of the fruit is gone. Then she takes another container and pours its liquid inside the bottle, swirling the mixture around gently."
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
    "She frowns but only for a second before She takes the potion bottle and throws it a few feet away. You watch the glass shatter and the suspicious-looking liquid seep into the dry dirt."
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
    "You watch by her side as she skips around the enclosed area, walking beneath floral arches and in between small fountains and benches. The entire garden is made up of only two colors of roses: red and white. "
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
                #$ fantasypoints += 1
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


screen option_major(ch, items):
        text _(ch):
            size 80
            color "#000"

        vbox:
            align (0.5,0.5)
            spacing 30
            for i in range(0, 2):
                button:
                    if i == 0:
                        background Frame("gui/button/fantasy_idle_background.png")
                        hover_background Frame("gui/button/fantasy_hover_background.png")
                        xysize(1920,150)
                        action items[i].action

                    elif i == 1:
                        background Frame("gui/button/reality_idle_background.png")
                        hover_background Frame("gui/button/reality_hover_background.png")
                        xysize(1920,150)
                        action items[i].action

                    hbox:
                        spacing 20
                        align (0.5, 0.5)
                        text items[i].caption

screen option(ch, items):
        text _(ch):
            size 80
            color "#000"

        vbox:
            align (0.5,0.5)
            spacing 30
            for i in items:
                button:
                    background Frame("gui/button/choice_idle_background.png")
                    hover_background Frame("gui/button/choice_hover_background.png")
                    xysize(960,75)
                    action i.action

                    hbox:
                        spacing 20
                        align (0.5, 0.5)
                        text i.caption

                        
screen option_onlyfantasy(ch, items):
        text _(ch):
            size 80
            color "#000"

        vbox:
            align (0.5,0.5)
            spacing 30
            for i in range(0, 2):
                button:
                    if i == 0:
                        background Frame("gui/button/fantasy_idle_background.png")
                        hover_background Frame ("gui/button/fantasy_hover_background.png")
                        
                        xysize(1920,150)
                        action items[i].action

                    elif i == 1:
                        background Frame("gui/button/fakereality_idle_background.png")
                        hover_background Frame("gui/button/fakereality_hover_background.png")
                        xysize(1920,150)
                        action items[i].action

                    hbox:
                        spacing 20
                        align (0.5, 0.5)
                        text items[i].caption


screen option_onlyreality(ch, items):
        text _(ch):
            size 80
            color "#000"

        vbox:
            align (0.5,0.5)
            spacing 30
            for i in range(0, 2):
                button:
                    if i == 0:
                        background Frame("gui/button/fakefantasy_idle_background.png")
                        hover_background Frame ("gui/button/fakefantasy_hover_background.png")
                        
                        xysize(1920,150)
                        action items[i].action

                    elif i == 1:
                        background Frame("gui/button/reality_idle_background.png")
                        hover_background Frame("gui/button/reality_hover_background.png")
                        xysize(1920,150)
                        action items[i].action

                    hbox:
                        spacing 20
                        align (0.5, 0.5)
                        text items[i].caption

screen option_branching(ch, items):
        text _(ch):
            size 80
            color "#000"

        vbox:
            align (0.5,0.5)
            spacing 30
            for i in range(0, 2):
                button:
                    if i == 0:
                        background Frame("gui/button/branchfantasy_idle.png")
                        hover_background Frame ("gui/button/branchfantasy_hover.png")
                        
                        xysize(1920,150)
                        action items[i].action

                    elif i == 1:
                        background Frame("gui/button/branchreality_idle.png")
                        hover_background Frame("gui/button/branchreality_hover.png")
                        xysize(1920,150)
                        action items[i].action

                    hbox:
                        spacing 20
                        align (0.5, 0.5)
                        text items[i].caption

screen option_afterwaking(ch, items):
        text _(ch):
            size 80
            color "#000"

        vbox:
            align (0.5,0.5)
            spacing 30
            for i in items:
                button:
                    background Frame("gui/button/branchreality_idle.png")
                    hover_background Frame("gui/button/branchreality_hover.png")
                    xysize(960,75)
                    action i.action

                    hbox:
                        spacing 20
                        align (0.5, 0.5)
                        text i.caption

