# https://leetcode.com/discuss/interview-question/373006
# Given a map Map < String, List < String >> userSongs with user names as keys 
# and a list of all the songs that the user has listened to as values.
#
# Also given a map Map < String, List < String >> songGenres, with song genre 
# as keys and a list of all the songs within that genre as values. The song 
# can only belong to only one genre.
#
# The task is to return a map Map < String, List < String >>, where the key is 
# a user name and the value is a list of the user's favorite genre(s). Favorite 
# genre is the most listened to genre. A user can have more than one favorite 
# genre if he/she has listened to the same number of songs per each of the genres.
#
# Example 1:
#     Input:
#     userSongs = {
#         "David": ["song1", "song2", "song3", "song4", "song8"],
#         "Emma":  ["song5", "song6", "song7"]
#     },
#     songGenres = {
#         "Rock":    ["song1", "song3"],
#         "Dubstep": ["song7"],
#         "Techno":  ["song2", "song4"],
#         "Pop":     ["song5", "song6"],
#         "Jazz":    ["song8", "song9"]
#     }
#     Output: {
#         "David": ["Rock", "Techno"],
#         "Emma":  ["Pop"]
#     }
#     Explanation:
#     David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
#     Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
# Example 2:
#     Input:
#     userSongs = {
#         "David": ["song1", "song2"],
#         "Emma":  ["song3", "song4"]
#     },
#     songGenres = {}
#     Output: {
#         "David": [],
#         "Emma":  []
#     }
from typing import List
class Solution:
    def getFavoriteGenres(self, userSongs, songGenres):
        userGenresTracker = {}
        userGenres = {}

        if userSongs == None or len(userSongs) == 0:
            userGenres
        if songGenres == None or len(songGenres) == 0:
            userGenres

        for user in userSongs:
            # print(user)
            genreCounter = {}
            # userGenresTracker.update({user:{}})
            for userSong in userSongs[user]:
                # print(userSong)
                for genre in songGenres:
                    if userSong in songGenres[genre]:
                        # print('found in', genre)
                        if genre in genreCounter:
                            # print("+1")
                            genreCounter[genre] += 1
                        else:
                            # print("added a new key")
                            genreCounter.update({genre: 1})
            maxGenreCount = max(genreCounter.items(), key=lambda x: x[1])[1]
            # print("maxGenreCount =", maxGenreCount)
            for genre in genreCounter:
                # print(genreCounter[genre])
                if genreCounter[genre] == maxGenreCount:
                    if user in userGenresTracker:
                        userGenresTracker[user].append(genre)
                    else:
                        userGenresTracker.update({user:[genre]})
                

        # Sort the dictionary userGenresTracker by the value so top genre is at the top
        # https: // careerkarma.com/blog/python-sort-a-dictionary-by-value/
        # print(userGenresTracker)   
        # for user in userGenresTracker:     
        #     userGenresTracker[user] = sorted(
        #         userGenresTracker[user].items(), key=lambda x: x[1], reverse=True)
        # print(userGenresTracker)

        return userGenresTracker

s = Solution()
userSongs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma":  ["song5", "song6", "song7"]
}
songGenres = {
    "Rock":    ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno":  ["song2", "song4"],
    "Pop":     ["song5", "song6"],
    "Jazz":    ["song8", "song9"]
}
solution = {
    "David": ["Rock", "Techno"],
    "Emma":  ["Pop"]
}
output = s.getFavoriteGenres(userSongs, songGenres)
# passed = None
# print("solution = %s" % solution)
# print("output = %s" % output)
print("%s | %s" % ("PASS" if (solution == output) else "FAIL", output))


