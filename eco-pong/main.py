from bottle import route, request, static_file, run, error
import backend

backend.score_track(6,3)

schools = ['Penns Primary School', 'William Cowper Primary School', 'Warren Farm Primary School', 'Chad Vale Primary School', 'Slade Road Primary School', 'Oval Primary School', 'Twickenham Primary School']
id_list=[1,2,6,19,29,32,37]

def idToSchool(newId):
    for counter in range(len(id_list)):
        if id_list[counter] == newId:
            return schools[counter]

def idToIndex(newId):
    for counter in range(len(id_list)):
        if id_list[counter] == newId:
            return counter

@route('/')
def root():
    return static_file('School selection.html.html', root='.')

@route('/gameOver',method='GET')
def gameOver():
    #allow users to check the status of any stacks they upload
    winner = int(request.query.winner)
    loser = int(request.query.loser)
    f = open("static/chart.js")
    chartJs = f.read()
    f.close()
    newScores = backend.score_track(winner,1)
    newScores = backend.score_track(loser,0)
    chartJs = chartJs.replace("$$schoolEnergyUseage$$", str(newScores))
    chartJs = chartJs.replace("$$schoolNames$$", str(schools))
    f = open("Leaderboard.html.html")
    html = f.read()
    f.close()
    html = html.replace("$$title$$", "Leaderboard - " + str(idToSchool(int(winner))) + " won")
    html = html.replace("$$monkey_script$$", chartJs)
    return html

@route('/newGame',method='GET')
def newGame():
    #allow users to check the status of any stacks they upload
    siteID1 = request.query.siteID1
    siteID2 = request.query.siteID2
    f = open("static/pong.js")
    pongJs = f.read()
    f.close()
    f = open("Game Location.html.html")
    html = f.read()
    f.close()

    energyScores = backend.back_end([2015,1,16,15,30,00])
    player1Energy = energyScores[idToIndex(int(siteID1))]
    player2Energy = energyScores[idToIndex(int(siteID2))]

    pongJs = pongJs.replace("$$player1ID$$", siteID1)
    pongJs = pongJs.replace("$$player2ID$$", siteID2)
    pongJs = pongJs.replace("$$player1Energy$$", str(player1Energy))
    pongJs = pongJs.replace("$$player2Energy$$", str(player2Energy))
    html = html.replace("Player 1", idToSchool(int(siteID1)))
    html = html.replace("Player 2", idToSchool(int(siteID2)))
    html = html.replace("$$monkey_script$$", pongJs)
    return html

@route('/leaderboard')
def leaderboard():
    f = open("static/chart.js")
    chartJs = f.read()
    f.close()
    energyScores = backend.back_end([2015,1,16,15,30,00])
    for counter in range(len(energyScores)):
        energyScores[counter] = 100 + energyScores[counter]
    chartJs = chartJs.replace("$$schoolEnergyUseage$$", str(energyScores))
    chartJs = chartJs.replace("$$schoolNames$$", str(schools))
    f = open("Leaderboard.html.html")
    html = f.read()
    f.close()
    html = html.replace("$$title$$", "Energy Usage Leaderboard")
    html = html.replace("$$monkey_script$$", chartJs)
    return html

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__':
    run(host='localhost', port=8080)
