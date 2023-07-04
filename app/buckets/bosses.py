from app.models.warcraftlogs import run_query
from app.models.logs_database import Boss
from app.extensions import db

#Ids for the expansion and the encounter. 
#Want to be able to reuse code for later raids and expansions if desired.
dragonflight_id = 5
aberrus_id = 33

def get_aberrus_boss_icons():
    """
    Logs API doesn't have icon information for bosses. 
    Queried API for bosses, added my own icons.
    Use this dict for get_aberrus_boss_icons function.
    """
    beginning_url = "https://wow.zamimg.com/images/wow/icons/large/inv_achievement_raiddragon_"
    boss_dict = [{
        'name' : 'Kazzara, the Hellforged',
        'icon' : f'{beginning_url}kazzara.jpg'
    },
        { 
        'name' : 'The Amalgamation Chamber',
        'icon' : f'{beginning_url}amalgamationchamber.jpg'
    },
        {
         'name' : 'The Forgotten Experiments',
         'icon' : f'{beginning_url}forgottenexperiments.jpg'
    },
        {
         'name' : 'Assault of the Zaqali',
         'icon' : f'{beginning_url}zaqaliassault.jpg'
    },
        {
         'name' : 'Rashok, the Elder',
         'icon' : f'{beginning_url}rashok.jpg'
    },
        {
         'name' : 'The Vigilant Steward, Zskarn',
         'icon' : f'{beginning_url}zskarn.jpg'
    },
        {
         'name' : 'Magmorax',
         'icon' : f'{beginning_url}magmorax.jpg'
    },
        {
         'name' : 'Echo of Neltharion',
         'icon' : f'{beginning_url}neltharion.jpg'
    },
        {
         'name' : 'Scalecommander Sarkareth',
         'icon' : f'{beginning_url}sarkareth.jpg'
    }]
    
    return boss_dict





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


def add_bosses_to_database():
    """Add bosses to our database."""
    icons = get_aberrus_boss_icons()
    bosses = query_encounters(dragonflight_id, aberrus_id)
    for boss in bosses:
        for icon in icons:
            if icon['name'] == boss['name']:
                new_boss = Boss(
                    boss_id = boss['id'],
                    name = boss['name'],
                    icon = icon['icon']
                )
                db.session.add(new_boss)
    return db.session.commit()
    