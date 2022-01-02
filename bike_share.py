import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply
        no month filter
        (str) day - name of the day of week to filter by, or "all" to
        apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city.
    while True:
        try:
            city = input("""What city would you like to learn about? \
                        Choose between 'chicago', 'new york city' or \
                        'washington'. """).lower()
            if city == 'chicago':
                print('Great, you chose to learn about Chicago!')
                break
            elif city == 'new york city':
                print('Great, you chose to learn about New York City!')
                break
            elif city == 'washington':
                print('Great, you chose to learn about Washington!')
                break
            else:
                print('Please insert the desired city name!')
                continue
        except:
            print('Oops, something went wrong!')

    # Get user input for month.
    while True:
        try:
            month = input("""What month are you interested in?
                        Choose between 'all', 'january', 'february', 'march', \
                        'april', 'may' or 'june'. """).lower()
            if month == 'all':
                print('Alright, let\'s see the data for all months!')
                break
            if month == 'january':
                print('Alright, January it is!')
                break
            elif month == 'february':
                print('Alright, February it is!')
                break
            elif month == 'march':
                print('Alright, March it is!')
                break
            elif month == 'april':
                print('Alright, April it is!')
                break
            elif month == 'may':
                print('Alright, May it is!')
                break
            elif month == 'june':
                print('Alright, June it is!')
                break
            else:
                print('Please type the desired month name in lowercase!')
                continue
        except:
            print('Oops, something went wrong!')

    # Get user input for day of week.
    while True:
        try:
            day = input("""What day of the week do you want to look at? \
                        Choose between 'all', 'monday', 'tuesday', \
                        'wednesday', 'thursday', 'friday', 'saturday' or \
                        'sunday'. """).lower()
            if day == 'all':
                print('Let\'s have a look at all days of the week!')
                break
            if day == 'monday':
                print('Let\'s have a look at Monday!')
                break
            elif day == 'tuesday':
                print('Let\'s have a look at Tuesday!')
                break
            elif day == 'wednesday':
                print('Let\'s have a look at Wednesday!')
                break
            elif day == 'thursday':
                print('Let\'s have a look at Thursday!')
                break
            elif day == 'friday':
                print('Let\'s have a look at Friday!')
                break
            elif day == 'saturday':
                print('Let\'s have a look at Saturday!')
                break
            elif day == 'sunday':
                print('Let\'s have a look at Sunday!')
                break
            else:
                print('Please type the desired day name in lowercase!')
                continue
        except:
            print('Oops, something went wrong!')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day
    if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply
        no month filter
        (str) day - name of the day of week to filter by, or "all" to
        apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month
        and day
    """

    df = pd.DataFrame([city, month, day])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # Display the most common month.
    popular_month = df['month'].mode()[0]
    print('Most frequent month: ', popular_month)

    # Display the most common day of week.
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most frequent day: ', popular_day_of_week)

    # Display the most common start hour.
    popular_hour = df['hour'].mode()[0]
    print('Most frequent start hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station.
    popular_start = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', popular_start)

    # Display most commonly used end station.
    popular_end = df['End Station'].mode()[0]
    print('Most commonly used end station: ', popular_end)

    # Display most frequent combination of start station and end station trip.
    start_end = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent combination of Start Station and End Station: ',
            start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time.
    total_duration = df['Trip Duration'].sum()
    print('Total travel time: ', total_duration)

    # Display mean travel time.
    mean_duration = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types.
    user_types = df['User Type'].value_counts()
    print('Different user types: ', user_types)

    # Display counts of gender.
    if "Gender" in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('Count by gender: ', gender_counts)
    else:
        print('Gender count not available.')

    # Display earliest, most recent, and most common year of birth.
    if "Birth Year" in df.columns:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('Earliest year of birth: ', earliest_birth)
        print('Most recent year of birth: ', recent_birth)
        print('Most common year of birth: ', common_birth)
    else:
        print('Birth-year data not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def head_display(df):
    """This function displays raw data."""

    first = 0
    last = 5

    while True:
        answer = input("""'\nWould you like to see the raw data? Enter yes \
        or no.\n'""")
        # Check if response is yes, print the raw data and increment count by 5.
        if answer.lower() == 'yes':
            print(df.iloc[first:last])
            first += 5
            last += 5
            continue
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        head_display(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
