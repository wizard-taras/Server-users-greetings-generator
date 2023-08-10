'''
Program file: server_users_greetings_generator.py

Purpose:
    To create a function used to greet users when they log in to the server.
Depending on the representative role of the user (admin, simple user, service engineer etc.)
greetings will be constructed differently.

Record of revisions:
      Date        Programmer      Description of change(-s)
      ----        ----------      -------------------------
    09/08/23    Koziupa Taras           Original code
    10/08/23    Koziupa Taras     Added: reports generation feature, the 'input_data'
                                    dictionary containing all the necessary information for
                                    greetings generation, current users list extraction from .csv file (local)

Define variables:
    input_data -- A dictionary containing usernames and reports data for the admin and serviceman
    users -- A list of all the users on the server
    admin_reports -- A list with necessary information for the admin report generation
    serviceman_reports -- A list with necessary information for the serviceman report generation
    user -- Temporary variable that stores username; used in if conditionals
    output -- A string composed of username and reports. Initiated only for specific
users (admin, serviceman, support engineer)
'''

import pandas as pnds
'''FUNCTIONS'''


def greetings(input_data):
    new_users, admin_reports, serviceman_reports = [input_data['new_users'], input_data['admin_reports'],
                                                input_data['serviceman_reports']]

    df = pnds.read_csv('users_csv.csv')
    current_users = df['users'].values.tolist()

    if current_users:
        for user in current_users:
            if user.lower() or user.upper() or user.title() not in new_users:
                if user not in ('admin', 'serviceman', 'support_eng'):
                    print(f"Hello, {user.title()}. Welcome to the server.")

                elif user == 'admin':
                    output = f'\nHello, {user.title()}. Welcome to the server. \nThe reports for you are:' \
                            f'\nNumber of active users by now: {admin_reports[0]}' \
                            f'\nTotal traffic consumed by the users previuos day, MB: {admin_reports[1]}'
                    print(output)

                elif user == 'serviceman':
                    output = f'\nHello, {user.title()}. Welcome to the server. \nThe reports for you are:' \
                            f'\nAvailable free space on the server SSD disks, GiB: {serviceman_reports[0]}' \
                            f'\nTotal SSD read/write fails: {serviceman_reports[1]}'
                    print(output)
            else: print(f"Sorry, {user.title()}, user with the provided name already exists. Try to pick another username.")
    else: print("No users in the server's database")


'''INPUT DATA'''
input_data = {'new_users': ['taras', 'steven', 'phoebe', 'admin', 'serviceman', 'support_eng'],
              'admin_reports': [1225, 5578801], 'serviceman_reports': [557, 17]}

greetings(input_data)