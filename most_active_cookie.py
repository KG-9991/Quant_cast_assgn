import argparse

#Func to fetch cookies info as per date
def fetchCookiesAsPerDate(file_content):
    #Initialized a nest dict with key as dates and values as dict of cookie and freq count
    cookies_as_per_dates = {}                

    for line in file_content:

        #Removes any unwanted ""
        filtered_line = line.strip('""')  

        #Splits the string into cookie and timestamp      
        cookie, timestamp = filtered_line.strip().split(',')           
        extracted_date = timestamp.split('T')[0]              #Fetches date

        #Checks if the date and cookie already exists in the dict
        if (extracted_date in cookies_as_per_dates.keys()) and (cookie in cookies_as_per_dates[extracted_date].keys()):   
            cookies_as_per_dates[extracted_date][cookie] += 1
        #Checks if the date exists in dict but not the cookie
        elif extracted_date in cookies_as_per_dates.keys():
            cookies_as_per_dates[extracted_date][cookie] = 1
        #If both and date and cookie are new
        else:
            cookies_as_per_dates[extracted_date] = {}
            cookies_as_per_dates[extracted_date][cookie] = 1
    return cookies_as_per_dates

#Func to fetch most active cookies as per the cookie info and date
def getMostActiveCookies(fetched_cookies, date):

    #Checks if the date exists in the log
    if date not in fetched_cookies.keys():
        return []
    cookies_per_date = fetched_cookies[date]

    #Sorting the dict as per the freq count in desc order
    sorted_cookies = sorted(cookies_per_date.items(), key=lambda x: x[1], reverse=True)
    max_frequency = sorted_cookies[0][1]

    #Fetching all cookies who have max_freq
    max_freq_cookies = [cookie_data[0] for cookie_data in sorted_cookies if cookie_data[1] == max_frequency]
    return max_freq_cookies

def main():
    parser = argparse.ArgumentParser(description='Get the most active cookie for a specified day.')
    parser.add_argument('filename',help='Path to the cookie log file')
    parser.add_argument('-d', '--date', type=str, help='Date in the format YYYY-MM-DD', required=True)
    args = parser.parse_args()

    with open(args.filename, 'r') as file:
        file_content = file.readlines()

    #Retrives cookies data as per date in a nested dict
    cookies_data = fetchCookiesAsPerDate(file_content)

    #Retrieves a list of most active cookies
    most_active_cookies = getMostActiveCookies(cookies_data,args.date)

    #Returns incorrect date mssg if the date doesn't exists in the log
    if len(most_active_cookies)==0:
        print("No such date exists in the log")
        return
    
    for cookie in most_active_cookies:
        print(cookie)
    return

if __name__ == "__main__":
    main()