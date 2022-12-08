import pandas as pd

catddog_df = pd.DataFrame({
    'Species':['Cat','Cat','Cat','Cat','Cat','Dog', 'Cat','Cat','Cat','Cat','Cat','Cat','Dog', 'Cat'],
    'Colour':['Red','Green','Red','Green','Red','Green', 'Red','Red','Green','Red','Green','Red','Green', 'Red'],
    'NumLegs':[4,3,4,3,4,3,4,4,3,4,3,4,4,4],
    'ColourFather': ['Red','Red','Red','Red','Red','Red', 'Red','Red','Red','Red','Red','Red','Red', 'Red'],
    'ColourMother': ['Red','Green','Red','Green','Red','Green', 'Red','Red','Green','Red','Green','Red','Green', 'Red']
})