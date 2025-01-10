#python3
###########################################
##############ATCG_TAGC()########
def ATCG_TAGC(seq):
    n=len(seq)
    temp=""
    i=0
    while i<n:
        temp+=A_T(seq[i])
        i+=1
    return temp
##########################################################################
#############A_T()###################
def A_T(a):
    if a=="A":
        a="T"
    elif a=="T":
        a="A"
    elif a=="G":
        a="C"
    elif a=="C":
        a="G" 
    return a
###############################################################
###########ATCG_CGAT()############
def ATCG_CGAT(seq):
    n=len(seq)
    temp=""
    i=0
    while i<n:
        temp+=A_T(seq[n-1-i])
        i+=1
    return temp
###############################################################
def file_name2(file_dir): #
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if 'scaffolds.fasta' in file:
                L.append(os.path.join(root, file))
    return L
def file_name1(file_dir): #
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if '.paf' in file:
                L.append(os.path.join(root, file))
    return L

dictseq={}
for i in file_name2("path_to_the_Whole-genome-sequence-obtained-from-SPAdes-assembly/"):
    if "the_Special-recognition-characters"  in i:
        #print(i)
        f2=open(i,'r')
        name=i.split("/")[-1].split("_scaffolds.fasta")[0]
        while 1:
            a=f2.readline().strip()
            b=f2.readline().strip()
            if a=="":break
            key=name+"_"+a
            if key in dictseq:
                
                if dictseq[a]!=b:
                    print("a")
            else:
                dictseq[key]=b
        f2.close()
print(len(dictseq))
f4=open('cassin.fasta','a')
for i in file_name1("path_to_the_paf_files/"):
    if "the_Special-recognition-characters" in i:
        #print(i)
        
        f3=open(i,"r")
        name=i.split("/")[-1].split("_scaffolds.fasta")[0]#Note that replacement should be based on the naming convention for recognition
        while 1:
            a=f3.readline().strip()
            if a=="":break
            b=a.split("\t")
            
            chr1=name+"_>"+b[0]
            site1=int(b[2])
            site2=int(b[3])
            flag=b[4]
            if flag=="-":
                f4.write(">"+b[5]+"_"+chr1+"\n"+ATCG_CGAT(dictseq[chr1][site1:site2])+"\n")
            else:        
                f4.write(">"+b[5]+"_"+chr1+"\n"+dictseq[chr1][site1:site2]+"\n")
        
    


f4.close()
print("The end!")
