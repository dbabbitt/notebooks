#!/usr/bin/env python
# coding: utf-8



# Soli Deo gloria



# In[1]:



"""
Class to connect to Jira server and perform some commonly actions (e.g.: execute a JQL)
DISCLAIMER: This is sample code written by Qxf2 Services to support a blog post about analyzing JIRA data using Python
This code does not represent Qxf2 Services's coding standards.
"""
from jira import JIRA
import arrow
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from jira import JIRAError
from requests.exceptions import ConnectionError



class ConnectJira():
    """
    Python Jira Library to automate jira dashboard
    """

    def __init__(self, server, username, password, project_name, agile_rest_path=None):
        "Initializer"
        self.error = None
        try:
            if agile_rest_path is None:
                jira_options = {'server': server,'agile_rest_path':'greenhopper'}
            else:
               jira_options = {'server': server,'agile_rest_path':agile_rest_path} 
            self.jira_obj = JIRA(jira_options, basic_auth=(username, password),validate=False)
            self.project = project_name
        except JIRAError as e:
            self.error = e.status_code
        except ConnectionError as e:
            self.error = e

    # this method stays in ConnectJira
    def execute_query(self, query=None):
        "Execute a given query"
        ticket_list = None
        error = None
        try:
            ticket_list = self.jira_obj.search_issues(
                query, maxResults=False)
            while ticket_list.total > len(ticket_list):
                ticket_list_extended = self.jira_obj.search_issues(
                    query, startAt=len(ticket_list), maxResults=ticket_list.total - len(ticket_list))
                ticket_list += ticket_list_extended
        except JIRAError as e:
            error = "error_msg:%s\n error_code:%s" %(e.text, e.status_code)
        finally:
            return {'ticket_list':ticket_list,'error':error} 
            
    # this method stays in ConnectJira
    def get_ticket(self, ticket, expand_args=None):
        "Fetch a given ticket"
        # For now, we still use the JIRA API.
        # But we just need to change this one method when we switch to using a DB

        return self.jira_obj.issue(ticket, expand=expand_args)
    
    # this method stays in ConnectJira
    def get_ticket_in_json(self, ticket):
        "Fetch a given ticket in json format"
        ticket_expanded = None
        error = None
        jql = "'key'='%s'" % (ticket)
        try:
            ticket_expanded = self.jira_obj.search_issues(jql, expand='changelog',fields='comment,created,status,reporter', json_result=True)
        except JIRAError as e:
            error = "error_msg:{}\n error_code:{}".format(e.text, e.status_code)

        return {'ticket':ticket_expanded, 'error':error}

    # this method stays in ConnectJira
    def get_statuses_from_jira(self):
        " get statuses from jira work flow"
        statuses = []
        error = None
        try:
            all_status = self.jira_obj.statuses()
            for status in all_status:
                statuses.append(status.name.lower())
        except Exception as e:
            error = e

        return {'statuses':statuses, 'error':error}

    # this method stays in ConnectJira
    def get_jira_project_boards(self,jira_project):
        "Return boards for the given project"
        jira_project_boards = []
        error = None
        try:
            jira_boards = self.jira_obj.boards()
            #Get jira_boards for the given project
            for board in jira_boards:
                if jira_project in (board.location.name or board.location.key) :
                   jira_project_boards.append({'id':board.id,'name':board.name})
        except Exception as e:
            error = e
        
        return {'jira_project_boards':jira_project_boards,'error':error} 
    
    # this method stays in ConnectJira
    def get_jira_project_sprints(self,jira_project_boards):
        "Return sprints for the given boards related to project"
        jira_project_sprints = []
        error = None
        try:
            board_ids = [board['id'] for board in jira_project_boards]
            for id in board_ids:
                jira_project_sprints.append(self.jira_obj.sprints(id))    
        except Exception as e:
            error = e
    
        return {'jira_project_sprints':jira_project_sprints,'error':error}

    # this method stays in ConnectJira
    def get_sprint_ticket_list(self,sprint_id):
        "Returns ticket for the given sprint id"
        sprint_ticket_list = None
        error = None
        jql = "sprint = %s"%sprint_id
        result = self.execute_query(jql)
        sprint_ticket_list = result['ticket_list']
        error = result['error'] 

        return {'sprint_ticket_list':sprint_ticket_list,'error':error}
 
    
    # this method stays in ConnectJira
    def get_sprint_details(self, sprint_id):
        "Returns sprint details for the given sprint id"
        sprint_details = None
        error = None
        try:
            sprint_details = self.jira_obj.sprint(sprint_id)
        except Exception as e:
            error = e

        return {'sprint_details':sprint_details, 'error':error}