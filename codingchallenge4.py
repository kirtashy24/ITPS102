print("=======================================")
print("     Welcome to the Kirt's Manga Recommender")
print("=======================================")
print("We will help you find a manga to read.\n")

genre = input("Choose a genre:\n\tAction (1)\n\tRomance (2)\n\tHorror (3)\n> ")

if genre == "1":
    print("\nYou have selected: Action")
    volume = input("Choose length:\n\tShort (1)\n\tMedium (2)\n\tLong (3)\n> ")
    
    if volume == "1":
        print("\nYou have selected: Short")
        date = input("Choose release date:\n\t2000s (1)\n\t2010s (2)\n> ")
        if date == "1":
            print("\nYou have selected: 2000s")
            print("\nRecommended Manga:")
            print("1. Fullmetal Alchemist\n\tA young alchemist and his brother seek the Philosopher's Stone after a failed ritual.")
            print("2. Naruto\n\tA determined ninja dreams of becoming the strongest leader of his village.")
        else:
            print("\nYou have selected: 2010s")
            print("\nRecommended Manga:")
            print("1. Attack on Titan\n\tHumanity fights for survival against giant man-eating Titans.")
            print("2. My Hero Academia\n\tIn a world of superpowers, one boy strives to become a true hero.")
    
    elif volume == "2":
        print("\nYou have selected: Medium")
        date = input("Choose release date:\n\t2000s (1)\n\t2010s (2)\n> ")
        if date == "1":
            print("\nYou have selected: 2000s")
            print("\nRecommended Manga:")
            print("1. Bleach\n\tA teenager gains the powers of a Soul Reaper and battles evil spirits.")
            print("2. D.Gray-man\n\tExorcists fight against demonic beings known as Akuma.")
        else:
            print("\nYou have selected: 2010s")
            print("\nRecommended Manga:")
            print("1. One Punch Man\n\tA hero who defeats any enemy with one punch seeks purpose in life.")
            print("2. Tokyo Ghoul\n\tA student becomes half-ghoul and struggles to survive between two worlds.")
    
    else:
        print("\nYou have selected: Long")
        date = input("Choose release date:\n\t2000s (1)\n\t2010s (2)\n> ")
        if date == "1":
            print("\nYou have selected: 2000s")
            print("\nRecommended Manga:")
            print("1. One Piece\n\tPirates sail the seas in search of the ultimate treasure, the One Piece.")
            print("2. Gintama\n\tA samurai and his friends take odd jobs in an alien-invaded Edo period.")
        else:
            print("\nYou have selected: 2010s")
            print("\nRecommended Manga:")
            print("1. Fairy Tail\n\tA guild of wizards go on adventures filled with magic and friendship.")
            print("2. Hunter x Hunter (2011)\n\tA boy sets out to become a Hunter and find his missing father.")

elif genre == "2":
    print("\nYou have selected: Romance")
    volume = input("Choose length:\n\tShort (1)\n\tMedium (2)\n\tLong (3)\n> ")
    
    if volume == "1":
        print("\nYou have selected: Short")
        date = input("Choose release date:\n\t2000s (1)\n\t2010s (2)\n> ")
        if date == "1":
            print("\nYou have selected: 2000s")
            print("\nRecommended Manga:")
            print("1. Lovely★Complex\n\tA tall girl and a short boy navigate love and comedy in high school.")
            print("2. Paradise Kiss\n\tA high school girl enters the fashion world and finds love.")
        else:
            print("\nYou have selected: 2010s")
            print("\nRecommended Manga:")
            print("1. Ao Haru Ride\n\tA shy girl reconnects with her first love in high school.")
            print("2. Orange\n\tA girl receives letters from her future self to save a friend's life.")

    elif volume == "2":
        print("\nYou have selected: Medium")
        date = input("Choose release date:\n\t2000s (1)\n\t2010s (2)\n> ")
        if date == "1":
            print("\nYou have selected: 2000s")
            print("\nRecommended Manga:")
            print("1. Kimi ni Todoke\n\tA misunderstood girl finds friendship and love in high school.")
            print("2. Boys Be\n\tAn anthology of short stories about different high school romances.")
        else:
            print("\nYou have selected: 2010s")
            print("\nRecommended Manga:")
            print("1. Maid Sama\n\tA strict student council president secretly works in a maid café.")
            print("2. Say I Love You\n\tA loner girl opens up after meeting a popular boy.")

    else:
        print("\nYou have selected: Long")
        date = input("Choose release date:\n\t2000s (1)\n\t2010s (2)\n> ")
        if date == "1":
            print("\nYou have selected: 2000s")
            print("\nRecommended Manga:")
            print("1. Boys Over Flowers\n\tA poor girl attends an elite school and clashes with a rich boy.")
            print("2. Nana\n\tTwo women named Nana share an apartment and their intertwined fates.")
        else:
            print("\nYou have selected: 2010s")
            print("\nRecommended Manga:")
            print("1. Your Lie in April\n\tA pianist rediscovers music and love after meeting a violinist.")
            print("2. Clannad\n\tA delinquent boy’s life changes after meeting a group of girls in high school.")

elif genre == "3":
    print("\nYou have selected: Horror")
    volume = input("Choose length:\n\tShort (1)\n\tMedium (2)\n\tLong (3)\n> ")
    
    if volume == "1":
        print("\nYou have selected: Short")
        date = input("Choose release date:\n\t2000s (1)\n\t2010s (2)\n> ")
        if date == "1":
            print("\nYou have selected: 2000s")
            print("\nRecommended Manga:")
            print("1. Uzumaki\n\tA town is cursed by spirals leading to horrifying events.")
            print("2. Tomie\n\tA girl cursed with immortality causes madness wherever she goes.")
        else:
            print("\nYou have selected: 2010s")
            print("\nRecommended Manga:")
            print("1. I Am a Hero\n\tA struggling manga artist finds himself in a zombie apocalypse.")
            print("2. Ajin\n\tImmortal beings known as Ajin are hunted by humans for experiments.")

    elif volume == "2":
        print("\nYou have selected: Medium")
        date = input("Choose release date:\n\t2000s (1)\n\t2010s (2)\n> ")
        if date == "1":
            print("\nYou have selected: 2000s")
            print("\nRecommended Manga:")
            print("1. Parasyte\n\tAliens invade human bodies, and one boy resists full takeover.")
            print("2. Goth\n\tTwo high school students are drawn to dark and violent mysteries.")
        else:
            print("\nYou have selected: 2010s")
            print("\nRecommended Manga:")
            print("1. Another\n\tA cursed class leads to mysterious deaths among students.")
            print("2. Corpse Party\n\tA group of students are trapped in a haunted elementary school.")

    else:
        print("\nYou have selected: Long")
        date = input("Choose release date:\n\t2000s (1)\n\t2010s (2)\n> ")
        if date == "1":
            print("\nYou have selected: 2000s")
            print("\nRecommended Manga:")
            print("1. Hellsing\n\tA vampire works for an organization that protects England from supernatural threats.")
            print("2. Bastard!!\n\tA powerful wizard wreaks havoc in a dark fantasy world.")
        else:
            print("\nYou have selected: 2010s")
            print("\nRecommended Manga:")
            print("1. Tokyo Ghoul\n\tA student becomes half-ghoul and struggles with his new identity.")
            print("2. The Promised Neverland\n\tChildren uncover the horrifying secret behind their orphanage.")

else:
    print("\nInvalid choice. Please restart and try again.")