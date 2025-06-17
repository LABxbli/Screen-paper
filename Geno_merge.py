#python3
######################################
######################

import os 
def file_name2(file_dir): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if '_1.cleanc.fq' in file:
                L.append(os.path.join(root, file))
    return L

for i in file_name2("path_to_the_Quality_filtered_data/"):
    print(i)
    name=i.split("_1.cleanc.fq")[0]
    f1=open(name+"_1.cleanc.fq",'r')
    f2=open(name+"_2.cleanc.fq",'r') 
    f3=open(name+'_m.fq','w')
    i=0
    while 1:
        a1=f1.readline()
        b1=f1.readline()
        c1=f1.readline()
        d1=f1.readline()
        a2=f2.readline()
        b2=f2.readline()
        c2=f2.readline()
        d2=f2.readline()
        if a1==''and a2==''and b1==''and b2==''and c1==''and c2==''and d1==''and d2=='':break
        if a1.split(" ")[0]==a2.split(" ")[0]:
            f3.write(">"+str(i)+"\n"+b1.strip()+"NNNNNNNNNNNNNATCGNNNNNNNNNNNNN"+b2.strip()+"\n")
            i+=1    
    f1.close()
    f2.close()
    f3.close()

print("The end!")
