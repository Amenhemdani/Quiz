import json
import re


def reponse(an,opt,d):
    l=d[an]
    lst=d[opt]
    i=ord(l)-97
    return lst[i]

def python(an,opt,d):
    r=reponse(an,opt,d)
    print(f"The reponse is {d[an]}\n it is {r}")

def capital(an,opt,q,d):
    r=reponse(an,opt,d)
    reg=r"(?:\w+)\s(\w+\s\w+\s\w+\s\w+)"
    pos=re.findall(reg,d[q])
    print(pos[0]+" is "+r)

def give_question(i,d,q,opt):
    lst=["a)","b)","c)","d)","e)"]
    print(f"Question {i}:\n") 
    print(d[q]+"?\n")
    for num,op in zip(lst,d[opt]) :
        print("   "+num+" "+op)

def choice(ph,mess):
    ch=input("\nChoice? ")
    while ch not in ph or len(ch)!=1:
        ch=input(f"Please choice {mess} : ")
    return ch

def incorrect(an,opt,q,d):
    print("\nIt is not correct")
    global choi
    if choi=="b" :
        python(an,opt,d)
    else:
        capital(an,opt,q,d)



def generate(d,i):
    q=f"Q{i}"
    opt=f"opt{i}"
    an=f"an{i}"
    hint=f"hint{i}"
    global time
    give_question(i,d,q,opt)
    ch=choice("abcde","a or b or c or d or e")
    if ch==d[an]:
        print(d[an])
        print("\nGreat this is True\n")
        global win
        win+=1
    elif ch=="e":
        print('\n'+d[hint])
        time+=1
        generate(d,i)
    elif time<1:
        print("\nIt is not correct \ntry again, it's simple \n")
        time+=1
        generate(d,i)
    else:
        print("*"*30)
        incorrect(an,opt,q,d)
        print("*"*30)

print("Which topic do you want to be quizzed about?")
print("  a) Capitals")
print("  b) Python\n")

choi=choice("ab","a or b")

if choi=="a":
    filename="questions_cap.json"
else:
    filename="questions_py.json"

with open(filename,"r") as f:
    win=0
    d=json.load(f)
    for i in range(1,6):
        print("-"*30)
        time=0
        generate(d,i)
    print(f"\nyou win in {win} questions")
