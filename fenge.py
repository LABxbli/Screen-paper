#python
###############################################
#######################

import os 
def file_name2(file_dir): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if '.txt' in file:
                L.append(os.path.join(root, file))
    return L

for i in file_name2("path_to_the_Sequence set containing the upstream and downstream fragments of the barcode/"):
    if "the_Special-recognition-characters" in i:
        print(i)
        name=i.split(".txt")[0]
        f1=open(name+".txt",'r')
        f2=open(name+'_1.fasta','w')
     
        f3=open(name+'_2.fasta','w')
        j=1
        while 1:#过滤后值过低，怀疑存在空行导致的中断，首先获取文件行数后，按行数读取截止。wc -l
            a1=f1.readline().strip()
            if a1=='':break
        
            b=a1.split("NNNNNNNNNNNNNATCGNNNNNNNNNNNNN")
            f2.write(">"+str(j)+"_1\n"+b[0]+"\n")
            f3.write(">"+str(j)+"_2\n"+b[1]+"\n")
            j+=1
        
                
        f1.close()
        f2.close()
        f3.close()

print("The end!")