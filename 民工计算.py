import numpy as np
import math
 

    
bonus=0.1 #基础设施建造速度加成
extra_bonus=0.05#造民工相对造基建额外建造速度加成
maxspeed=75#无加成的满工厂单地建造速度上限
voa=6000#基建建造量
vob=10800#民工建造量
voc=0.2#每级基建建设后的建造速度增加倍率


def base(st,ed):
    st=int(st)
    ed=int(ed)
    if st != ed:
        return base(st+1,ed)+math.ceil(voa/(voc*st+1)/maxspeed/(1+bonus))
    if st == ed:
        return 0
        
def TD(st,ed,T):
    return base(st,ed)+math.ceil(vob*T/(voc*ed+1)/maxspeed/(1+bonus+extra_bonus))
    
def count(st,ed,printif,T):
    day=0
    fac_onlyst=0
    fac_st2ed=0
    accum_fac_onlyst=0
    accum_fac_st2ed=0
    accum_fac_onlystused=0
    accum_fac_st2edused=0
    while 1:
        if day==T : return -1
        if st == ed: return -1
        accum_fac_onlyst+=fac_onlyst
        accum_fac_st2ed+=fac_st2ed
        accum_fac_onlystused+=1
        accum_fac_st2edused+=1
        if day == TD(st,st,fac_onlyst+1):
            fac_onlyst+=1
            accum_fac_onlystused=0
        if day == TD(st,ed,fac_st2ed+1):
            fac_st2ed+=1
            accum_fac_st2edused=0
        if printif==1:
            print( day,fac_onlyst,fac_st2ed,accum_fac_onlyst,accum_fac_st2ed,accum_fac_onlystused,accum_fac_st2edused,(TD(st,st,fac_st2ed)-TD(st,st,fac_onlyst)-accum_fac_onlystused),(fac_st2ed-fac_onlyst)*(TD(st,st,fac_st2ed)-TD(st,st,fac_onlyst)-accum_fac_onlystused)*(((TD(st,st,fac_st2ed)-TD(st,st,fac_onlyst)-accum_fac_onlystused)/(TD(st,ed,1)-base(st,ed))/2)))
     #   if accum_fac_st2edused+15*accum_fac_st2ed+(fac_st2ed-fac_onlyst)*(TD(st,st,fac_onlyst+1)-TD(st,st,fac_onlyst)-accum_fac_onlystused)>= accum_fac_onlyst+15*accum_fac_onlystused and fac_onlyst<=fac_st2ed and fac_onlyst>0 and fac_st2ed>0:
        if accum_fac_st2ed+((fac_st2ed-fac_onlyst)*(TD(st,st,fac_st2ed)-TD(st,st,fac_onlyst)-accum_fac_onlystused))*(((TD(st,st,fac_st2ed)-TD(st,st,fac_onlyst)-accum_fac_onlystused)/(TD(st,ed,1)-base(st,ed))*(TD(st,st,fac_st2ed)-TD(st,st,fac_onlyst)-accum_fac_onlystused))/2+1) >= accum_fac_onlyst and fac_onlyst<=fac_st2ed and fac_onlyst>0 and fac_st2ed>0:
            return fac_st2ed
        day += 1

def countmatrix(x,T):
    a=np.zeros((6,6))
    i=0
    j=0
    for i in range(6):
        for j in range(i,6):
            a[i][j]=count(i,j,x,T)
    print(a)

#count(3,5,1,2000)
#count(0,5,1)
print("基建建造速度=",bonus,"民工额外建造速度",extra_bonus)
countmatrix(0,2000)
#TD(3,5,1)-base(3,5)