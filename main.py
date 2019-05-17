from flask import Flask, render_template, url_for, request, redirect
from letters import *
from computersTurn import *
from game import *

app = Flask(__name__)

# home site
@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', title='Home')

# Routing site to go to correct game mode
@app.route("/routingToGame")
def routingToGame():
    # Getting information from url
    language= request.args.get('language')
    game = request.args.get('game')
    # Making correct url to go to
    if game == "twoPlayer":
        temp = "/twoPlayer?language=" + language + "&turn=1"
    else:
        temp = "/playerVsComputer?language=" + language
    # Redirect to correct site, making turn = 1 so you start your turn
    return redirect(temp) 

# Game: Two player
@app.route("/twoPlayer", methods = ['GET','POST'])
def TwoPlayer():
    # Getting information from url
    if request.method == 'POST':
        language = request.form['language']
        randLettersString = request.form['randLettersString']
        wordList = request.form['wordList']
        scoreList = request.form['scoreList']
        score = score_of_word(wordList.replace(':', ''), language)

        turn = request.form['turn']
        # comp turn
        compWord = computers_turn(language)
        if turn == '1':
            if scoreList:
                scoreList += ':'
            scoreList += str(score)
            turn = '2'
        else:
            scoreList += ',' + str(score)
            turn = '1'
    else:
        turn = '1'
        scoreList = ''
        userWord = None
        language = request.args.get('language')
        randLettersString = request.args.get('randLetterString')

    game = "/twoPlayer"
    if scoreList.count(',') == 5:
        scores = (scoreList.split(':'))
        playerOneScore = 0
        playerTwoScore = 0
        for i in range(len(scores)):
            scores[i] = scores[i].split(',')
            playerOneScore += int(scores[i][0])
            playerTwoScore += int(scores[i][1])
        if playerOneScore >= playerTwoScore:
            winner = 'Player One'
        else:
            winner = 'Player Two'
        otherPlayer = 'Player Two'
        return render_template('gameOver.html', playerScores=str(playerOneScore)
                               , computerScore=str(playerTwoScore)
                               , winner=winner
                               , scoreList = scoreList
                               , otherPlayer = otherPlayer)

    randLetters = get_rand_letters(language)
    # random letters from tuple to string

    randLettersString = (''.join([i[0] for i in randLetters])).lower()
    return render_template('twoPlayer.html', l=randLetters,
                           url=game,
                           language=language,
                           randLettersString=randLettersString
                           , wordList=''
                           , scoreList=scoreList
                           , turn = turn)


@app.route("/playerVsComputer", methods = ['GET','POST'])
def playerVsComputer():
    # Getting information from url
    if request.method == 'POST':
        language = request.form['language']
        randLettersString = request.form['randLettersString']
        wordList = request.form['wordList']
        scoreList = request.form['scoreList']
        score = score_of_word(wordList.replace(':', ''), language)
        #setja score í scoreforuser
        if scoreList:
            scoreList += ':'
        scoreList+= str(score)
        
        #comp turn
        compWord = computers_turn(language)
        scoreList += ',' + str(compWord[1])
        compWord = compWord[0].upper()
    else:
        compWord = ''
        scoreList=''
        userWord = None
        language = request.args.get('language')
        randLettersString = request.args.get('randLetterString')
    
    game = "/playerVsComputer"
    if scoreList.count(',') == 5:
        scores = (scoreList.split(':'))
        playerScores = 0
        computerScore = 0
        for i in range(len(scores)):
            scores[i] = scores[i].split(',')
            playerScores += int(scores[i][0])
            computerScore += int(scores[i][1])
        if playerScores >= computerScore:
            winner = 'Player'
        else:   
            winner = 'The Computer'
        otherPlayer = 'The Computer'
        return render_template('gameOver.html', playerScores = str(playerScores)
                                            ,computerScore = str(computerScore)
                                            ,winner = winner
                                            ,scoreList = scoreList
                                            , otherPlayer = otherPlayer)

    randLetters = get_rand_letters(language)
    # random letters from tuple to string
    randLettersString = (''.join([i[0] for i in randLetters])).lower()
    return render_template('playerVsComputer.html', l=randLetters, 
                                            url = game,  
                                            language = language, 
                                            randLettersString = randLettersString
                                            ,wordList = ''
                                            ,scoreList = scoreList
                                            ,compWord = compWord)

@app.route("/playerVsComputerGame" , methods = ['GET','POST'])
def player_vs_computer_game():
    if request.method == 'POST':
        compWord = request.form['compWord']
        wordList = request.form['wordList']
        userWord = request.form['userWord']
        language = request.form['language']
        randLettersString = request.form['randLettersString']
        scoreList = request.form['scoreList']
    else:
        print('error')
    #TJEKKA HVORT AÐ ORÐIÐ SÉ VALDID
    word = ValidateWord(userWord, language, randLettersString)
    #EF VALID, SENDA ÞAÐ INN Í LISTA
    if word != '' and word not in wordList.split(':'):
        if wordList != '':
            wordList += ':'
        wordList += word

    lettertuples = string_to_tuple(randLettersString, language)
    return render_template('playerVsComputer.html', l=lettertuples, 
                                            url = '/playerVsComputer',  
                                            language = language, 
                                            randLettersString = randLettersString
                                            ,wordList = wordList
                                            ,scoreList = scoreList
                                            ,compWord = compWord)

@app.route("/twoPlayerGame" , methods = ['GET','POST'])
def two_player_game():
    if request.method == 'POST':
        wordList = request.form['wordList']
        userWord = request.form['userWord']
        language = request.form['language']
        turn = request.form['turn']
        randLettersString = request.form['randLettersString']
        scoreList = request.form['scoreList']
    else:
        print('error')
    #TJEKKA HVORT AÐ ORÐIÐ SÉ VALDID
    word = ValidateWord(userWord, language, randLettersString)
    #EF VALID, SENDA ÞAÐ INN Í LISTA
    if word != '' and word not in wordList.split(':'):
        if wordList != '':
            wordList += ':'
        wordList += word


    lettertuples = string_to_tuple(randLettersString, language)
    return render_template('twoPlayer.html', l=lettertuples,
                                            url = '/playerVsComputer',
                                            language = language,
                                            randLettersString = randLettersString
                                            ,wordList = wordList
                                            ,scoreList = scoreList
                                            ,turn = turn)

@app.route("/gameOver")
def gameOver():
    return render_template('gameOver.html', title='Game Over')

if __name__ == '__main__':
    app.run(debug=True)