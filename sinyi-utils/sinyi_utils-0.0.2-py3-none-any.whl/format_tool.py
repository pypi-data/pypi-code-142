def roc_era_to_ad(roc_era):
    roc_era = roc_era.replace('-',"").replace(" ","").replace('_',"")
    if roc_era: 
        if len(roc_era) == 7 :
            year = roc_era[:-4]
            year = str(int(year)+1911)
            return year+roc_era[-4:]
        else:
            return None