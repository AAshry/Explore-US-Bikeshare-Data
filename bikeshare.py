#!/usr/bin/env python

import time
import pandas as pd
import numpy as np
import sys




CITY_DATA = { 'chicago':'chicago.csv',
              'new york city':'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    while True:
        print("Please enter which city data you want to see [C]hicago, [NY]city"
              "[W]ashington 'or' [E]xit : ")
        city= input()
        if city=='c'or city=='C':
            city='chicago'
            print('Okay you will see the data of Chicago city')
        elif city=='ny' or city=='NY':
            city='new york city'
            print('Okay you will see the data of NY city')
        elif city=='w'or city=='W':
            city='washington'
            print('Okay you will see the data of Washington city')
        elif city=='e' or city=='E':
            print('okay see you soon')
            sys.exit()
        else:
            print('You choose wrong city')
            continue
        break
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July']

    while True:
        print('Please enter which month data you want to see or type all to see all data :')
        month=input()
        if month.title() in months:
            month=month.title()
            print('Okay we will display the data from {}'.format(month))
        elif month.lower()=='all':
            print('Great! you will see all the data ')
        else:
            print('Sorry Invalid inpute')
            continue
        break
    week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday",
                          "Saturday","Sunday")


    while True:
        print('Which day of the week you want to display its data or type all to see all the week data:')
        day=input()
        if day.title() in week_days:
            print('Okay you will see the data of {}'.format(day))
        elif day.lower()=='all':
            print('Cool! you will see the data from entire week')
        else:
            print('Sorry Invalid inpute')
            continue
        break

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_popular_month=df['month'].mode()[0]
    print('The most common month is: {}'.format(most_popular_month))


    # display the most common day of week
    most_popular_day=df['day_of_week'].mode()[0]

    print('The most common day of week: {}'.format(most_popular_day))

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_popular_hour=df['hour'].mode()[0]
    print('The most common hour is: {}'.format(most_popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station=df['Start Station'].value_counts().idxmax()
    print('The most popular start station is: {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station=df['End Station'].value_counts().idxmax()
    print('The most popular end station is: {}'.format(popular_end_station))


    # display most frequent combination of start station and end station trip

    df['combination']=df['Start Station']+df['End Station']
    popular_trip=df['combination'].mode()[0]
    print('The Combination of start and end stations is: {} '.format(popular_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total time traveld is: {}'.format(total_travel_time))

    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean of traveled time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type=df['User Type'].value_counts()
    print('the count of user type is : {}'.format(count_user_type))

    # Display counts of gender
    try:
        count_gender_type=df['Gender'].value_counts()
        print('The count of gender type is: {}'.format(count_gender_type))

    except KeyError:
        print('Sorry gender data is not available ')

    # Display earliest, most recent, and most common year of birth
    try:
        Earliest_year_of_birth=df['Birth Year'].max()
        print('The Oldest people birth year is: {}'.format(Earliest_year_of_birth))

    except KeyError:
        print('Sorry Birth Year Data is not avaliable for this month')

    try:
        Most_recent_year_of_birth=df['Birth Year'].min()

        print('The youngest people birth year is: {}'.format(Most_recent_year_of_birth))
    except KeyError :
        print('Sorry Birth Year Data is not avaliable for this month')

    try:
        Common_year_of_birth=df['Birth Year'].value_counts().idxmax()
        print('The Most common birth year is: {}'.format(Common_year_of_birth))

    except:
        print('Sorry Birth Year Data is not avaliable for this month')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_data(df):
    start_data=0
    raw_data=''

    while True:
        print ('You want display first 5 five trips? Yes or No ')
        raw_data=input()
        if raw_data.lower()=='yes':
            print(df.head(5))
            break
        elif raw_data.lower()=='no':
            break
        else:
            print('Invalid answer please answer with Yes or No')
            continue

            
    while raw_data.lower()=='yes':
        print('Would you like to display more 5 trips ?')
        start_data+=5
        raw_data=input()        
        if raw_data.lower()=='yes' :
            print(df[start_data:start_data+5])
            
                 
                           
        elif raw_data.lower()=='no':
                 break
        else:
                 print('Invalid answer please answer with Yes or No')
                 continue
                   


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()