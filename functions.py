# Function to clean the columns names

def clean_columns(df): 
    cols = []

    for a in range(len(df.columns)):
        cols.append(df.columns[a].lower().replace(' ', '_'))
    df.columns = cols
    return df

# Function to plot the evolution of the migrants over the years

def plot_nationalites(df):
    countries = ['spain', 'france', 'italy', 'moldova',
       'united_kingdom', 'romania', 'ukraine', 'total_africa', 'angola',
       'cape_verde', 'guine-bissau', 'mozambique', 's._tomé_and_prince',
       'total_america', 'brazil', 'total_asia', 'china', 'india', 'nepal']

    for country in countries:
        plt.figure(figsize=(10, 6))
        plt.plot(df['year'], df[country], marker='o', linestyle='-', label=country)

        plt.xlabel('Year')
        plt.ylabel('Residents')
        plt.title('Evolution by year')
        plt.legend()

        plt.grid(True)
        plt.show()

# Function to extract the info on the countries and also create a xlsx file with the dfs

def countries_dataframes(df, country_list):
    country_dataframes = {}

    for country in country_list:
        df_name = country + '_df'
        country_df = df[['year', country]]
        country_df.columns = ['year', 'total_residents']
        country_df['country'] = 'country'
        country_dataframes[df_name] = country_df

        # 
        excel_file_path = f'project_files/{df_name}.xlsx'
        country_df.to_excel(excel_file_path, index=False)
        print(f'DataFrame for {country} salved in {excel_file_path}')

    return country_dataframes

# A function to plot the population balance 

def plot_balance(df):
    df['year'] = pd.to_numeric(df['year'])

    plt.figure(figsize=(10, 6))
    plt.plot(df['year'], df['total_balance'], label='Total Balance', marker='o')
    plt.plot(df['year'], df['natural_balance'], label='Natural Balance', marker='o')
    plt.plot(df['year'], df['migratory_balance'], label='Migratory Balance', marker='o')

    plt.xlabel('Year')
    plt.ylabel('Balance')
    plt.title('Balance Over Years')

    plt.legend()


    plt.show()

