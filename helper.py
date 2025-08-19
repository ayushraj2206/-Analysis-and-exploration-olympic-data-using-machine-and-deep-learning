import numpy as np

def fetch_medal_tally(df, Year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if Year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if Year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if Year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(Year)]
    if Year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == Year) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')
    x['total'] = x['total'].astype('int')

    return x

def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team','NOC','Year','City','Sport','Event','Medal'])
    medal_tally = medal_tally.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold', ascending=False).reset_index()

    medal_tally['total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    medal_tally['Gold'] = medal_tally['Gold'].astype('int')
    medal_tally['Silver'] = medal_tally['Silver'].astype('int')
    medal_tally['Bronze'] = medal_tally['Bronze'].astype('int')
    medal_tally['total'] = medal_tally['total'].astype('int')


    return medal_tally

def country_year_list(df):
    Years = df['Year'].unique().tolist()
    Years.sort()
    Years.insert(0, "Overall")

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, "Overall")

    return Years, country

def data_over_time(df,col):
    nations_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('Year')
    nations_over_time.rename(columns = {'count':col},inplace=True)
    return nations_over_time