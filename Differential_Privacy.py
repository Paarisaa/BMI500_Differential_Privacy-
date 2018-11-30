# -*- coding: utf-8 -*-
"""
This code is written for homework #12 for BMI500 course.

@author: Parisa Sarikhani 
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy 

#file_path='./adult_age_gender_race_dataset.csv'
def Diff_Privacy(file_path,Epsilon):
    # Read the csv file and 
    data=pd.read_csv(file_path)
    df = pd.DataFrame(data) 
    max_Age=df['Age'].max() #Sensitivity

    # plot histogram of original age: 
    
    bin_edges=[5*i+17 for i in range(16)]
    if Epsilon==0.1:# just plot the original histogram just for epsilon=0.1
        count = plt.hist(df['Age'],bins=bin_edges,histtype='bar',rwidth=1,color='white', edgecolor = "black",linestyle = '-')
        _ = plt.xlabel('Age')
        _ = plt.ylabel('# of adults')
        plt.title('Original histogram')
        plt.savefig('Original histogram.png')
        plt.show()
    
    count = plt.hist(df['Age'],bins=bin_edges,histtype='bar',rwidth=1,color='white', edgecolor = "black",linestyle = '-')
    _ = plt.xlabel('Age')
    _ = plt.ylabel('# of adults')
                   

    # generate laplasian samples
    mean=0
    sigma=max_Age/Epsilon
    S = numpy.random.laplace(mean, sigma, len(bin_edges))
    New_count=[count[0][j]+S[j] for j in range(len(S)-1)]
    for i in range(len(New_count)):
        if New_count[i]<0:
            New_count[i]=0
    #plot noisy histogram    
    new_bin=[bin_edges[k]+2.5 for k in range(len(bin_edges))]
    newcount = plt.bar(new_bin[:-1],New_count, width =5 , edgecolor = "red",linestyle = '--',label='')

    _ = plt.xlabel('Age')
    _ = plt.ylabel('# of adults')

    plt.legend(['Original histogram','Noisy histogram'])
    plt.title('Epsilon= '+str(Epsilon))
    plt.savefig('histograms'+str(Epsilon)+'.png')
    plt.show()
    Error=numpy.mean(numpy.abs(count[0]-New_count))
    plt.close()
    return Error


if __name__== "__main__":
    
    #file_path='./adult_age_gender_race_dataset.csv'
    #[0.1,0.2,0.4,0.8,1]
    EPS=sys.argv[2]
    EPS=(EPS).split(',')
    epsilons=[]
    for a in EPS:
        epsilons.append(float(a))
        
    ERROR=[]
    for Epsilon in epsilons:
        
        Error=Diff_Privacy(sys.argv[1],Epsilon)
        ERROR.append(Error)
        print('Error for Epsilon= '+str(Epsilon)+' = '+ str(Error))
    plt.plot(EPS,ERROR)
    plt.title('Mean of error between original and noisy histograms over bins of length 5')
    plt.xlabel('Epsilon')
    plt.ylabel('Mean of error')
    plt.savefig('Error plot')
    plt.show()
