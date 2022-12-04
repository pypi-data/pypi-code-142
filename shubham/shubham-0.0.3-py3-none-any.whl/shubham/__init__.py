

def knowme():
    print('''Hi, I'm Shubham Mohanty
A passionate student, learner, science enthusiast from India.
    A school student interested in programming, robotics, arduino, computers, gamedev and rc building.
''')
   
def currency():
    while True:
        currencyList = {'andorra': 'EUR', 'united arab emirates': 'AED', 'afghanistan': 'AFN', 'antigua and barbuda': 'XCD', 'anguilla': 'XCD', 'albania': 'ALL', 'armenia': 'AMD', 'angola': 'AOA', 'antarctica': '', 'argentina': 'ARS', 'american samoa': 'USD', 'austria': 'EUR', 'australia': 'AUD', 'aruba': 'AWG', 'åland': 'EUR', 'azerbaijan': 'AZN', 'bosnia and herzegovina': 'BAM', 'barbados': 'BBD', 'bangladesh': 'BDT', 'belgium': 'EUR', 'burkina faso': 'XOF', 'bulgaria': 'BGN', 'bahrain': 'BHD', 'burundi': 'BIF', 'benin': 'XOF', 'saint barthélemy': 'EUR', 'bermuda': 'BMD', 'brunei': 'BND', 'bolivia': 'BOB', 'bonaire': 'USD', 'brazil': 'BRL', 'bahamas': 'BSD', 'bhutan': 'BTN', 'bouvet island': 'NOK', 'botswana': 'BWP', 'belarus': 'BYR', 'belize': 'BZD', 'canada': 'CAD', 'cocos [keeling] islands': 'AUD', 'democratic republic of the congo': 'CDF', 'central african republic': 'XAF', 'republic of the congo': 'XAF', 'switzerland': 'CHF', 'ivory coast': 'XOF', 'cook islands': 'NZD', 'chile': 'CLP', 'cameroon': 'XAF', 'china': 'CNY', 'colombia': 'COP', 'costa rica': 'CRC', 'cuba': 'CUP', 'cape verde': 'CVE', 'curacao': 'ANG', 'christmas island': 'AUD', 'cyprus': 'EUR', 'czechia': 'CZK', 'germany': 'EUR', 'djibouti': 'DJF', 'denmark': 'DKK', 'dominica': 'XCD', 'dominican republic': 'DOP', 'algeria': 'DZD', 'ecuador': 'USD', 'estonia': 'EUR', 'egypt': 'EGP', 'western sahara': 'MAD', 'eritrea': 'ERN', 'spain': 'EUR', 'ethiopia': 'ETB', 'finland': 'EUR', 'fiji': 'FJD', 'falkland islands': 'FKP', 'micronesia': 'USD', 'faroe islands': 'DKK', 'france': 'EUR', 'gabon': 'XAF', 'united kingdom': 'GBP', 'grenada': 'XCD', 'georgia': 'GEL', 'french guiana': 'EUR', 'guernsey': 'GBP', 'ghana': 'GHS', 'gibraltar': 'GIP', 'greenland': 'DKK', 'gambia': 'GMD', 'guinea': 'GNF', 'guadeloupe': 'EUR', 'equatorial guinea': 'XAF', 'greece': 'EUR', 'south georgia and the south sandwich islands': 'GBP', 'guatemala': 'GTQ', 'guam': 'USD', 'guinea-bissau': 'XOF', 'guyana': 'GYD', 'hong kong': 'HKD', 'heard island and mcdonald islands': 'AUD', 'honduras': 'HNL', 'croatia': 'HRK', 'haiti': 'HTG', 'hungary': 'HUF', 'indonesia': 'IDR', 'ireland': 'EUR', 'israel': 'ILS', 'isle of man': 'GBP', 'india': 'INR', 'british indian ocean territory': 'USD', 'iraq': 'IQD', 'iran': 'IRR', 'iceland': 'ISK', 'italy': 'EUR', 'jersey': 'GBP', 'jamaica': 'JMD', 'jordan': 'JOD', 'japan': 'JPY', 'kenya': 'KES', 'kyrgyzstan': 'KGS', 'cambodia': 'KHR', 'kiribati': 'AUD', 'comoros': 'KMF', 'saint kitts and nevis': 'XCD', 'north korea': 'KPW', 'south korea': 'KRW', 'kuwait': 'KWD', 'cayman islands': 'KYD', 'kazakhstan': 'KZT', 'laos': 'LAK', 'lebanon': 'LBP', 'saint lucia': 'XCD', 'liechtenstein': 'CHF', 'sri lanka': 'LKR', 'liberia': 'LRD', 'lesotho': 'LSL', 'lithuania': 'EUR', 'luxembourg': 'EUR', 'latvia': 'EUR', 'libya': 'LYD', 'morocco': 'MAD', 'monaco': 'EUR', 'moldova': 'MDL', 'montenegro': 'EUR', 'saint martin': 'EUR', 'madagascar': 'MGA', 'marshall islands': 'USD', 'macedonia': 'MKD', 'mali': 'XOF', 'myanmar [burma]': 'MMK', 'mongolia': 'MNT', 'macao': 'MOP', 'northern mariana islands': 'USD', 'martinique': 'EUR', 'mauritania': 'MRO', 'montserrat': 'XCD', 'malta': 'EUR', 'mauritius': 'MUR', 'maldives': 'MVR', 'malawi': 'MWK', 'mexico': 'MXN', 'malaysia': 'MYR', 'mozambique': 'MZN', 'namibia': 'NAD', 'new caledonia': 'XPF', 'niger': 'XOF', 'norfolk island': 'AUD', 'nigeria': 'NGN', 'nicaragua': 'NIO', 'netherlands': 'EUR', 'norway': 'NOK', 'nepal': 'NPR', 'nauru': 'AUD', 'niue': 'NZD', 'new zealand': 'NZD', 'oman': 'OMR', 'panama': 'PAB', 'peru': 'PEN', 'french polynesia': 'XPF', 'papua new guinea': 'PGK', 'philippines': 'PHP', 'pakistan': 'PKR', 'poland': 'PLN', 'saint pierre and miquelon': 'EUR', 'pitcairn islands': 'NZD', 'puerto rico': 'USD', 'palestine': 'ILS', 'portugal': 'EUR', 'palau': 'USD', 'paraguay': 'PYG', 'qatar': 'QAR', 'réunion': 'EUR', 'romania': 'RON', 'serbia': 'RSD', 'russia': 'RUB', 'rwanda': 'RWF', 'saudi arabia': 'SAR', 'solomon islands': 'SBD', 'seychelles': 'SCR', 'sudan': 'SDG', 'sweden': 'SEK', 'singapore': 'SGD', 'saint helena': 'SHP', 'slovenia': 'EUR', 'svalbard and jan mayen': 'NOK', 'slovakia': 'EUR', 'sierra leone': 'SLL', 'san marino': 'EUR', 'senegal': 'XOF', 'somalia': 'SOS', 'suriname': 'SRD', 'south sudan': 'SSP', 'são tomé and príncipe': 'STD', 'el salvador': 'USD', 'sint maarten': 'ANG', 'syria': 'SYP', 'swaziland': 'SZL', 'turks and caicos islands': 'USD', 'chad': 'XAF', 'french southern territories': 'EUR', 'togo': 'XOF', 'thailand': 'THB', 'tajikistan': 'TJS', 'tokelau': 'NZD', 'east timor': 'USD', 'turkmenistan': 'TMT', 'tunisia': 'TND', 'tonga': 'TOP', 'turkey': 'TRY', 'trinidad and tobago': 'TTD', 'tuvalu': 'AUD', 'taiwan': 'TWD', 'tanzania': 'TZS', 'ukraine': 'UAH', 'uganda': 'UGX', 'u.s. minor outlying islands': 'USD', 'united states': 'USD', 'uruguay': 'UYU', 'uzbekistan': 'UZS', 'vatican city': 'EUR', 'saint vincent and the grenadines': 'XCD', 'venezuela': 'VEF', 'british virgin islands': 'USD', 'u.s. virgin islands': 'USD', 'vietnam': 'VND', 'vanuatu': 'VUV', 'wallis and futuna': 'XPF', 'samoa': 'WST', 'kosovo': 'EUR', 'yemen': 'YER', 'mayotte': 'EUR', 'south africa': 'ZAR', 'zambia': 'ZMW', 'zimbabwe': 'ZWL'}

        choice = int(input('''
        1)CONVERT CURRENCY
        2)CONVERT COUNTRY NAME TO CURRENCY CODE
        
        Enter the corresponding menu item no.: '''))
        
        if choice ==1:
            url = "https://api.exchangerate.host/latest" 
            cfrom = input("Enter currency code in uppercase|| FROM: ")
            cto = input("Enter currency code in uppercase|| TO: ")
            afrom = int(input("Enter amount to be converted: "))
            
            import requests
            try:
                out = requests.get(url, params = {"base": cfrom})
                out = out.json()
                total = afrom*(out["rates"][cto])
                total = "%.2f" % total
                print(afrom, cfrom, '------>', total,cto)
            except:
                print("There is some error")    

        elif choice ==2:
            try:
                countryName = input("Enter the country name(lowercase): ")
                correspondingCurrency = currencyList[countryName]
                print("The currency code for ",countryName, " is:", correspondingCurrency)
            except:
                print("Country not found in the database")
        else:
            print("Enter correct value")    
        print(" ")
        curstay = input("Enter q or Q to exit and any other key to run this function again: ")
        if curstay == ('q' or 'Q'):
            break
        


