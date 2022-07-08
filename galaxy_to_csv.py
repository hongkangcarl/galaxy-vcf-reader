import pandas as pd
import os

path = input('Please paste the address of the FOLDER containing the vcf files: ')

files = os.listdir(path)
files.sort()

j = 0
df = pd.DataFrame(columns = ['tRNA', 'POS', 'REF', 'ALT', 'ADP', 'VAR', 'FILE_NAME'])
for file_name in files:
    if file_name[-4:] == '.vcf':
        with open(path + '/' + file_name) as file:

            data = file.read()
            s1 = data.find('\n#CHROM')
            chrom = data[s1:]
            table = (chrom.split('\n'))[2:-1]
            for i in range(len(table)):
                str_list = (table[i]).split('\t')
                df.loc[j, 'tRNA'] = str_list[0][18:]
                df.loc[j, 'POS'] = str_list[1]
                df.loc[j, 'REF'] = str_list[3]
                df.loc[j, 'ALT'] = str_list[4]
                df.loc[j, 'ADP'] = int((str_list[7].split(';'))[0][4:])
                df.loc[j, 'VAR'] = float(((str_list[9].split(':'))[6]).strip('%'))
                df.loc[j, 'FILE_NAME'] = file_name[:-4]
                j += 1

df.to_csv(path + '/vcf_converted.csv')

print('Finished!')