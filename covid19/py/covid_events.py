
from datetime import datetime
import pandas as pd

date_code = '%B %d, %Y'
rows_list = []

row_dict = {}
row_dict['event_date'] = datetime.strptime('January 7, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Ohio claims to have the first COVID-19 patient'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('January 20, 2020', date_code)
row_dict['state_name'] = 'Washington'
row_dict['event_description'] = 'The first recorded U.S. case of the new virus was reported in an American citizen traveling from Wuhan, China, to his home in Washington state.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('January 21, 2020', date_code)
row_dict['state_name'] = 'Washington'
row_dict['event_description'] = 'A man who had returned from Wuhan was hospitalized for the virus in Washington state. He was released after two weeks of treatment.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('January 31, 2020', date_code)
row_dict['state_name'] = 'California'
row_dict['event_description'] = 'Another case of a person who returned from Wuhan was confirmed, which marked the seventh known case in the U.S.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('February 5, 2020', date_code)
row_dict['state_name'] = 'Wisconsin'
row_dict['event_description'] = 'The twelfth case is discovered: another college student from Wisconsin.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('February 6, 2020', date_code)
row_dict['state_name'] = 'California'
row_dict['event_description'] = '57-year-old Patricia Dowd of San Jose, California became the first Covid-19 death in the United States discovered by April 2020. She died at home without any known recent foreign travel, after being unusually sick from flu in late January, then recovering, working from home, and suddenly dying on February 6. A February 7 autopsy was completed in April (after virus tests on tissue samples) and attributed the death to Transmural Myocardial Ischemia (Infarction) with a Minor Component of Myocarditis due to COVID-19 Infection. Her case indicates that community transmission was happening undetected in the US, most likely since December.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('February 21, 2020', date_code)
row_dict['state_name'] = 'California'
row_dict['event_description'] = 'Two more cases of people who had returned from China are confirmed in California.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('February 26, 2020', date_code)
row_dict['state_name'] = 'California'
row_dict['event_description'] = 'The first case of community transmission, because it had no known origin, is confirmed.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('February 29, 2020', date_code)
row_dict['state_name'] = 'Washington'
row_dict['event_description'] = 'The first death from coronavirus in the U.S. was reported at EvergreenHealth Medical Center in Kirkland, Washington.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 2, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'Governor Andrew Cuomo announces the state\'s first reported case of COVID-19: a woman in her late 30s, who apparently contracted the virus while traveling in Iran and is self-isolating at home, in New York City.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 2, 2020', date_code)
row_dict['state_name'] = 'Oregon'
row_dict['event_description'] = 'Oregon confirmed its second case, a household contact of its first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 2, 2020', date_code)
row_dict['state_name'] = 'Rhode Island'
row_dict['event_description'] = 'The Rhode Island Department of Health announces a presumptive case in a person in their 40s who had traveled to Italy in mid-February, and a second case, a teenager who had traveled with the first person.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 2, 2020', date_code)
row_dict['state_name'] = 'New Hampshire'
row_dict['event_description'] = 'New Hampshire officials announce the state\'s first case, an employee with Dartmouth–Hitchcock Medical Center who had been to Italy.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 3, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'On March 3, when the state has no confirmed cases, Ohio Governor Mike DeWine cancels the Arnold Classic due to coronavirus concerns, a move which the Washington Post said seemed radical at the time.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 3, 2020', date_code)
row_dict['state_name'] = 'Arizona'
row_dict['event_description'] = 'Arizona\'s Department of Health Services reports a new confirmed case in Maricopa County, a man in his 20s who had made contact with a case outside of Arizona. The man was isolated in his home.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 3, 2020', date_code)
row_dict['state_name'] = 'New Hampshire'
row_dict['event_description'] = 'Public health officials confirm a second case of coronavirus in an individual who made contact with the first case after the first case defied quarantine orders and attended a private event organized by Dartmouth College\'s Tuck School of Business in White River Junction, Vermont.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 3, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'New York officials announce the state\'s second confirmed case: a man in his 50s in New Rochelle, Westchester County who had not recently traveled to any foreign countries affected by the outbreak.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 3, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'Governor Roy Cooper announces the state\'s first confirmed case: a person who had traveled to Washington and was "exposed at a long term care facility". They are in stable condition and in isolation at their home.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 4, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'New York officials confirm four new cases of coronavirus: the wife, son, and daughter of the second case, as well as the man\'s neighbor who drove him to the hospital. The new cases prompt the partial closure of the main campus of Yeshiva University, where the man\'s son is a student, as well as the high school in the Bronx borough of New York City where the daughter is a student. On the same day, another five confirmed cases are reported in a friend of the second case, as well as that friend\'s wife, two sons, and daughter.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 5, 2020', date_code)
row_dict['state_name'] = 'Nevada'
row_dict['event_description'] = 'Announces their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 5, 2020', date_code)
row_dict['state_name'] = 'Colorado'
row_dict['event_description'] = 'Announces their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 5, 2020', date_code)
row_dict['state_name'] = 'Tennessee'
row_dict['event_description'] = 'Announces their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 5, 2020', date_code)
row_dict['state_name'] = 'Maryland'
row_dict['event_description'] = 'Announces their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 5, 2020', date_code)
row_dict['state_name'] = 'New Jersey'
row_dict['event_description'] = 'Announces a second presumptive case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 5, 2020', date_code)
row_dict['state_name'] = 'Washington'
row_dict['event_description'] = 'Announces 31 new cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 5, 2020', date_code)
row_dict['state_name'] = 'Nevada'
row_dict['event_description'] = 'Public health officials in Las Vegas report that state\'s first confirmed case of coronavirus: a man in his 50s in Clark County who recently traveled to Washington state and Texas. Also, public health officials announce a second confirmed case of coronavirus in Reno. The new case, a man in his 50s, is in isolation at his home; the new case is linked to at least two other confirmed cases in Sonoma County, California and in Placer County, California among passengers who had been aboard the Grand Princess on a cruise from San Francisco to Mexico during the previous month.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Hawaii'
row_dict['event_description'] = 'Reports their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Utah'
row_dict['event_description'] = 'Reports their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Nebraska'
row_dict['event_description'] = 'Reports their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Kentucky'
row_dict['event_description'] = 'Reports their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'Reports their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'Reports their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Connecticut'
row_dict['event_description'] = 'Reports their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Reports their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'Reports their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Oklahoma'
row_dict['event_description'] = 'Reports their first case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Arizona'
row_dict['event_description'] = 'Public health officials announce the state\'s third case and first community transmission case in a Pinal County woman.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Connecticut'
row_dict['event_description'] = 'Governor Ned Lamont confirm his state\'s first case of coronavirus in a hospital employee, a New York resident who is currently under self-quarantine back home in Westchester County, New York.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Hawaii'
row_dict['event_description'] = 'Governor David Ige announces its first case of coronavirus, a resident that was a passenger of the Grand Princess which stopped in Hawaii in late February.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'The state reports its first case in an Indianapolis man who returned from travel to Boston.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Kentucky'
row_dict['event_description'] = 'Governor Andy Beshear confirms the states first case, a Lexington resident.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'Announces its first presumptive case, an elderly person living in Ramsey County, who had been on a cruise ship recently. The patient is reported to be in quarantine in their home.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Nebraska'
row_dict['event_description'] = 'Governor Pete Ricketts announces the first presumptive positive case of coronavirus in Nebraska, a woman in her 30s from Douglas County who came back from England at the end of February. She was initially hospitalized at Methodist Hospital, and was being transferred to the Biocontainment Unit at the University of Nebraska Medical Center after her test result came back positive.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'Public health officials announce a second confirmed case of coronavirus in a man in Chatham County who had recently traveled to Italy.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Oklahoma'
row_dict['event_description'] = 'Officials announce its first confirmed case of coronavirus in a Tulsa County man who had recently traveled to Italy.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'Governor Tom Wolf announces the first two confirmed cases of coronavirus in Delaware County and in Wayne County.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'Rhode Island'
row_dict['event_description'] = 'The state confirms its third case, a woman who had contact with a positive case in New York in late February.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 6, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Reports two presumptive cases in Kershaw County and Charleston County.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 7, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'Announces its first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 7, 2020', date_code)
row_dict['state_name'] = 'Kansas'
row_dict['event_description'] = 'Announces its first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 7, 2020', date_code)
row_dict['state_name'] = 'Missouri'
row_dict['event_description'] = 'Announces its first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 7, 2020', date_code)
row_dict['state_name'] = 'District of Columbia'
row_dict['event_description'] = 'Announces its first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 7, 2020', date_code)
row_dict['state_name'] = 'Washington'
row_dict['event_description'] = 'A new death is reported for March 7 in Washington. This brings the total confirmed U.S. deaths due to coronavirus to 19, 16 in Washington, 1 in California, and 2 in Florida.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 7, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'Governor Tom Wolf announces two new positive cases in Montgomery County; both cases are related to travel within the United States.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Iowa'
row_dict['event_description'] = 'Report their first cases of infection with the coronavirus.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Vermont'
row_dict['event_description'] = 'Report their first cases of infection with the coronavirus.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Hawaii'
row_dict['event_description'] = 'Second case is reported by Governor David Ige and State health officials is an elderly man who tested positive after returning from travel to Washington state earlier in the month. He is hospitalized and in isolation at Kaiser Permanente\' Moanalua medical facility.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'Second and third cases are reported, both in Hendricks County. The third case is an elementary student, resulting in recommendation from Hendricks County Health Department for closure of Hickory Elementary school for two weeks beginning March 9. This is the first school closing to occur in Indiana due to the current outbreak.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Iowa'
row_dict['event_description'] = 'Governor Kim Reynolds confirms the state\'s first three positive cases in Johnson County.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'The state of Minnesota reports a new case in Carver County and a total of 2 cases in Minnesota. The patient experienced symptoms on March 2, and is in the 50–59 age group. Thus far, both cases have been associated with travel.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'four more presumptive positive cases, for a total of six. One recently traveled to Italy, two are connected to a previous case, and one is of unknown origin.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Vermont'
row_dict['event_description'] = 'Vermont health officials announced the state\'s first "presumptive positive" case in Bennington County.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 9, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor Mike DeWine declares a state of emergency after Ohio reports its first cases of COVID-19.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 9, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'A case is reported in Noble County, the state\'s 4th.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Iowa'
row_dict['event_description'] = 'Five new presumptive positive cases are announced, bringing the statewide total to eight. Governor Reynolds signs a Proclamation of Disaster Emergency.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Kentucky'
row_dict['event_description'] = 'Governor Beshear confirms two new cases bringing the state\'s total to six.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Missouri'
row_dict['event_description'] = 'St. Louis County Executive Dr. Sam Page reports that the father and younger sister of the state\'s first coronavirus patient violated a self-quarantine order, attending a father-daughter function for her high school, Villa Duchesne, at the Ritz-Carlton Hotel in Clayton. The pair also attended a party for students from both Villa and the John Burroughs School before heading to the hotel. Villa cancels classes following the announcement, and the Burroughs students in attendance at the party were asked to stay home from school until further notice; they are ultimately cleared by medical professionals in consultation with the school later the same week, and the Ritz-Carlton was to undergo substantial cleaning.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'Five new presumptively positive cases are reported in Wake County. According to NCDHHS, all five had traveled to Boston in late February to attend a conference. This brings the total number of cases in North Carolina to 7.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The Ohio State University suspends face-to-face instruction until March 30. Governor DeWine declares a state of emergency.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'One additional presumptive positive case is reported, raising the total to 7. Additionally, there is a "possible" case at Clemson University.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 10, 2020', date_code)
row_dict['state_name'] = 'South Dakota'
row_dict['event_description'] = 'Report their first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 10, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Report their first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 10, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'Mitigation measures are expanded with a transition to online classes for universities and colleges.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 10, 2020', date_code)
row_dict['state_name'] = 'Massachusetts'
row_dict['event_description'] = 'Mitigation measures are expanded with a transition to online classes for universities and colleges.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 10, 2020', date_code)
row_dict['state_name'] = 'Washington'
row_dict['event_description'] = 'Mitigation measures are expanded with a transition to online classes for universities and colleges.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 10, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'The first semi-containment zone is announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 10, 2020', date_code)
row_dict['state_name'] = 'Massachusetts'
row_dict['event_description'] = 'Governor Charlie Baker declares a state of emergency as the number of cases doubles overnight to 92, 70 of them related to a meeting at Biogen in February. Harvard University orders its students to vacate the campus by Sunday, March 15.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 10, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'A third case in the state is confirmed in Anoka County. The individual is in the 30–39-year-old range and had no reported underlying conditions. The resident is in critical condition. According to health officials, the case was not transmitted in the state and there is no evidence that the virus is spreading from person to person in Minnesota. Governor Tim Walz signs a $21 million bill for funding COVID-19 preparedness.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 10, 2020', date_code)
row_dict['state_name'] = 'South Dakota'
row_dict['event_description'] = 'Health officials announce the state\'s first five confirmed cases and one death. The lone death tested positive for COVID-19, but the cause of death is still being investigated.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Arkansas'
row_dict['event_description'] = 'Reported their first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Delaware'
row_dict['event_description'] = 'Reported their first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Mississippi'
row_dict['event_description'] = 'Reported their first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'New Mexico'
row_dict['event_description'] = 'Reported their first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'North Dakota'
row_dict['event_description'] = 'Reported their first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Wyoming'
row_dict['event_description'] = 'Reported their first cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Washington'
row_dict['event_description'] = 'Governor Jay Inslee orders a halt to all gatherings of greater than 250 in three counties'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor Mike DeWine orders all public gatherings of more than 1,000 people to be banned statewide.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 10, 2020', date_code)
row_dict['state_name'] = 'Connecticut'
row_dict['event_description'] = 'Several towns in Connecticut announce schools will close for at least two weeks beginning March 12, including New Canaan, where the state\'s third case was confirmed.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Florida'
row_dict['event_description'] = 'A man wearing a mask and gloves (without symptoms) who had tested positive for Coronavirus boards a JetBlue flight from JFK in New York to PBI Airport in West Palm Beach, potentially exposing both airports and an entire plane to the virus. Despite this, Florida officials release all passengers without requiring isolation or testing.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'The state had five more cases, bringing the total to eleven. The University of Notre Dame announce that in-person classes will be suspended and moved online until at least April 13.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Maine'
row_dict['event_description'] = 'The University of Maine in Orono announce that in-person classes will be cancelled for the remainder of the semester beginning March 23, and that all classes will be transitioned to online only. In addition, all students living on campus were required to be moved out by March 22.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'The University of Minnesota announces that all in-person classes will be suspended until at least April 1 following spring break. Two more cases were confirmed, bringing the total number of cases to five. The Mayo Clinic in Rochester began "drive-through testing" for the virus, though patients still needed to be approved to be tested by telephone screening.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Missouri'
row_dict['event_description'] = 'Washington University in Saint Louis announces a switch to online classes until at least late April and asked undergraduates to go home by March 15. University of Missouri\'s Columbia campus cancels classes March 12 and 13 and directs that in-person classes should be taught by other means for March 16 through 20 (prior to the March 21 through 29 spring recess).'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Mississippi'
row_dict['event_description'] = 'Health officials report the state\'s first case, a man who had recently traveled to Florida.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'New Mexico'
row_dict['event_description'] = 'Three presumptive positive cases, a couple in their 60s who recently traveled to Egypt and one in her 70s who recently traveled to the New York City area.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Oklahoma'
row_dict['event_description'] = 'NBA player Rudy Gobert tested positive for COVID-19 prior to the game between the Utah Jazz and the Oklahoma City Thunder at Chesapeake Energy Arena in Oklahoma City. The game was postponed and the NBA announced that the 2019–20 NBA season would be suspended.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'South Dakota'
row_dict['event_description'] = 'Three presumptive positive cases, bringing state total to eight.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Arkansas'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Colorado'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Connecticut'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Kentucky'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Maryland'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Massachusetts'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'New Mexico'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Utah'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Washington'
row_dict['event_description'] = 'Public school closures are announced.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Georgia'
row_dict['event_description'] = 'Report their first deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Kansas'
row_dict['event_description'] = 'Report their first deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Alabama'
row_dict['event_description'] = 'Despite having no recorded cases in the state, the University of Alabama System as well as Auburn University both announced they are transitioning to online remote attendance when courses resume from spring break.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Alaska'
row_dict['event_description'] = 'State officials announced the first positive case of coronavirus in the state.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Colorado'
row_dict['event_description'] = 'The first school districts in the state, including Denver Public Schools, announced closures. An employee at University of Colorado Boulder tested positive for coronavirus. The Colorado Department of Corrections suspended in-person visitation in state prisons. The state reported 11 new cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Connecticut'
row_dict['event_description'] = 'A number of school districts announced closures beginning on March 13 through at least March 27, including those in the cities of Bridgeport, New Haven, and Stamford, among several others.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Delaware'
row_dict['event_description'] = 'Governor John Carney declared a state of emergency following the announcement of three more cases, connected with the University of Delaware.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Hawaii'
row_dict['event_description'] = 'The University of Hawaii announced classes at all campuses will be held online beginning March 23. Chaminade and other colleges in the state follow suit. BYU-Hawaii suspends classes for three days to prepare for remote learning.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'Went from 11 to 12 cases. Governor Holcomb Announces New Steps to Protect Public.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Maine'
row_dict['event_description'] = 'Maine Governor Janet Mills announced the state\'s first confirmed case, a woman in her 50s in Androscoggin County. The woman is said to be quarantined inside her home.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'The Minnesota Department of Health has confirmed nine total cases in the state, affecting Anoka, Carver, Dakota, Hennepin, Olmsted, Ramsey, and Stearns counties.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'New Mexico'
row_dict['event_description'] = 'All public schools in the state will be closed for three weeks starting Monday, March 16.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The Ohio State University suspends all face-to-face classes for the rest of the spring semester. Spring break is extended until March 22 so that faculty have time to prepare. Students living in residence halls are to begin moving out. Mike DeWine is the first governor to announce statewide school closings: starting March 16 all K–12 schools in Ohio will be closed for three weeks. He also bans "mass gatherings" of 100 or more people.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Colorado'
row_dict['event_description'] = 'Reported its first death.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 12, 2020', date_code)
row_dict['state_name'] = 'Alabama'
row_dict['event_description'] = 'First case announced in Montgomery County.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Georgia'
row_dict['event_description'] = 'Governor Brian Kemp declared a public health emergency in the state of Georgia.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Idaho'
row_dict['event_description'] = 'The state\'s first confirmed case was announced, a woman in her 50s who recently traveled to New York.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Illinois'
row_dict['event_description'] = 'All schools are closed beginning Tuesday, March 17 through the end of March.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Kentucky'
row_dict['event_description'] = 'First of Kentucky\'s COVID-19 patients to be declared fully recovered is discharged from University of Kentucky Medical Center.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'Governor Walz declares a state of emergency and asks the state legislature to pass several emergency bills, including one to help speed up testing for the virus. He also urges that all events with 250 or more attendees be cancelled or postponed.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Missouri'
row_dict['event_description'] = 'Two more presumptive positive cases were reported, bring the total number of cases up to 4. St. Louis County declares a state of emergency and bans gatherings larger than 250 people.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'New Hampshire'
row_dict['event_description'] = 'Governor Christopher Sununu declares a state of emergency in New Hampshire due to Covid-19. Six cases are confirmed.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Oregon'
row_dict['event_description'] = 'Governor Kate Brown announces a statewide K–12 school closure through to the end of March.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'Governor Wolf announces that all Pennsylvania schools will close for ten days.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Rhode Island'
row_dict['event_description'] = '20 cases are confirmed.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Governor Henry McMaster declares a state of emergency and closes schools in Kershaw and Lancaster Counties for 14 days due to evidence of the virus\'s spreading in these counties.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'South Dakota'
row_dict['event_description'] = 'One new case in McCook County. Governor Kristi Noem declares a state of emergency, all schools to close between March 16–20.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'West Virginia'
row_dict['event_description'] = 'While the state still had no confirmed cases of COVID-19, Governor Jim Justice announces all schools across the state would close beginning on March 16, 2020 for an indefinite period of time as a proactive measure.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 14, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'First death was reported in the news media'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 14, 2020', date_code)
row_dict['state_name'] = 'New Jersey'
row_dict['event_description'] = 'Governor of announced the state\'s second death on Twitter. This brought reported deaths to 7 for the day.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'All schools ordered to close for two weeks. Governor Roy Cooper also issued an executive order to prevent mass gathering.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 14, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine and Department of Health Director Amy Acton on March 14 recommended Ohioans postpone elective surgeries.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 14, 2020', date_code)
row_dict['state_name'] = 'Oklahoma'
row_dict['event_description'] = 'Governor Kevin Stitt took a selfie with his family in a crowded restaurant. Stitt tweeted, "It\'s packed tonight!" and was criticized on social media for ignoring social distancing. Stitt deleted the tweet in response to the backlash.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 14, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'Governor Ralph Northam announced Virginia\'s first death from the coronavirus.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Alabama'
row_dict['event_description'] = 'The Alabama Department of Public Health counted 22 cases of coronavirus: Jefferson County, 12 cases; Tuscaloosa County, 3 cases; Shelby County, 2 cases; Baldwin County, Elmore, County, Lee, Limestone, and Montgomery Counties, 1 case each.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Arizona'
row_dict['event_description'] = 'Governor Doug Ducey and Superintendent Kathy Hoffman ordered all schools closed through March 27.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Connecticut'
row_dict['event_description'] = 'All schools ordered closed after March 16 until at least March 31.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Illinois'
row_dict['event_description'] = 'Governor J.B. Pritzker announces that the state will order restaurants and bars to close to dine-in customers.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Maine'
row_dict['event_description'] = 'Governor Mills declares a state of emergency with 7 cases confirmed.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'There are now 35 confirmed cases with at least three spread person-to-person in the state. Governor Walz closes all schools from March 18 until at least March 27. During the shutdown meals and mental health services will still be provided to students in need. Under the governor\'s order, schools will remain open for the elementary-aged children of health care workers and other emergency workers. Teachers will be using this time to plan for a possibility of weeks of long-distance learning.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'New Hampshire'
row_dict['event_description'] = 'Governor Sununu orders all public K–12 schools to transition to remote learning effective Monday, March 16 through April 3, 2020, requiring remote learning to begin by March 23, 2020.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'Mecklenburg County which encompassed the city of Charlotte declared a state of emergency in the county after 2 more new cases are found in the county, bringing the total in the county to 4 and the total statewide to 33.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'North Dakota'
row_dict['event_description'] = 'Governor Burgum ordered all schools to be closed from March 16 to March 20. It was confirmed the state lab had tested 112 individuals for the virus with one case coming back positive from a person with travel history.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'New York City mayor DeBlasio announces New York City public schools, the largest public school system in the country, will close starting Monday, March 16. The closure will last at least through April 20.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine orders all bars and restaurants to close beginning at 9:00 pm. Establishments may continue providing take-out and delivery services.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Oklahoma'
row_dict['event_description'] = 'Governor Stitt declares a state of emergency.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Puerto Rico'
row_dict['event_description'] = 'Governor Wanda Vázquez Garced issues an island-wide curfew through March 30 and closes all businesses not involved in food sales, medicine, or banking.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Governor McMaster announces school closures starting on March 16. The city of Myrtle Beach declares a state of emergency and closes city facilities that are normally open to the public, including the city library and recreation centers. Nine new cases confirmed in South Carolina, bringing the total to 28.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Colorado'
row_dict['event_description'] = 'Colorado announced 29 new positive cases of COVID-19, bringing the state total to 160. Mayor Hancock of Denver orders all bars and restaurants to close by 8:00 am starting March 17 (excepting food delivery and pickup) and also bans gatherings of more than 50 people in the city. Governor Polis expanded the closures by ordering a state-wide closure of dine-in services. Polis also ordered the closure of gyms, casinos, and theaters.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'District of Columbia'
row_dict['event_description'] = 'The Supreme Court of the United States postponed oral arguments scheduled for late March and April 1. Similar precautions were taken in 1918 in response to the Spanish flu and in 1798 and 1793 in response to Yellow fever outbreaks. 18 cases of coronavirus have been reported in DC.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'California'
row_dict['event_description'] = 'As of 12:01 am Monday, March 16, Los Angeles Mayor Eric Garcetti ordered all bars, movie theaters, gyms and fitness centers closed, and for restaurants to limit themselves to take-out and delivery only.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'Several clinics, including Mayo and M Health Fairview are reporting only positive tests, not the total number of tests. Affected counties now include Anoka, Benton, Blue Earth, Carver, Dakota, Hennepin, Olmsted, Ramsey, Renville, Stearns, Sherburne, Waseca, Washington, and Wright. Governor Walz has ordered the closure of public places, including all: restaurants, bars, coffee shops, gyms, theaters, breweries, ski resorts, and other public places until at least March 27. Bars and restaurants in the state were closed only to dine-in customers; the businesses were allowed to continue to serve customers by take out or delivery orders. He said this order may be extended.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state has 50 confirmed cases of COVID-19. Bowling alleys, fitness centers, gyms, movie theaters, public recreation centers, trampoline parks, and water parks are ordered to be shut and gatherings of more than 50 people are banned. Governor DeWine announces the presidential primary elections, scheduled for the next day, will be cancelled on orders of Department of Health director Amy Acton.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'Oklahoma'
row_dict['event_description'] = 'Ten cases of coronavirus have been confirmed; Governor Stitt declares a state of emergency.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'Oregon'
row_dict['event_description'] = 'Governor Brown and public health officials issue new statewide mandates, banning all public gatherings of 25 or more people and restricting restaurants to take-out or delivery service. Only essential businesses such as grocery stores, pharmacies, retail stores and workplaces are exempted.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'Governor Wolf extends a shutdown order to the entire state. The order was originally for four southeastern Pennsylvania counties outside Philadelphia.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'Vermont'
row_dict['event_description'] = 'Public schools began a transition in which student attendance was optional Monday, March 16 and Tuesday, March 17, but faculty and staff were expected to attend to help with an orderly shut down, with schools tentatively to reopen April 7. Plans were being made to continue providing special needs services and meals for those students who depend on them.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'Texas'
row_dict['event_description'] = 'The first death from the coronavirus occurred in Matagorda County.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'Alabama'
row_dict['event_description'] = 'Alabama had a total of 39 cases, where the majority of them (21 cases) are located in Jefferson County.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Alaska'
row_dict['event_description'] = 'Alaska confirmed three new cases, bringing the total to six. Alaska government banned dine-in food service.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Arkansas'
row_dict['event_description'] = 'Arkansas reports, the first time in almost a week, that there are no new cases in the state.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'California'
row_dict['event_description'] = 'Beginning at 12:01 am on Tuesday, March 17, San Francisco, Marin, Santa Clara, Santa Cruz, San Mateo, Contra Costa, and Alameda Counties (combined population seven million) are placed under a mandatory "shelter in place" order.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Florida'
row_dict['event_description'] = 'Governor of Florida announces it has 24 new cases, increasing the total to 216 cases. The governor also orders businesses that sell liquor to reduce their occupancy by half, and to limit parties on beaches to only ten people per group.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Kansas'
row_dict['event_description'] = 'Governor Laura Kelly orders all K–12 schools to close for the remainder of the school year.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Illinois'
row_dict['event_description'] = 'The state announces its first death as 55 new cases are added, including 22 at a nursing home in Willowbrook, DuPage County, Illinois. The state total is now 166. Turnout for the 2020 Illinois Democratic primary was low, but Chicago broke a World War II-era record for mail-in voting.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Maryland'
row_dict['event_description'] = 'Maryland postponed all state primaries until June 2 to reduce the risk of coronavirus infection to the Marylanders.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'The Minnesota Department of Health announces that due to the national shortage of materials for medical testing for the virus they will be limiting testing to those who are hospitalized, ill healthcare workers and those who live in long-term care facilities. The restrictions will be in place until the state is supplied with additional tests.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'The state announces it has 65 confirmed coronavirus cases. The state also announces it had conducted 1,100 tests.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state had 67 confirmed cases. Governor DeWine orders elective surgeries be postponed.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'All liquor stores closed indefinitely.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Governor McMaster issues an executive order requiring the mandatory shutdown of dine-in service in restaurants and bars and prevented a gathering of more than 50 people. The state also had 47 cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Oregon'
row_dict['event_description'] = 'The governor extended school closures through April 28.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'South Dakota'
row_dict['event_description'] = 'Closure of K–12 schools extended an extra week. Set to resume on March, 30.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Texas'
row_dict['event_description'] = 'The second death in Texas is reported. A resident of a retirement community in Arlington died on Sunday, March 15.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'Governor Northam announces a ban on gatherings of more than 10 people. 15 new cases are reported, bringing the total to 67 cases in Virginia.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'West Virginia'
row_dict['event_description'] = 'Confirmed its first case; it was the last state to do so.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Florida'
row_dict['event_description'] = 'The Clearwater City Council voted to close down Clearwater Beach for two weeks, starting March 23 at 6 a.m.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Maryland'
row_dict['event_description'] = 'The state added 22 more coronavirus cases, to the total of 63 cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'The first death from coronavirus in the state is reported, a man in his 50s who had underlying medical conditions. The state also announces 30 more confirmed cases, bringing the total number there to 110.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'Governor Walz criticizes the federal response to the virus. The state had approximately 1700 frozen samples to be tested, but had not yet been, due to the lack of facilities for testing. The state had 77 positive results out of at least 2762 tests.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Montana'
row_dict['event_description'] = 'Governor Steve Bullock announces 2 additional cases in Gallatin county, bringing the confirmed total to 12 in Montana.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'The number of cases in the state jumped to 81.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces 181 Divisions of Motor Vehicle locations will close until further notice. Five will stay open to process commercial driver license applications and renewals, and he proposes a grace period for people whose licenses have expired. Barbershops, salons, and tattoo parlors are closed. Businesses that do stay open are asked to take their employees\' temperatures every day before allowing them entry to work and to send sick employees home. Mayor Andrew Ginther declares a state of emergency in Columbus, Ohio.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Oregon'
row_dict['event_description'] = 'Governor Brown issues executive order extending the closure of K–12 public schools until April 28.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'The state announces its first death in Northampton County following the addition of 37 new cases bringing the total to 133 cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'The state confirms more cases of the COVID-19, totaling at 60 cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Utah'
row_dict['event_description'] = 'U.S. congressman Ben McAdams tests positive for coronavirus.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'California'
row_dict['event_description'] = 'The state has ordered the closure of all museums, malls and other all non-essential workplaces effective March 20 11:59 p.m. All 40 million citizens in the state are ordered to stay home. More than 900 state residents have been infected and 19 have died. The Academy of Motion Picture Arts and Sciences is considering changing its criteria for qualifications in the 2021 Oscar ceremony because so many movie theaters are closed.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'Hawaii'
row_dict['event_description'] = 'Two cruise ships are prevented from disembarking despite not having any cases of Covid-19 on board.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'Massachusetts'
row_dict['event_description'] = 'The Massachusetts Medical Society says there is a "dire" shortage of protective medical equipment in the state.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'The state reports two additional coronavirus deaths. Meanwhile, the total number of cases in the state rises to 334, an increase of 254 from the previous day. Officials attribute the spike to an increase in testing.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'The state confirmed its first community spread of the coronavirus. The number of cases in North Carolina rises to 134. ProPublica reveals that Senator Richard Burr (R-NC) allegedly used his position as chairman of the Senate Intelligence Committee to mislead the public about COVID-19. He personally made between $582,029 and $1.56 million by selling off stock days before the market crashed. Police in Guilford County, North Carolina stopped a truck with nine tons of stolen toilet paper.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state has 119 cases of COVID-19 resulting in 33 hospitalizations. Governor DeWine signs state active duty proclamation that will activate 300 personnel from the Ohio National Guard to help with humanitarian efforts.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'The state\'s department of education announces that all statewide assessments will be canceled for the remainder of the 2019–2020 school year. Pennsylvania has a current total of 196 coronavirus cases. Governor Wolf ordered a statewide shutdown of "non-life sustaining businesses" by 8:00 p.m. Enforcement of this order is planned to begin at 12:01 a.m. Saturday, March 21.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Governor McMaster issues a new executive order: all non-essential state employees stay home. Public universities are also encouraged to finish the semester online. 81 cases are confirmed in the state.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'Virginia officials are requesting law enforcement to avoid arrests while possible. The administration also asks magistrates and judges to consider alternatives to incarceration. Virginia reports 24 new COVID-19 cases, bringing the total to 101.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'California'
row_dict['event_description'] = 'Los Angeles Mayor Eric Garcetti promises that no one will go to jail for violating the stay-at-home order that goes into effect at midnight. However, a major purpose of the order is to provide enforcement for businesses that are not complying. Marijuana dispensaries are classified "essential".'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'Illinois'
row_dict['event_description'] = 'Governor Pritzker issues a stay-at-home order. The order will become effective March 21 and will remain in place until April 7 but could go longer.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'Governor Cuomo issues a state-wide order that all non-essential workers must stay at home, noting that the number of coronavirus cases in the state has gone from zero on March 4 to over 2,900. The same day, Coronavirus cases in New York exceed 7000.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'The state reports 225 new cases of coronavirus, bringing the total number of cases there to 549. A fourth death from coronavirus is reported, a man in his 50s from Oakland County who had underlying health conditions.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'The state activates North Carolina National Guard to assist in logistics and transportation of medical supplies, as the state reports it has 179 cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state reported its first coronavirus death, Mark Wagoner Sr, a 76-year-old attorney from Lucas County in the Toledo area. The state had a total of 169 cases. Governor DeWine announces that senior centers and senior daycare centers will close.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'Tennessee'
row_dict['event_description'] = '15 recovery cases are confirmed in Nashville. However, the health department confirmed the state\'s first death of coronavirus.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'Texas'
row_dict['event_description'] = 'Dallas mega-church preacher Robert Jeffress agrees to move his Sunday services online.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'Governor Northam activated Virginia National Guard. The state announced they have 114 cases of COVID-19, with 20 hospitalizations.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'Florida'
row_dict['event_description'] = 'Governor DeSantis is considering a new strategy to put positive COVID-19 patients into isolation shelters such as abandoned convention centers and hotels instead of returning the patients to their home where they can infect their own family. Cases in Florida reached 763 presumptive positive cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Four more deaths from coronavirus are reported, bringing to total number of deaths in the state to eight. Also, the total number of cases of coronavirus in the state rises to 807.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'The state confirmed the first death due to the virus; the patient was from Ramsey County and was in their 80\'s. The patient had contracted the virus from a confirmed case.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state has 247 confirmed cases of COVID-19. Facilities providing daycare and assistance for adults with developmental disabilities are closed unless they serve 10 people or less.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'Cases in the state increased to 273. Hospitals in the state begin restricting the visitors to the hospital.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Governor McMaster orders local law enforcement to disperse crowds on state beaches. Cases in the state grow to 173.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'Tennessee'
row_dict['event_description'] = 'The state\'s second confirmed death due to the coronavirus occurred in Nashville. The man was the brother of Minnesota state Lieutenant Governor Peggy Flanagan.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'The state reports it has confirmed 158 total cases in the state.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'California'
row_dict['event_description'] = 'Governor Newsom states that testing should prioritize healthcare workers, hospitalized persons, senior citizens, persons with immune system issues, and other high-risk persons.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 22, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'Health authorities recommend health facilities stop testing non-hospitalized patients, in part because of a shortage of PPE (Personal Protective Equipment) for health care workers. The state had announced initial tests will begin Tuesday, March 22 to see how effective three drugs are against COVID-19. The U.S. FDA (Food and Drug Administration) has shipped 70,000 doses of hydroxychloroquine, 10,000 of Zithromax, and 750,000 doses of chloroquine to the state.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 22, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'Mecklenburg County announced that they will cover one week cost of people staying in hotels and motels to keep the tenants from being evicted. The state also confirms a total of 306 cases, and reports that 6,438 tests have been conducted.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 22, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The Ohio Department of Health issues a stay at home order. All non-essential businesses are ordered closed until April 6, 2020. The state had 351 confirmed cases with 83 hospitalizations.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 22, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'Montgomery County officials announce the first known death from COVID-19 in that county. The statewide total of deaths related to COVID-19 is three.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 22, 2020', date_code)
row_dict['state_name'] = 'Washington'
row_dict['event_description'] = 'President Donald Trump also announces approval of Washington emergency declaration, and have instructed Federal assistance to be given to assist the local recovery efforts in fighting the coronavirus.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 22, 2020', date_code)
row_dict['state_name'] = 'West Virginia'
row_dict['event_description'] = 'Governor Justice urges West Virginians to stay home as much as possible. 12 cases of COVID-19 are detected in the state.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 22, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'An additional death from coronavirus in the state is reported, an older man from Washtenaw County who had underlying medical conditions. The total number of deaths in the state is now nine. 258 new cases of coronavirus are reported in the state, bringing the total number of cases to 1,065.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 22, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'Governor Northam announces that Virginia Schools are closed for the remainder of the 2019–2020 school year.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 23, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Total number of cases reached 1,328 with 15 deaths. Governor Whitmer issued a stay-at-home order to go into effect at midnight on March 24 and last until April 13.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 23, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'The governor made several announcements regarding the state\'s response to the virus: a small business loan program would be made available for possibly 5000 businesses during the week for amounts between $2,500 and $35,000, all elective veterinary surgeries would be halted and that he would be revising the budget for the response to the virus asking for an additional $365 million. The state had 235 positive total confirmed cases and 1 death. The governor had also quarantined himself after a member of his security team tested positive for the virus. He claimed to be experiencing no symptoms. Senator Amy Klobuchar\'s husband was hospitalized due to the coronavirus.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 23, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = '442 people in the state have tested positive for COVID-19. 104 people have been hospitalized and six people have died due to the illness. Governor DeWine institutes a hiring freeze for all state government positions, except those involved in fighting the virus, and a freeze on contract services. The stay at home order signed on March 22 goes into effect at 11:59 pm.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 23, 2020', date_code)
row_dict['state_name'] = 'Oregon'
row_dict['event_description'] = 'Governor Brown issues a stay at home order, "to the maximum extent possible", except for when carrying out essential tasks like getting groceries, refueling their vehicles, or obtaining health care.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 23, 2020', date_code)
row_dict['state_name'] = 'New Mexico'
row_dict['event_description'] = 'Governor Lujan-Grisham closes all non-essential businesses statewide effective March 24.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 24, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'The state announces a total of 262 confirmed cases in the state. Twenty-two of those cases require hospitalization and there is 1 confirmed death. There are 15 people hospitalized and 88 patients who had required isolation no longer do.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 24, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state has 564 confirmed COVID-19 cases: 145 hospitalizations and 8 deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 24, 2020', date_code)
row_dict['state_name'] = 'Rhode Island'
row_dict['event_description'] = 'Governor Gina Raimondo announces that there are 124 confirmed cases. She claims that "many, many" have recovered.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 24, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Governor McMaster announces that K–12 schools statewide will remain closed through the month of April.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 24, 2020', date_code)
row_dict['state_name'] = 'Alaska'
row_dict['event_description'] = 'Governor Dunleavy orders everyone arriving in Alaska to self-quarantine for 14 days upon arrival, effective March 25, with limited exceptions.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 25, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'The number of deaths from coronavirus increases to 43, while 507 new cases are reported. This brings the total number of cases in the state to 2,294.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 25, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'As of 2:00 pm, there are 704 confirmed cases of COVID-19, with 182 resulting in hospitalization (including 75 ICU admissions). Ten people have died from the virus. Though 704 cases have been confirmed in the state, the actual number of cases is believed to be much higher. The Ohio General Assembly passes House Bill 197, which does many things, such as extending primary voting to April 28 and banning water utilities from disconnecting service.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 26, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = '17 additional deaths from coronavirus are reported, bringing the total number of deaths in the state to 60. The total number of cases in the state increases to 2,856.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 26, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Ohio has 867 confirmed COVID-19 cases, with 223 of those cases resulting in hospitalization and 15 resulting in death.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 26, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'The state had 1,687 confirmed cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 26, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'President Trump announces that USNS Comfort will be heading up to New York City to assist local hospitals. The ship is scheduled to depart on March 28 and scheduled to arrive in New York City on March 30. Governor Cuomo announces the state will allow two patients to share one ventilator.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 27, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'The number of deaths of coronavirus in the state increases to 92, while the total number of cases climbs to 3,657.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 26, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = '1,137 people in Ohio have the virus, with 276 needing hospitalization. 19 COVID-19 patients have died. Governor DeWine signs House Bill 197, which extends the primary election through April 28, bans water disconnections, waives standardized testing requirements for public schools, and extends the state income tax filing and payment deadline to July 15.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 27, 2020', date_code)
row_dict['state_name'] = 'Colorado'
row_dict['event_description'] = 'The 8:00 pm Denver Howl is started by folks in a neighborhood near the now closed Denver Botanic Gardens and Denver Zoo.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 28, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'President Donald Trump approves the state\'s disaster declaration.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 28, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'According to the Ohio Department of Health, the state has 1,406 cases of COVID-19, 344 of which resulted in hospitalization and 25 of which resulted in death. Ohio Department of Health director Amy Acton reports that the virus\'s peak is expected in mid-May and that during that peak, there could be up to 10,000 cases a day. Governor DeWine asks the FDA to issue an emergency waiver for the use of new technology that can sterilize face masks.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 28, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'State Representative Isaac Robinson passes away of suspected coronavirus at the age of 44. Meanwhile, the state\'s total number of coronavirus cases increases to 5,524 with 132 deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 29, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state has 1,653 cases with 403 hospitalizations including 139 ICU admissions, and 29 deaths..'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 30, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Ohio has 1,933 cases of COVID-19, including 475 that resulted in hospitalization and 39 that resulted in death. Governor DeWine extends the closure of schools to May 1.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 31, 2020', date_code)
row_dict['state_name'] = 'Georgia'
row_dict['event_description'] = 'Governor Brian Kemp suspends in class instruction for all Georgia public schools for the remainder of the 2019–2020 school year. Students will continue their education through online formats.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 31, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Ohio has 2,199 cases; 585 resulted in hospitalization and 55 resulted in death. Governor DeWine announces an order requiring that organizations with ventilators or similar devices report them to the state. President Trump approves the state\'s Disaster Declaration.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 1, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There are 2,547 confirmed cases. 679 people have been hospitalized and 65 have died. Governor DeWine announced during his daily press conference that there is a new method to divide the state into hospital capacity regions.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 2, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'Superintendent of Public Instruction Jennifer McCormick directs that Indiana schools will close for the rest of the academic year, and continue providing instruction remotely.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 2, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governor Whitmer officially closes schools in the state for the rest of the 2019–20 school year.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 2, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There are 2,902 confirmed cases with 802 of them leading to hospitalization and 81 leading to death. Governor Dewine extends the state\'s stay at home order through May 1 with new restrictions: campgrounds must close, all retail businesses must post signs limiting how many people are allowed in at one time, and wedding receptions are limited to 10 people. The order also establishes a state board to evaluate what is and is not an essential business.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 3, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'Governor Eric Holcomb announces a two-week extension of Indiana\'s stay-at-home order. The new order will run through April 20.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 3, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state has 3,312 confirmed cases with 895 of them leading to hospitalization and 91 leading to death.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 4, 2020', date_code)
row_dict['state_name'] = 'Alabama'
row_dict['event_description'] = 'Governor Kay Ivey announces a stay-at-home order through April 30. Attorney General Steve Marshall said the order can be enforced criminally, but he said he hopes it will not come to that. Disobeying the order is a Class C misdemeanor that can carry a $500 penalty.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 4, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There are 3,739 total cases including 1,006 that resulted in hospitalization and 102 that resulted in death. Governor DeWine signs an executive order removing training requirements for mental health and marriage counselors to make telehealth visits more easily accessible.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 5, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There are 4,043 confirmed cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 5, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'The state has 11,510 cases. 1,072 lead to hospitalization and 150 lead to death.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 6, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'The state\'s number of coronavirus cases increases to 4,944 with 139 deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 6, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The number of cases surpasses 4,400. Governor DeWine names six facilities that will be converted into health care facilities if necessary.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 7, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'The state legislature votes to extend Michigan\'s emergency declaration to April 30.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 7, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Governor McMaster issues a "home or work" order.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 8, 2020', date_code)
row_dict['state_name'] = 'Georgia'
row_dict['event_description'] = 'Governor Brian Kemp extends the statewide shelter in place order through the end of April.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 8, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'Governor Walz extends Minnesota\'s stay at home order until May 4.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 8, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The number of cases increases to 5,148. Apple CEO Tim Cook donates 100,000 N95 masks to Ohio health care workers.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 9, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'The state\'s amount of coronavirus cases increases to 6,351 with 245 deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 9, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governor Whitmer officially extends the state\'s stay-at-home order through April 30. It was originally set to expire on the 14th.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 9, 2020', date_code)
row_dict['state_name'] = 'Missouri'
row_dict['event_description'] = 'Governor Parson orders all Missouri public, private, and charter schools to be closed for in-person instruction for the rest of the school year.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 9, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state has more than 5,500 confirmed cases and more than 200 deaths. During Governor DeWine\'s daily press conference, about 75 people gather outside to protest the state\'s restrictions.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 10, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'The field hospital at the TCF Center in downtown Detroit begins accepting COVID-19 patients.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 10, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces an emergency amendment to Ohio Department of Medicaid\'s provider agreement. The new changes are intended to remove barriers to health care and reduce burdens on hospitals and providers. The Food and Drug Administration (FDA) grants STERIS, an Ohio-based company, a temporary Emergency Use Authorization for decontaminating compatible N95 and N95-equivalent respirators. The Ohio Bureau of Workers\' Compensation Board of Directors approves a plan to send up to $1.6 billion to Ohio employers in spring of 2020.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 12, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'The total number of cases of coronavirus in the state increases to 7,928 with 343 deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 13, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Nursing homes are now required to inform families of cases within 24 hours. Liquor sales are now limited to state residents only in the counties of Ashtabula, Trumbull, Mahoning, Columbiana, Jefferson, and Belmont. Protesters again gathered outside the statehouse during Governor DeWine\'s press conference.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 13, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'The total number of cases of coronavirus in the state increases to 8,527 with 387 deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 14, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There are 7,280 cases of COVID-19, including 2,156 that resulted in hospitalizations and 324 that resulted in death. Governor DeWine announces that his administration is seeking a Medicaid waiver from the federal government to remove certain healthcare restrictions. A hundred people protest outside the Statehouse during his press conference.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 15, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'A large scale rally called "Operation Gridlock" takes place in Lansing to protest Governor Whitmer\'s stay-at-home order.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 15, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces that he has asked the Ohio Hospital Association to begin developing a plan to start treating people whose non-COVID-19 elective procedures were deferred or delayed. He also announces that Ohio\'s partnership with the Battelle Memorial Institute is expanding. This will allow the institute to extend their sterilization services to EMS providers and law enforcement agencies.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 16, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state has 8,414 confirmed and probable cases. Governor DeWine announces that he will work closely with the Governors of Illinois, Indiana, Kentucky, Michigan, Minnesota, and Wisconsin to reopen the region\'s economy in a coordinated way.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 17, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'Governor Holcomb extends the stay-at-home order until May 1.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 17, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Detroit mayor Mike Duggan announces that all essential workers in the city, regardless of whether they exhibit symptoms or not, are now eligible to be tested for COVID-19.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 17, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state has 9,107 confirmed and probable cases and 418 confirmed and probable deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 17, 2020', date_code)
row_dict['state_name'] = 'Texas'
row_dict['event_description'] = 'Governor Greg Abbott announced a phased reopening of Texas\' economy beginning April 20.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 18, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'Dozens protest outside of the Governors mansion in Indianapolis after the issue of the latest stay-at-home order; this despite the number of cases in the state continuing to go up.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 20, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces that Ohio\'s K–12 schools would remain closed for the remainder of the academic year. Hundreds of protesters again gather at the Ohio Statehouse during his press conference.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 20, 2020', date_code)
row_dict['state_name'] = 'Texas'
row_dict['event_description'] = 'In reiterating his earlier statements on Tucker Carlson Tonight, Texas Lieutenant Governor Dan Patrick (politician) tells Carlson, "... there are more important things than living" as a justification for the state moving ahead with reopening businesses in the coming days despite the coronavirus outbreak.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 21, 2020', date_code)
row_dict['state_name'] = 'Georgia'
row_dict['event_description'] = 'Governor Kemp announced on April 20 that many businesses could reopen on April 24, including "gyms, hair salons, bowling alleys and tattoo parlors", with restaurants and movie theaters allowed to reopen on April 27. This move has brought widespread condemnation from inside and outside Georgia, with Atlanta Mayor Keisha Lance Bottoms saying she will "continue to ask Atlantans to please stay at home" and Stacy Abrams, the 2018 Democratic candidate for governor, calling reopening "dangerously incompetent. The Institute for Health Metrics and Evaluation\'s April 21 prediction lists the earliest safe date for Georgia to shift from social distancing measures as June 19. As of April 21, the state had more than 20,000 confirmed cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 22, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = '14,117 people have tested positive for COVID-19. 610 have died and 2,882 have been hospitalized. The Ohio Department of Health establishes a tier system to prioritize testing.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 23, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'DeWeine shares additional details on how the state will re-open. Phase one of the re-opening will begin on May 1.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 24, 2020', date_code)
row_dict['state_name'] = 'Alaska'
row_dict['event_description'] = 'Restaurants were allowed to open using only 25 percent of capacity and with tables at least 10 feet apart.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 24, 2020', date_code)
row_dict['state_name'] = 'Georgia'
row_dict['event_description'] = 'Barber shops cut hair with face masks and latex gloves in place. Beauty salons asked customers to sign legal waivers before coloring hair.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 24, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governor Whitmer extends the state\'s stay-at-home order to May 15 while loosening some restrictions.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 24, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state has 15,169 reported COVID-19 cases.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 25, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There are 15,587 cases, 711 of which resulted in death.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 27, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governor Whitmer unveils her plan to reopen the state\'s economy, called the MI Safe Start Plan, which calls for workplaces with the least risk of virus transmission to be the first to reopen.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 27, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'All businesses are required to enforce mandatory facial covering for employees and customers and limited to no more than 50% of their spaces\' fire code occupancy. The state also announces that on May 1 all nonessential medical procedures can resume, and veterinarians and dentists can reopen. Manufacturing and construction can resume May 4, and all non essential retail may reopen May 12.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 30, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governor Whitmer extends the state\'s emergency declaration through May 28.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 30, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The total number of cases is 18,027. Governor DeWine announces in his press conference that he will extend the stay-at-home order, though he does not give a specific date. The Ohio Department of Health\'s website says the extension will last until May 29.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 1, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'Despite one of the largest increases the state has had in a day, Governor Holcomb ends the stay-at-home order and institutes a five-stage plan for getting Indiana "back on track". Holcomb says he hopes Indiana can completely be back to normal on July 4.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 1, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'A "Stay Healthy and Safe at Home" order replaces the previous stay-at-home order. Starting May 1, medical procedures that do not require an overnight stay in a hospital can proceed. Another large protest occurs during Governor Dewine\'s press conference.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 1, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governor Whitmer signs an executive order to resume residential and commercial construction, and well as real estate activities beginning May 7.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 2, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There are 19,335 reported cases. Protests at the statehouse continued.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 3, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There are 19,914 total cases with 1,038 deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 4, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'The state begins stage 2 of its "back on track", with many different businesses including retail and malls opening at 50% capacity. Restaurants will be able to open next week.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 4, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There are 20,474 cases reported, including 1,056 deaths. Manufacturing, distribution, and construction open up. General offices may also reopen, though employees are to work from home when possible.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 5, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine discusses the state\'s economy during a press conference. At the end of February, Ohio was $200 million ahead of projections for the year. Ohio now has a projected budget shortfall of $776.9 million for the fiscal year, which will end June 30.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 6, 2020', date_code)
row_dict['state_name'] = 'Maryland'
row_dict['event_description'] = 'Governor Larry Hogan announces that Maryland Public Schools are closed for the remainder of the 2019–2020 school year.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 6, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces a $775 million budget reduction over the next two months. Medicaid spending will be reduced by $210 million. Spending on K–12 schools will be reduced by $300 million. Spending on other education will be reduced by $55 million and higher education spending will be reduced by $110 million. All other agencies will lose $100 million.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 7, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor Dewine announces that barbershops and salons can reopen on May 15. Also on May 15, patio service can resume at bars and restaurants. Parties at restaurants and bars must have 10 people or less and must be separated by a physical barrier or six feet of space. Restaurants and bars can resume dine-in services May 21.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 7, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governer Whitmer extends the state\'s stay-at-home order an additional two weeks to May 28. She also announces that automobile manufacturing in the state can resume on May 11.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 12, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The state now has 25,250 reported cases, including 1,436 deaths. Malls and retail stores are allowed to re-open to the public, though there are restrictions placed on customers.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 14, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Another smaller protest occurs at the state capitol building against Governor Whitmer\'s stay-at-home order. The spike in new cases is attributed to backlogged data from labs in the state.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 14, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'More announcements: campgrounds will open on May 21; horse racing will open on May 22; the Ohio Bureau of Motor Vehicles (BMV), gyms, fitness centers, pools, and sports leagues (only for sports involving limited or no contact) will open on May 26; and childcare centers will re-open on May 31.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 15, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There are 26,357 cases including 1,534 deaths. Outdoor dining at restaurants resumes. Personal services such as salons, spas, massage therapy, tattoo services, and piercing services re-open.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 18, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governer Whitmer announces that bars, restaurants, and retail stores in the Upper Peninsula and upper Lower Peninsula can reopen as early as May 22.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 19, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces an "Urgent Health Advisory: Ohioans protecting Ohioans" order. Elements of the previous stay-at-home order are now "strong recommendations."'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 20, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces that three new orders have been signed. One order partially rescinds the April 30 Stay Safe Ohio Order, one issues a series of health advisories, and the Camp Safe Ohio Order specifies how campgrounds in Ohio can reopen.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 21, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Campgrounds re-open. Lieutenant Governor Husted announces that bowling alleys, miniature golf, and batting cages can reopen May 26, so long as they follow certain protocols. He also says wedding venues and banquet halls may open on June 1 but ... six feet between tables, no congregating, and no more than 300 people.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 21, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governor Whitmer announces that auto dealerships and retail stores can reopen by appointment only and with certain guidelines in place beginning on May 26. She also lifts medical restrictions across the state beginning May 29. Gatherings of up to 10 people are also authorized.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 22, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governor Whitmer extends the state\'s stay-at-home order by another two weeks to June 12.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 26, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There have been 33,006 reported cases, leading to 5,579 hospitalizations and 2,002 deaths. 1,450 of the hospitalizations were ICU admissions. Governor DeWine announces that congregate care unified response teams will begin testing in nursing homes this week. BMVs re-open.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 26, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'There have been 33,439 reported cases, leading to 5,700 hospitalizations and 2,044 deaths.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 28, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces that the state is expanding the criteria for who can get tested for the virus. The new criteria allows anyone with symptoms to be tested.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 31, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Child care providers and day camps are allowed to re-open.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('June 1, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The Ohio State Controlling Board approves $873 million in COVID-19 relief funds.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('June 1, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governor Whitmer lifts the state\'s stay-at-home order; outdoor gatherings of up to a hundred are allowed. On June 8, dine-in service can resume.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('June 2, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'DeWine announces that all surgeries can resume.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('June 2, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'DeWine announces that entertainment facilities such as movie theaters and zoos may re-open in one week and that casinos, racinos, amusement parks, water parks, and outdoor theaters can reopen in two weeks. He also says that his office will approve a safety plan which will allow the Memorial Tournament to be held from July 13–19.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('June 11, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'DeWine announces that anyone who wants to get tested for COVID-19 can be tested.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('June 11, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'McMaster announces that South Carolina will not shut down again despite increase in infection rates since Memorial Day holiday weekend.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('June 30, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'DeWine announces that nursing homes will be open for outdoor visitation starting July 20.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('July 2, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor Mike DeWine released guidelines for schools to follow as they re-open.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('July 5, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'For the first time since the beginning of the outbreak, no additional deaths from coronavirus are reported in the state.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('July 7, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces that people over age 10 will be required to wear masks in seven counties: Butler County, Cuyahoga County Ohio, Franklin County, Hamilton County, Huron County, Montgomery County, and Trumbull County.'
rows_list.append(row_dict.copy())

events_df = pd.DataFrame(rows_list)