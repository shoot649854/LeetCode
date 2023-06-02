from collections import Counter
import pandas as pd 
import time
import operator
import random


def count_complaints_by_state1(df):
    state_comp_count = {}
    for idx, row in df.iterrows():
        state = row['State']
        if state in state_comp_count:
            state_comp_count[state] += 1
        else:
            state_comp_count[state] = 1
    return state_comp_count

def count_complaints_by_state2(df):
    df['Point'] = 1
    state_comp_count_df = df.groupby('State')['Point'].sum().reset_index()
    state_comp_count_df.set_index("State", drop=True, inplace=True)
    state_comp_count_dict = state_comp_count_df.to_dict()['Point']
    return state_comp_count_dict

def count_complaints_by_state3(df):
    state_comp_count_dict = Counter(df['State'])
    return state_comp_count_dict