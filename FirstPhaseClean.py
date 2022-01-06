# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd

df = pd.read_csv('/Users/maryamtanveer/Desktop/This Is It.csv')

#print(df.columns)

#This function turns the forward coded Likert Scale parts of the survey into numerical values; This is called for the Ongoing Consent and Communicative Sexuality
def ForwardCoded(number):
    for index in range(0, len(df.index)):
        x = df.iat[index, number]
        if "strongly agree" == str(x).lower():
            df.loc[index, number] = '7'
        if "agree" == str(x).lower():
            df.loc[index, number] = '6'
        if "somewhat agree" == str(x).lower():
            df.loc[index, number] = '5'
        if "neither agree nor disagree" == str(x).lower():
            df.loc[index, number] = '4'
        if "neither agree or disagree" == str(x).lower():
            df.loc[index, number] = '4'
        if "somewhat disagree" == str(x).lower():
            df.loc[index, number] = '3'
        if "disagree" == str(x).lower():
            df.loc[index, number] = '2'
        if "strongly disagree" == str(x).lower():
            df.loc[index, number] = '1'
#This function turns the reverse coded Likert Scale parts of the survey into numerical values; This is called for Subtle Coercion
def ReverseCoded(number):
    for index in range(0, len(df.index)):
        x = df.iat[index, number]
        if "strongly agree" == str(x).lower():
            df.loc[index, number] = '1'
        if "agree" == str(x).lower():
            df.loc[index, number] = '2'
        if "somewhat agree" == str(x).lower():
            df.loc[index, number] = '3'
        if "neither agree or disagree" == str(x).lower():
            df.loc[index, number] = '4'
        if "neither agree nor disagree" == str(x).lower():
            df.loc[index, number] = '4'
        if "somewhat disagree" == str(x).lower():
            df.loc[index, number] = '5'
        if "disagree" == str(x).lower():
            df.loc[index, number] = '6'
        if "strongly disagree" == str(x).lower():
            df.loc[index, number] = '7'
            
#This function nulls the rest of the answers within subscale if they select Prefer not to answer for any questions within the subscale
def my_function(index, number):
    # ongoing consent
    if 18 <= number <= 23:
        for column in range(18, 24):
            df.loc[index, column] = "NA"
        #print("ongoing consent")
    # subtle coercion
    if 24 <= number <= 29:
        for column in range(24, 30):
            df.loc[index, column] = "NA"
        #print("subtle coercion")
    # communicative sexuality
    if 30 <= number <= 37:
        for column in range(30, 38):
            df.loc[index, column] = "NA"
        #print("communicative sexuality")

#semester
#Converts semesters into numerical scores
for index in range(0, len(df.index)):

    y = df.columns.get_loc("2")
    x = df.iat[index, y]

    if "Fall 2016" == str(x):
        df.loc[index, y] = 1
    if "Spring 2017" == str(x):
        df.loc[index, y] = 2
    if "Fall 2017" == str(x):
        df.loc[index, y] = 3
    if "Spring 2018" == str(x):
        df.loc[index, y] = 4
    if "Fall 2018" == str(x):
        df.loc[index, y] = 5
    if "Spring 2019" == str(x):
        df.loc[index, y] = 6
    if "Fall 2019" == str(x):
        df.loc[index, y] = 7
    if "Spring 2020" == str(x):
        df.loc[index, y] = 8
    if "Fall 2020" == str(x):
        df.loc[index, y] = 9
    if "Spring 2021" == str(x):
        df.loc[index, y] = 10
    if "Other" == str(x):
        df.loc[index, y] = 11
    if "Prefer not to answer" == str(x):
        df.loc[index, y] = 11
    df.loc[0, df.columns.get_loc('2')] = 'Semester'
#transfer status
for index in range(0, len(df.index)):
    y = df.columns.get_loc("23")
    x = df.iat[index, y]
    if "Yes" == str(x):
        df.loc[index, y] = 1
    if "No" == str(x):
        df.loc[index, y] = 0
    if "Prefer not to answer" == str(x):
        df.loc[index, y] = 'NA'
    df.loc[0, df.columns.get_loc('23')] = 'Transfer Status'
#spring scholar
#Converts spring scholar status into numerical scores
for index in range(0, len(df.index)):
    y = df.columns.get_loc("24")
    x = df.iat[index, y]
    if "Yes" == str(x):
        df.loc[index, y] = 1
    if "No" == str(x):
        df.loc[index, y] = 0
    if "Prefer not to answer" == str(x):
        df.loc[index, y] = 'NA'
    df.loc[0, df.columns.get_loc('24')] = 'Spring Scholar Status'
#race
#Converts race into numerical scores
for index in range(0, len(df.index)):
    y = df.columns.get_loc("25")
    x = df.iat[index, y]
    if "White" == str(x):
        df.loc[index, y] = 1
    elif "Black or African American" == str(x):
        df.loc[index, y] = 2
    elif "Asian" == str(x):
        df.loc[index, y] = 3
    elif "Latinx or Hispanic" == str(x):
        df.loc[index, y] = 4
    elif "Native Hawaiian or other Pacific Islander" == str(x):
        df.loc[index, y] = 5
    elif "American Indian or Alaska Native" == str(x):
        df.loc[index, y] = 6
    elif "Prefer Not to Answer" == str(x):
        df.loc[index, y] = 7
    elif "Prefer to Self-Describe" == str(x):
        df.loc[index, y] = 7
    else:
        df.loc[index, y] = 8
    df.loc[0, df.columns.get_loc('25')] = 'Race'
#gender
#Converts gender into numerical scores
for index in range(0, len(df.index)):
    y = df.columns.get_loc("27")
    x = df.iat[index, y]
    if "Woman" == str(x):
        df.loc[index, y] = 1
    elif "Man " == str(x):
        df.loc[index, y] = 2
    elif "Trans" == str(x):
        df.loc[index, y] = 3
    elif "Nonbinary	" == str(x):
        df.loc[index, y] = 3
    elif "Prefer Not to Answer" == str(x):
        df.loc[index, y] = 4
    elif "Prefer to Self-Describe" == str(x):
        df.loc[index, y] = 4
    df.loc[0, df.columns.get_loc('27')] = 'Gender'
#sexuality
#Converts sexuality into numerical scores
for index in range(0, len(df.index)):
    y = df.columns.get_loc("29")
    x = df.iat[index, y]
    if "Straight (Heterosexual) " == str(x):
        df.loc[index, y] = 1
    elif "Bisexual " == str(x):
        df.loc[index, y] = 2
    elif "Lesbian " == str(x) or "Pansexual " == str(x) or "Gay " == str(x) or "Queer " == str(x) \
            or "Asexual " == str(x) or "Questioning or unsure " == str(x)\
            or "Same-gender loving " == str(x):
        df.loc[index, y] = 3
    elif "Prefer Not to Answer" == str(x):
        df.loc[index, y] = 4
    elif "Prefer to Self-Describe" == str(x):
        df.loc[index, y] = 4
    df.loc[0, df.columns.get_loc('29')] = 'Sexuality'
#age
#Converts age into numerical scores
for index in range(1, len(df.index)):
    y = df.columns.get_loc("31")
    x = df.iat[index, y]
    df.loc[index, y] = x
    df.loc[0, df.columns.get_loc('31')] = 'Age'
    if "prefer not to answer" == str(x).lower():
        df.loc[index, y] = 17
#relationship
#Converts relationship into numerical scores
for index in range(0, len(df.index)):
    y = df.columns.get_loc("32")
    x = df.iat[index, y]
    if "Single" == str(x):
        df.loc[index, y] = 1
    elif "Steady, monogamous, committed relationship" == str(x):
        df.loc[index, y] = 2
    elif "Open relationship" == str(x):
        df.loc[index, y] = 3
    elif "Casually dating/hooking up" == str(x):
        df.loc[index, y] = 4
    elif "Prefer Not to Answer" == str(x):
        df.loc[index, y] = 5
    elif "Prefer to Self-Describe" == str(x):
        df.loc[index, y] = 5
    df.loc[0, df.columns.get_loc('32')] = 'Relationship Status'
#religion
#Converts religion into numerical scores
for index in range(0, len(df.index)):
    y = df.columns.get_loc("34")
    x = df.iat[index, y]
    if "Protestant" == str(x):
        df.loc[index, y] = 1
    if "Roman Catholic" == str(x):
        df.loc[index, y] = 1
    if "Mormon" == str(x):
        df.loc[index, y] = 1
    if "Eastern or Greek Orthodox" == str(x):
        df.loc[index, y] = 1
    if "Jewish" == str(x):
        df.loc[index, y] = 2
    if "Muslim" == str(x) or "Buddhist" == str(x) or "Hindu" == str(x):
        df.loc[index, y] = 3
    if ("Atheist" == str(x)) or ("Agnostic" == str(x)) or ("Nothing in particular" == str(x)) or (
            "Something else" == str(x)):
        df.loc[index, y] = 4
    if ("Prefer to Self-Describe" == str(x)) or ("Prefer Not to Answer" == str(x)):
        df.loc[index, y] = 5
    df.loc[0, df.columns.get_loc('34')] = 'Religious Affiliation'
#council
for index in range(0, len(df.index)):
    y = df.columns.get_loc("37")
    x = df.iat[index, y]
    if "Panhellenic Council (Panhel)" == str(x):
        df.loc[index, y] = 1
    if "National Pan-Hellenic Council (NPHC)" == str(x):
        df.loc[index, y] = 1
    if "Interfraternity Council (IFC)" == str(x):
        df.loc[index, y] = 2
    if "Multicultural Greek Council (MGC)" == str(x):
        df.loc[index, y] = 3
    df.loc[0, df.columns.get_loc('37')] = 'Council'
#region
#Converts region into numerical scores
for index in range(1, len(df.index)):
    x = df.iat[index, df.columns.get_loc('38')]
    answer = str(x)
    # Northeast - 1
    # Midwest - 2
    # South - 3
    # West - 4
    # Other - 5

    if answer in ["Connecticut", "Maine", "Massachusetts", "New Hampshire", "Rhode Island", "Vermont", "New Jersey",
                  "New York", "Pennsylvania"]:
        df.loc[index, df.columns.get_loc('38')] = 1
    elif answer in ["Indiana", "Illinois", "Michigan", "Ohio", "Wisconsin", "Iowa", "Nebraska", "Kansas",
                    "North Dakota", "Minnesota", "South Dakota", "Missouri"]:
        df.loc[index, df.columns.get_loc('38')] = 2
    elif answer in ["Delaware", "District of Columbia", "Florida", "Georgia", "Maryland", "North Carolina",
                    "South Carolina", "Virginia", "West Virginia", "Alabama", "Kentucky", "Mississippi", "Tennessee",
                    "Arkansas", "Louisiana", "Oklahoma", "Texas"]:
        df.loc[index, df.columns.get_loc('38')] = 3
    elif answer in ["Arizona", "Colorado", "Idaho", "New Mexico", "Montana", "Utah", "Nevada", "Wyoming", "Alaska",
                    "California", "Hawaii", "Oregon", "Washington"]:
        df.loc[index, df.columns.get_loc('38')] = 4
    else:
        df.loc[index, df.columns.get_loc('38')] = 5

    df.loc[0, df.columns.get_loc('38')] = 'Region Score'
#tulane activities
#Converts activities into numerical scores within new columns
for index in range(1, len(df.index)):
    x = df.iat[index, df.columns.get_loc('4')]
    if "SAPHE Workshops (Consent Conversation, Sexual Violence 101, etc.)" in str(x):
        df.loc[index, 'SAPHE Workshops'] = '1'
    else:
        df.loc[index, 'SAPHE Workshops'] = '0'
    if "Pre-orientation or Orientation event(s) or program(s) focused on sex, sexuality, and/or sexual violence (Summer reading project e.g. Beartown, online modules, discussions with Wave Leaders during orientation, The Hook Up, etc.)" in str(
            x):
        df.loc[index, 'Preorientation'] = '1'
    else:
        df.loc[index, 'Preorientation'] = '0'
    if "One Wave Workshop" in str(x):
        df.loc[index, 'One Wave Workshop'] = '1'
    else:
        df.loc[index, 'One Wave Workshop'] = '0'
    if "SAPHE's Healthy Relationships Week (Includes social media posts by SAPHE during this week)" in str(x):
        df.loc[index, 'HRW'] = '1'
    else:
        df.loc[index, 'HRW'] = '0'
    if "Sex Week (Includes social media posts during this week)" in str(x):
        df.loc[index, 'Sex Week'] = '1'
    else:
        df.loc[index, 'Sex Week'] = '0'
    if "My Sister's Keeper" in str(x):
        df.loc[index, 'My Sister\'s Keeper'] = '1'
    else:
        df.loc[index, 'My Sister\'s Keeper'] = '0'
    if "Tulane-affiliated organization’s social media posts or content regarding sex, sexuality, or sexual violence (Instagram posts/stories, Tweets, etc.)" in str(
            x):
        df.loc[index, 'Tulane Social Media'] = '1'
    else:
        df.loc[index, 'Tulane Social Media'] = '0'
    if "Sexual Assault Awareness Month" in str(x):
        df.loc[index, 'SAAM'] = '1'
    else:
        df.loc[index, 'SAAM'] = '0'
    if "Other" in str(x):
        df.loc[index, 'Tulane Other'] = '1'
    else:
        df.loc[index, 'Tulane Other'] = '0'
    if "Prefer not to answer" in str(x):
        df.loc[index, 'Tulane Prefer not to answer'] = '1'
    else:
        df.loc[index, 'Tulane Prefer not to answer'] = '0'
#tulane helpfulness
#Converts helpfulness into numerical scores
for index in range(1, len(df.index)):
    # Tulane Helpfulness
    y = df.columns.get_loc('13_1')
    x = df.iat[index, y]
    if "Helpful" == str(x):
        df.loc[index, y] = '5'
    if "Somewhat helpful" == str(x):
        df.loc[index, y] = '4'
    if "Neither Helpful or Unhelpful" == str(x):
        df.loc[index, y] = '3'
    if "Somewhat unhelpful" == str(x):
        df.loc[index, y] = '2'
    if "Not at all helpful" == str(x):
        df.loc[index, y] = '1'
    if "Prefer not to answer" == str(x):
        df.loc[index, y] = '0'
    df.loc[0, y] = 'Tulane Helpfulness'
#non tulane activities
#Converts activities into numerical scores within new columns
for index in range(1, len(df.index)):
    x = df.iat[index, df.columns.get_loc('14')]
    if "Sexual health education (includes discussions surrounding sex and sexuality, consent, sexual violence, sexually transmitted diseases, puberty, etc.)" in str(
            x):
        df.loc[index, 'Sexual Health Education'] = '1'
    else:
        df.loc[index, 'Sexual Health Education'] = '0'
    if "Non-Tulane-affiliated organization’s social media posts or content regarding sex, sexuality, or sexual violence (Instagram posts/stories, Tweets, etc.)" in str(
            x):
        df.loc[index, 'Non-Tulane Social Media'] = '1'
    else:
        df.loc[index, 'Non-Tulane Social Media'] = '0'
    if "Discussions with peers about sex, sexuality, and/or sexual violence" in str(x):
        df.loc[index, 'Discussions with Peers'] = '1'
    else:
        df.loc[index, 'Discussions with Peers'] = '0'
    if "Discussions with family members about sex, sexuality, and/or sexual violence" in str(x):
        df.loc[index, 'Discussions with Family'] = '1'
    else:
        df.loc[index, 'Discussions with Family'] = '0'
    if "Television/Movies/Music about sex, sexuality, and/or sexual violence" in str(x):
        df.loc[index, 'Media'] = '1'
    else:
        df.loc[index, 'Media'] = '0'
    if "Other" in str(x):
        df.loc[index, 'Other'] = '1'
    else:
        df.loc[index, 'Other'] = '0'
    if "Prefer not to answer" in str(x):
        df.loc[index, 'Non-Tulane Prefer not to answer'] = '1'
    else:
        df.loc[index, 'Non-Tulane Prefer not to answer'] = '0'
#non tulane helpfulness
#Converts helpfulness into numerical scores
for index in range(2, len(df.index)):
    # Non-Tulane Helpfulness
    y = df.columns.get_loc('19_1')
    x = df.iat[index, y]

    if "Helpful" == str(x):
        df.loc[index, y] = '5'
    if "Somewhat Helpful" == str(x):
        df.loc[index, y] = '4'
    if "Neither Helpful or Unhelpful" == str(x):
        df.loc[index, y] = '3'
    if "Somewhat unhelpful" == str(x):
        df.loc[index, y] = '2'
    if "Not at all helpful" == str(x):
        df.loc[index, y] = '1'
    if "Prefer not to answer" == str(x):
        df.loc[index, y] = '0'
    df.loc[0, y] = 'Non-Tulane Helpfulness'

# Q49_1

#print('This is the FIRST column number: ' + str(df.columns.get_loc('20_1')))
#print('This is the LAST column number: ' + str(df.columns.get_loc('22_8')))
#consent scale
#Creates new columns with labels
for number in range(18, 38):
    if "18" in str(number):
        df.loc[0, number] = 'Ongoing Consent - 1'
        ForwardCoded(number)
    if "19" in str(number):
        df.loc[0, number] = 'Ongoing Consent - 2'
        ForwardCoded(number)
    if "20" in str(number):
        df.loc[0, number] = 'Ongoing Consent - 3'
        ForwardCoded(number)
    if "21" in str(number):
        df.loc[0, number] = 'Ongoing Consent - 4'
        ForwardCoded(number)
    if "22" in str(number):
        df.loc[0, number] = 'Ongoing Consent - 5'
        ForwardCoded(number)
    if "23" in str(number):
        df.loc[0, number] = 'Ongoing Consent - 6'
        ForwardCoded(number)
        # ongoing consent is 18 through 23
    if "24" in str(number):
        df.loc[0, number] = 'Subtle Coercion - 1'
        ReverseCoded(number)
    if "25" in str(number):
        df.loc[0, number] = 'Subtle Coercion - 2'
        ReverseCoded(number)
    if "26" in str(number):
        df.loc[0, number] = 'Subtle Coercion - 3'
        ReverseCoded(number)
    if "27" in str(number):
        df.loc[0, number] = 'Subtle Coercion - 4'
        ReverseCoded(number)
    if "28" in str(number):
        df.loc[0, number] = 'Subtle Coercion - 5'
        ReverseCoded(number)
    if "29" in str(number):
        df.loc[0, number] = 'Subtle Coercion - 6'
        ReverseCoded(number)
        # subtle coercion is 24 through 29 -- this will be reverse coded
    if "30" in str(number):
        df.loc[0, number] = 'Communicative sexuality - 1'
        ForwardCoded(number)
    if "31" in str(number):
        df.loc[0, number] = 'Communicative sexuality - 2'
        ForwardCoded(number)
    if "32" in str(number):
        df.loc[0, number] = 'Communicative sexuality - 3'
        ForwardCoded(number)
    if "33" in str(number):
        df.loc[0, number] = 'Communicative sexuality - 4'
        ForwardCoded(number)
    if "34" in str(number):
        df.loc[0, number] = 'Communicative sexuality - 5'
        ForwardCoded(number)
    if "35" in str(number):
        df.loc[0, number] = 'Communicative sexuality - 6'
        ForwardCoded(number)
    if "36" in str(number):
        df.loc[0, number] = 'Communicative sexuality - 7'
        ForwardCoded(number)
    if "37" in str(number):
        df.loc[0, number] = 'Communicative sexuality - 8'
        ForwardCoded(number)
        # communicative sexuality is 30 though 37
#consent scale NULLer
#Calls the function that nulls the subscales
for number in range(18, 38):
    for index in range(0, len(df.index)):
        x = df.iat[index, number]
        if "Prefer not to answer" == str(x):
            my_function(index, number)
            #print(number)

# print(df)

# df.to_csv(r'/Users/maryamtanveer/Desktop/Clean Data.csv')


# df = pd.read_csv(r'/Users/maryamtanveer/Desktop/Second Cut.csv')
# print("hello")
# print(df.index)

# df.drop(df.columns[[0, 62]], axis=1, inplace=True)

#print(df.columns)

df.to_csv(r'/Users/maryamtanveer/Desktop/Final Cut.csv')

df.columns = ['DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','DELETE ME','DELETE ME','DELETE ME','DELETE ME',
              'DELETE ME','Progress','Semester','Transfer_Status','Spring_Scholar_Status',
              'Race','Gender','Sexuality','Age','Relationship_Status','Religious_Affiliation',
              'Council','Region_Score','SAPHE_Workshops','Preorientation','One_Wave_Workshop',
              'HRW','Sex_Week','My_Sisters_Keeper','Tulane_Social_Media','SAAM','Tulane_Other',
              'Tulane_Prefer_Not_to_Answer','Tulane_Helpfulness','Sexual_Health_Education',
              'Non_Tulane_Social_Media','Discussions_with_Peers','Discussions_with_Family','Media',
              'Other','Non_Tulane_Prefer_not_to_answer','Non_Tulane_Helpfulness','Ongoing_Consent_1',
              'Ongoing_Consent_2','Ongoing_Consent_3','Ongoing_Consent_4','Ongoing_Consent_5',
              'Ongoing_Consent_6','Subtle_Coercion_1','Subtle_Coercion_2','Subtle_Coercion_3',
              'Subtle_Coercion_4','Subtle_Coercion_5','Subtle_Coercion_6','Communicative_Sexuality_1',
              'Communicative_Sexuality_2','Communicative_Sexuality_3','Communicative_Sexuality_4',
              'Communicative_Sexuality_5','Communicative_Sexuality_6','Communicative_Sexuality_7',
              'Communicative_Sexuality_8']
df.head()

df.to_csv('/Users/maryamtanveer/Desktop/Final Cut.csv')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
