import argparse
import pandas as pd

def read_csv(csv_path):
    """Takes a csv path, and returns a Pandas DataFrame

    TO DO
    -----
    Build in validation of file format, column types, etc.

    Parameters
    ----------
    csv_path : str
        The file location of the CSV

    Returns
    -------
    df : DataFrame
        A Pandas DataFrame that can be processed further
    """
    
    df = pd.read_csv(csv_path)

    return df

def event_summary(df, out_csv = None):
    """Takes an input DataFrame of specimen occurrences and then calculates
    various summary stats for each species. It then combines the stats into a
    DataFrame, and optionally outputs this in CSV format.

    TO DO
    -----
    Everything

    Parameters
    ----------
    df : DataFrame
        The processed and validated occurrence DataFrame from read_csv()
    out_csv: str
        Output path for summary CSV file

    Returns
    -------
    event_df : DataFrame
        A Pandas DataFrame with all of the event summary stats
    """
    
    print('Event summary: ' + out_csv)

    return event_df

def month_summary(phenology_df, out_csv=None):
    """Takes an input DataFrame of specimen occurrences and then counts breaks
    down counts by month. It then combines the counts into a DataFrame, and 
    optionally outputs this in CSV format.

    TO DO
    -----
    Everything

    Parameters
    ----------
    df : DataFrame
        The processed and validated occurrence DataFrame from read_csv()
    out_csv: str
        Output path for summary CSV file

    Returns
    -------
    month_df : DataFrame
        A Pandas DataFrame with all of the month summary stats
    """
    month_list = ['Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr',
                 'May','Jun']
    species_list = phenology_df['species'].unique().tolist()

    count_list = []
    for species in species_list:
        count_dict = {'species':species}
        for month in month_list:
            month_check = phenology_df['monthStart'] == month
            species_check = phenology_df['species'] == species
            occurrence_count = phenology_df[month_check & species_check]['numSpecimen'].sum()
            count_dict[month] = occurrence_count
        count_list.append(count_dict)

    month_df = pd.DataFrame(count_list)
    month_df = month_df.set_index('species')
    month_df = month_df[month_list]

    return month_df


if __name__ == '__main__':
    ap = argparse.ArgumentParser()

    ap.add_argument('-c', "--csv", required=True,
                    help="file path of input csv")
    ap.add_argument("-e", "--event_summary",
                    help="file path of ouput event summary")
    ap.add_argument("-m", "--month_summary",
                    help="file path for ouput month summary")
    args = ap.parse_args()

    df = read_csv(args.csv)

    if args.event_summary is not None:
        event_summary(df, args.event_summary)

    if args.month_summary is not None:
        month_summary(df, args.month_summary)

