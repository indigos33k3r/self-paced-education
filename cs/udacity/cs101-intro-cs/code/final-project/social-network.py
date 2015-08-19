# -------------------------------- #
# Intro to CS Final Project        #
# Gaming Social Network            #
# -------------------------------- #
#
# For students who have paid for the full course experience:
# please check submission instructions in the Instructor Note below.
# -----------------------------------------------------------------------------

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know
# what they are doing, having taken our web development class). However, it is
# up to you to create a data structure that manages the game-network info
# and to define several procedures that operate on the network.
#
# In a website, the data is stored in a database. In our case, however, all the
# information comes in a big string of text. Each pair of sentences in the text
# is formatted as follows:
#
# <username> is connected to <name1>, <name2>,...,<nameN>.
# <username> likes to play <game1>,...,<gameN>.
#
# Your friend records the information in that string based on user activity on
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a gamer profile. For example:
#
# John is connected to Bryant, Debra, Walter.
# John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Consider the data structures that we have used in class - lists, dictionaries
# and combinations of the two - (e.g. lists of dictionaries). Pick one which
# will allow you to manage the data above and implement the procedures below.
#
# You can assume that <username> is a unique identifier for a user. In other
# words, there is only one John in the network. Furthermore, connections aren't
# symmetric - if John is connected with Alice, it does not mean that Alice is
# connected with John.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged
# to define any additional procedures that can assist you in accomplishing
# a task. You are encouraged to test your code by using 'print' and the
# Test Run button.
# -----------------------------------------------------------------------------

example_input = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


def create_data_structure(string_input):
    """Generate a network of friends and the games they play.

    Keyword arguments:
    string_input -- a string containing games and friend data
    """
    network = {}

    if not string_input:
        return network

    sentences = string_input.split('.')

    for i in range(0, len(sentences)-1, 2):
        connections = sentences[i].split(' is connected to ')
        games = map(str.strip, sentences[i+1]
                    .split(' likes to play ')[1].split(','))
        user = connections[0]
        friends = map(str.strip, connections[1].split(','))
        network[user] = {
            'friends': friends,
            'games': games
        }

    return network


def get_connections(network, user):
    """Get a user's friends.

    Keyword arguments:
    network -- a dictionary containing users' connections and games
    user -- the name of a person in the network
    """
    try:
        return network[user]['friends']
    except KeyError:
        return None


def get_games_liked(network, user):
    """Get the list of games that a user likes.

    Keyword arguments:
    network -- a dictionary containing users' connections and games
    user -- the name of a person in the network
    """
    try:
        return network[user]['games']
    except KeyError:
        return None


def add_connection(network, user_A, user_B):
    """Add a connection between two users in the network.

    Keyword arguments:
    network -- a dictionary containing users' connections and games
    user_A -- the name of a person in the network that will be gaining a friend
    user_B -- the name of a person in the network that will be added
    """
    try:
        if user_B in network:
            if user_B not in network[user_A]['friends']:
                network[user_A]['friends'].append(user_B)
                return network
        else:
            return False
    except KeyError:
        return False


def add_new_user(network, user, games):
    """Add a user to the network.

    Keyword arguments:
    network -- a dictionary containing users' connections and games
    user -- the name of a person that will be added
    games -- the list of games that the new user likes to play
    """
    if user not in network:
        network[user] = {
            'friends': [],
            'games': games
        }
    return network


def get_secondary_connections(network, user):
    """Get the 2nd level of connections of a given user.

    Keyword arguments:
    network -- a dictionary containing users' connections and games
    user -- the name of a person in the network
    """
    try:
        return list(set([secondary for primary in network[user]['friends']
                        for secondary in network[primary]['friends']]))
    except KeyError:
        return None


def connections_in_common(network, user_A, user_B):
    """Get the shared connections of two users.

    Keyword arguments:
    network -- a dictionary containing users' connections and games
    user_A -- the name of a person in the network
    user_B -- the name of a person in the network
    """
    try:
        return len([friend for friend in network[user_A]['friends']
                    if friend in network[user_B]['friends']])
    except KeyError:
        return False


def path_to_friend(network, start, end, path=None):
    """Get a possible path from one user to another, based on their connections.

    Keyword arguments:
    network -- a dictionary containing users' connections and games
    start -- the name of a person in the network
    end -- the name of a person in the network
    path -- history (default = [])
    """
    if (start not in network) or (end not in network) or (start == end):
        return None

    if path is None:
        path = []
    path = path + [start]

    if end in network[start]['friends']:
        return path + [end]

    for node in network[start]['friends']:
        if node not in path:
            newpath = path_to_friend(network, node, end, path)
            if newpath:
                return newpath
    return None


# Make-Your-Own-Procedure (MYOP)
# -----------------------------------------------------------------------------

def top_games(network):
    """Get the top 5 most liked games among users in the network.

    Keyword arguments:
    network -- a dictionary containing users' connections and games
    """
    top_games, games = [], []
    for user in network:
        for game in network[user]['games']:
            games.append(game)
    games = sorted(games, key=games.count, reverse=True)
    for g in games:
        if g not in top_games:
            top_games.append(g)
    return top_games[:5]

# Tests
# -----------------------------------------------------------------------------

# net = create_data_structure(example_input)
# print get_connections(net, "Debra1")
# print get_connections(add_new_user(net, "Bob", []), "Bob")
# print get_connections(net, "Debra")
# print path_to_friend(net, 'John', 'Ollie')
# print add_new_user(net, "Debra", [])
# print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])
# print get_connections(net, "Mercedes")
# print get_connections(net, "John")
# print get_connections(net, "Robin")
# print add_connection(net, "John", "Freda")
# print get_secondary_connections(net, "Mercedes")
# print connections_in_common(net, "Mercedes", "John")
# print top_games(net)


net = create_data_structure('')
print net
