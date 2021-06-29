"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    valid_paragrph=[]
    for paragraph in paragraphs:
        if select(paragraph):
            valid_paragrph += [paragraph]
    if len(valid_paragrph) <= k:
        return ''
    else:
        return valid_paragrph[k]

    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph):
        paragraph = split(lower(remove_punctuation(paragraph)))
        for word in topic:
            if word in paragraph:
                return True
        return False
    return select
    # END PROBLEM 2

def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    #print(typed_words)
    reference_words = split(reference)
    #print(reference_words)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    correct = 0
    if typed == '' or reference == '':
        return 0.0
    else:
        for i in range(min(len(reference_words),len(typed_words))):
            if typed_words[i] == reference_words[i]:
                correct += 1
        return correct * 100 / len(typed_words)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.
    打字速度；五个字符作为一个单词；
    @typed 待计算的字符串
    @elapsed 完成该字符串的时间（秒）
    @return float 每分钟键入单词数"""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed)/(5*elapsed)*60
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"

    lst = []
    for i in valid_words:
        diff = diff_function(user_word, i,limit)
        if i == user_word:
            return user_word
        else:
            lst.append([diff,i])
    if min(lst,key = lambda item:item[0])[0] > limit:
        return user_word
    return min(lst,key = lambda item:item[0])[1]
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6

    if limit < 0:    #一定要变limit
        return 10000 #要不然不通过Check that the recursion stops when the limit is reached
    if start == goal:
        return 0
    elif start =='' or goal =='':
        limit -= max(len(goal),len(start))
        return max(len(goal),len(start))
    else:
        if start[0] == goal[0]:
            return shifty_shifts(start[1:],goal[1:],limit)
        else:
            return shifty_shifts(start[1:],goal[1:],limit-1)+1
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if limit < 0:
        return 10000
    if start == goal:
        return 0
    elif start == '' or goal == '':
        limit -= max(len(start),len(goal))
        return max(len(start),len(goal))
    elif start[0] == goal[0]:
        return pawssible_patches(start[1:], goal[1:], limit)
    else:
        add =  pawssible_patches(start, goal[1:], limit-1)
        remove =  pawssible_patches(start[1:], goal, limit-1)
        substitute =  pawssible_patches(start[1:], goal[1:], limit-1)

        return min(add,remove,substitute) + 1
    """
    #这个其实很好想，但后来发现考虑的太狭隘了，发现一个通不过的案例就要加一个elif
    #还是麻烦，看上面的穷举递归吧
    #assert limit > 0, "reset the limit"
    if start == goal:
        return 0
    elif start =='' or goal == '':
        return max(len(start), len(goal))

    elif start[0] == goal[0]:
        return pawssible_patches(start[1:], goal[1:], limit)

    elif len(start)== len(goal)== 1:
        return 1

    elif start[0] == goal[1]:
        return pawssible_patches(start, goal[1:], limit) +1

    elif start[1] == goal[0]:
        return pawssible_patches(start[1:], goal, limit) +1

    elif start[1] == goal[1] and start[0] != goal[0]:
        return pawssible_patches(start[1:], goal[1:], limit) +1
"""

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            count+=1
        else:
            break
    progress = count / len(prompt)
    send({'id': user_id, 'progress': progress})
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> game = time_per_word(p, ['collar', 'plush', 'blush', 'repute'])
    >>> all_words(game)
    ['collar', 'plush', 'blush', 'repute']
    >>> all_times(game)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    list = []
    for item in times_per_player:
        list += [[item[i]-item[i-1] for i in range(1, len(item))]]
    return game(words, list)

    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    lst_time = []
    for word_indice in word_indices:
        lst0 = []
        for player_indice in player_indices:
            lst0.append(time(game,player_indice,word_indice))
        lst_time.append(lst0)
    lst_player = []
    for i in lst_time:
        lst_player.append(i.index(min(i)))
    lst_final = []
    for i in player_indices :
        lst_final.append([])#创造一个空列表，里面包含了n个空列表
    for word_index in range(len(lst_player)):
        player_index = lst_player[word_index]
        lst_final[player_index] = lst_final[player_index] + [word_at(game, word_index)]
    return lst_final

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
