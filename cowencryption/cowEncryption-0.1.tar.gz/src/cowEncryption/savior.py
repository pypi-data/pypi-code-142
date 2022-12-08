import re

class Main:
    def __init__(self, file, jenis):
        self.jenis = jenis
        self.file = file
        self.decToEnc = {
            "a":"KANoejfanAINFa", 
            "b":"fdsfsdfsewfw", 
            "c":"fwhwiuqhidbq",
            "d":"hdakshdq", 
            "e":"hhcxxfgx", 
            "f":"fdfndkasjf", 
            "g":"bdsajbdja", 
            "h":"jdsajbdjsa", 
            "i":"dsawwqdasda", 
            "j":"bjbbjbb",
            "k":"jiowqnw",
            "l":"v7767yc",
            "m":"913udh",
            "n":"Idnwqi",
            "o":"(hwdqndaK",
            "p":"HDqnakdna",
            "q":"Jojasndkan",
            "r":"Hqhdasjdkc",
            "s":"Ljfqeifnas",
            "t":"PWqdbwbqndq",
            "u":"JCNasbcqih",
            "v":"Nsadhduhwxja",
            "w":"OD(QJdsna",
            "x":"Mxjw1`jojdoqwdq",
            "y":"CMiqhiqnc1",
            "z":"jcwIJDandsakdnwq",
            '!':'31ncwojdw',
            '@':'928jsdbfj',
            '#':'02jfkdskm',
            '$':'021jqjinqdwq',
            '%':'19u1kdnfs',
            '^':'9u32uinfwbc',
            '&':'91ue1dadsaiqwni',
            '*':'43cgvhmiiwwcmimw',
            '(':'10nkanksdsa',
            ')':'51nicnaksnknec',
            '_':'832ubffjdsfs',
            '-':'402nksnvknskndsk',
            '\\':'7f35gvv',
            '|':'93njnjvdfs',
            '<':'28hfsjfcb8982',
            '>':'f93jndksnfsfds',
            '/':'ciwjwc9wnfwnfwe00n',
            '?':'jbbfcfxrxs76v',
            '`':'dfknsnfs9fdsfdsqweq',
            '~':'fndsn92n2jnflaknsaknda',
            ',':'bb7h8yt6ftcgvib',
            '.':'idnqwbidhwqnd1121',
            ';':'njniidsninvsvs7787878',
            ':':'buu09ud',
            '"':'invis02nksdnvs',
            ' ':'fskfinin2891313b',
            "'":"asdbuqb219",
            '\n':'henceut',
            '0':'dabsbdajw@31',
            '1':'kasdaononoaeno',
            '2':'iwne-wfjnw',
            '3':'ncksdfiewbcwibomcwscs',
            '4':'orwem=vw',
            '5':'$nfap[sdfse',
            '6':'\[buvucuc',
            '7':'vib@kdsnkcs',
            '8':'awndai1nd1isa',
            '9':'dnasnda0hb1',
            '=':'uvuvoiy8ghvhvyv',
            '{':'fnfkdsfwppnkncmamdnf',
            '}':'i2nfnw$@wfke',
            '[':'19uabdaasd!',
            ']':'aindsak^sjfnd',
            "\t":"ewnfocnncknscdc",
            "\n":"ovrwoinqosinqx889"
        }
        self.enc, self.run = [], []
        self.lala = lambda x: "".join(i for i in self.decToEnc.keys() if self.decToEnc[i]==x)

class Encryption(Main):
    def encPrem(self):
        try:
            if(self.jenis=="file"):
                with open(self.file, "r") as f:
                    for _ in list(f.read()):
                        self.enc.append(_)
                    with open(self.file[0:-3]+"_enc.py", "a") as e:
                        e.write(f"from cowEncryption.savior import Running\n\nexec(\"Running('{''.join(self.decToEnc[x.lower()] for x in self.enc)}', 'running').decPrem('running')\")")
                return "[success] file saved: "+str(self.file[0:-3])+"_enc.py"
        except FileNotFoundError:
            return "[filed] error file not found error!"
        except:
            return "[filed] error character! don't use a emote or char ilegal"

class Running(Main):
    def decPrem(self, password):
        if(password=="Oloy2811#awokawok176" or password=="running"):
            encToDec, dd = {}, ""
            for k,v in self.decToEnc.items():
                encToDec.update({v:k})
            if(self.jenis=="file" and password=="Oloy2811#awokawok176"):
                with open(self.file, "r") as f:
                    data = re.findall("Running\(\'(.*)\',", str(f.read()))
                    for _ in data[0]:
                        dd += _
                        with open(self.file[0:-3]+"_dec.py", "a") as e:
                            if dd in self.decToEnc.values():
                                e.write(encToDec[dd])
                                dd = ""
            else:
                for _ in self.file:
                    dd += _
                    if dd in self.decToEnc.values():
                        self.run.append(encToDec[dd])
                        dd = ""
                exec("".join(x for x in self.run))
            dd = ""
        else:
            exit("wrong password!")
