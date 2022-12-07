import sys, csv, argparse
data = []
parser = argparse.ArgumentParser()
parser.add_argument('file',help='the csv file to display')
parser.add_argument('-s','--style',help='output style number',type=int)
args = parser.parse_args()
with open(args.file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        #print(row)
        data.append(row)
        #data.append(row.removesuffix(',').split(','))



#print(data)
#for x in data: print(x)
d  = '╔╚╗╝╦╩══║║╠╣╬'
s  = '┌└┐┘┬┴──││├┤┼'
do = '╔╚╗╝╤╧═─║│╟╢┼'
so = '┌└┐┘╥╨─═│║╞╡╬'
sr = '╭╰╮╯┬┴──││├┤┼'

c = s
if args.style == 1:
    c = s

if args.style == 2:
    c = d

if args.style == 3:
    c = do

if args.style == 4:
    c = so

if args.style == 5:
    c = sr


dr = c[0]#'┌'
ur = c[1]#'└'
dl = c[2]#'┐'
ul = c[3]#'┘'
drl = c[4]#'┬'
url = c[5]#'┴'
rl = c[6]#'─'
rl1 = c[7]#'─'
ud = c[8]#'│'
ud1 = c[9]#'│'
udr = c[10]#'├'
udl = c[11]#'┤'
udrl = c[12]#'┼'

#data = [['1', '2', '3'],
#        ['2', '4', '6'],
#        ['3', '6', '9']]
longests = list(bytes(len(data[0])))
for x in range(len(data)):
    #print(data[x])
    for y in range(len(data[x])):
        if len(data[x][y]) > longests[y]:
            longests[y] = len(data[x][y])
ndata = []
# print(longests)
for x in range(len(data)):
    ndata.append([])
    for y in range(len(data[x])):
        ndata[x].append(data[x][y] + ' ' * (longests[y] - len(data[x][y])))

# print(ndata)


text = ''
texts = []
datas = []
mids = []
tops = []

bots = []

for x in range(len(longests)):
    tops.append(rl * (longests[x] + 2))
    mids.append(rl1 * (longests[x] + 2))
    bots.append(rl * (longests[x] + 2))

top = dr + drl.join(tops) + dl
mid = '\n' + udr + udrl.join(mids) + udl + '\n'
bot = ur + url.join(bots) + ul

for x in ndata:
    datas.append(ud + ' ' + (' ' + ud1 + ' ').join(x) + ' ' + ud)
texts.append(top)
texts.append(mid.join(datas))
texts.append(bot)
# print(texts)

print('\n'.join(texts))
