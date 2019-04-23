import numpy
import sklearn
import csv
import random
def main():
    file = 'C:\\Users\\dafoland\\Desktop\\table2.csv'
    generate_rows(1000,file)
    print("Done")

def generate_rows (tup,file):
    f1 = open(file, 'w+')
    string4 = ["AAAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
               "HHHHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
               "OOOOxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
               "VVVVxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]
    # write columns
    f1.write("unique1,unique2,two,four,ten,twenty,onePercent,tenPercent,twentyPercent,fiftyPercent,unique3,evenOnePercent,oddOnePercent,stringu1,stringu2,string4\n")
    # fill in data
    for x in range(tup):
        out_str = ""
        unique1 = random.randint(0,tup)
        f1.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % \
              (unique1,x,unique1 % 2,unique1 % 4,unique1 % 10,unique1 % 20,unique1 % 100,unique1 % 10,unique1 % 5, \
               unique1 % 2,unique1,((unique1 % 100)*2),((unique1 % 100)*2+1),convert(unique1),convert(x),string4[x%4]))

    f1.close()

def convert(unique):
    result = []
    tmp = []
    # use algo to create char array
    while (unique > 0):
        rem = unique % 26
        tmp.append(chr(ord('A') + int(rem)))
        unique = unique // 26;
    tmp.reverse()

    # append with A's to make 7 digits
    for i in (range(7-len(tmp))):
        result.append('A')

    # append with char array
    for i in tmp:
        result.append(i)

    # concat result string with 45 X characters
    return ("".join(result)+"X"*45)

if __name__ == "__main__":
    main()