# Full list of countries you are considering for travel
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# Initialize an empty list for rankings
travel_rankings = []

# Use enumerate to label each destination
for index, value in enumerate(countries, start=1):
    temp_string = "Destination " +  str(index) + ": " + countries[index-1]
    travel_rankings.append(temp_string)

# Testing
print("Travel destination rankings:", travel_rankings)