from app.models.warcraftlogs import run_query
from app.models.logs_database import Boss
from app.extensions import db

#Ids for the expansion and the encounter. 
#Want to be able to reuse code for later raids and expansions if desired.
dragonflight_id = 5
aberrus_id = 33

def populate_bosses():
    
    URL = "https://wow.zamimg.com/images/wow/icons/large/inv_achievement_raiddragon_"
    ABERRUS_BOSSES = [
        Boss.add_boss(boss_id=2688, name="Kazzara, the Hellforged", icon=f"{URL}kazzara.jpg", nickname="Kazzara"),
        Boss.add_boss(boss_id=2687, name="The Amalgamation Chamber", icon=f"{URL}amalgamationchamber.jpg"),
        Boss.add_boss(boss_id=2682, name="Assault of the Zaqali", icon=f"{URL}zaqaliassault.jpg", nickname="Assault"),
        Boss.add_boss(boss_id=2693, name="The Forgotten Experiments", icon=f"{URL}forgottenexperiments.jpg"),
        Boss.add_boss(boss_id=2680, name="Rashok, the Elder", icon=f"{URL}rashok.jpg", nickname="Rashok"),
        Boss.add_boss(boss_id=2689, name="The Vigilant Steward, Zskarn", icon=f"{URL}zskarn.jpg", nickname="Zskarn"),
        Boss.add_boss(boss_id=2683, name="'Magmorax", icon=f"{URL}magmorax.jpg"),
        Boss.add_boss(boss_id=2684, name="Echo of Neltharion", icon=f"{URL}neltharion.jpg", nickname="Neltharion"),
        Boss.add_boss(boss_id=2685, name="Scalecommander Sarkareth", icon=f"{URL}sarkareth.jpg", nickname="Sarkareth")
    ]


def query_encounters(expansion_id, zone_id):
    """Query logs API for boss info."""
    query = f'''
        query gameData {{
            worldData {{expansion(id: {expansion_id}){{
                zones {{
                    name,
                    id,
                    encounters {{
                        name, id
                    }}
                }}
            }}
        }}
    }}
    '''
    results = run_query(query)

    try:
        encounters = []
        zones = results['data']['worldData']['expansion']['zones']

        for zone in zones:
            if zone['id'] == zone_id:
                encounters.extend(zone['encounters'])

    except (KeyError) as e:
        print(f"Error accessing response data: {e}")

    return encounters


