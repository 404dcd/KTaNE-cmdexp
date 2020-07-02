print("KTaNE-cmdexp")
print("***********")
print("RED\tr")
print("BLUE\tb")
print("WHITE\tw")
print("YELLOW\ty")
print("BLACK\tB")
print("GREEN\tg")

cmaps = {"r": "red", "b": "blue", "w": "white", "y": "yellow", "B": "black", "g": "green"}

try:
    exec(open("DATA.txt", "r").read())
    lastSerialOdd = True if int(last) % 2 == 1 else False
    vowelSerial = bool(vowels)
    batteries = int(bats)
    indics = []
    if bool(car): indics.append("CAR")
    if bool(frk): indics.append("FRK")
    pp = bool(parallel)
except:
    print("\n>>> WARNING: DATA.txt NOT FORMATTED CORRECT!")
print("\n")

def wires():
    w = input("[wires] wires >> ").replace(" ", "")
    if len(w) == 3:
        if "r" not in w: print("<< cut SECOND wire")
        elif w[-1] == "w": print("<< cut LAST wire")
        elif w.count("b") > 1: print("<< cut LAST BLUE wire")
        else: print("<< cut LAST wire")
    elif len(w) == 4:
        if w.count("r") > 1 and lastSerialOdd: print("<< cut LAST RED wire")
        elif w[-1] == "y" and "r" not in w: print("<< cut FIRST wire")
        elif w.count("b") == 1: print("<< cut FIRST wire")
        elif w.count("y") > 1: print("<< cut LAST wire")
        else: print("<< cut SECOND wire")
    elif len(w) == 5:
        if w[-1] == "B" and lastSerialOdd: print("<< cut FOURTH wire")
        elif w.count("r") == 1 and w.count("y") > 1: print("<< cut FIRST wire")
        elif "B" not in w: print("<< cut SECOND wire")
        else: print("<< cut FIRST wire")
    else:
        if "y" not in w and lastSerialOdd: print("<< cut THIRD wire")
        elif w.count("y") == 1 and w.count("w") > 1: print("<< cut FOURTH wire")
        elif "r" not in w: print("<< cut LAST wire")
        else: print("<< cut FOURTH wire")

def rHeldButton():
    print("<< HOLD button")
    col = input("[button] [held] colour > ")
    if col == "b": print("< release when 4 in any position")
    elif col == "w": print("< release when 1 in any position")
    elif col == "y": print("< release when 5 in any position")
    else: print("< release when 1 in any position")

def button():
    bcol = input("[button] colour >> ").strip()[0]
    txt = input("[button] text >> ").lower().strip()[0]
    if bcol == "b" and txt == "a": rHeldButton()
    elif batteries > 1 and txt == "d": print("<< CLICK button")
    elif bcol == "w" and "CAR" in indics: rHeldButton()
    elif batteries > 2 and "FRK" in indics: print("<< CLICK button")
    elif bcol == "y": rHeldButton()
    elif bcol == "r" and txt == "h": print("<< CLICK button")
    else: rHeldButton()

keys = [
    ["balloon", "pyramid", "lambda", "lightning", "spaceship", "h", "backc"],
    ["e", "balloon", "backc", "curly", "wstar", "h", "question"],
    ["copyright", "butt", "curly", "inkblot", "halfr", "lambda", "wstar"],
    ["six", "paragraph", "p", "spaceship", "inkblot", "question", "smiley"],
    ["trident", "smiley", "p", "c", "paragraph", "snake", "bstar"],
    ["six", "e", "hash", "ae", "trident", "n", "omega"]
]
def keypad():
    symbs = input("[keypad] symbols >> ").strip().split(" ")
    found = False
    print("<< ", end="")
    for k in keys:
        if all([y in k for y in symbs]):
            found = True
            for word in k:
                if word in symbs:
                    print(word, end="  ")
            print()
    if not found:
        print("?????")

fullSimon = {
    True: {
        0: {"r": "b", "b": "r", "g": "y", "y": "g"},
        1: {"r": "y", "b": "g", "g": "b", "y": "r"},
        2: {"r": "g", "b": "r", "g": "y", "y": "b"}
    },
    False: {
        0: {"r": "b", "b": "y", "g": "g", "y": "r"},
        1: {"r": "r", "b": "b", "g": "y", "y": "g"},
        2: {"r": "y", "b": "g", "g": "b", "y": "r"}
    }
}
def simon():
    strikes = int(input("[simon] strikes? >> ").strip()[0])
    while True:
        flashes = input("[simon] flashes /q >> ").strip()
        if flashes == "q": return
        print("<< ", end="")
        for flash in flashes:
            converted = fullSimon[vowelSerial][strikes][flash]
            print(cmaps[converted], end=" ")
        print()

fullWho = {
    'ready': ['yes', 'okay', 'what', 'middle', 'left', 'press', 'right', 'blank', 'ready', 'no', 'first', 'uhhh', 'nothing', 'wait'],
    'first': ['left', 'okay', 'yes', 'middle', 'no', 'right', 'nothing', 'uhhh', 'wait', 'ready', 'blank', 'what', 'press', 'first'],
    'no': ['blank', 'uhhh', 'wait', 'first', 'what', 'ready', 'right', 'yes', 'nothing', 'left', 'press', 'okay', 'no', 'middle'],
    'blank': ['wait', 'right', 'okay', 'middle', 'blank', 'press', 'ready', 'nothing', 'no', 'what', 'left', 'uhhh', 'yes', 'first'],
    'nothing': ['uhhh', 'right', 'okay', 'middle', 'yes', 'blank', 'no', 'press', 'left', 'what', 'wait', 'first', 'nothing', 'ready'],
    'yes': ['okay', 'right', 'uhhh', 'middle', 'first', 'what', 'press', 'ready', 'nothing', 'yes', 'left', 'blank', 'no', 'wait'],
    'what': ['uhhh', 'what', 'left', 'nothing', 'ready', 'blank', 'middle', 'no', 'okay', 'first', 'wait', 'yes', 'press', 'right'],
    'uhhh': ['ready', 'nothing', 'left', 'what', 'okay', 'yes', 'right', 'no', 'press', 'blank', 'uhhh', 'middle', 'wait', 'first'],
    'left': ['right', 'left', 'first', 'no', 'middle', 'yes', 'blank', 'what', 'uhhh', 'wait', 'press', 'ready', 'okay', 'nothing'],
    'right': ['yes', 'nothing', 'ready', 'press', 'no', 'wait', 'what', 'right', 'middle', 'left', 'uhhh', 'blank', 'okay', 'first'],
    'middle': ['blank', 'ready', 'okay', 'what', 'nothing', 'press', 'no', 'wait', 'left', 'middle', 'right', 'first', 'uhhh', 'yes'],
    'okay': ['middle', 'no', 'first', 'yes', 'uhhh', 'nothing', 'wait', 'okay', 'left', 'ready', 'blank', 'press', 'what', 'right'],
    'wait': ['uhhh', 'no', 'blank', 'okay', 'yes', 'left', 'first', 'press', 'what', 'wait', 'nothing', 'ready', 'right', 'middle'],
    'press': ['right', 'middle', 'yes', 'ready', 'press', 'okay', 'nothing', 'uhhh', 'blank', 'left', 'first', 'what', 'no', 'wait'],
    'you': ['sure', 'you', 'are', 'your', "you're", 'next', 'uh', 'huh', 'ur', 'hold', 'what?', 'you', 'uh', 'uh', 'like', 'done', 'u'],
    'you are': ['your', 'next', 'like', 'uh', 'huh', 'what?', 'done', 'uh', 'uh', 'hold', 'you', 'u', "you're", 'sure', 'ur', 'you', 'are'],
    'your': ['uh', 'uh', 'you', 'are', 'uh', 'huh', 'your', 'next', 'ur', 'sure', 'u', "you're", 'you', 'what?', 'hold', 'like', 'done'],
    "you're": ['you', "you're", 'ur', 'next', 'uh', 'uh', 'you', 'are', 'u', 'your', 'what?', 'uh', 'huh', 'sure', 'done', 'like', 'hold'],
    'ur': ['done', 'u', 'ur', 'uh', 'huh', 'what?', 'sure', 'your', 'hold', "you're", 'like', 'next', 'uh', 'uh', 'you', 'are', 'you'],
    'u': ['uh', 'huh', 'sure', 'next', 'what?', "you're", 'ur', 'uh', 'uh', 'done', 'u', 'you', 'like', 'hold', 'you', 'are', 'your'],
    'uh huh': ['uh', 'huh', 'your', 'you', 'are', 'you', 'done', 'hold', 'uh', 'uh', 'next', 'sure', 'like', "you're", 'ur', 'u', 'what?'],
    'uh uh': ['ur', 'u', 'you', 'are', "you're", 'next', 'uh', 'uh', 'done', 'you', 'uh', 'huh', 'like', 'your', 'sure', 'hold', 'what?'],
    'what?': ['you', 'hold', "you're", 'your', 'u', 'done', 'uh', 'uh', 'like', 'you', 'are', 'uh', 'huh', 'ur', 'next', 'what?', 'sure'],
    'done': ['sure', 'uh', 'huh', 'next', 'what?', 'your', 'ur', "you're", 'hold', 'like', 'you', 'u', 'you', 'are', 'uh', 'uh', 'done'],
    'next': ['what?', 'uh', 'huh', 'uh', 'uh', 'your', 'hold', 'sure', 'next', 'like', 'done', 'you', 'are', 'ur', "you're", 'u', 'you'],
    'hold': ['you', 'are', 'u', 'done', 'uh', 'uh', 'you', 'ur', 'sure', 'what?', "you're", 'next', 'hold', 'uh', 'huh', 'your', 'like'],
    'sure': ['you', 'are', 'done', 'like', "you're", 'you', 'hold', 'uh', 'huh', 'ur', 'sure', 'u', 'what?', 'next', 'your', 'uh', 'uh'],
    'like': ["you're", 'next', 'u', 'ur', 'hold', 'done', 'uh', 'uh', 'what?', 'uh', 'huh', 'you', 'like', 'sure', 'you', 'are', 'your']
    }
def whoS2(msgd):
    match = input(f"[whoson] [step 2] {msgd} > ")
    print("<< ", end="")
    [print(t, end="    ") for t in fullWho[match]]
    print()

def whoson():
    msg = ""
    display = input("[whoson] display (or `empty`) >> ").strip().lower()
    if display in ("first", "okay", "ur", "c"):
        msg += "top "
    elif display in ("yes", "nothing", "blank", "led", "read", "red", "you", "your", "you're", "their", "they are"):
        msg += "middle "
    else:
        msg += "bottom "
    
    if display in ("yes", "nothing", "empty", "led", "reed", "leed", "they're", "they are"):
        msg += "left"
    else:
        msg += "right"
    whoS2(msg)

def query(): return int(input("[memory] display >> ").strip()[0]), input("[memory] nums >> ").strip()

def memory():
    history = [] # (position, label)
    d, n = query()
    if d == 1 or d == 2:
        print(f"<< press {n[1]}")
        history.append((1, n[1]))
    elif d == 3:
        print(f"<< press {n[2]}")
        history.append((2, n[2]))
    else:
        print(f"<< press {n[3]}")
        history.append((3, n[3]))
    
    d, n = query()
    if d == 1:
        print("<< press 4")
        history.append((n.index("4"), 4))
    elif d == 2 or d == 4:
        print(f"<< press {n[history[0][0]]}")
        history.append((history[0][0], n[history[0][0]]))
    else:
        print(f"<< press {n[0]}")
        history.append((0, n[0]))
    
    d, n = query()
    if d == 1:
        print(f"<< press {history[1][1]}")
        history.append((n.index(history[1][1]), history[1][1]))
    elif d == 2:
        print(f"<< press {history[0][1]}")
        history.append((n.index(history[0][1]), history[0][1]))
    elif d == 3:
        print(f"<< press {n[2]}")
        history.append((2, n[2]))
    else:
        print("<< press 4")
        history.append((n.index("4"), 4))
    
    d, n = query()
    if d == 1:
        print(f"<< press {n[history[0][0]]}")
        history.append((history[0][0], n[history[0][0]]))
    elif d == 2:
        print(f"<< press {n[0]}")
        history.append((0, n[0]))
    else:
        print(f"<< press {n[history[1][0]]}")
        history.append((history[1][0], n[history[1][0]]))
    
    d, n = query()
    if d == 1:
        print(f"<< press {history[0][1]}")
        history.append((n.index(history[0][1]), history[0][1]))
    elif d == 2:
        print(f"<< press {history[1][1]}")
        history.append((n.index(history[1][1]), history[1][1]))
    elif d == 3:
        print(f"<< press {history[3][1]}")
        history.append((n.index(history[3][1]), history[3][1]))
    else:
        print(f"<< press {history[2][1]}")
        history.append((n.index(history[2][1]), history[2][1]))

morseCode = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z"
}
freqs = {
    "she": "505", # shell
    "hal": "515", # halls
    "sli": "522", # slick
    "tri": "532", # trick
    "box": "535", # boxes
    "lea": "542", # leaks
    "str": "545", # strobe
    "bis": "552", # bistro
    "fli": "555", # flick
    "bom": "565", # bombs
    "bre": "572", # break
    "bri": "575", # brick
    "ste": "582", # steak
    "sti": "592", # sting
    "vec": "595", # vector
    "bea": "600" # beats
}
def morse():
    message = input("[morse] first three >> ").strip().split(" ")
    word = ""
    for char in message[:3]:
        if char in morseCode:
            word += morseCode[char]
        else: 
            word.append("X")
    if word in freqs:
        print(f"<< {word} - 3.{freqs[word]} MHz")
    else:
        print(f"<< {word} - ?????")
    
def compli():
    wall = input("[compli] rbsl? >> ").lower().strip().split(" ")
    madec = False
    for indx in range(len(wall)):
        v = "".join(sorted(wall[indx]))
        if v in ("l", "bs", "blrs"):
            continue # Never cut these wires
        elif v in ("r", "b", "br", "blr"):
            if not lastSerialOdd:
                print(f"<< cut wire {indx+1}")
                madec = True
        elif v in ("bl", "brs", "bls"):
            if pp:
                print(f"<< cut wire {indx+1}")
                madec = True
        elif v in ("lr", "lrs", "ls"):
            if batteries >= 2:
                print(f"<< cut wire {indx+1}")
                madec = True
        else:
            print(f"<< cut wire {indx+1}")
            madec = True
    if not madec:
        print("<< DO NOT cut any wires")


wseqs = {
    "r": ["c", "b", "a", "ac", "b", "ac", "abc", "ab", "b"],
    "b": ["b", "ac", "b", "a", "b", "bc", "c", "ac", "a"],
    "B": ["abc", "ac", "b", "ac", "b", "bc", "ab", "c", "c"]
}
def seqwir():
    occurs = {"r": 0, "b": 0, "B": 0}
    for zz in range(4):
        _ = zz
        wires = input("[seqwir] wires >> ").strip().split(" ")
        if wires == ["q"]: return
        madecut = False
        for ind in range(len(wires)):
            col = wires[ind][0]
            goto = wires[ind][1].lower()
            cutif = wseqs[col][occurs[col]]
            if goto in cutif:
                madecut = True
                if ind == 0: print("<< cut FIRST wire")
                elif ind == 1: print("<< cut SECOND wire")
                else: print("<< cut THIRD wire")
            occurs[col] += 1
        if not madecut: 
            print("<< DO NOT cut any wires")

maz = {
    (1, 2): 1,
    (3, 6): 1,
    (2, 4): 2,
    (5, 2): 2,
    (4, 4): 3,
    (6, 4): 3,
    (1, 1): 4,
    (1, 4): 4,
    (4, 6): 5,
    (5, 3): 5,
    (3, 5): 6,
    (5, 1): 6,
    (2, 1): 7,
    (2, 6): 7,
    (4, 1): 8,
    (3, 4): 8,
    (1, 5): 9,
    (3, 2): 9
}
def mazes():
    coord = input("[mazes (beta)] marker >> ").strip().split(" ")
    gpair = tuple(map(int, coord))
    print(f"<< Use maze {maz[gpair]}")

possibles = [
    "about", "after", "again", "below", "could",
    "every", "first", "found", "great", "house",
    "large", "learn", "never", "other", "place",
    "plant", "point", "right", "small", "sound",
    "spell", "still", "study", "their", "there",
    "these", "thing", "think", "three", "water",
    "where", "which", "world", "would", "write"
    ]
def pwords():
    choices = []
    for i in range(3):
        choices.append(input(f"[pwords] column {i+1} >> ").strip().lower())
    found = False
    print("<< ", end="")
    for pw in possibles:
        totalsame = 0
        for index in range(3):
            if pw[index] in choices[index]:
                totalsame += 1
        if totalsame == 3:
            found = True
            print(pw.upper(), end=" ")
    if not found:
        print("?????")
    else:
        print()

hscreen = """
wires:\t\tWires (simple)
button:\t\tThe Button
keypad:\t\tKeypads (symbols)
simon:\t\tSimon Says
whoson:\t\tWho's on First
memory:\t\tMemory
morse:\t\tMorse Code
compli:\t\tComplicated Wires
seqwir:\t\tWire Sequences
mazes:\t\tMazes
pwords:\t\tPasswords

Note: typing first two letters will also work."""

# handler
while True:
    print()
    mainin = input(">>> ").strip().lower()
    if mainin in ("h", "help"):
        print(hscreen)
        continue
    elif mainin in ("q", "quit", "exit"):
        exit()
    mainin = mainin.replace(" ", "")[:2]
    if mainin == "wi": wires()
    elif mainin == "bu": button()
    elif mainin == "ke": keypad()
    elif mainin == "si": simon()
    elif mainin == "wh": whoson()
    elif mainin == "me": memory()
    elif mainin == "mo": morse()
    elif mainin == "co": compli()
    elif mainin == "se": seqwir()
    elif mainin == "ma": mazes()
    elif mainin == "pw": pwords()
    else: continue