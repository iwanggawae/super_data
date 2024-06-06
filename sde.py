import random #line:1
import pandas as pd #line:2
from termcolor import colored #line:3
import time #line:4
from tqdm import tqdm #line:5
import pingouin as pg #line:6
for i in tqdm (range (100 ),desc ="Loading SUPER DATA...",ascii =False ,ncols =75 ):#line:9
    time .sleep (0.05 )#line:10
print ("We Are Ready.")#line:12
print ("-"*40 )#line:13
print (colored ("SUPER DATA",'green',attrs =['bold']))#line:14
print ("BY @iwanggawae V1")#line:15
print ("-"*40 )#line:16
try :#line:18
    num_participants =int (input ("Masukkan jumlah partisipan: "))#line:19
    num_questions =int (input ("Masukkan jumlah pertanyaan: "))#line:20
except ValueError :#line:21
    print (colored ("!!!MASUKKAN ANGKA!!!",'red',attrs =['bold']))#line:22
    sys .exit (1 )#line:23
def generate_data (O0OO0OOOO0000O0O0 ,O00O0OOO00000OO0O ):#line:26
    O00OOOOO0O000O000 =[]#line:27
    O0OOO0O00O0O0OO00 =O0OO0OOOO0000O0O0 *O00O0OOO00000OO0O #line:28
    O00000O00OO0OOOOO ={1 :0.009 ,2 :0.015 ,3 :0.190 ,4 :0.320 ,5 :0.314 }#line:37
    OO00O0OO0O000OO00 ={O0OOOOO0000OOO00O :round (O0OOOO0000000O0O0 *O0OOO0O00O0O0OO00 )for O0OOOOO0000OOO00O ,O0OOOO0000000O0O0 in O00000O00OO0OOOOO .items ()}#line:42
    while sum (OO00O0OO0O000OO00 .values ())!=O0OOO0O00O0O0OO00 :#line:45
        O000OO0OO0O0OO000 =max (OO00O0OO0O000OO00 ,key =OO00O0OO0O000OO00 .get )#line:46
        OO00O0OO0O000OO00 [O000OO0OO0O0OO000 ]+=1 #line:47
    O000OOOOO000O0OOO ={O000OO000O0OOOO0O :0 for O000OO000O0OOOO0O in range (1 ,6 )}#line:49
    for OO000OO0OOO00OO00 in range (1 ,O0OO0OOOO0000O0O0 +1 ):#line:51
        O00OO00OOO0O0O00O =[OO000OO0OOO00OO00 ]#line:52
        for _O00O0OOO0O0OOOOOO in range (O00O0OOO00000OO0O ):#line:53
            while True :#line:54
                O00000O0O0O0OOO00 =random .randint (1 ,5 )#line:55
                if O000OOOOO000O0OOO [O00000O0O0O0OOO00 ]<OO00O0OO0O000OO00 [O00000O0O0O0OOO00 ]:#line:56
                    break #line:57
            O00OO00OOO0O0O00O .append (O00000O0O0O0OOO00 )#line:58
            O000OOOOO000O0OOO [O00000O0O0O0OOO00 ]+=1 #line:59
        O00OOOOO0O000O000 .append (O00OO00OOO0O0O00O )#line:60
    O0OO000OO0OOO0O00 =['Participant']+[f'Q{O000O0OOOO00O0OOO+1}'for O000O0OOOO00O0OOO in range (O00O0OOO00000OO0O )]#line:62
    return pd .DataFrame (O00OOOOO0O000O000 ,columns =O0OO000OO0OOO0O00 )#line:63
cronbach_alpha_value =0 #line:66
while cronbach_alpha_value <=0.68 :#line:67
    print (colored ("Data belum Reliabel, akan mengenerate ulang...",'red',attrs =['bold']))#line:68
    df =generate_data (num_participants ,num_questions )#line:69
    reliability_data =df .iloc [:,1 :]#line:72
    cronbach_alpha =pg .cronbach_alpha (reliability_data )#line:73
    cronbach_alpha_value =cronbach_alpha [0 ]#line:74
    print (f"Cronbach's Alpha: {cronbach_alpha_value}")#line:76
summary_data ={'Total':df .iloc [:,1 :].sum (),'Average':df .iloc [:,1 :].mean ()}#line:82
summary_df =pd .DataFrame (summary_data ).T #line:85
summary_df .index .name ='Statistics'#line:86
reliability_summary =pd .DataFrame ({'Cronbach\'s Alpha':[cronbach_alpha_value ],'N of Items':[num_questions ]})#line:89
with pd .ExcelWriter ('hasil_kuesioner.xlsx')as writer :#line:92
    df .to_excel (writer ,sheet_name ='Data',index =False )#line:93
    summary_df .to_excel (writer ,sheet_name ='Summary')#line:94
    reliability_summary .to_excel (writer ,sheet_name ='Reliability')#line:95
print (colored ("Data SUDAH RELIABEL!",'green',attrs =['bold']))#line:97
print ("Data telah berhasil diekspor ke hasil_kuesioner.xlsx")#line:98
