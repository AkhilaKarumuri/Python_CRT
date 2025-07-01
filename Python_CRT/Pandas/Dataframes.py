import pandas as pd
Data={
    'Student 1':
    {'Name':'Akhila',
    'Branch':'CSE',
    'Roll':'1',
    'Skills':['Python','DSA','SQL','C']
    },
    'Student 2':
    {
        'Name':'Amulya',
        'Branch':'BioInformatics',
        'Roll':'2',
        'Skilla':['Docking','Chipseq','RNAseq','Gromacs']
    },
}
Data=pd.DataFrame(Data)
print(Data)
print(type(Data))