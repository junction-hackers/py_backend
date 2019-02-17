# MOCK AI

## TO IMPLEMENT USEABLE AI NEXT TIME

from victim_api import get_victims, get_searchers, set_matched

def detectMatchingSearchers(victim):
    searchers = get_searchers()
    if searchers:
        data = {"searcher": searchers[0]["id"],
                "matches": [
                        {
                            "victim_id":victim,
                            "accuracy": 99
                        },
                    ]
                }
        set_matched(data)


def detectMatchingVictims(searcher):
    victims = get_victims()
    if victims:
        data = {"searcher": searcher,
                "matches": [
                        {
                            "victim_id":victim["id"],
                            "accuracy": 99
                        } for victim in victims
                    ]
                }
        set_matched(data)


