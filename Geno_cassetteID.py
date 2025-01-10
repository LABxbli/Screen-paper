#python3
###############################
import os 
import cv2
import numpy as np
import pylab
import matplotlib.pyplot as plt


def file_name2(file_dir):
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if '.fa' in file:
                L.append(os.path.join(root, file))
    return L

def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    return cv_img 

def allfiles(fileo,filen):
    name="cp "+fileo+" "+filen
    os.system(name)
dictseq2={}              
for i in file_name2('path_to_the_assembled or extracted sequence files/'):
    if "the_Special-recognition-characters"  in i:
        #print(i)
        bar=i.split("/")[-2]
        dictseq2[bar]=[]
        f1=open(i,"r")
        while 1:
            a=f1.readline().strip()
            b=f1.readline().strip()
            if a=="":break
            dictseq2[bar].append(b)
        f1.close()
################################################################################    
fw=open("barcode_cassette_Flanking_seq.csv","w")
cassette1="TTCCCTGCCGCTGCAACACGCCCCGCGCTANNNNNNNNNNNNNNNNNNNNNNACTGACGTCGAGCCTTCTGGCAGACTAGTTGCTCCTGAGTCCAAC"
cassette2="GTTGGACTCAGGAGCAACTAGTCTGCCAGAAGGCTCGACGTCAGTNNNNNNNNNNNNNNNNNNNNNNTAGCGCGGGGCGTGTTGCAGCGGCAGGGAA"

def bmds1213(seq):
    seqb=seq.upper()
    lenb=len(seqb)
    origin_longth=12##########
    step=1
    start=0
    end=start+origin_longth
    flag=0
    num=0
    seqs=[]
    while end <=lenb:#
        if (seqb[start:end]in cassette1) or (seqb[start:end]in cassette2):
            flag=1
            #print(seqr[start:end])
            end=end+step
        elif flag==1:
            #print(seqr[start:end-step])
            q1=cassette1.find(seqb[start:end-step])
            q2=cassette2.find(seqb[start:end-step])
            p=end-start
            seqs.append(q1)
            seqs.append(q2)
            seqs.append(start)
            seqs.append(end-step)#########
            seqs.append(p)
            num+=1
            flag=2
            start=end
            end=start+origin_longth
        elif flag==2 or flag==0:
            start=start+1
            end=start+origin_longth        
    if flag==0:
        return -1
    elif flag==1:#
        q1=cassette1.find(seqb[start:end-step])
        q2=cassette2.find(seqb[start:end-step])
        p=end-start
        seqs.append(q1)
        seqs.append(q2)
        seqs.append(start)
        seqs.append(end-step)
        seqs.append(p)
        return seqs    
    else:        
        return seqs
for key in dictseq2:
    for seq in dictseq2[key]:
        bms=bmds1213(seq)
        if bms!=-1:
            #D8_D6_3,[-1, 2, 200, 243, 44, -1, 67, 265, 295, 31]
            #1C15_4,[0, -1, 295, 325, 31, 52, -1, 347, 392, 46]
            c=seq
            if len(bms)==10 and bms[5]==52:
                rg=c[bms[7]:bms[8]]
                ds=c[bms[8]:]
                bar=c[bms[3]:bms[7]]
                fw.write(key+"["+bar+"]<"+rg+">"+ds+"\n")
                
            elif len(bms)==10 and bms[6]==67:
                rg=c[bms[2]:bms[3]]
                ds=c[:bms[2]]
                bar=c[bms[3]:bms[7]]
                fw.write(key+"["+ATCG_CGAT(bar)+"]<"+ATCG_CGAT(rg)+">"+ATCG_CGAT(ds)+"\n")
        
        

fw.close()

print("the end")

print("the end")    
    
        
