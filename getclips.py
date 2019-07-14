#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging

#import cgi
#import cgitb
#cgitb.enable()
import sys
import time
import requests
import json
debug=False

config = json.load(open('config.json'))
assert(config)
assert(len(config['client_id']) > 0)

def twitchApiRequest(client_id, path, params):
    allowed_paths = { "clips":1, "games":1, "users":1 }
    #params.pop('path', None)
    assert( allowed_paths[path] )
    url = "https://api.twitch.tv/helix/" + path
    #headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    headers = {'Client-ID': client_id}
    r = requests.get(url, headers=headers, params=params)
    return r

def getClips(client_id, args):
    #https://dev.twitch.tv/docs/api/reference/#get-clips
    params = { }
    broadcaster_id = args.pop('broadcaster_id', None)
    game_id = args.pop('game_id', None)
    id = args.pop('id', None)
    if (id):
        params['id'] = id
    if (broadcaster_id):
        params['broadcaster_id'] = broadcaster_id
    if (game_id):
        params['game_id'] = game_id
    return twitchApiRequest(client_id, 'clips', params)

#def getUsers(client_id, args):
    #https://dev.twitch.tv/docs/api/reference/#get-users
    #params = { login: args['login'] }
    #return twitchApiRequest(client_id, 'users', params)

#def getGames(client_id, args):
    #https://dev.twitch.tv/docs/api/reference/#get-games
    #params = { id: args['id'] }
    #return twitchApiRequest(client_id, 'games', params)

def handleUserRequest(client_id, args):
    path = args.pop('path')
    if (path == 'clips'):
        return getClips(client_id, args)
    #elif (path == 'users'):
        #return getUsers(client_id, args)
    #elif (path == 'games'):
        #return getGames(client_id, args)

print("Content-Type: application/json; charset=utf-8")

args = json.load(sys.stdin)
r = handleUserRequest(config['client_id'], args)

print("Status: "+str(r.status_code) )

print("")
print(r.text)
