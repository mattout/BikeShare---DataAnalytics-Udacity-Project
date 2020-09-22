import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city=''
    month=''
    day=''
    print()
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_selection=input('Please enter the name of city you want to explore:\n\nFor "Chicago" >> press "c"\nFor "New York City" >> press "n"\nFor "Washington" >> press "w"\n').lower()
            valid_cities={'c':'chicago','n':'new york city','w':'washington'}
            if city_selection in valid_cities:
                city=valid_cities[city_selection]
                break
            else:
                print('\nYou have entered a wrong selection. Please try again')
        except KeyboardInterrupt:
            break


    #print(city)

    while True:
        if city=='':
            break
        valid_times=["m","d","b","n"]
        try:
            time_selection=input('\nHow would you like to filter on {} ? Select one of the below choices:\n\nBy month >> press"m"\nBy day >> press "d"\nBy both month and day >> press "b"\nWith no Filter >> press "n"\n'.format(city.title())).lower()
            #valid_times=['m','d','b','n']
            if time_selection not in valid_times :
                print('\nYou have entered a wrong selection. Please try again')
            else:
                if time_selection=='m':
                    while True:
                        try:
                            month_selection=input('\nPlease Choose Month from the below:\n\nJanuary >> press "jan"\nFebruary >> press "feb"\nMarch >> press "mar"\nApril >> press "apr"\nMay >> press "may"\nJune >> press "jun"\n').lower()
                            valid_months={'jan':'january','feb':'february','mar':'march','apr':'april','may':'may','jun':'june'}
                            if month_selection in valid_months:
                                month=valid_months[month_selection]
                                day='all'
                                break
                            else:
                                print('\nYou have entered a wrong selection. Please try again')
                        except KeyboardInterrupt:
                            #print('\nYou chose to close. See you next time.. Bye')
                            break

                    break
                elif time_selection=='d':
                    while True:
                        try:
                            day_selection=input('\nPlease Choose day of the week from the below selection:\n\n(mon-tue-wed-thu-fri-sat-sun)\n').lower()
                            valid_days={'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday','sat':'Saturday'}
                            if day_selection in valid_days:
                                month='all'
                                day=valid_days[day_selection]
                                break
                            else:
                                print('\nYou have entered a wrong selection. Please try again')
                        except KeyboardInterrupt:
                            #print('You chose to close. See you next time.. Bye')
                            break
                    break
                elif time_selection=='b':
                    while True:
                        try:
                            month_selection=input('\nPlease Choose Month from the below:\n\nJanuary >> press "jan"\nFebruary >> press "feb"\nMarch >> press "mar"\nApril >> press "apr"\nMay >> press "may"\nJune >> press "jun"\n').lower()
                            valid_months={'jan':'january','feb':'february','mar':'march','apr':'april','may':'may','jun':'june'}
                            if month_selection in valid_months:
                                month=valid_months[month_selection]
                                #day='all'
                                break
                            else:
                                print('\nYou have entered a wrong selection. Please try again')
                        except KeyboardInterrupt:
                            #print('\nYou chose to close. See you next time.. Bye')
                            break

                    while True:
                        if month=='':
                            break
                        try:
                            day_selection=input('\nPlease Choose day of the week from the below selection:\n\n(mon-tue-wed-thu-fri-sat-sun)\n').lower()
                            valid_days={'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday','sat':'Saturday'}
                            if day_selection in valid_days:
                                #month='all'
                                day=valid_days[day_selection]
                                break
                            else:
                                print('\nYou have entered a wrong selection. Please try again')
                        except KeyboardInterrupt:
                            #print('You chose to close. See you next time.. Bye')
                            break
                    break
                else:
                    month='all'
                    day='all'
                    break

        except KeyboardInterrupt:
            #print('\nYou chose to close. See you next time.. Bye')
            break

    #print(city,month,day)

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    df['combination']='From '+df['Start Station']+' To '+df['End Station']



    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_common_month_string=months[most_common_month -1]
    print("Most Common month is {}\n".format(most_common_month_string))

    # TO DO: display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print("Most Common day of week is {}\n".format(most_common_day))


    # TO DO: display the most common start hour
    most_common_hour=df['hour'].mode()[0]
    print("Most Common Start Hour is {}\n\n".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


############    Cut part to be put here ###########
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print("Most Common Start Station is {}\n\n".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print("Most Common End Station is {}\n\n".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip

    most_common_combination=df['combination'].mode()[0]
    print("Most Common combination of start station and end station is {}\n\n".format(most_common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=int(df['Trip Duration'].sum())
    #print(total_travel_time)
    #print(type(total_travel_time))
    #ttt=str(datetime.timedelta(seconds=total_travel_time))
    #ttt_list=ttt.split(":")

    print("Total travel time is {} minutes and {} seconds\n".format(total_travel_time//60,total_travel_time%60))



    # TO DO: display mean travel time
    mean_travel_time=int(df['Trip Duration'].mean())
    #mtt=str(datetime.timedelta(seconds=mean_travel_time))
    #mtt_list=mtt.split(":")

    print("Mean travel time is {} minutes and {} seconds\n".format(mean_travel_time//60,mean_travel_time%60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types=df["User Type"].value_counts()
    print('Counts of user types as below:\n{}\n'.format(counts_user_types))

    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print("No Gender classification in this city")
    else:
        counts_gender=df["Gender"].value_counts()
        print('Counts of genders as below:\n{}\n'.format(counts_gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print("No Birth Year classification in this city")
    else:
        print('Earliest Birth Year is {}'.format(int(df['Birth Year'].min())))
        print('Most Recent Birth Year is {}'.format(int(df['Birth Year'].max())))
        print('Most Common Birth Year is {}'.format(int(df['Birth Year'].mode()[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:

        city, month, day = get_filters()
        if city=='' or month=='' or day=='':

            print('\nYou chose to close. See you next time.. Bye')
            break
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        row_num=0
        print_5= input('\nWould you like to see first 5 inputs from the data? (yes/no)')
        if print_5 == 'yes':
            print(df.head())

            next_row=5
            while True:
                print_5_again= input('\n\nWould you like to see next 5 inputs? (yes/no)')
                if print_5_again == 'yes':
                    print(df.iloc[next_row:next_row+5,:])
                    next_row=next_row+5
                else:
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thanks for using Bikeshare.. Hope you enjoyed')
            break


if __name__ == "__main__":
	main()
