"""
Här är keno,

jag börjar med att importera några biblotek

--------------------------------------------------------------------->

os: är för att kunna ladda ner styles för du har förmodligen inte det
och för att kunna göra endel andra commandon som -- cls -- det betyder clear

styles: för att kunna göra färger, loadingbars och andra kolla saker

random: för att detta program ska kunna lura folk

time: för att kunna göra lite coola pauser

json: för att spara info

--------------------------------------------------------------------->
"""
from os import system

#vi använder system för att få styles om man inte har den installerat
import styles, random, time, json

system("cls")   # Detta är för att terminalen annars kommer vara ganska ful av ord





"""Extras"""
#detta är pris listan, jag vet det är overkill
pris_lista = {
    "1":
    {
        "0": 0,
        "1": 10
    },

    "2":
    {
        "0": 0,
        "1": 0,
        "2": 30
    },

    "3":
    {
        "0": 0,
        "1": 0,
        "2": 5,
        "3": 60
    },

    "4":
    {
        "0": 0,
        "1": 0,
        "2": 5,
        "3": 10,
        "4": 120
    },

    "5":
    {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 5,
        "4": 40,
        "5": 800
    },

    "6":
    {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 5,
        "4": 15,
        "5": 90,
        "6": 1700
    },

    "7":
    {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 5,
        "5": 50,
        "6": 400,
        "7": 10000
    },

    "8":
    {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 5,
        "5": 15,
        "6": 100,
        "7": 1000,
        "8": 45000
    },

    "9":
    {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 5,
        "6": 50,
        "7": 250,
        "8": 5000,
        "9": 250000
    },

    "10":
    {
        "0": 5,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 5,
        "6": 15,
        "7": 100,
        "8": 800,
        "9": 15000,
        "10": 1000000
    },

    "11":
    {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 5,
        "6": 10,
        "7": 30,
        "8": 200,
        "9": 2000,
        "10": 80000,
        "11": 5000000
    }
}

pris_lista_kung = {
    "1":
    {
        "0": 0,
        "1": 170
    },

    "2":
    {
        "0": 0,
        "1": 40,
        "2": 240
    },

    "3":
    {
        "0": 0,
        "1": 25,
        "2": 50,
        "3": 400
    },

    "4":
    {
        "0": 0,
        "1": 30,
        "2": 30,
        "3": 60,
        "4": 800
    },

    "5":
    {
        "0": 0,
        "1": 30,
        "2": 15,
        "3": 30,
        "4": 150,
        "5": 2500
    },

    "6":
    {
        "6": 10000,
        "5": 300,
        "4": 50,
        "3": 15,
        "2": 10,
        "1": 30,
        "0": 0
    },

    "7":
    {
        "0": 0,
        "7": 25000,
        "6": 1000,
        "5": 150,
        "4": 30,
        "3": 10,
        "2": 10,
        "1": 30
    },

    "8":
    {
        "0": 0,
        "8": 130000,
        "7": 2000,
        "6": 300,
        "5": 30,
        "4": 15,
        "3": 10,
        "2": 10,
        "1": 30
    },

    "9":
    {
        "0": 0,
        "9": 600000,
        "8": 10000,
        "7": 500,
        "6": 100,
        "5": 15,
        "4": 10,
        "3": 10,
        "2": 10,
        "1": 30
    },

    "10":
    {
        "0": 5,
        "10": 2000000,
        "9": 30000,
        "8": 1600,
        "7": 200,
        "6": 50,
        "5": 15,
        "4": 10,
        "3": 10,
        "2": 10,
        "1": 30
    },

    "11":
    {
        "0": 0,
        "11": 20000000,
        "10": 160000,
        "9": 4000,
        "8": 500,
        "7": 100,
        "6": 15,
        "5": 15,
        "4": 10,
        "3": 10,
        "2": 10,
        "1": 30
    }
}
#---------------------------------------------




"""funktioner och metoder:"""
def isInt(x=str(None)):
    #den här kollar om det man valde är en int eller inte
    try:
        x = int(x)
        return True
    except:
        return False


#här är spelet
class GamblingGame():
    #här under kommer viktiga variabler att "sättas" typ self.name = name
    def __init__(self):
        #reklam generation
        self.GenereraAds()

        #här får vi för- och efternamn
        self.förnamn = self.GetFörname()
        self.efternamn = self.GetEfternamn()

        #spelarens siffror
        self.siffror_användaren = []

        #spelets siffror
        self.spel_siffror = []
        self.antalRätt = 0

        #hur många siffror man valde
        self.current_siffror = 0

        #vinnst
        self.pris = 0
    #--------------------------------------------------------------------



    #här under kommer allt viktigt att vara
    def main(self):
        #kungkeno eller inte
        self.kungkeno = self.väljerkungkeno()

        #väljer siffror
        self.spelets_siffror()

        #här är starten för gambling och ett lyckligt liv
        print(styles.Colors["GREEN"] + "Välkommen till lyckans dal: ", self.förnamn, self.efternamn)
        
        #här kommer man att få välja siffror och välja hur många man vill ha
        self.antal = self.väljAntalSiffror()
        self.vilkaSiffrorVäljs(self.antal)

        #först tar vi bort all text, sen skriver vi ut vad använder har för inställningar
        system("cls")
        #skriver namn
        print(styles.Colors["CYAN"] + f"Du har valt namnet: {self.förnamn} {self.efternamn}")
        
        #här tar vi och skriver ut vilka tal man valde
        print("du valde dessa siffror att chanse med:")
        for x in range(len(self.siffror_användaren)):
            #om det är sista siffran skrivs siffran bara ut
            if len(self.siffror_användaren) - x == 1:
                print(self.siffror_användaren[x])
            else:
                #men om det inte är sista siffran så skrivs den ut med : i slutet
                print(self.siffror_användaren[x], end=" : ", flush=True)
                #sen sätter vi en delay på 0.2 sek, så att det ska vara lite loadingbar aktickt
                time.sleep(0.2)
        
        #här under så är spelet
        self.vinnster()

        #spara info om använderän
        self.SparaInfo()
        
        #spela igen
        ja = ["JA", "ja", "Ja", "yes", "YES", "Yes"]
        spelaigen = input(styles.Colors["BOLD"] + "Spela Igen? (JA/NEJ): ")
        if spelaigen in ja:
            #återställer allt igen
            self.antalRätt = 0
            self.siffror_användaren = []
            self.spel_siffror = []
            self.spelets_siffror()
            
            #återstartar main
            self.main()
    #--------------------------------------



    #för- och efternamn
    def GetFörname(self):
        #gör en loop ända tills vi får förnamn
        while True:
            #här är förnamn en input så att man kan skriva in sitt förnamn
            förnamn = input(styles.Colors["GREEN"] + "Förnamn: ")

            #här kollar vi om det är giltilgt
            if förnamn != "":
                False
                return förnamn
    def GetEfternamn(self):
        #gör en loop ända tills vi får efternamn
        while True:
            #här är efternamn en input så att man kan skriva in sitt efternamn
            efternamn = input(styles.Colors["GREEN"] + "Efternamn: ")

            #här kollar vi om det är giltilgt
            if efternamn != "":
                False
                return efternamn
    #------------------



    #här kommer vi att välja om man vill köra med kungkeno
    def väljerkungkeno(self):
        ja = ["ja", "JA", "yes", "Ja", "Yes", "YES", "y", "Y"]
        svar = input("Kung Keno, ger upp till 20 miljoner kronor (Ja/Nej): ")

        if svar in ja:
            return True
        else:
            return False
    #-----------------------------------------------------

    

    #här kommer man att kunna välja siffror att spela med
    def väljAntalSiffror(self):
        #här kommer man att få välja på ett tall mellan 1 - 11
        while True:
            print(styles.Colors["BLUE"] + "\nVar vänligt och välj hur många siffror du vill chansa med (1 - 11)")
            antal = input(styles.Colors["ENDC"] + ": ")

            #här kollar vi om det är en int, så att det funkar med programmet
            #vi kollar också om det är mindre än 11 eller mer än 1 så klart kan man fortfarande ta 1 och 11
            if isInt(antal) == True and int(antal) <= 11 and int(antal) >= 1:
                False
                self.current_siffror = int(antal)
                return int(antal)
    def vilkaSiffrorVäljs(self, antal=int(1)):
        #här välja alla siffror som användaren vill chansa med
        for x in range(antal):
            #jag vet att vi har en till loop i en loop, men det är för att jag inte vill ha errors
            #och vi använder run = True, för bara True funkade inte
            run = True
            while run:
                #här tar vi en input på vilka siffror som ska användas
                svar = input(styles.Colors["CYAN"] + f"Siffra {x + 1}: ")
                #vi gör en enkel koll på om det är siffror, är det det så lägger vi till dem i listan
                #vi sätter också en spär så att man inte kan ta 100 eller 0
                if isInt(svar) == True and int(svar) >= 1 and int(svar) <= 70 and svar not in self.siffror_användaren:
                    self.siffror_användaren.append(svar)
                    run = False
    #----------------------------------------------------
    


    #spelets siffror kommer väljas här under
    def spelets_siffror(self):
        self.spel_siffror = random.sample(range(1, 70), 20)

        #väljer en kung siffra
        if self.kungkeno == True:
            #x = random.randint(1, 20)
            #self.kungSiffra = self.spel_siffror[(x-1)]
            self.kungSiffra = 65
    #---------------------------------------


    
    #här under kommer vi kolla om man van något när man spelade
    def vinnster(self):
        #skriver vilka siffror som valdes, inc kung siffran
        print("\n\n")
        print(styles.Colors["BLUE"] + "Dessa siffror kan man vinna på:")
        for x in self.spel_siffror:
            print(str(x) + " ", sep="", end="", flush=True)
            time.sleep(0.1)
        print("\n")
        time.sleep(0.2)
        if self.kungkeno == True:
            print("Denna siffran var kung Keno: " + str(self.kungSiffra))
        
        print("\n")
        time.sleep(0.5)

        #sen kollar vi om några siffror passar
        if self.kungkeno == False:
            for x in self.spel_siffror:
                if str(x) in self.siffror_användaren:
                    print(styles.Colors["GREEN"] + "Du gissade rätt på: ", styles.Colors["ENDC"] + str(x))
                    print("\n")
                    self.antalRätt += 1
        
            #räknar ut priset
            p = pris_lista[str(self.current_siffror)]
            self.pris = p[str(self.antalRätt)]
        
        else: #här kollar vi om man van på kungkeno
            if str(self.kungSiffra) in self.siffror_användaren:
                for x in self.spel_siffror:
                    if str(x) in self.siffror_användaren:
                        print(styles.Colors["GREEN"] + "Du gissade rätt på: ", styles.Colors["ENDC"] + str(x))
                        print("\n")
                        self.antalRätt += 1

                #om vi då hittar kung siffran då vinner man annars förlorar man, så här räknar vi priser
                p = pris_lista_kung[str(self.current_siffror)]
                self.pris = p[str(self.antalRätt)]
            
            else:
                self.pris = 0
        

        #lägger till priser i din plångbok, eller skapar en plånbok som sedan får priset
        try:
            self.valet += int(self.pris)
        
        except:
            self.valet = int(self.pris)

        #skriver ut hur mycket man van
        if self.pris > 0 and self.kungkeno == False:
            print(styles.Colors["GREEN"] + f"{self.förnamn} du hade {self.antalRätt} antal rätt")
            print(styles.Colors["GREEN"] + "Du van just " + str(self.pris) + "kr")
        
        elif self.kungkeno == True and self.pris > 0:
            print(styles.Colors["GREEN"] + f"DU VAN JUST PÅ KUNG KENO {self.förnamn}")
            print(styles.Colors["GREEN"] + "DU KAN NU VARA", styles.Colors["BOLD"] + str(self.pris) + "KR", "STOLTARE ÖVER DIG SJÄLV")
        elif self.kungkeno == True and self.pris <= 0:
            print(styles.Colors["WARNING"] + f"Tyvärr {self.förnamn} men denna gången var inte lyckan din")
            time.sleep(1)
            self.GenereraAds()
        else:
            print(styles.Colors["WARNING"] + f"Du van tyvärr inget {self.förnamn}")
            print("Bättre Lycka nästa gång för: ")
            time.sleep(1)
            self.GenereraAds()
        print("\n")
    #----------------------------------------------------------
    


    #här under kommer vi att spara info så att vi kan generera reklam - denna börs inte tas bort
    def SparaInfo(self):
        try:
            with open("appInfo.json") as f:
                data = json.load(f)

                #sen sparar vi och skriver över allt som ska skriva över
                data["senastAnvändt"].append(self.current_siffror)
                data["pengar"] += self.valet

                #här räknar vi ut vad som aftast används
                data["medelAnvänr"] = self.vilketÅterkommerFlestGånger(data["senastAnvändt"])

                with open("appInfo.json", "w") as f:
                    json.dump(data, f, indent=4)

        except:
            with open("appInfo.json", "w") as f:
                #här bygger upp info delen om den inte redan finns
                user_info = {
                        "namn": self.förnamn,
                        "efternamn": self.efternamn,
                        "pengar": self.valet,
                        "senastAnvändt": [],
                        "medelAnvänr": 0,
                    }

                #sen sparar vi och skriver över medelvärde
                user_info["senastAnvändt"].append(self.current_siffror)
                user_info["medelAnvänr"] = self.vilketÅterkommerFlestGånger(user_info["senastAnvändt"])

                json.dump(user_info, f, indent=4)
    #-------------------------------------------------------------------------------------------



    #Här kollar vi vilket numer som nämns oftast i en lista
    def vilketÅterkommerFlestGånger(self, lista):
        return max(set(lista), key = lista.count)
    #------------------------------------------------------



    #här skapas alla ads: OBS - ta inte bort
    def GenereraAds(self):
        try:
            with open("appInfo.json") as f:
                data = json.load(f)

                medelvärd = data["medelAnvänr"]
                pengar = str(100000000) + "$"
                sattsning = str(medelvärd)

                print(styles.Colors["WARNING"] + """
                https://www.fancytextpro.com/BigTextGenerator?qtext=%24Jack%20Pott%24

                   $$\       $$$$$\                     $$\             $$$$$$$\             $$\     $$\        $$\    
                 $$$$$$\     \__$$ |                    $$ |            $$  __$$\            $$ |    $$ |     $$$$$$\  
                $$  __$$\       $$ | $$$$$$\   $$$$$$$\ $$ |  $$\       $$ |  $$ | $$$$$$\ $$$$$$\ $$$$$$\   $$  __$$\ 
                $$ /  \__|      $$ | \____$$\ $$  _____|$$ | $$  |      $$$$$$$  |$$  __$$\\_$$  _|\_$$  _|  $$ /  \__|
                \$$$$$$\  $$\   $$ | $$$$$$$ |$$ /      $$$$$$  /       $$  ____/ $$ /  $$ | $$ |    $$ |    \$$$$$$\  
                 \___ $$\ $$ |  $$ |$$  __$$ |$$ |      $$  _$$<        $$ |      $$ |  $$ | $$ |$$\ $$ |$$\  \___ $$\ 
                $$\  \$$ |\$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | \$$\       $$ |      \$$$$$$  | \$$$$  |\$$$$  |$$\  \$$ |
                \$$$$$$  | \______/  \_______| \_______|\__|  \__|      \__|       \______/   \____/  \____/ \$$$$$$  |
                 \_$$  _/                                                                                     \_$$  _/ 
                   \ _/                                                                                         \ _/
                """)
                print(styles.Colors["WARNING"] + styles.Colors["BOLD"] + f"Nu kan du vinna UPP TILL {pengar} om du sattsar på {sattsning} stycken siffror!!!")
        
        except:
            print(styles.Colors["WARNING"] + styles.Colors["BOLD"] + "Du kan nu vinna UPP TILL 100 000$ på bara någon runda!!!")
    #---------------------------------------





"""starta programmet:"""
if __name__ == "__main__":
    GamblingGame().main()