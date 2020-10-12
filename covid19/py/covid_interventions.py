
from datetime import datetime
import pandas as pd

date_code = '%B %d, %Y'
rows_list = []

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 3, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'On March 3, when the state has no confirmed cases, Ohio Governor Mike DeWine cancels the Arnold Classic due to coronavirus concerns, a move which the Washington Post said seemed radical at the time.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 4, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'New cases prompt the partial closure of the main campus of Yeshiva University, where the man\'s son is a student, as well as the high school in the Bronx borough of New York City where the daughter is a student.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'The third case is an elementary student, resulting in recommendation from Hendricks County Health Department for closure of Hickory Elementary school for two weeks beginning March 9. This is the first school closing to occur in Indiana due to the current outbreak.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 9, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor Mike DeWine declares a state of emergency after Ohio reports its first cases of COVID-19.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Iowa'
row_dict['event_description'] = 'Governor Reynolds signs a Proclamation of Disaster Emergency.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Missouri'
row_dict['event_description'] = 'St. Louis County Executive Dr. Sam Page reports that the father and younger sister of the state\'s first coronavirus patient violated a self-quarantine order, attending a father-daughter function for her high school, Villa Duchesne, at the Ritz-Carlton Hotel in Clayton. The pair also attended a party for students from both Villa and the John Burroughs School before heading to the hotel. Villa cancels classes following the announcement, and the Burroughs students in attendance at the party were asked to stay home from school until further notice; they are ultimately cleared by medical professionals in consultation with the school later the same week, and the Ritz-Carlton was to undergo substantial cleaning.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 8, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The Ohio State University suspends face-to-face instruction until March 30. Governor DeWine declares a state of emergency.'
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
row_dict['event_description'] = 'Governor Tim Walz signs a $21 million bill for funding COVID-19 preparedness.'
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
row_dict['event_description'] = 'The University of Notre Dame announce that in-person classes will be suspended and moved online until at least April 13.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Maine'
row_dict['event_description'] = 'The University of Maine in Orono announce that in-person classes will be cancelled for the remainder of the semester beginning March 23, and that all classes will be transitioned to online only. In addition, all students living on campus were required to be moved out by March 22.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'The University of Minnesota announces that all in-person classes will be suspended until at least April 1 following spring break. The Mayo Clinic in Rochester began "drive-through testing" for the virus, though patients still needed to be approved to be tested by telephone screening.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Missouri'
row_dict['event_description'] = 'Washington University in Saint Louis announces a switch to online classes until at least late April and asked undergraduates to go home by March 15. University of Missouri\'s Columbia campus cancels classes March 12 and 13 and directs that in-person classes should be taught by other means for March 16 through 20 (prior to the March 21 through 29 spring recess).'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 11, 2020', date_code)
row_dict['state_name'] = 'Oklahoma'
row_dict['event_description'] = 'NBA player Rudy Gobert tested positive for COVID-19 prior to the game between the Utah Jazz and the Oklahoma City Thunder at Chesapeake Energy Arena in Oklahoma City. The game was postponed and the NBA announced that the 2019–20 NBA season would be suspended.'
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
row_dict['state_name'] = 'Colorado'
row_dict['event_description'] = 'The first school districts in the state, including Denver Public Schools, announced closures. The Colorado Department of Corrections suspended in-person visitation in state prisons.'
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
row_dict['event_description'] = 'Governor Holcomb Announces New Steps to Protect Public.'
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
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'Georgia'
row_dict['event_description'] = 'Governor Brian Kemp declared a public health emergency in the state of Georgia.'
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
row_dict['event_description'] = 'St. Louis County declares a state of emergency and bans gatherings larger than 250 people.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'New Hampshire'
row_dict['event_description'] = 'Governor Christopher Sununu declares a state of emergency in New Hampshire due to Covid-19.'
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
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Governor Henry McMaster declares a state of emergency and closes schools in Kershaw and Lancaster Counties for 14 days due to evidence of the virus\'s spreading in these counties.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 13, 2020', date_code)
row_dict['state_name'] = 'South Dakota'
row_dict['event_description'] = 'Governor Kristi Noem declares a state of emergency, all schools to close between March 16–20.'
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
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'Governor Walz closes all schools from March 18 until at least March 27. During the shutdown meals and mental health services will still be provided to students in need. Under the governor\'s order, schools will remain open for the elementary-aged children of health care workers and other emergency workers. Teachers will be using this time to plan for a possibility of weeks of long-distance learning.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'New Hampshire'
row_dict['event_description'] = 'Governor Sununu orders all public K–12 schools to transition to remote learning effective Monday, March 16 through April 3, 2020, requiring remote learning to begin by March 23, 2020.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'Mecklenburg County which encompassed the city of Charlotte declared a state of emergency in the county.'
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
row_dict['event_description'] = 'Governor McMaster announces school closures starting on March 16. The city of Myrtle Beach declares a state of emergency and closes city facilities that are normally open to the public, including the city library and recreation centers.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 15, 2020', date_code)
row_dict['state_name'] = 'Colorado'
row_dict['event_description'] = 'Mayor Hancock of Denver orders all bars and restaurants to close by 8:00 am starting March 17 (excepting food delivery and pickup) and also bans gatherings of more than 50 people in the city. Governor Polis expanded the closures by ordering a state-wide closure of dine-in services. Polis also ordered the closure of gyms, casinos, and theaters.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 16, 2020', date_code)
row_dict['state_name'] = 'District of Columbia'
row_dict['event_description'] = 'The Supreme Court of the United States postponed oral arguments scheduled for late March and April 1. Similar precautions were taken in 1918 in response to the Spanish flu and in 1798 and 1793 in response to Yellow fever outbreaks.'
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
row_dict['event_description'] = 'Bowling alleys, fitness centers, gyms, movie theaters, public recreation centers, trampoline parks, and water parks are ordered to be shut and gatherings of more than 50 people are banned. Governor DeWine announces the presidential primary elections, scheduled for the next day, will be cancelled on orders of Department of Health director Amy Acton.'
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
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Alaska'
row_dict['event_description'] = 'Alaska government banned dine-in food service.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'California'
row_dict['event_description'] = 'Beginning at 12:01 am on Tuesday, March 17, San Francisco, Marin, Santa Clara, Santa Cruz, San Mateo, Contra Costa, and Alameda Counties (combined population seven million) are placed under a mandatory "shelter in place" order.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Florida'
row_dict['event_description'] = 'The governor also orders businesses that sell liquor to reduce their occupancy by half, and to limit parties on beaches to only ten people per group.'
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
row_dict['event_description'] = 'The state announces it had conducted 1,100 tests.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine orders elective surgeries be postponed.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'All liquor stores closed indefinitely.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 17, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Governor McMaster issues an executive order requiring the mandatory shutdown of dine-in service in restaurants and bars and prevented a gathering of more than 50 people.'
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
row_dict['event_description'] = 'Governor Northam announces a ban on gatherings of more than 10 people.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Florida'
row_dict['event_description'] = 'The Clearwater City Council voted to close down Clearwater Beach for two weeks, starting March 23 at 6 a.m.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 18, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'Governor Walz criticizes the federal response to the virus. The state had approximately 1700 frozen samples to be tested, but had not yet been, due to the lack of facilities for testing. The state had 77 positive results out of at least 2762 tests.'
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
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'ProPublica reveals that Senator Richard Burr (R-NC) allegedly used his position as chairman of the Senate Intelligence Committee to mislead the public about COVID-19. He personally made between $582,029 and $1.56 million by selling off stock days before the market crashed. Police in Guilford County, North Carolina stopped a truck with nine tons of stolen toilet paper.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine signs state active duty proclamation that will activate 300 personnel from the Ohio National Guard to help with humanitarian efforts.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'Pennsylvania'
row_dict['event_description'] = 'The state\'s department of education announces that all statewide assessments will be canceled for the remainder of the 2019–2020 school year. Governor Wolf ordered a statewide shutdown of "non-life sustaining businesses" by 8:00 p.m. Enforcement of this order is planned to begin at 12:01 a.m. Saturday, March 21.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'South Carolina'
row_dict['event_description'] = 'Governor McMaster issues a new executive order: all non-essential state employees stay home. Public universities are also encouraged to finish the semester online.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 19, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'Virginia officials are requesting law enforcement to avoid arrests while possible. The administration also asks magistrates and judges to consider alternatives to incarceration.'
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
row_dict['event_description'] = 'Governor Cuomo issues a state-wide order that all non-essential workers must stay at home.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'North Carolina'
row_dict['event_description'] = 'The state activates North Carolina National Guard to assist in logistics and transportation of medical supplies.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces that senior centers and senior daycare centers will close.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'Texas'
row_dict['event_description'] = 'Dallas mega-church preacher Robert Jeffress agrees to move his Sunday services online.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 20, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'Governor Northam activated Virginia National Guard.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'Florida'
row_dict['event_description'] = 'Governor DeSantis is considering a new strategy to put positive COVID-19 patients into isolation shelters such as abandoned convention centers and hotels instead of returning the patients to their home where they can infect their own family.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 21, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Facilities providing daycare and assistance for adults with developmental disabilities are closed unless they serve 10 people or less.'
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
row_dict['event_description'] = 'Mecklenburg County announced that they will cover one week cost of people staying in hotels and motels to keep the tenants from being evicted.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 22, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The Ohio Department of Health issues a stay at home order. All non-essential businesses are ordered closed until April 6, 2020.'
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
row_dict['event_description'] = 'Governor Justice urges West Virginians to stay home as much as possible.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 22, 2020', date_code)
row_dict['state_name'] = 'Virginia'
row_dict['event_description'] = 'Governor Northam announces that Virginia Schools are closed for the remainder of the 2019–2020 school year.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 23, 2020', date_code)
row_dict['state_name'] = 'Michigan'
row_dict['event_description'] = 'Governor Whitmer issued a stay-at-home order to go into effect at midnight on March 24 and last until April 13.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 23, 2020', date_code)
row_dict['state_name'] = 'Minnesota'
row_dict['event_description'] = 'The governor made several announcements regarding the state\'s response to the virus: a small business loan program would be made available for possibly 5000 businesses during the week for amounts between $2,500 and $35,000, all elective veterinary surgeries would be halted and that he would be revising the budget for the response to the virus asking for an additional $365 million. The governor had also quarantined himself after a member of his security team tested positive for the virus.'
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
row_dict['state_name'] = 'Rhode Island'
row_dict['event_description'] = 'Governor Gina Raimondo claims that "many, many" have recovered.'
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
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'The Ohio General Assembly passes House Bill 197, which does many things, such as extending primary voting to April 28 and banning water utilities from disconnecting service.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 26, 2020', date_code)
row_dict['state_name'] = 'New York'
row_dict['event_description'] = 'President Trump announces that USNS Comfort will be heading up to New York City to assist local hospitals. The ship is scheduled to depart on March 28 and scheduled to arrive in New York City on March 30. Governor Cuomo announces the state will allow two patients to share one ventilator.'
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
row_dict['event_description'] = 'Governor DeWine asks the FDA to issue an emergency waiver for the use of new technology that can sterilize face masks.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 30, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine extends the closure of schools to May 1.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 31, 2020', date_code)
row_dict['state_name'] = 'Georgia'
row_dict['event_description'] = 'Governor Brian Kemp suspends in class instruction for all Georgia public schools for the remainder of the 2019–2020 school year. Students will continue their education through online formats.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('March 31, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces an order requiring that organizations with ventilators or similar devices report them to the state. President Trump approves the state\'s Disaster Declaration.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 1, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announced during his daily press conference that there is a new method to divide the state into hospital capacity regions.'
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
row_dict['event_description'] = 'Governor Dewine extends the state\'s stay at home order through May 1 with new restrictions: campgrounds must close, all retail businesses must post signs limiting how many people are allowed in at one time, and wedding receptions are limited to 10 people. The order also establishes a state board to evaluate what is and is not an essential business.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 3, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'Governor Eric Holcomb announces a two-week extension of Indiana\'s stay-at-home order. The new order will run through April 20.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 4, 2020', date_code)
row_dict['state_name'] = 'Alabama'
row_dict['event_description'] = 'Governor Kay Ivey announces a stay-at-home order through April 30. Attorney General Steve Marshall said the order can be enforced criminally, but he said he hopes it will not come to that. Disobeying the order is a Class C misdemeanor that can carry a $500 penalty.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 4, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine signs an executive order removing training requirements for mental health and marriage counselors to make telehealth visits more easily accessible.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 6, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine names six facilities that will be converted into health care facilities if necessary.'
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
row_dict['event_description'] = 'Apple CEO Tim Cook donates 100,000 N95 masks to Ohio health care workers.'
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
row_dict['event_description'] = 'During Governor DeWine\'s daily press conference, about 75 people gather outside to protest the state\'s restrictions.'
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
row_dict['event_date'] = datetime.strptime('April 13, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Nursing homes are now required to inform families of cases within 24 hours. Liquor sales are now limited to state residents only in the counties of Ashtabula, Trumbull, Mahoning, Columbiana, Jefferson, and Belmont. Protesters again gathered outside the statehouse during Governor DeWine\'s press conference.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('April 14, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Governor DeWine announces that his administration is seeking a Medicaid waiver from the federal government to remove certain healthcare restrictions. A hundred people protest outside the Statehouse during his press conference.'
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
row_dict['event_description'] = 'Governor DeWine announces that he will work closely with the Governors of Illinois, Indiana, Kentucky, Michigan, Minnesota, and Wisconsin to reopen the region\'s economy in a coordinated way.'
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
row_dict['event_description'] = 'Governor Kemp announced on April 20 that many businesses could reopen on April 24, including "gyms, hair salons, bowling alleys and tattoo parlors", with restaurants and movie theaters allowed to reopen on April 27. This move has brought widespread condemnation from inside and outside Georgia, with Atlanta Mayor Keisha Lance Bottoms saying she will "continue to ask Atlantans to please stay at home" and Stacy Abrams, the 2018 Democratic candidate for governor, calling reopening "dangerously incompetent. The Institute for Health Metrics and Evaluation\'s April 21 prediction lists the earliest safe date for Georgia to shift from social distancing measures as June 19.'
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
row_dict['event_description'] = 'Governor DeWine announces in his press conference that he will extend the stay-at-home order, though he does not give a specific date. The Ohio Department of Health\'s website says the extension will last until May 29.'
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
row_dict['event_description'] = 'Protests at the statehouse continued.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 4, 2020', date_code)
row_dict['state_name'] = 'Indiana'
row_dict['event_description'] = 'The state begins stage 2 of its "back on track", with many different businesses including retail and malls opening at 50% capacity. Restaurants will be able to open next week.'
rows_list.append(row_dict.copy())

row_dict = {}
row_dict['event_date'] = datetime.strptime('May 4, 2020', date_code)
row_dict['state_name'] = 'Ohio'
row_dict['event_description'] = 'Manufacturing, distribution, and construction open up. General offices may also reopen, though employees are to work from home when possible.'
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
row_dict['event_description'] = 'Malls and retail stores are allowed to re-open to the public, though there are restrictions placed on customers.'
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
row_dict['event_description'] = 'Outdoor dining at restaurants resumes. Personal services such as salons, spas, massage therapy, tattoo services, and piercing services re-open.'
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
row_dict['event_description'] = 'Governor DeWine announces that congregate care unified response teams will begin testing in nursing homes this week. BMVs re-open.'
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

interventions_df = pd.DataFrame(rows_list)