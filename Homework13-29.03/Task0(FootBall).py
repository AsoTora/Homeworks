"""Задача 0
Реализовать систему хранения информации о футбольном чемпионате. Информация опирается на следующие основные классы: Team (команда), Player (игрок), Match (матч). Эти классы связаны друг с другом посредством ассоциации.

Атрибуты классов

Team  -- Teams.txt

id — уникальный численный идентификатор.
name — имя.
players — игроки, играющие за данную команду в рамках чемпионата.

Player  -- Players.txt

id — уникальный численный идентификатор.
name — имя
team – команда.

Match -- Matches.txt

id — уникальный численный идентификатор.
date — дата.
location — место.
result — счёт.
team1 — первая команда. ## cсылка на объект команды
team2 — вторая команда.  ## вывод всех игроков команд
players – игроки, участвовавшие в матче. ## вывод только тех, что играли (или team1.players + team2.players)

Реализовать возможность сохранения записей в файл,
 а также возможность поиска информации о матчах в указанные даты 
 (предусмотреть возможность поиска по временному периоду) с выводом информации по командам и игрокам,
 участвовавшим в матчах.
"""
# украдено, но понято
import json


class Player:
    def __init__(self, id):
        """
        Вместо того, чтобы париться, перенося строку с информацией вручную в словарь, можно просто кажду линию
        загрузить через json.load_string
        """
        with open('Players') as f:
            for line in f.readlines():
                temp_dict = json.loads(line)  # временный словарь
                if temp_dict["id"] == id:
                    self.id = id
                    self.name = temp_dict["name"]
                    self.team = temp_dict["team"]
                    return  # stop
            raise NotImplementedError('check Players file')

    def __str__(self):
        return self.name


class Team:
    def __init__(self, id):
        with open('Teams') as f:
            for line in f.readlines():
                temp_dict = json.loads(line)
                if temp_dict['id'] == id:
                    self.id = id
                    self.name = temp_dict['name']
                    self.players = {}
                    for player_id in temp_dict['players']:
                        self.players[player_id] = Player(player_id)
                    return  # stop
            raise NotImplementedError('check Teams file')

    def __str__(self):
        return self.name


class Match(object):
    def __init__(self, id):
        with open('Match') as file:
            for string in file.readlines():
                temp_dict = json.loads(string)
                if temp_dict["id"] == id:
                    self.id = id
                    self.date = (temp_dict["date"])
                    self.location = temp_dict["location"]
                    self.result = temp_dict["result"]
                    self.team1 = Team(temp_dict["team1"])
                    self.team2 = Team(temp_dict["team2"])
                    return
            raise NotImplementedError('check Match file')

    @property
    def team1_players(self):
        players = str()
        for i in self.team1.players.values():
            players += str(i) + '\n' + '\t'
        return players

    @property
    def team2_players(self):
        players = str()
        for i in self.team2.players.values():
            players += str(i) + '\n' + '\t'
        return players

    def __str__(self):
        return """Match id: {}, Date: {}, Location: {}, {} vs {}, Result {}, team {} players: {},
                team {} players: {}""".format(self.id, self.date, self.location, self.team1, self.team2, self.result,
                                              self.team1, self.team1_players, self.team2, self.team2_players)

#
# class Championship:
#     def __init__(self):
#         with open('Match') as file:
#             self.matches = []
#             for string in file.readlines():
#                 dictionary = json.loads(string)
#                 self.matches.append(Match(dictionary["id"]))
#
#     def menu(self):
#         menu_str = "Press q for exit\t Press 1 for show all matches\t Press 2 for show matches in date"
#         while True:
#             print(menu_str)
#             key = input()
#             if key == 'q':
#                 break
#             elif key == '1':
#                 pass
#             elif key == '2':
#                 def date_input():
#                     while True:
#                         date = input("Please input date yy/mm/dd\n")
#                         date = date.split()
#                         if len(date) > 3:
#                             print("Error. Try again\n")
#                             continue
#                         else:
#                             return date
#
#                 def date_is_not_valid(first, second):
#                     if len(first) == 0:
#                         return True
#                     for i in range(0, len(first)):
#                         if int(first[i]) > int(second[i]):
#                             return True
#                     return False
#
#                 first_date = date_input()
#                 second_date = date_input()
#                 while date_is_not_valid(first_date, second_date):
#                     print("Error. Try again\n")
#                     first_date = date_input()
#                     second_date = date_input()
#                 for match in self.matches:
#                     for i in range(0, len(first_date)):
#                         if match.date[i] < int(first_date[i]):
#                             break
#                     else:
#                         if len(second_date) != 0:
#                             for i in range(0, len(second_date)):
#                                 if match.date[i] > int(second_date[i]):
#                                     break
#                             else:
#                                 print(match)
#                         else:
#                             print(match)
#
#
# c = Championship()
# c.menu()