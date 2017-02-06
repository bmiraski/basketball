import math
import random


def gmeff(team):
    (ind,name,off,ostd,de,dstd,pace)=team
    return (random.normalvariate(off,ostd), random.normalvariate(de,dstd))
    
def gmpace(ta,tb,npace):
    (ind,name,off,ostd,de,dstd,pace)=ta
    (indb,nameb,offb,ostdb,deb,dstdb,paceb)=tb
    a = pace / npace
    b = paceb / npace
    return (npace * a * b)

def game(teama,teamb,noff,npace):
    (offa,defa)=gmeff(teama)
    (offb,defb)=gmeff(teamb)
    pace=gmpace(teama,teamb,npace)
    a = offa / noff
    x = defb / noff
    aoffa = noff * a * x
    b = offb / noff
    y = defa / noff
    aoffb = noff * b * y
    scorea = aoffa * (pace/100)
    scoreb = aoffb * (pace/100)
    return (scorea,scoreb)

def ewp(scored,allowed):
    ewp=scored ** 11.5 / (scored ** 11.5 + allowed ** 11.5)
    return ewp

def logfive(ewp1,ewp2):
    pw=(ewp1-(ewp1*ewp2))/(ewp1+ewp2-(2*ewp1*ewp2))
    return pw

def pace1(ta,tb,npace):
    (off,ostd,de,dstd,pace)=ta
    (offa,ostda,dea,dstda,pacea)=tb
    offa=gmoffeff(teama)
    defa=gmdefeff(teama)
    defb=gmoffeff(teamb)
    offb=gmoffeff(teamb)





def sim100(teama, teamb, natoff, natpace):
    x = 100
    y = 0
    wina=0
    winb=0

    while y < x:
        gm=game(teama,teamb,natoff,natpace)
        (scorea,scoreb)=gm
        if scorea > scoreb:
            wina += 1
            y += 1
        elif scoreb > scorea:
            winb += 1
            y += 1
    return (wina,winb)

def pickwin(score):
    (wina,winb)=score
    x=random.uniform(0,100)
    if x < wina:
        return True
    else:
        return False



natpace=69.9
natoff=102.7

vcu=(107.9,15.1,93.7,12.0,69.5)
stb=(110.9,13.9,102.9,12.5,71)
nd=(115.4,14.7,99.9,13.1,67.8)
unc=(116.9,15.8,96.6,18.4,74.3)

#result100=sim100(nd,unc,natoff,natpace)
#(wina,winb)=result100

#end = pickwin(result100)

#awin = str(wina)
#bwin = str(winb)

#print ("Team a won " + awin + " games. Team b won " + bwin + " games.")

#if end == True:
#    print("Team A wins")
#else:
#    print("Team B wins")

#result = game(nd,unc,natoff,natpace)
#(scorea,scoreb) = result

#scra = str(int(scorea))
#scrb = str(int(scoreb))

#if scorea > scoreb:
#    winner = "Team A wins."
#else:
#    winner = "Team B wins."

#print ("Final Score: " + scra + ":" + scrb + ". " + winner)

#print (logfive(ewp(115.4,99.9),ewp(116.9,96.6)))

#sked=[(vcu,stb),(vcu,unc),(vcu,nd),(nd,unc),(stb,nd),(stb,unc)]

tmdata=[(0,"Do not use",0,0,0,0,0),(1,"VCU",107.9,15.1,93.7,12.0,69.5),(2,"St. Bonaventure",110.9,13.9,102.9,12.5,71),(3,"Notre Dame",115.4,14.7,99.9,13.1,67.8),(4,"North Carolina",116.9,15.8,96.6,18.4,74.3)]

sked=[(1,2),(1,4),(1,3),(3,4),(2,3),(2,4)]

record=[(0,0),(0,0),(0,0),(0,0),(0,0)]


for a in range(len(sked)):
    (aind,bind)=sked[a]
    teama=tmdata[aind]
    teamb=tmdata[bind]
    (aind,aname,aoff,aostd,adef,adstd,apace)=teama
    (bind,bname,boff,bostd,bdef,bdstd,bpace)=teamb
    (awin,aloss)=record[aind]
    (bwin,bloss)=record[bind]
    gmres=game(teama,teamb,natoff,natpace)
    (scorea,scoreb) = gmres
    if scorea > scoreb:
        winner = aname + " wins game"
        awin += 1
        bloss += 1
    else:
        winner = bname + " wins game"
        bwin += 1
        aloss += 1
    print(winner + " " + str(a+1) + "." + " Final Score: " + str(int(scorea)) + ":" + str(int(scoreb)))
    record[aind]=(awin,aloss)
    record[bind]=(bwin,bloss)

print ("Final Records:")

for x in range(len(record)-1):
    (ind,name,off,ostd,de,dstd,pace)=tmdata[x+1]
    (tmwin,tmloss)=record[x+1]
    print (name + ": " + str(tmwin) + "-" + str(tmloss))


