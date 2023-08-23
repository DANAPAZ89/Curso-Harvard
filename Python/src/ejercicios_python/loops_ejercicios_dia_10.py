# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# 2. Iterate 10 to 0 using for loop, do the same using while loop.
# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######

# 4. Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

# 5. Print the following pattern:
"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# 7. Use for loop to iterate from 0 to 100 and print only even numbers
# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
# 9. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# 10. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# 11. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# 12. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# 13. Go to the data folder and use the countries_data.py file.
"""
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world
"""

# 1.
print("\nEJERCICIO 1\n")
for i in range(11):
    print(i)

x = 0
while x < 11:
    print(x)
    x = x + 1
# 2.
print("\nEJERCICIO 2\n")
for number in range(10,-1,-1):
    print(number)
x = 10
while x > -1:
    print(x)
    x = x-1

# 3.
print("\nEJERCICIO 3\n")
hashtag = "#"
x = 0
while x < 8:
    print(hashtag)
    hashtag = hashtag + "#"
    x = x + 1

# 4. 
print("\nEJERCICIO 4\n")
hashtag = "#"
x = 0
for i in range(7):
    while x < 7:
        hashtag = hashtag + " #"
        x = x + 1
    print(hashtag)

# 5.
print("\nEJERCICIO 5\n")
x = 0
while x < 11:
    print(f"{x} x {x} = {x * x}")
    x = x + 1

# 6.
print("\nEJERCICIO 6\n")
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for languaje in lst:
    print(languaje)

# 7.
print("\nEJERCICIO 7 \n")
for i in range(101):
    if (i % 2) == 0:
        print(i)

# 8.
print("\nEJERCICIO 8 \n")
for i in range(101):
    if (i % 2) != 0:
        print(i)

# 9.
print("\nEJERCICIO 9 \n")
suma = 0
for i in range(101):
    suma = suma + i
print(f"The sum of all numbers is {suma}")

#10.
print("\nEJERCICIO 10\n")
pares = 0
impares = 0
for i in range(101):
    if i % 2 == 0:
        pares += i
    else:
        impares += i
print(f"The sum of even numbers is {pares}")
print(f"The sum of odd numbers is {impares}")
    
# 11.
print("\nEJERCICIO 11\n")
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

for i in countries:
    if "land" in i:
        print(i)

# 12.
print("\nEJERCICIO 12\n")
fruits = ['banana', 'orange', 'mango', 'lemon']
range = len(fruits)-1
for i in fruits:
    fruit = range - fruits.index(i)
    print(f"{fruits[fruit]}")

# 13.
print("\nEJERCICIO 13\n")
import countries_data
print(type(countries_data))