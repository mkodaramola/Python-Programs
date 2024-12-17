import wikipedia as wk


toSearch = wk.search('cell')

print(toSearch)
print(toSearch[0])

print(wk.summary(toSearch[0],sentences=2))

# import yadisk_api as ya

# disk = ya.YandexDisk('samsung')
# info = disk.get_disk_info()

# print(info) 