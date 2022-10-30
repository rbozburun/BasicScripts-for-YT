import subprocess

# Run the "netsh wlan show profiles" command to get all saved wifi profiles.
get_profiles = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], stdout=subprocess.PIPE)
raw_profiles = get_profiles.stdout.decode('utf-8')
#print(get_profiles.stdout.decode('utf-8'))

profiles =[]
# Get the profile names and store them into profiles list.
for line in raw_profiles.split('\n'):
    if 'User Profile' in line:
        profile_prefix_space = line.split(':')[1]
        profile = profile_prefix_space[1:]
        #print(profile)
        profiles.append(profile)


#Run the "netsh wlan show profile name='ProfileName' key=clear" command to get cleartext password
for profile in profiles:
    profile_details = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile[:-1], 'key=clear'], stdout=subprocess.PIPE)
    details = profile_details.stdout.decode('utf-8')
    for line in details.split('\n'):
        if 'Key Content' in line:
            pwd_with_space = line.split(':')[1]
            pwd = pwd_with_space[1:]
            print(profile)
            print_line = "    |================> " + pwd
            print(print_line)
            print()
            


    

