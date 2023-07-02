from app.models.warcraftlogs import Boss


def get_boss_list():
    #Get list of bosses
    #Icon info was gotten from wowhead, the warcraftlogs API didn't have it
    #I want the icon information to easily upload the pictures using wowzamimg
    beginning_url = "https://wow.zamimg.com/images/wow/icons/large/inv_achievement_raiddragon_"
    aberrus_bosses = [
        Boss(id = 2688, name = "Kazzara, the Hellforged", icon=f'{beginning_url}kazzara.jpg'),
        Boss(id = 2687, name = "The Amalgamation Chamber", icon=f'{beginning_url}amalgamationchamber.jpg'),
        Boss(id = 2693, name = "The Forgotten Experiments", icon=f'{beginning_url}forgottenexperiments.jpg'),
        Boss(id = 2682, name = "Assault of the Zaqali", icon=f'{beginning_url}zaqaliassault.jpg'),
        Boss(id = 2680, name = "Rashok, the Elder", icon=f'{beginning_url}rashok.jpg'),
        Boss(id = 2689, name = "The Vigilant Steward, Zskarn", icon=f'{beginning_url}zskarn.jpg'),
        Boss(id = 2683, name = "Magmorax", icon=f'{beginning_url}magmorax.jpg'),
        Boss(id = 2684, name = "Echo of Neltharion", icon=f'{beginning_url}neltharion.jpg'),
        Boss(id = 2685, name = "Scalecommander Sarkareth", icon=f'{beginning_url}sarkareth.jpg')
    ]
    
    return aberrus_bosses

def boss_ids(boss_list):
    boss_id_list = [l.boss_id for l in boss_list]
    return boss_id_list
        