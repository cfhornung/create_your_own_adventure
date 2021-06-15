"""Plants are Life!"""

__author__ = "720053793"
# Note to grader... You should pick fake plant and then yes to pick the alien plant
from random import randint
# global variables
player: str = "player"
points: int = 0
name: str = "name"
ALI_EN: str = "\U0001F47D"
C_AT: str = "\U0001F640"
FACE_PALM: str = "\U0001F926"
CHERYL_EMOJI: str = "\U0001F467"
SUN_FLOWER: str = "\U0001F33B"
DAY_Z: str = "\U0001F33C"
TWO_LIP: str = "\U0001F337"
ANT_S: str = "\U0001F41C"
F_AKE: str = "\U0001F334"
POTH_OS: str = "\U0001F331"
ALOE_VERA: str = "\U0001F335"
BURNED_LEAF: str = "\U0001F342"
CHICK_EN: str = "\U0001F357"
HUN_GRY: str = "\U0001F37D"
EM_PORIUM: str = "\U0001F3DE"
FOUN_TAIN: str = "\U000026F2"
SUN_SHINE: str = "\U00002600"
PARTIAL_SUN: str = "\U0001F324"
RAIN_DROP: str = "\U0001F4A7"
CON_GRATS: str = "\U0001F973"
CRY_ING: str = "\U0001F62D"
SK_ULL: str = "\U00002620"
SP_LASH: str = "\U0001F4A6"
WORD_BUBBLE: str = "\U0001F5E8"
W_AVE: str = "\U0001F44B"
GOOD_LUCK: str = "\U0001F91E"
PRESS_ENTER: str = "\U0001F446"
CLAP_HANDS: str = "\U0001F44F"
HURR_AY: str = "\U0001F44F"
BAM_BOO: str = "\U0001F38D"
bye_bye = (r"""
 ▄▄▄▄▄▄▄▄▄▄   ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄ 
▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌
▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌
▐░▌       ▐░▌     ▐░▌     ▐░▌           ▀ 
▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  ▄ 
▐░░░░░░░░░░▌      ▐░▌     ▐░░░░░░░░░░░▌▐░▌
 ▀▀▀▀▀▀▀▀▀▀        ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀ 
                                                                   ░                                                    
""")


# ----------- MAIN FUNCTION----------------------------
def main() -> None:
    """Entry Point."""
    global points
    greet()
    input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
    print(f"{CHERYL_EMOJI} Cheryl: {WORD_BUBBLE}\n\n'Welcome to Cheryl's Emporium!") 
    print(f"How can I help you, {player}?'")
    print(f"{SUN_FLOWER}" * 20)
    input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
    print(f"You: {WORD_BUBBLE}\n\n'Hi Cheryl! I keep killing my plants, so now I need a new one!\n\
I would like to get...'\n")
    answer: int = int(input(f"1. {POTH_OS} Pothos\n2. {ALOE_VERA} Aloe Vera\n3. {F_AKE} Fake plant\
\n\n(enter 1, 2, 3. Or press ENTER to quit)\n\n"))
    if answer == 1:
        pothos()
        # THIS IS THE GAME LOOP
        end_pothos(points)
    elif answer == 2:
        how_many: int = int(input("How many do you want?\n\n(enter and integer < 0)"))
        aloe(how_many)
        # THIS IS THE GAME LOOP
        end_aloe(points, how_many)
    else: 
        print(f"{CHERYL_EMOJI} Cheryl: {WORD_BUBBLE}\nI'm sorry, {player}, but we don't have fake plants.")
        a: str = input(f"Would you like this {BAM_BOO} alien hybrid instead? (yes/no)\n\n")
        if a == "yes":
            print(r"""
                ▄▄▄       ██▓     ██▓▓█████  ███▄    █                  
               ▒████▄    ▓██▒    ▓██▒▓█   ▀  ██ ▀█   █                  
               ▒██  ▀█▄  ▒██░    ▒██▒▒███   ▓██  ▀█ ██▒                 
               ░██▄▄▄▄██ ▒██░    ░██░▒▓█  ▄ ▓██▒  ▐▌██▒                 
                ▓█   ▓██▒░██████▒░██░░▒████▒▒██░   ▓██░                 
                ▒▒   ▓▒█░░ ▒░▓  ░░▓  ░░ ▒░ ░░ ▒░   ▒ ▒                  
                 ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░ ░ ░  ░░ ░░   ░ ▒░                 
                 ░   ▒     ░ ░    ▒ ░   ░      ░   ░ ░                  
                     ░  ░    ░  ░ ░     ░  ░         ░                  
                                                                        
 ██▓ ███▄    █ ██▒   █▓ ▄▄▄        ██████  ██▓ ▒█████   ███▄    █  ▐██▌ 
▓██▒ ██ ▀█   █▓██░   █▒▒████▄    ▒██    ▒ ▓██▒▒██▒  ██▒ ██ ▀█   █  ▐██▌ 
▒██▒▓██  ▀█ ██▒▓██  █▒░▒██  ▀█▄  ░ ▓██▄   ▒██▒▒██░  ██▒▓██  ▀█ ██▒ ▐██▌ 
░██░▓██▒  ▐▌██▒ ▒██ █░░░██▄▄▄▄██   ▒   ██▒░██░▒██   ██░▓██▒  ▐▌██▒ ▓██▒ 
░██░▒██░   ▓██░  ▒▀█░   ▓█   ▓██▒▒██████▒▒░██░░ ████▓▒░▒██░   ▓██░ ▒▄▄  
░▓  ░ ▒░   ▒ ▒   ░ ▐░   ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▀▀▒ 
 ▒ ░░ ░░   ░ ▒░  ░ ░░    ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░  ░ 
 ▒ ░   ░   ░ ░     ░░    ░   ▒   ░  ░  ░   ▒ ░░ ░ ░ ▒     ░   ░ ░     ░ 
 ░           ░      ░        ░  ░      ░   ░      ░ ░           ░  ░    
                   ░                                                                     ░                                                    
""")
            print("Cool beans! I'm going to have to have you sign this waiver. K THNX BYE!")
            alien()
            end_alien(points)
        else:
            play_again = play()
            if play_again == "yes":
                if __name__ == "__main__":
                    main()
            else:
                print(bye_bye)
                quit()
    return None


# ----------- GREET FUNCTION----------------------------
def greet() -> None:
    """Salutations!"""
    global player
    player = input("What is your name?\n\n")
    print(r"""
    
.--.      .--.    .-''-.    .---.        _______      ,-----.    ,---.    ,---.    .-''-.   
|  |_     |  |  .'_ _   \   | ,_|       /   __  \   .'  .-,  '.  |    \  /    |  .'_ _   \  
| _( )_   |  | / ( ` )   ',-./  )      | ,_/  \__) / ,-.|  \ _ \ |  ,  \/  ,  | / ( ` )   ' 
|(_ o _)  |  |. (_ o _)  |\  '_ '`)  ,-./  )      ;  \  '_ /  | :|  |\_   /|  |. (_ o _)  | 
| (_,_) \ |  ||  (_,_)___| > (_)  )  \  '_ '`)    |  _`,/ \ _/  ||  _( )_/ |  ||  (_,_)___| 
|  |/    \|  |'  \   .---.(  .  .-'   > (_)  )  __: (  '\_/ \   ;| (_ o _) |  |'  \   .---. 
|  '  /\  `  | \  `-'    / `-'`-'|___(  .  .-'_/  )\ `"/  \  ) / |  (_,_)  |  | \  `-'    / 
|    /  \    |  \       /   |        \`-'`-'     /  '. \_/``".'  |  |      |  |  \       /  
`---'    `---`   `'-..-'    `--------`  `._____.'     '-----'    '--'      '--'   `'-..-'   
,---------.    ,-----.                                                                      
\          \ .'  .-,  '.                                                                    
 `--.  ,---'/ ,-.|  \ _ \                                                                   
    |   \  ;  \  '_ /  | :                                                                  
    :_ _:  |  _`,/ \ _/  |                                                                  
    (_I_)  : (  '\_/ \   ;                                                                  
   (_(=)_)  \ `"/  \  ) /                                                                   
    (_I_)    '. \_/``".'                                                                    
    '---'      '-----'                                                                      
.-------.   .---.        ____    ,---.   .--.,---------.                                    
\  _(`)_ \  | ,_|      .'  __ `. |    \  |  |\          \                                   
| (_ o._)|,-./  )     /   '  \  \|  ,  \ |  | `--.  ,---'                                   
|  (_,_) /\  '_ '`)   |___|  /  ||  |\_ \|  |    |   \                                      
|   '-.-'  > (_)  )      _.-`   ||  _( )_\  |    :_ _:                                      
|   |     (  .  .-'   .'   _    || (_ o _)  |    (_I_)                                      
|   |      `-'`-'|___ |  _( )_  ||  (_,_)\  |   (_(=)_)                                     
/   )       |        \\ (_ o _) /|  |    |  |    (_I_)                                      
`---'       `--------` '.(_,_).' '--'    '--'    '---'                                      
  .---.    .-./`)  ________     .-''-.  .---.                                               
  | ,_|    \ .-.')|        |  .'_ _   \ \   /                                               
,-./  )    / `-' \|   .----' / ( ` )   '|   |                                               
\  '_ '`)   `-'`"`|  _|____ . (_ o _)  | \ /                                                
 > (_)  )   .---. |_( )_   ||  (_,_)___|  v                                                 
(  .  .-'   |   | (_ o._)__|'  \   .---. _ _                                                
 `-'`-'|___ |   | |(_,_)     \  `-'    /(_I_)                                               
  |        \|   | |   |       \       /(_(=)_)                                              
  `--------`'---' '---'        `'-..-'  (_I_)                                               
                                                                                            
    """)
    # welcome message
    greeting: str = (f"\n\n{W_AVE} Nice to meet you, {player}. Let's get started!")
    print(greeting)
    # returns none
    return None


def play() -> str:
    """Correcting Type Safety Errors."""
    play_again: str = input("Want to play again? (yes/no)")
    return play_again
    

# --------------------- POTHOS MAIN -------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------

def pothos() -> None:
    """Option One."""
    global points
    global name
    points = 0
    print(f"{CHERYL_EMOJI} Cheryl: {WORD_BUBBLE}\n'Great choice, \
{player}! {POTH_OS} Pothos are easy to take care of!'")
    input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
    print(f"They like indirect sunlight {PARTIAL_SUN}, nutrient rich \
soil {HUN_GRY}, and a moderate amount of water! {RAIN_DROP} \n\n\
{GOOD_LUCK} GOOD LUCK!!!!!!!")
    input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
    print(f"\n\n         {SUN_FLOWER} Week One....\n\n")
    week_one_p()
    if points > 0:
        print(f"You've earned {points}! Let's keep going...")
        input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
        print(f"\n\n         {DAY_Z} Week Two....\n\n")
        week_two_p()
        if points > 0:
            print(f"\n\nYou NOW have {points} points! Let's keep going...")
            input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
            print(f"         {TWO_LIP} Week Three....\n\n")
            week_three_p()
            if points > 0:
                print(f"CONGRADULATIONS, {player}!! {HURR_AY} YOU MADE IT TO THE END!")
                print(f"{CLAP_HANDS}" * 10)
                print(f"Your high score is {points}!")
                end_pothos(points)
            else:
                print(f"Sorry, you lost {CRY_ING}\nScore: {points}\n\n")
                play_again = play()
                if play_again == "yes":
                    if __name__ == "__main__":
                        main()
                else:
                    print(bye_bye)
                    quit()
        else:
            print(f"Sorry, you lost {CRY_ING}\nScore: {points}\n\n")
            play_again = play()
            if play_again == "yes":
                if __name__ == "__main__":
                    main()
            else:
                print(bye_bye)
                quit()
    else:
        print(f"Sorry, you lost {CRY_ING}\nScore: {points}\n\n")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit()
    return None


# --------------------------------- WEEK ONE POTHOS--------------------------
def week_one_p() -> None:
    """Week One."""
    global points
    global name
    name = input("What would you like to name your plant?\n\n")
    print(f"{name}!! What a great name!!\nOk, {player}, Where would you like to put {name}?")
    input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
    answer: int = int(input(f"I would like to put {name}....\n\
    1. {SUN_SHINE} Hanging in my window.\n\
    2. {PARTIAL_SUN} On my kitchen table.\n\
    3. {SP_LASH} In my bathroom.\n\n(enter 1, 2, 3. Or press ENTER to quit)\n\n"))
    if answer == 1:
        print(f"Hmm, {name} seems to be doing just fine.\n\
But some of {name}'s leaves are burning {BURNED_LEAF}. Must be the direct sunlight {SUN_SHINE}.")
        points += 5
    elif answer == 2:
        print(f"YAYAYAY! {name} is wicked happy here! {HURR_AY}")
        points += 10
    else:
        print(f"RIP {name} {SK_ULL}{SK_ULL}{SK_ULL}.... There is NO SUN LIGHT! Better luck next time? {CRY_ING}")
        points -= 20
        
    return None


# ------------------------------- WEEK TWO POTHOS -----------------------
def week_two_p() -> None:
    """Week two."""
    global points
    global name
    answer: int = int(input(f"Uh Oh! {name} is looking a little THIRSTY {SP_LASH}\n\
How much water do you want to give {name}, {player}?\n\
    1. {SP_LASH}{SP_LASH}\n\
    2. {RAIN_DROP}\n\
    3. Nah, {name} looks great as is!\n\n(enter 1, 2, 3. Or press ENTER to quit)\n\n"))
    if answer == 1:
        print(f"Nice, but the water is overflowing! Maybe a little less next time.\n\
you earned 5 points!! {CLAP_HANDS}")
        print(f"{SP_LASH}")
        points += 5
    elif answer == 2:
        print(f"Just the right amount of water for {name}! {HURR_AY} \
You earned 10 points!!! {CLAP_HANDS}{CLAP_HANDS}")
        points += 10
    else:
        print(f"{player}, {player}, {player} {FACE_PALM} .... Plants need water. Now {name} is sad. {CRY_ING}\n\
MINUS 5 POINTS!!")
        points -= 5
    return None


# -------------------------------- WEEK THREE POTHOS ----------------------
def week_three_p() -> None:
    """Week Three."""
    global points
    global name
    answer: int = int(input(f"Uh Oh! {name} is looking a little HUNGRY {HUN_GRY}\n\
What food do you want to give {name}, {player}?\n\
    1. {CHICK_EN} Chicken\n\
    2. Six miracle grow spikes, please!\n\
    3. Um, 20-20-20?\n\n(enter 1, 2, 3. Or press ENTER to quit)\n\n"))
    if answer == 1:
        print(f"You got ants now, {player}. Ants. {ANT_S}{ANT_S}{ANT_S} MINUS 5 POINTS {CRY_ING}")
        points -= 5
    elif answer == 2:
        print(f"Welp, you done did it. You killed {name}. {SK_ULL}{SK_ULL}{SK_ULL}")
        points -= 20
    else:
        print(f"{player}, {player}, {player}.... GOOD JOB {player}!! {HURR_AY}{HURR_AY}{HURR_AY}\n\n\
That was the perfect combination of Nitrogen, Phosphate, and Potash!\n\
PLUS 20 POINTS!! {CLAP_HANDS}{CLAP_HANDS}{CLAP_HANDS}")
        points += 20
    return None


# --------------------------------- END POTHOS -------------------------
def end_pothos(points: int) -> None:
    """Ending Quotes."""
    if points < 25:
        print("You are an ok plant parent")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit()
    elif points == 40:
        print(f"You have a perfect Score!! You are a plant expert!! {DAY_Z}")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit()
    else:
        print(f"Great job! You did better than some! {DAY_Z}")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit()   


# --------------------- ALOE MAIN -------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------
def aloe(how_many: int) -> int:
    """Option Two."""
    global player
    points = 0
    print(f"{CHERYL_EMOJI} Cheryl: {WORD_BUBBLE}\n'Great choice\
, {player}! {ALOE_VERA} Aloes are easy to take care of!'")
    input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
    print(f"They like full sun {SUN_SHINE}, vitamin rich soil \
{HUN_GRY}, and they love to get bone dry and then a nice drench!!{SP_LASH}")
    print(f"{GOOD_LUCK} GOOD LUCK!!!!!!!")
    input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
    print(f"\n\n         {SUN_FLOWER} Week One....\n\n")
    points = week_one_a(points, how_many)
    if points > 0:
        print(f"You've earned {points}! Let's keep going...")
        input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
        print(f"\n\n         {DAY_Z} Week Two....\n\n")
        points += week_two_a(points, how_many)
        if points > 0:
            print(f"\n\nYou NOW have {points} points! Let's keep going...")
            input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
            print(f"         {TWO_LIP} Week Three....\n\n")
            points += week_three_a(points, how_many)
            if points > 0:
                print(f"CONGRADULATIONS, {player}!! {HURR_AY} YOU MADE IT TO THE END! {CON_GRATS}")
                print(f"{CLAP_HANDS}" * 10)
                print(f"Your high score is {points}!")
                end_aloe(points, how_many)
            else:
                print(f"Sorry, you lost {CRY_ING}\nScore: {points}\n\n")
                play_again = play()
                if play_again == "yes":
                    if __name__ == "__main__":
                        main()
                else:
                    print(bye_bye)
                    quit()
        else:
            print(f"Sorry, you lost {CRY_ING}\nScore: {points}\n\n")
            play_again = play()
            if play_again == "yes":
                if __name__ == "__main__":
                    main()
            else:
                print(bye_bye)
                quit()
    else:
        print(f"Sorry, you lost {CRY_ING}\nScore: {points}\n\n")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit()
    return points


def multi_five(how_many: int) -> int:
    """Multiply by five."""
    multi_five: int = (how_many * 5)
    return multi_five


def multi_ten(how_many: int) -> int:
    """Multiply by ten."""
    multi_ten: int = (how_many * 10)
    return multi_ten


def multi_twenty(how_many: int) -> int:
    """Multiply by twenty."""
    multi_twenty: int = (how_many * 20)
    return multi_twenty


def multi_hundred(how_many: int) -> int:
    """Multiply by hundred."""
    multi_hundred: int = (how_many * 100)
    return multi_hundred

    
# --------------------------------- WEEK ONE ALOE--------------------------
# -------------------------------------------------------------------------
def week_one_a(points: int, how_many: int) -> int:
    """Week One."""
    global name
    name = input("What would you like to name your plant(s)?\n\n")
    print(f"{name}!! What a great name!!\nOk, {player}, Where would you like to put {name}?")
    input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
    answer: int = int(input(f"I would like to put {name}....\n\
    1. {SUN_SHINE} Hanging in my window.\n\
    2. {SP_LASH} In my bathroom.\n\
    3. {PARTIAL_SUN} On my dinning table.\n\n(enter 1, 2, 3. Or press ENTER to quit)\n\n"))
    if answer == 1:
        print(f"YAY, {name} seems to LOVE the window!! {SUN_SHINE}.")
        m_ten = multi_ten(how_many)
        print(f"You earned {m_ten} points!")
        points += m_ten
    elif answer == 2:
        print(f"OH NOOO {name} DIED!!! {CRY_ING}")
        m_hundred = multi_hundred(how_many)
        print(f"You lost {m_hundred} points!")
        points -= m_hundred
    else:
        print(f"Noice. Good Job! {name} is pretty happy.")
        m_five = multi_five(how_many)
        print(f" You earned {m_five} points!")
        points += m_five
    return points


# ------------------------------- WEEK TWO ALOE ---------------------------
# -------------------------------------------------------------------------

def week_two_a(points: int, how_many: int) -> int:
    """Week two."""
    global name
    answer: int = int(input(f"Uh Oh! {name} is looking a little THIRSTY {SP_LASH}\n\
How much water do you want to give {name}, {player}?\n\
    1. Let's just wing it!\n\
    2. {RAIN_DROP} Just a little every day.\n\
    3. Nah, {name} looks great as is!\n\n(enter 1, 2, 3. Or press ENTER to quit)\n\n"))
    if answer == 1:
        water: int = randint(1, 10)
        if water < 6:
            print(f"Hmmm, {water}oz is not really enough")
            m_five = multi_five(how_many)
            print(f" You earned {m_five} points!")
            points += m_five
        else:
            print(f"Yay!! {water}oz was good for {name}!")
            m_ten = multi_ten(how_many)
            print("You earned {m_ten} points!")
            points += m_ten
    elif answer == 2:
        print(f"Did you listen to anything Cheryl {CHERYL_EMOJI} said??? oy.")
        m_five = multi_five(how_many)
        print(f"You lost {m_five} points!")
        points -= m_five
    else:
        print(f"Eh, {name} is alright. At least you didn't Over water {name}!")
        m_five = multi_five(how_many)
        print(f" You earned {m_five} points!")
        points += m_five
    return points


# -------------------------------- WEEK THREE ALOE -----------------------
# -------------------------------------------------------------------------

def week_three_a(points: int, how_many: int) -> int:
    """Week Three."""
    global name
    answer: int = int(input(f"Uh Oh! {name} is looking a little HUNGRY {HUN_GRY}\n\
What food do you want to give {name}, {player}?\n\
    1. Just some multi vitamins! Cheryl said they like vitamins!\n\
    2. Liquid 10-40-10!\n\
    3. Grandular 10-40-10!\n\n(enter 1, 2, 3. Or press ENTER to quit)\n\n"))
    if answer == 1:
        print(f"Do you think plants are humans? Oy!! A human multi-vitamin? {player}, get it together")
        m_hundred = multi_hundred(how_many)
        print(f"You lost {m_hundred} points!")
        points -= m_hundred
    elif answer == 2:
        print(f"YUM YUM YUM YUM YUM!!! Just what the doctor ordered! {HURR_AY}")
        points += (20 * how_many)
    else:
        print(f"Ooooo, {name} likes it! {CLAP_HANDS}\n But, Less mobile nutrients like phosphorus can't \n\
get closer than the individual granule containing them")
        m_ten = multi_ten(how_many)
        points += m_ten
        print(f"You earned {m_ten} points!")
    return points


# --------------------------------- END ALOE ------------------------------
# -------------------------------------------------------------------------

def end_aloe(points: int, how_many: int) -> None:
    """Ending Quotes."""
    if points < (25 * how_many):
        print("You are an ok plant parent")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit()
    elif points == (40 * how_many):
        print(f"You have a perfect Score!! You are a plant expert!! {DAY_Z}")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit()
    else:
        print(f"Great job! You did better than some! {DAY_Z}")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit() 


# --------------------- ALIEN MAIN ------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------

def alien() -> None:
    """Option THREE."""
    global points
    global name
    points = 0
    print(f"Cheryl:\nGreat choice, {player}? Tell me how it goes!")
    print(f"I have no advice for {BAM_BOO} alien plants.... GOOD LUCK!")
    input("\n\n\nPress Enter to continue...\n\n\n")
    name = input(f"What would you like to name your alien plant? {ALI_EN}\n\n")
    print(f"\n\n        {ALI_EN} Week One....\n\n")
    week_one_x()
    if points > 0:
        print(f"You've earned {points}! Let's keep going...")
        input(f"\n\n\n{PRESS_ENTER} Press Enter to continue...\n\n\n")
        print(f"\n\n         {ALI_EN} Week Two....\n\n")
        week_two_x()
        if points > 0:
            print(f"\n\nYou NOW have {points} points! Let's keep going...")
            input("\n\n\nPress Enter to continue...\n\n\n")
            print(f"\n\n         {ALI_EN} Week Three....\n\n")
            week_three_x()
            if points > 0:
                print(f"CONGRADULATIONS, {player}!! {HURR_AY} YOU MADE IT TO THE END!")
                print(f"{CLAP_HANDS}" * 10)
                print(f"Your high score is {points}!")
                end_alien(points)
            else:
                print(f"Sorry, you lost {CRY_ING}\nScore: {points}\n\n")
                play_again = play()
                if play_again == "yes":
                    if __name__ == "__main__":
                        main()
                else:
                    print(bye_bye)
                    quit()
        else:
            print(f"Sorry, you lost {CRY_ING}\nScore: {points}\n\n")
            play_again = play()
            if play_again == "yes":
                if __name__ == "__main__":
                    main()
            else:
                print(bye_bye)
                quit()
    else:
        print(f"Sorry, you lost {CRY_ING}\nScore: {points}\n\n")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit()
    return None


# --------------------------------- WEEK ONE ALIEN-------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

def week_one_x() -> None:
    """Week One."""
    global points
    global name
    print(f"{name}!! What a great name!!\nOk, {player}, Where would you like to put {name}?")
    input("\n\n\nPress Enter to continue...\n\n\n")
    answer: str = input(f"Keep {name} inside or outside?\n(in for inside/enter for outside)\n\n")
    if answer == "in":
        print("\n\nOk, here goes nothing!")
        inside: int = randint(1, 10)
        if inside < 6:
            print(f"{name} seems happy! {ALI_EN}")
            points += 100
        else:
            print(f"{name} ate the cat!!! {C_AT} BAD {name}!! I guess {name} likes meat.")
            points += 50
    else:
        print(f"{SK_ULL}{SK_ULL}{SK_ULL}{SK_ULL}{SK_ULL}{SK_ULL}{SK_ULL}{SK_ULL}{SK_ULL}{SK_ULL}{SK_ULL}{SK_ULL}")
        print(f"\n\nGood job, {player}. You pissed off {name} and he covered your house in it's sticky foliage.\n\
Now you're locked inside and now you died of starvation. It wasn't quick. You suffered. {SK_ULL}")
        points -= 100
    return None


# --------------------------------- WEEK TWO ALIEN-------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
def week_two_x() -> None:
    """Week two."""
    global points
    global name
    question: str = input(f"Alien plants like water right?\nWould you like to give {name} water??\n(yes/no)\n\n")
    if question == "yes":
        print("Ok, here goes nothing!")
        water: int = randint(1, 10)
        if water < 6:
            print(f"{name} seems happy! {ALI_EN} 100 Points!")
            points += 100
        else:
            print(f"HELP HELP!!! {name} is attacking me AHHHHH")
            points -= 100
    else:
        print("Coward! Whatever, here's 20 points")
        points += 20
    return None


# --------------------------------- WEEK THREE ALIEN-----------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
def week_three_x() -> None:
    """Week Three."""
    global points
    global name
    answer: str = input(f"Is {name} hungry?? mabybe? \n(yes/no)\n\n")
    if answer == "no":
        print(f"AHHHH {name} IS EATING ME!!!")
        points -= 10000
    else:
        food: int = int(input(f"What would you like to feed {name}?\n\
            1. {CHICK_EN}\n\
            2. Plant food\n\
            3. Pasta\n(enter 1, 2, or 3)\n\n"))
        if food == 1:
            print(f"{BAM_BOO} {name}:{WORD_BUBBLE}\n\n\
'Thanks Master!!! I am forever grateful and I will never disobey again!'")
            print(f"\nWow, didn't see that comming!! GREAT JOB!!{CLAP_HANDS}")
            print(f"\nAlso... {name} can talk?!?")
            print("You earned 100,000 points!")
            points += 100000
        elif food == 2:
            print(f"{name} died!!!! You killed him!! {CRY_ING}")
            points -= 100000
        else:
            print(f"{name} spit it in your face. 10 points")
            points += 10
    return None


# --------------------------------- END ALIEN -----------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


def end_alien(points: int) -> None:
    """Ending Quotes."""
    if points < 81:
        cat: str = "\U0001F431"
        print(f"Thank kittens {cat} that you're alive! One false move and you'd be dead!")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit()
    elif points == 1200:
        print(f"You have a perfect Score!! That was completely by accident! Way to go!! {DAY_Z}")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit()
    else:
        print(f"Great job! You survived! (btw, there is no return policy) {DAY_Z}")
        play_again = play()
        if play_again == "yes":
            if __name__ == "__main__":
                main()
        else:
            print(bye_bye)
            quit() 


if __name__ == "__main__":
    main()