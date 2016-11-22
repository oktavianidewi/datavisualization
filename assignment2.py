import pandas as pd
import numpy

data = pd.read_csv('dataset/ool_pds.csv', low_memory = False)

question_ids = ['W1_M1', 'W1_M1_OTHER_TEXT', 'W1_M1A', 'W1_M2', 'W1_M3', 'W1_M4', 'W1_M5', 'W1_M6', 'W1_M7', 'W1_M8', 'W1_M9', 'W1_M10', 'W1_M11', 'W1_M12']
# question_ids = ['W1_M1', 'W1_M2', 'W1_M3', 'W1_M4', 'W1_M5', 'W1_M6', 'W1_M7', 'W1_M8', 'W1_M9', 'W1_M10', 'W1_M11', 'W1_M12']
question_names = ['What is your religion?', '[Other] What is your religion?', 'Would you describe yourself as a born-again or evangelical Christian?', 'What was the racial makeup of your place of worship?', 'Churches or places of worship should be involved in political matters', ' Churches or places of worship should allow more women to become members of the clergy', 'How often do you attend religious services?', 'Aside from attending regular services, in the past 12 months have you been an active member of your church or place of worship?', 'In the last year, have you heard any discussions of politics at your church or place of worship?', 'Have you talked to people about political matters at your church or place of worship?', 'Has a member of the clergy or someone in an official position at your church or place of worship talked about the need for people to become more involved in politics?', 'Has any local or national political leader spoken at a regular religious service at your church or place of worship?', ' Has a member of the clergy, or someone in an official position at your church or place of worship, ever suggested that you vote for or against certain candidates in an election?', 'What about suggesting that you take action on a political issue such as sign a petition or write a letter?']
# question_names = ['What is your religion?', 'What was the racial makeup of your place of worship?', 'Churches or places of worship should be involved in political matters', ' Churches or places of worship should allow more women to become members of the clergy', 'How often do you attend religious services?', 'Aside from attending regular services, in the past 12 months have you been an active member of your church or place of worship?', 'In the last year, have you heard any discussions of politics at your church or place of worship?', 'Have you talked to people about political matters at your church or place of worship?', 'Has a member of the clergy or someone in an official position at your church or place of worship talked about the need for people to become more involved in politics?', 'Has any local or national political leader spoken at a regular religious service at your church or place of worship?', ' Has a member of the clergy, or someone in an official position at your church or place of worship, ever suggested that you vote for or against certain candidates in an election?', 'What about suggesting that you take action on a political issue such as sign a petition or write a letter?']
questions = zip(question_ids, question_names)

for q_id, q_name in questions:
    # data[q_id] = pd.to_numeric(data[q_id])
    """
    data[q_id] = data[q_id].convert_objects(convert_numeric=True)
    print 'Counts for ', q_id, ' with question: ', q_name
    raw = data[q_id].value_counts(sort=False, dropna=False)
    print 'Percentages for ', q_id, ' with question: ', q_name
    percent = data[q_id].value_counts(sort=False, dropna=False, normalize = True)
    print raw
    print percent
    """
    rawt = data.groupby(q_id).size()
    percentaget = data.groupby(q_id).size() * 100 / len(data)
    print 'Counts for ', q_id, ' with question: ', q_name
    print rawt
    print 'Percentages for ', q_id, ' with question: ', q_name
    print percentaget