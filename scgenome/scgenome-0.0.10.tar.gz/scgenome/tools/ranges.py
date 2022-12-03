



def dataframe_to_pyranges(data):
    data = pr.PyRanges(data.reset_index().rename(columns={
        'chr': 'Chromosome',
        'start': 'Start',
        'end': 'End',
    })[['Chromosome', 'Start', 'End', 'bin']])

    return data

def pyranges_to_dataframe(data):
    data = data.as_df().rename(columns={
        'Chromosome': 'chr',
        'Start': 'start',
        'End': 'end',
    })

    return data
