import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
#import pkg_resources
#try:
#    import importlib.resources as pkg_resources
#except ImportError:
    # Try backported to PY<37 `importlib_resources`.
#    import importlib_resources as pkg_resources
import numpy as np
arr=np.array([[0, 'TN0007250012', 'Consolider', 'ADWYA', 'Societe Adwya',
        'ADWYA'],
       [1, 'TN0007500010', 'Alléger', 'Ae Tech', 'Ae Tech', 'AETEC'],
       [2, 'TN0002300358', 'Conserver', 'AIR LIQUIDE Tun',
        'Air Liquide Tunisie', 'AL'],
       [3, 'TN0003800703', 'Conserver', 'AL KIMIA', 'Societe Chimique',
        'ALKM'],
       [4, 'TN0003400058', 'Consolider', 'AMEN BANK', 'Amen Bank', 'AB'],
       [5, 'TN0001500859', 'Vendre', 'Ateliers Mecaniques Sahel',
        'Societe Les Ateliers Mecaniques du Sahel SA', 'AMS'],
       [6, 'TN0007300015', 'Consolider', 'ARTES RENAULT',
        'ARTES RENAULT', 'ARTES'],
       [7, 'TN0007140015', 'Consolider', 'ASSAD',
        "Societe L'Accumulateur Tunisien", 'ASSAD'],
       [8, 'TN0003000452', 'Consolider', 'ASTREE SA', 'ASTREE SA', 'AST'],
       [9, 'TN0003600350', 'Acheter', 'ATB', 'Arab Tunisian Bank', 'ATB'],
       [10, 'TN0007740012', 'Acheter', 'Atelier Meuble Interieurs',
        'Atelier du Meuble Interieurs SA', 'SAMAA'],
       [11, 'TN0004700100', 'Acheter', 'ATL', 'Arab Tunisian Lease',
        'ATL'],
       [12, 'TN0001600154', 'Acheter', 'ATTIJARI BANK',
        'Banque Attijari De Tunisie', 'BS'],
       [13, 'TN0006610018', 'Conserver', 'ATTIJARI LEASING',
        'Attijari Leasing', 'TJL'],
       [14, 'TN0007580012', 'Conserver', 'Best Lease', 'Best Lease',
        'BL'],
       [15, 'TN0006550016', 'Consolider', 'Ste Assurance Salim',
        'Ste Assurance Salim SA', 'BHASS'],
       [16, 'TN0001900604', 'Consolider', 'BH', "Banque De L'Habitat",
        'BH'],
       [17, 'TN0006720049', 'Allèger', 'Modern Leasing',
        'Modern Leasing', 'ML'],
       [18, 'TN0001800457', 'Acheter', 'BIAT',
        'Banque Internationale Arabe Tunisie', 'BIAT'],
       [19, 'TN0003100609', 'Conserver', 'BNA',
        'Banque Nationale Agricole', 'BNA'],
       [20, 'TN0002200053', 'Consolider', 'BT', 'Banque De Tunisie',
        'BT'],
       [21, 'TN0001300557', 'Allèger', 'BTEI',
        'Banque De Tunisie Et Des Emirats', 'BTEI'],
       [22, 'TN0007400013', 'Consolider', 'Carthage Cement',
        'Carthage Cement', 'CC'],
       [23, 'TN0007590011', 'Allèger', 'Cellcom', 'Cellcom', 'CELL'],
       [24, 'TN0007640014', 'Acheter', 'Cerealis Sa', 'Cerealis Sa',
        'CREAL'],
       [25, 'TN0004200853', 'Acheter', 'CIL',
        'Compagnie Internationale De Leasing', 'CIL'],
       [26, 'TN0007350010', 'Consolider', 'Les Ciments de Bizerte',
        'Les Ciments De Bizerte', 'SCB'],
       [27, 'TN0007550015', 'Consolider', 'City Cars', 'City Cars',
        'CITY'],
       [28, 'TN0007670011', 'Acheter', 'Societe Delice Holding',
        'Societe Delice Holding', 'DH'],
       [29, 'TN0006650014', 'Vendre', 'ELECTROSTAR', 'Electrostar',
        'LSTR'],
       [30, 'TN0007410012', 'Conserver', 'Ennakl Automobiles',
        'Ennakl Automobiles SA', 'NAKL'],
       [31, 'TN0007210016', 'Conserver', 'ESSOUKNA', 'Essoukna', 'SOKNA'],
       [32, 'TN0007570013', 'Acheter', 'Euro-Cycles', 'Euro-Cycles',
        'ECYCL'],
       [33, 'TN0007130016', 'Vendre', 'GIF FILTRATION', 'GIF FILTRATION',
        'GIF'],
       [34, 'TN0007310139', 'Conserver', 'Hannibal Lease',
        'Hannibal Lease', 'HANL'],
       [35, 'TN0003200755', 'Conserver', 'ICF',
        'Les Industries Chimiques du Fluor', 'ICF'],
       [36, 'TN0007510019', 'Acheter', 'Land Or', 'Land Or', 'LNDOR'],
       [37, 'TN0006440010', 'Conserver', 'MAGASIN GENERAL',
        'Magasin General', 'SMG'],
       [38, 'TN0007660012', 'Vendre', 'Maghreb Inter Publicite',
        'Maghreb Inter Publicite', 'MIP'],
       [39, 'TN0001000108', 'Conserver', 'MONOPRIX', 'MONOPRIX', 'MNP'],
       [40, 'TN0007620016', 'Consolider', 'Mpbs', 'Mpbs', 'MPBS'],
       [41, 'TN0007540016', 'Acheter', 'New Body Li', 'New Body Li',
        'NBL'],
       [42, 'TN0007700016', 'Conserver', 'OfficePlast', 'OfficePlast',
        'PLAST'],
       [43, 'TN0007530017', 'Acheter', 'One Tech Ho', 'One Tech Ho',
        'OTH'],
       [44, 'TN0002500650', 'Conserver', 'PLACEMENT DE TUNISIE',
        'Placements De Tunisie - Sicaf', 'PLTU'],
       [45, 'TN0005700018', 'Acheter', 'POULINA GROUP HLD',
        'Poulina Group Holding', 'POULA'],
       [46, 'TN0007610017', 'Acheter', 'Sah', 'Sah', 'SAH'],
       [47, 'TN0007730013', 'Conserver', 'Sanimed SA', 'Sanimed SA',
        'SMD'],
       [48, 'TN0007340011', 'Vendre', 'SERVICOM', 'Servicom', 'SERVI'],
       [49, 'TN0001100254', 'Acheter', 'SFBT',
        'Societe Frigorifique Et Brasserie', 'SFBT'],
       [50, 'TN0006590012', 'Conserver', 'SIAME',
        "Societe Industrielle D'Appareillage", 'SIAM'],
       [51, 'TN0004000055', 'Conserver', 'SIMPAR',
        'Ste Immobilere et de Participations', 'SIMP'],
       [52, 'TN0006670012', 'Allèger', 'SIPHAT',
        'Societe Des Industries Pharma', 'SIPHA'],
       [53, 'TN0007180011', 'Conserver', 'SITS',
        'Ste Immobiliere Tuniso Seoudienne', 'SITS'],
       [54, 'TN0006780019', 'Conserver', 'SOMOCER',
        'Societe Moderne De Ceramique', 'SOMOC'],
       [55, 'TN0007290018', 'Conserver', 'SOPAT',
        'Ste De Production Agricole Teboulba', 'SOPAT'],
       [56, 'TN0007600018', 'Conserver', 'Sotemail', 'Sotemail', 'SOTEM'],
       [57, 'TN0006530018', 'Vendre', 'SOTETEL',
        "Société Tunisienne d'Entreprises de Télécommunication", 'SOTE'],
       [58, 'TN0007630015', 'Acheter', 'Sotipapier', 'Sotipapier',
        'STPAP'],
       [59, 'TN0006660013', 'Acheter', 'SOTRAPIL',
        'Ste de Transport par Pipelines', 'STPIL'],
       [60, 'TN0006580013', 'Consolider', 'SOTUMAG',
        'Ste Tunisienne des Marches de Gros', 'MGR'],
       [61, 'TN0006560015', 'Acheter', 'SOTUVER',
        'Societe Tunisienne De Verreries', 'STVR'],
       [62, 'TN0001400704', 'Acheter', 'SPDIT-SICAF', 'SPDIT-SICAF',
        'SPDI'],
       [63, 'TN0006060016', 'Consolider', 'STAR', 'STAR', 'STAR'],
       [64, 'TN0002600955', 'Conserver', 'S.T.B',
        'Societe Tunisienne De Banque', 'STB'],
       [65, 'TN0005030010', 'Vendre', 'STIP',
        'Ste Tun Des Industries Pneumatiques', 'STIP'],
       [66, 'TN0007650013', 'Vendre', 'Tawasol Group Holding SA',
        'Tawasol Group Holding SA', 'TGH'],
       [67, 'TN0007440019', 'Consolider', 'TELNET', 'Telnet Holding',
        'TLNET'],
       [68, 'TN0007270010', 'Acheter', 'TPR',
        'Societe Tunisie Profiles Aluminium', 'TPR'],
       [69, 'TN0004100202', 'Acheter', 'TUN INVEST - SICAR',
        'TUN INVEST - SICAR', 'TINV'],
       [70, 'TN0007380017', 'Consolider', 'Tunis Re', 'Tunis Re', 'TRE'],
       [71, 'TN0001200401', 'Alléger', 'TUNIS AIR',
        "Societe Tunisienne De L'Air", 'TAIR'],
       [72, 'TN0002100907', 'Acheter', 'TUNISIE LEASING',
        'Tunisie Leasing', 'TLS'],
       [73, 'TN0007690019', 'Allèger',
        'Universal Auto Distributors Holding',
        'Universal Auto Distributors Holding SA', 'UADH'],
       [74, 'TN0002400505', 'Conserver', 'UBCI', 'UBCI', 'UBCI'],
       [75, 'TN0003900107', 'Consolider', 'UIB',
        'Union Internationale De Banques', 'UIB'],
       [76, 'TN0007720014', 'Acheter', 'Unimed', 'Unimed SA', 'UMED'],
       [77, 'TN0007200017', 'Conserver', 'EL WIFACK LEASING',
        'El Wifack Leasing', 'WIFAK']])
symbol=pd.DataFrame(arr.T,['Unnamed: 0', 'isin', 'recommendation', 'name', 'full_name', 'symbol']).T
# relative-import the *package* containing the templates

#template = pkg_resources.read_text(templates, 'temp_file')
# or for a file-like stream:
#template = pkg_resources.open_text(templates, 'temp_file')
#import get_data
#stream = pkg_resources.resource_stream(__name__,'data/symbol_recommendation.csv')
#symbol= pd.read_csv(stream)
#symbol=pd.read_csv('symbol_recommendation.csv')
#symbol=get_dataset()
from src import replace_x
def list_stocks():
    return symbol.filter(['isin','name','full_name','symbol'],axis=1)
class company:
    def __init__(self,stock):
        self.stock=stock
        self.mysymbol=symbol.filter(symbol.index[(symbol['symbol']==self.stock)],axis=0)['isin'].to_numpy()[0]
        link='https://www.afc.com.tn/entreprise?isin='+self.mysymbol+'#content'
        page = requests.get(link)
        self.soup = BeautifulSoup(page.content,"html.parser")
    def income_statement_indicators(self):
        ''' in this income_statement_indicators you can find the Return on equity ROE ratio,gearing ratio,EBIT and 
        EBITDA and others for the last 4 years  '''
        ratio_resultat=self.soup.find('div', attrs={'class':'mod_ind_res'}).find('table')
        output_rows2=[]
        for table_row in ratio_resultat.findAll('tr'):
            columns2 = table_row.findAll('td')
            output_row2 = []
            for column in columns2:
                output_row2.append(column.text)
            output_row2.extend([symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]])
            output_rows2.append(output_row2)
        df_ratio_resultat = pd.DataFrame(output_rows2,columns=['ratios','2019','2020','2021','2022','Stock'])[1:]
        df_ratio_resultat['2019']=pd.to_numeric(df_ratio_resultat['2019'],errors = 'coerce')
        df_ratio_resultat['2020']=pd.to_numeric(df_ratio_resultat['2020'],errors = 'coerce')
        df_ratio_resultat['2021']=pd.to_numeric(df_ratio_resultat['2021'],errors = 'coerce')
        df_ratio_resultat['2022']=pd.to_numeric(df_ratio_resultat['2022'],errors = 'coerce')
        df_ratio_resultat1=df_ratio_resultat.T
        df_ratio_resultat1.columns=df_ratio_resultat['ratios']
        df_ratio_resultat1=df_ratio_resultat1[1:-1]
        df_ratio_resultat1['Stock']=symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]
        return df_ratio_resultat1
    def balance_sheet_indicators(self):
        ratio_bilan=self.soup.find('div', attrs={'class':'mod_ind_bilan'}).find('table')
        output_rows1=[]
        for table_row in ratio_bilan.findAll('tr'):
            columns1 = table_row.findAll('td')
            output_row1 = []
            for column in columns1:
                output_row1.append(column.text)
            output_row1.extend([symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]])
            output_rows1.append(output_row1)
        df_ratio_bilan = pd.DataFrame(output_rows1)
        df_ratio_bilan=df_ratio_bilan[1:]
        df_ratio_bilan.columns=['ratios','2019','2020','2021','2022','Stock']
        df_ratio_bilan['2019']=df_ratio_bilan['2019'].str.replace(',','.')
        df_ratio_bilan['2019']=pd.to_numeric(df_ratio_bilan['2019'],errors = 'coerce')
        df_ratio_bilan['2020']=df_ratio_bilan['2020'].str.replace(',','.')
        df_ratio_bilan['2020']=pd.to_numeric(df_ratio_bilan['2020'],errors = 'coerce')
        df_ratio_bilan['2021']=df_ratio_bilan['2021'].str.replace(',','.')
        df_ratio_bilan['2021']=pd.to_numeric(df_ratio_bilan['2021'],errors = 'coerce')
        df_ratio_bilan['2022']=df_ratio_bilan['2022'].str.replace(',','.')
        df_ratio_bilan['2022']=pd.to_numeric(df_ratio_bilan['2022'],errors = 'coerce')
        df_ratio_bilan1=df_ratio_bilan.T
        df_ratio_bilan1.columns=df_ratio_bilan['ratios']
        df_ratio_bilan1=df_ratio_bilan1[1:-1]
        df_ratio_bilan1['Stock']=symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]
        return df_ratio_bilan1
        #Indicateurs boursiers
    def stock_market_indicators(self):
        ind_bourse=self.soup.find('div', attrs={'class':'mod_ind_bourse'}).find('table')
        output_rows = []
        for table_row in ind_bourse.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                output_row.append(column.text)
            output_row.extend([symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]])
            output_rows.append(output_row)
        df_ind_bourse = pd.DataFrame(output_rows)
        df_ind_bourse=df_ind_bourse[1:].drop(columns=1)
        df_ind_bourse.drop(df_ind_bourse.index[(df_ind_bourse[0]=='Secteur')],axis=0,inplace=True)
        df_ind_bourse.drop(df_ind_bourse.index[(df_ind_bourse[0]=='Marché')],axis=0,inplace=True)
        df_ind_bourse.columns=['ratios','2019','2020','2021','2022','Stock']
        df_ind_bourse['2019']=df_ind_bourse['2019'].apply(replace_x)
        df_ind_bourse['2019']=pd.to_numeric(df_ind_bourse['2019'],errors = 'coerce')
        df_ind_bourse['2020']=df_ind_bourse['2020'].apply(replace_x)
        df_ind_bourse['2020']=pd.to_numeric(df_ind_bourse['2020'],errors = 'coerce')
        df_ind_bourse['2021']=df_ind_bourse['2021'].apply(replace_x)
        df_ind_bourse['2021']=pd.to_numeric(df_ind_bourse['2021'],errors = 'coerce')
        df_ind_bourse['2022']=df_ind_bourse['2022'].apply(replace_x)
        df_ind_bourse['2022']=pd.to_numeric(df_ind_bourse['2022'],errors = 'coerce')
        df_ind_bourse1=df_ind_bourse.T
        df_ind_bourse1.columns=df_ind_bourse['ratios']
        df_ind_bourse1=df_ind_bourse1[1:-1]
        df_ind_bourse1['Stock']=symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]
        return df_ind_bourse1
    def shareholders(self):
        actionnaire=self.soup.find('div', attrs={'class':'mod_act_ent'}).find('table')
        output_rows = []
        for table_row in actionnaire.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                output_row.append(column.text)
            output_row.extend([symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]])
            output_rows.append(output_row)
        df_actionnaire = pd.DataFrame(output_rows)[1:]
        df_actionnaire.columns=['Actionnaire','Type','Pourcentage','Stock']
        return df_actionnaire
    def Dividende(self):
        ind_divend=self.soup.find('div', attrs={'class':'mod_div_ent'}).find('table')
        output_rows = []
        for table_row in ind_divend.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                output_row.append(column.text)
            output_row.extend([symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]])
            output_rows.append(output_row)
        Dividende = pd.DataFrame(output_rows[1:],columns=['Dividende par action','Actions concernées','Montant total','Exercice','Date de distribution','Stock'])
        Dividende['Actions concernées']=Dividende['Actions concernées'].str.replace(' ','')
        Dividende['Montant total']=Dividende['Montant total'].str.replace(' ','')
        Dividende['Montant total']=Dividende['Montant total'].str.replace('DT','')
        Dividende['Dividende par action']=Dividende['Dividende par action'].str.replace(' ','')
        Dividende['Dividende par action']=Dividende['Dividende par action'].str.replace('DT','')
        Dividende['Dividende par action']=pd.to_numeric(Dividende['Dividende par action'],errors = 'coerce')
        Dividende['Actions concernées']=pd.to_numeric(Dividende['Actions concernées'],errors = 'coerce')
        Dividende['Montant total']=pd.to_numeric(Dividende['Montant total'],errors = 'coerce')
        Dividende['Date']=pd.to_datetime(Dividende['Date de distribution'], format='%d/%m/%Y')
        return Dividende
class news:
    def company(stock):
        List=[]
        List_description=[]
        url=f'https://www.ilboursa.com/marches/news_valeur.aspx?p=1&s={stock}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content,"html.parser")
        num_page=soup.find('ul', attrs={'id':'pagin'}).find_all('li')[-1].text
        for j in range(1,int(num_page)):
            text_sentiment=soup.find('div', attrs={'class':'home_content mt15 lh25'}).find_all('a')
            for i in range(len(text_sentiment)):
                date=soup.find_all('span', attrs={'class':'sp1'})
                List.append({'News':text_sentiment[i].text,'Date':date[i].text,'Stock':stock,'link':f"https://www.ilboursa.com/marches/{text_sentiment[i]['href']}"})
        news_data=List
        for link in range(len(news_data)):
            page = requests.get(news_data[link]['link'])
            soup = BeautifulSoup(page.content,"html.parser")
            text_article=soup.find('div', attrs={'class':'inarticle txtbig'}).find_all('p')
            article=""
            for i in text_article:
                article+=i.text
            List_description.append({'Description':article})
        df_news=pd.DataFrame(news_data,columns=['News','Date','Stock','link'])
        df_desc=pd.DataFrame(List_description,columns=['Description'])
        return pd.concat([df_news,df_desc],axis=1)