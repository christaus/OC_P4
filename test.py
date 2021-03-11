# from json import dumps

# from tinydb import TinyDB

from simulate_matchs import simulate_match
from tournament import Tournament


def test():
    rounds_to_test = 4
    tournois = Tournament({"rounds": rounds_to_test})
    properties = [
        {
            "surname": "DUPUIS",
            "forename": "Mélanie",
            "birthday": 22,
            "sex": False,
            "rank": 1092,
        },
        {
            "surname": "DUBOIS",
            "forename": "Natasha",
            "birthday": 20,
            "sex": False,
            "rank": 1083,
        },
        {
            "surname": "MARK",
            "forename": "Henry",
            "birthday": 42,
            "sex": True,
            "rank": 2093,
        },
        {
            "surname": "MALFOY",
            "forename": "Lucie",
            "birthday": 45,
            "sex": False,
            "rank": 2099,
        },
        {
            "surname": "DUCHATEAU",
            "forename": "Edouard",
            "birthday": 57,
            "sex": True,
            "rank": 1021,
        },
        {
            "surname": "ARMAND",
            "forename": "Jacques",
            "birthday": 37,
            "sex": True,
            "rank": 2097,
        },
        {
            "surname": "LOPEZ",
            "forename": "Julia",
            "birthday": 19,
            "sex": False,
            "rank": 2000,
        },
        {
            "surname": "LYNCH",
            "forename": "David",
            "birthday": 99,
            "sex": True,
            "rank": 1999,
        },
    ]
    for _ in properties:
        tournois.add_player(_)

    # db = TinyDB("data/db.json")
    # players_table = db.table("players")
    # players_table.truncate()
    for player in tournois.players:
        print(player.surname)

        # Serialization players
        # players_table.insert(dumps(player.__dict__))

    for _ in range(tournois.rounds + 1):
        print(f"Tour numéro {_ + 1}")
        tournois.new_tour()
        tournois.stop_tour()
        simulate_match(tournois)
        print(
            f"Affichage du score {tournois.players[0].surname} {tournois.players[0].forename}"
        )
        print(f"Score: {tournois.score_player(tournois.players[0])}")


if __name__ == "__main__":
    test()
