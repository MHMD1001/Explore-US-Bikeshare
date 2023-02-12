import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Note : Please make sure not typing a space before or after any required input')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['Chicago', 'New York City', 'Washington']
    city = input('\nChoose a city from the following \n(Chicago, New York City, Washington)        : ').title()
    while city not in cities :
        city = input('Kindly Choose one of the given cities : ').title()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['All', 'January', 'Febrauary', 'March', 'April', 'May', 'June']
    month = input('\nEnter a month from january to june : ').title()
    while month not in months:
        month = input('Enter a month from january to june : ').title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['All', 'Saturday', 'Sunday', 'Monday', 'Tuseday', 'Wednesday', 'Thrusday', 'Friday'] 
    day = input('\nEnter a day (Saturday, Sunday...etc) : ').title()
    while day not in days:
        day = input('Enter day correctly (Saturday, Sunday...etc) : ').title()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # convert the Start Time column to datetime
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']== day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_comonth = df['month'].mode()[0]
    print('Most Common Month Is :\n',most_comonth)

    # TO DO: display the most common day of week
    most_comday = df['day_of_week'].mode()[0]
    print('Most Common Day Is :\n',most_comday)

    # TO DO: display the most common start hour
    most_csth = df['Start Time'].dt.hour.mode()[0]
    print('Most Common Start Hour Is :\n',most_csth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_comSS = df['Start Station'].mode()[0]
    print ('Most Common Start Station Is :\n',most_comSS)

    # TO DO: display most commonly used end station
    most_comES = df['End Station'].mode()[0]
    print ('Most Common End Station Is :\n',most_comES)

    # TO DO: display most frequent combination of start station and end station trip
    most_fqcomb = 'Start Station : ' + df['Start Station'] + '  ,  ' + 'End Station : ' + df['End Station']
    print('Most Frequent Combination Of Start Station And End Station Trip :\n',most_fqcomb.mode()[0])
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    t_tr = df['Trip Duration'].sum()
    print('Total Travel Time : ',format(t_tr/60,'.2f'),'minutes = ',format(t_tr/3600,'.2f'),'hours')


    # TO DO: display mean travel time
    Avg_time = df['Trip Duration'].mean()
    print('Average Trip Time : ',format(Avg_time,'.2f'),' seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User Types :\n',user_type)

    # TO DO: Display counts of gender
    if 'Gender' not in df.columns.tolist() :
        counts_gender = 'No Data Avilable'
    else:
        counts_gender = df['Gender'].value_counts()
    
    print('Users Gender Counts :\n',counts_gender)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns.tolist():
        print('No Data Available')
    else:
        print('Users Earliest Year Of Birth : ',df['Birth Year'].min())
        print('Users Most Recent Year Of Birth : ',df['Birth Year'].max())
        print('Users Most Common Year Of Birth : ',df['Birth Year'].mode()[0])
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        i =0
        #while True:
        sample = input('do you want to display a sample of data : ').lower()
        if sample ==  'yes':
            print(df.head())
            while True:
                i = i +5
                sample = input('do you want to display a more of data : ').lower()
                if sample == 'yes':
                    print(df[i:i+5])
                else :
                    break
            
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
