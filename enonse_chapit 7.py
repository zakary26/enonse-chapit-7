chwa=True
while(chwa == True):
    print("Ou ka kalkile tab yon nonb ")
    nbtab = input("Antre yon nonb ou ka chwazi youn depi lan 1 rive lan 10 : ")# mande itilizate a yon nonb
    while not nbtab:
        nbtab = input("Tanpri, tape yon nonb : ")
        break
    i=1
    r=0
    while( i <= 10):# kalkile tab itilizate a 
           r = i * int(nbtab)
           print(str(i) + " * " + nbtab +" = " + str(r))
           i+=1
        
    print("Eske w vle kalkile yon tab toujou ?")
    chwait = input("Si; wi, tape; W, si; non tape; N : ")# mande itilizate a si l vle kontinye 

    while(chwait != 'N' and chwait != 'W'):# asire ke itilizate tape youn lan de let sa yo(an majiskil)
        chwait = input("Si; wi, tape; W, si; non tape; N : ")
        
        if(chwait=='W'):
            chwa=True
        elif(chwait=='N'):
            chwa=False
            print(" Babay mesi paske w te itilize pwgram sa")
