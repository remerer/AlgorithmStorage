import time
year = time.localtime().tm_year
mon = time.localtime().tm_mon
day = time.localtime().tm_mday
print(year,'%02d'%mon,day,sep='-')