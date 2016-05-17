# -*- coding: utf-8 -*-
"""
Created on Fri May 13 21:30:42 2016

@author: matt
"""

def findStones(game_id, game_end, end_stone):
    import numpy as np
    import cv2
    
    img_path = '/home/matt/Documents/curling/Images/test{game_id}/test{game_id}_{game_end}_{end_stone}.jpg'.format(game_id=game_id, game_end=game_end, end_stone=end_stone)
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,15,
                                param1=50,param2=13,minRadius=5,maxRadius=10)
    
    if circles is not None:
        cnt = 0
        circles = np.round(circles[0, :]).astype("int")
        data = []
        for (x,y,r) in circles:
            data.append([x,y])
            cnt += 1
        
        data.append(cnt)
        
        return data
        
    return False
    
print(findStones(986,1,12))

import json

json_path = '/home/matt/Documents/curling/Games/test986.json'

with open(json_path) as json_data:
    data = json.load(json_data)

def getEndResult(homeData, awayData):
    if len(homeData) == 3:
        if homeData['score'] != 'X':
            if int(homeData['hammer']) == 1 and int(homeData['score']) > 0:
                return ['home_score', int(homeData['score']), 'home']
            elif int(awayData['hammer']) == 1 and int(awayData['score']) > 0:
                return ['away_score', int(awayData['score']), 'away']
            elif int(homeData['hammer']) == 0 and int(homeData['score']) > 0:
                return ['home_steal', int(homeData['score']), 'away']
            elif int(awayData['hammer']) == 0 and int(awayData['score']) > 0:
                return ['away_steal', int(awayData['score']), 'home']
            else:
                if int(homeData['hammer']) == 1:
                    return ['blank', 0, 'home']
                else:
                    return ['blank', 0, 'away']

def getHomeAwayData(game):
    data = []
    for x in ['HOME', 'AWAY']:
        data.append(game[x]['abbr'])
        data.append(game[x]['color'])
        data.append(game[x]['totalscore'])
    return data

def getShotDetail(homeData, awayData, end_number, stone_number):
    data = []
    data.append(end_stone_number['TASK'])
    data.append(stone_number['HANDLE'])
    data.append(stone_number['POINTS'])
    return data

columns = ['game_id', 'home', 'home_color','home_final_score', 'away',  'away_color', 'away_final_score', 
           'end', 'end_result', 'end_score', 'hammer', 'throwing_team', 'stone', 'Rocks_in_play',
           'Task', 'Handle', 'shot_points']
           
#for each file:
#set game_id
#getHomeAwayData(send full data)
#for each end
#getEndResult(send home 'ENDS', send away 'ENDS' )
#getShotDetail()