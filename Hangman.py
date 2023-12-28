import random
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
A=['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords','caliph','cobweb','cockiness','croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip','espionage','euouae','exodus','faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki','kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack','larynx','lengths','lucky','luxury','lymph','marquis','matrix','megahertz','microwave','mnemonic','mystify','naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz','quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch','stronghold','stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths','unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism','walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern','xylophone','yachtsman','yippee','yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie']
a2={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
q=1
while q==1:
    i=random.choice(A)
    print("Your word has", len(i), "letters")
    B=Convert(i)
    C=['_']*len(i)
    print(*C)
    a=10
    x=0
    y=0
    z=1
    a1={0}
    while a>0 and z>0:
        x=input("guess: ")
        a1.add(x)
        y=C.count('_')
        for k in range(0,len(i)):
            if B[k]==x:
                C[k]=x
        z=C.count('_')
        if y-z==0 and x in B:
            print()
            print("You have already guessed this letter.")
        elif y-z==0 and x not in B:    
            a-=1
        print()
        if z!=0:
            print(f"You have {a} guesses left")
            print("Available letters: ",*sorted((a2.difference(a1))))
            print(*C)
            print()
    if z==0:
        print("Congrats! You have the correct word.")
    else: print("Sorry, you lose.","The word was: ", i)
    print()
    q=int(input("Type 1 and hit enter to play again, or any other number to exit: "))
    print()
p=0
p=input("Hit enter to close")





































