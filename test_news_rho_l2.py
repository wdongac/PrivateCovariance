from functions import test_news_rho, parse_args
from multiprocessing import Process
import time

seeds = [364836,955196,322565,997826,414339,795812,
         100093,255436,824037,333081,990013,568677,
         526216,343823,408852,547163,246087,324836,
         846056,161463,209729,786839,258794,638302,
         740218,408790,821784,592220,182601,608033,
         540647,567087,151261,658076,874087,465663,
         567061,301987,809260,401763,537224,856124,
         225509,580458,942575,95868,134327,970833,
         353413,455588,150842,784657,192866,844467,
         828027,973370,659307,973330,945919,263152,
         81350,872306,664628,277807,5898,473534,
         625392,983981,648864,834039,664941,391841,
         439876,928112,644082,542677,254974,256578,
         730606,632776,501376,754374,189732,42862,
         237474,832717,985259,178198,357973,352542,
         713750,912318,961140,281869,106312,184130,
         763799,169478,694192,82906,583344,180041,
         826962,429064,371531,551650,453275,964658,
         50626,883271,748215,328473,775984,664119,
         764077,901929,154347,724112,904688,247924,
         730528,790401,800967,42020,881178,439327,
         36003,800542,445517,58401,338147,530769,
         797197,492637,708897,227206,945611,146895,
         363954,166114,512334,868618,385874,753903,
         480086,566660,818504,589500,126763,226600,
         715623,110324,984248,950713,857543,221603,
         212180,543878,986311,231577,439218,132432,
         476741,352849,884244,390835,686776,317205,
         76688,873356,744875,437907,193037,229016,
         530824,683579,634124,175013,150635,928086,
         684125,243717,872209,77472,465091,424930,
         339936,167368,315176,568710,527139,547000,
         316485,589297,462917,239071,392588,14409,
         260126,739341,205200,915744,208519,423414,
         944127,839131,828871,261385,865302,709330,
         923113,667214,632408,206204,959219,250102,
         821648,995027,804529,313288,914637,887923,
         278429,32499,702419,628665,229681,14966,
         709567,377986,469522,501336,313821,682771,
         485828,534755,836197,919541,251364,176469,
         864255,279611,348733,784556,485501,433118,
         691390,876457,672883,290164,907135,288974,
         773168,356284,143555,980079,995768,661004,
         923556,302972,157146,863392,679421,583677,
         772003,833547,923177,93907,250909,607976,
         653230,876154,311643,189836,497217,357062,
         433344,909194,369235,495259,706328,841954,
         174751,390918,469230,71874,901096,26636,
         1062,22788,708185,656940,246325,747831,
         863071,40826,531969,908014,617231,545624,
         182652,664961,991887,320881,384432,177886,
         938944,567832,873730,469278,329697,234128,
         503703,527336,662171,100688,304674,218892,
         698041,677087,519899,39520,11318,740033,
         85658,158770,199826,39263,343803,767559,
         210120,349480,480427,165054,919757,736727,
         246010,338119,486791,200588,332430,753789,
         628348,202443,8823,630484,142871,677935,
         102060,887613,996219,803007,584070,265500,
         701054,504801,783315,592718,557720,335868,
         787008,383375,568090,38880,209651,613067,
         609233,296943,418971,937785,360040,271365,
         520906,679476,884346,928811,238088,99366,
         406337,253419,274430,949597,701038,532196,
         464014,929066,357004,251510,539215,360366,
         876727,583542,781755,580584,196953,815954,
         745494,919067,268667,225245,560499,524383,
         414750,262822,908636,887272,46000,73459,
         15471,60851,844251,566439,366084,466750,
         874536,710689,508679,396903,570663,912932,
         534299,155202,172919,96935,555743,584122,
         823023,73004,230264,671157,894258,413918,
         891119,686764,996578,223503,893483,437565,
         706435,313959,149155,926364,662833,974870,
         453842,667292,9923,952896,367092,819822,
         839227,948283,462814,73029,318720,700708,
         870603,637340,330937,635810,222643,359909,
         128455,720910,640341,245589,820404,991792,
         463150,553816,672111,144683,583387,884990,
         131334,307329,172956,292331,469628,402231,
         281670,385666,455373,290703,661231,37539,
         37903,240403,878254,517127,191052,163956,
         480732,909061,443463,303545,150777,385761,
         755453,291652,440013,49251,15588,669726,
         44523,922619,551325,661240,118095,948164,
         926528,532338,849450,537952,45124,542525,
         131439,984712,518908,720351,331158,169251,
         120582,969295,135928,731176,934257,156597,
         271166,295145,625249,483009,942286,416152,
         743703,890939,497952,371858,890969,969593,
         645916,303095,79197,324590,797027,218631,
         60213,797726,574827,492534,176923,401818,
         570763,195709,609591,369502,504311,126733,
         804766,192780,720248,603942,22238,859697,
         459016,437866,233830,363115,79239,43993,
         168933,373984,542122,929366,227414,515870,
         809389,174032,476580,489784,253697,896410,
         177870,600355,426745,597540,736000,673225,
         680082,179799,543283,7562,595755,172218,
         22233,937518,818939,952678,319065,511361]

pargs = parse_args()
pargs.delta = 1e-10
rhos = [0.0001,0.001,0.01,0.1,1,10]
pargs.n = 15657
pargs.d = 128 #32, 128, 512
pargs.mp = False
m = len(rhos)
norm = 'l2'
scale = 1
run_range = range(0,50)
seeds_sub = [[seeds[k*m+j] for j in range(m)] for k in run_range]
folders = ['./results/test_news_rho_d128/test_run'+str(k)+'/' for k in run_range]
params = [['nPaths','rhos','seeds','n','N','s','d','beta','delta'],
[str(1),'|'.join([str(rhoi) for rhoi in rhos]),'|'.join([str(seed) for seed in seeds_sub]),
 str(pargs.n),str(pargs.N),str(pargs.s),str(pargs.d),str(pargs.beta),str(pargs.delta)]]

if __name__ == '__main__':
    tick = time.time()
    print('Starting test_news_rho_zCDP for range '+str(run_range[0])+' - '+str(run_range[-1]))
    if pargs.mp:
        ps = []
        for i in run_range:
            ps.append(Process(target=test_news_rho,args=[pargs,rhos,folders[i-run_range[0]],params,norm,False,scale]))
            ps[i-run_range[0]].start()
        for i in run_range:
            ps[i-run_range[0]].join()
    else:
        for i in run_range:
            print('test '+str(i))
            test_news_rho(pargs,rhos,folders[i-run_range[0]],params,norm,False,scale)
    print('Finished. Time elapsed: ',time.time() - tick)