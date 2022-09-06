allpen = 270
dozenpen = 12
dozen = allpen // dozenpen
pen = allpen % dozenpen

print("볼펜 {0}개는 {1}다스이며 다스에 들어가지 않은 볼펜은 {2}개이다.".format(allpen, dozen, pen))