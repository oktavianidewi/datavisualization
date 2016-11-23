import pandas as pd
import numpy as np

data = pd.read_csv('dataset/ool_pds.csv', low_memory = False)

question_ids = ['W1_M1', 'W1_M2', 'W1_M3', 'W1_M4', 'W1_M5', 'W1_M6', 'W1_M7', 'W1_M8', 'W1_M9', 'W1_M10', 'W1_M11', 'W1_M12']
question_names = ['What is your religion?', 'What was the racial makeup of your place of worship?', 'Churches or places of worship should be involved in political matters', ' Churches or places of worship should allow more women to become members of the clergy', 'How often do you attend religious services?', 'Aside from attending regular services, in the past 12 months have you been an active member of your church or place of worship?', 'In the last year, have you heard any discussions of politics at your church or place of worship?', 'Have you talked to people about political matters at your church or place of worship?', 'Has a member of the clergy or someone in an official position at your church or place of worship talked about the need for people to become more involved in politics?', 'Has any local or national political leader spoken at a regular religious service at your church or place of worship?', ' Has a member of the clergy, or someone in an official position at your church or place of worship, ever suggested that you vote for or against certain candidates in an election?', 'What about suggesting that you take action on a political issue such as sign a petition or write a letter?']
questions = zip(question_ids, question_names)
answer_name = [
    {1:'Baptist any denomination', 2:'Protestant (e.g., Methodist, Lutheran, Presbyterian, Episcopal)',3:'Catholic',4:'Mormon',5:'Jewish',6:'Muslim',7:'Hindu',8:'Buddhist',9:'Pentecostal',10:'Eastern Orthodox',11:'Other Christian',12:'Other non-Christian, please specify',13:'None',14:'Refused',-1:'Refused'},
    {'1':'Mostly Black','2':'Mostly White','3':'Mostly Latino','4':'Mostly Asian','5':'Something else','6':'Don\'t Know','-1':'Refused'},
    {'1':'Strongly agree','2':'Somewhat agree','3':'Somewhat disagree','4':'Strongly disagree','-1':'Refused'},
    {'1':'Strongly agree','2':'Somewhat agree','3':'Somewhat disagree','4':'Strongly disagree','-1':'Refused'},
    {'1':'More than once a week', '2':'Once a week', '3':'Once or twice a month', '4':'A few times a year', '5':'Once a year or less', '6':'Never', '7':'Not asked', '8':'Missing/Refused', '-1':'Refused'},
    {'1':'Yes','2':'No','-1':'Refused'},
    {'1':'Yes','2':'No','-1':'Refused'},
    {'1':'Yes','2':'No','-1':'Refused'},
    {'1':'Yes','2':'No','-1':'Refused'},
    {'1':'Yes','2':'No','-1':'Refused'},
    {'1':'Yes','2':'No','-1':'Refused'},
    {'1':'Yes','2':'No','-1':'Refused'}]

answers = {}
for id, question_id in enumerate(question_ids):
    answers[question_id] = answer_name[id]

for q_id, q_name in questions:
    data[q_id] = data[q_id].map(answers[q_id])
    print '[ Question ID : ',q_id,'] ', q_name
    """
    data[q_id] = data[q_id].convert_objects(convert_numeric=True).dropna().astype(int)
    raw = data[q_id].value_counts(sort=True, dropna=True)
    percent = data[q_id].value_counts(sort=False, dropna=True, normalize = True)
    all = pd.DataFrame({'raw':raw, 'percentage':percent})
    """

    rawt = data.groupby(q_id).size()
    percentaget = data.groupby(q_id).size() * 100 / len(data)
    all = pd.DataFrame({'Count':rawt, 'Percentage':percentaget})
    print 'Count and Percentage Value'
    print all
    print ''
    print 'Count and percentage value greater than its mean value'
    print all.loc[all['Count'] > rawt.mean() ]
    print ''
