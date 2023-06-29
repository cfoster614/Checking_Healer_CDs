from app.models.warcraftlogs import Spell, Query
from json import JSONDecodeError

def get_healer_cd_list():
    """Return a list of the names of healing cooldowns that we want to query"""
    healingCds = [
        
        # DRs
        "Aura Mastery",
        "Power Word: Barrier",
        "Spirit Link Totem",
        "Rallying Cry",
        "Darkness",
        "Anti-Magic Zone",
        # Druid
        "Tranquility",
        "Convoke the Spirits",
        "Flourish",
        # Shaman
        "Healing Tide Totem",
        "Ascendance",
        # Holy priest
        "Holy Word: Salvation",
        "Divine Hymn",
        # Disc priest
        "Rapture",
        "Evangelism",
        # Monk
        "Revival",
        "Invoke Yu'lon, the Jade Serpent",
        # Evoker
        "Rewind",
        "Dream Flight",
        "Emerald Communion",
        "Stasis",
        # Paladin
        "Avenging Wrath",
        "Avenging Crusader"
    ]

    return healingCds


def query_cooldowns():
    """Return a list of all the ids, icons, and names of all the healer spells in the API.
    
    Should be a list with dicts inside
    [{"id" : 2899, icon : "string", "name" : "string"},
    {"id" : 2899, icon : "string", "name" : "string"}]
    """
    healerCds = get_healer_cd_list()
    filtered_abilities = []
    page = 1
    has_more_pages = True

    while has_more_pages and len(filtered_abilities) < 200:
        query = f'''
            query gameData{{
                gameData{{
                abilities(limit: 100, page: {page}) {{
                    data {{
                        id
                        name
                        icon
                    }},
                    has_more_pages
                }}
            }}
        }}
        '''
        new_query = Query(query)
        response_data = new_query.run_query()

        try:
            abilities = response_data['data']['gameData']['abilities']['data']
            filtered_abilities.extend(
                ability for ability in abilities if ability['name'] in healerCds)
            print(abilities)
            has_more_pages = response_data['data']['gameData']['abilities']['has_more_pages']
            page += 1
        except (KeyError, JSONDecodeError) as e:
            print(f"Error accessing response data: {e}")
            break
    return filtered_abilities


def get_spell_info():
    """Return a list of all the ids, icons, and names of all the healer spells in the API.
    
    Should be a list with dicts inside
    [{"id" : 2899, "icon" : "spell_nature_tranquility.jpg", "name" : "Tranquility},
    ...rest of spells]
    
    This should be a help function that takes the query info from query_cooldowns. 
    However, currently since it took so long to get these results, I'm just putting the printed info into a list.
    """
    spells = [{'id': 740, 'name': 'Tranquility', 'icon': 'spell_nature_tranquility.jpg'},
              {'id': 8918, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 9862, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 9863, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 15259, 'name': 'Darkness', 'icon': 'spell_shadow_twilight.jpg'},
              {'id': 15307, 'name': 'Darkness', 'icon': 'spell_shadow_twilight.jpg'},
              {'id': 15308, 'name': 'Darkness', 'icon': 'spell_shadow_twilight.jpg'},
              {'id': 15309, 'name': 'Darkness', 'icon': 'spell_shadow_twilight.jpg'},
              {'id': 15310, 'name': 'Darkness', 'icon': 'spell_shadow_twilight.jpg'},
              {'id': 21791, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 25817, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 26983, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 28200, 'name': 'Ascendance',
                  'icon': 'inv_misc_gem_pearl_04.jpg'},
              {'id': 28204,
               'name': 'Ascendance',
               'icon': 'spell_lightning_lightningbolt01.jpg'},
              {'id': 31115, 'name': 'Rallying Cry',
                  'icon': 'trade_engineering.jpg'},
              {'id': 31732,
               'name': 'Rallying Cry',
               'icon': 'ability_warrior_battleshout.jpg'},
              {'id': 31821, 'name': 'Aura Mastery',
                  'icon': 'spell_holy_auramastery.jpg'},
              {'id': 31842,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_divineillumination.jpg'},
              {'id': 31884,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 34550, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 35350, 'name': 'Stasis', 'icon': 'inv_misc_pocketwatch_01.jpg'},
              {'id': 36527, 'name': 'Stasis', 'icon': 'spell_frost_frost.jpg'},
              {'id': 38659, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 43430,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 44203, 'name': 'Tranquility',
                  'icon': 'spell_nature_cyclone.jpg'},
              {'id': 44205, 'name': 'Tranquility',
                  'icon': 'spell_nature_cyclone.jpg'},
              {'id': 44206, 'name': 'Tranquility',
                  'icon': 'spell_nature_cyclone.jpg'},
              {'id': 44207, 'name': 'Tranquility',
                  'icon': 'spell_nature_cyclone.jpg'},
              {'id': 44208, 'name': 'Tranquility',
                  'icon': 'spell_nature_cyclone.jpg'},
              {'id': 45996,
               'name': 'Darkness',
               'icon': 'spell_shadow_shadesofdarkness.jpg'},
              {'id': 46268, 'name': 'Darkness',
                  'icon': 'spell_shadow_focusedpower.jpg'},
              {'id': 46269, 'name': 'Darkness',
                  'icon': 'spell_shadow_focusedpower.jpg'},
              {'id': 47535, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 47536, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 47537, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 48444, 'name': 'Tranquility',
                  'icon': 'spell_nature_cyclone.jpg'},
              {'id': 48445, 'name': 'Tranquility',
                  'icon': 'spell_nature_cyclone.jpg'},
              {'id': 48446, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 48447, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 50461,
               'name': 'Anti-Magic Zone',
               'icon': 'spell_deathknight_antimagiczone.jpg'},
              {'id': 50462,
               'name': 'Anti-Magic Zone',
               'icon': 'spell_shadow_antimagicshell.jpg'},
              {'id': 50837,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 51052,
               'name': 'Anti-Magic Zone',
               'icon': 'spell_deathknight_antimagiczone.jpg'},
              {'id': 51972, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 52893,
               'name': 'Anti-Magic Zone',
               'icon': 'spell_shadow_netherprotection.jpg'},
              {'id': 52894,
               'name': 'Anti-Magic Zone',
               'icon': 'spell_shadow_netherprotection.jpg'},
              {'id': 53636,
               'name': 'Anti-Magic Zone',
               'icon': 'spell_shadow_netherprotection.jpg'},
              {'id': 53637,
               'name': 'Anti-Magic Zone',
               'icon': 'spell_shadow_netherprotection.jpg'},
              {'id': 55113,
               'name': 'Avenging Wrath',
               'icon': 'inv_inscription_tradeskill01.jpg'},
              {'id': 57054, 'name': 'Tranquility',
                  'icon': 'spell_nature_tranquility.jpg'},
              {'id': 31842,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_divineillumination.jpg'},
              {'id': 31884,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 43430,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 47535, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 47536, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 47537, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 50837,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 55113,
               'name': 'Avenging Wrath',
               'icon': 'inv_inscription_tradeskill01.jpg'},
              {'id': 62618,
               'name': 'Power Word: Barrier',
               'icon': 'spell_holy_powerwordbarrier.jpg'},
              {'id': 63652, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 63653, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 63654, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 63655, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 63853, 'name': 'Rapture', 'icon': 'spell_holy_rapture.jpg'},
              {'id': 64843, 'name': 'Divine Hymn',
                  'icon': 'spell_holy_divinehymn.jpg'},
              {'id': 64844, 'name': 'Divine Hymn',
                  'icon': 'spell_holy_divinehymn.jpg'},
              {'id': 66011,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 70619, 'name': 'Divine Hymn',
                  'icon': 'spell_holy_divinehymn.jpg'},
              {'id': 75994, 'name': 'Flourish',
                  'icon': 'ability_druid_flourish.jpg'},
              {'id': 81661,
               'name': 'Evangelism',
               'icon': 'spell_holy_divineillumination.jpg'},
              {'id': 81662,
               'name': 'Evangelism',
               'icon': 'spell_holy_divineillumination.jpg'},
              {'id': 81782,
               'name': 'Power Word: Barrier',
               'icon': 'spell_holy_powerwordbarrier.jpg'},
              {'id': 87154, 'name': 'Evangelism',
               'icon': 'spell_holy_blessedrecovery.jpg'},
              {'id': 98007,
               'name': 'Spirit Link Totem',
               'icon': 'spell_shaman_spiritlink.jpg'},
              {'id': 98008,
               'name': 'Spirit Link Totem',
               'icon': 'spell_shaman_spiritlink.jpg'},
              {'id': 108280,
               'name': 'Healing Tide Totem',
               'icon': 'ability_shaman_healingtide.jpg'},
              {'id': 113127,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 115310, 'name': 'Revival', 'icon': 'spell_monk_revival.jpg'},
              {'id': 115725,
               'name': 'Power Word: Barrier',
               'icon': 'trade_engineering.jpg'},
              {'id': 121163,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 125562, 'name': 'Divine Hymn',
                  'icon': 'spell_holy_divinehymn.jpg'},
              {'id': 127945,
               'name': 'Healing Tide Totem',
               'icon': 'ability_shaman_healingtide.jpg'},
              {'id': 131773, 'name': 'Divine Hymn',
                  'icon': 'spell_holy_divinehymn.jpg'},
              {'id': 143474,
               'name': 'Healing Tide Totem',
               'icon': 'ability_shaman_healingtide.jpg'},
              {'id': 145558,
               'name': 'Healing Tide Totem',
               'icon': 'ability_shaman_healingtide.jpg'},
              {'id': 145637,
               'name': 'Power Word: Barrier',
               'icon': 'spell_holy_powerwordbarrier.jpg'},
              {'id': 145641,
               'name': 'Power Word: Barrier',
               'icon': 'spell_holy_powerwordbarrier.jpg'},
              {'id': 145645,
               'name': 'Power Word: Barrier',
               'icon': 'spell_holy_powerwordbarrier.jpg'},
              {'id': 146722,
               'name': 'Healing Tide Totem',
               'icon': 'spell_fire_selfdestruct.jpg'},
              {'id': 146753,
               'name': 'Healing Tide Totem',
               'icon': 'spell_fire_selfdestruct.jpg'},
              {'id': 146810,
               'name': 'Power Word: Barrier',
               'icon': 'trade_engineering.jpg'},
              {'id': 151175,
               'name': 'Spirit Link Totem',
               'icon': 'spell_shaman_spiritlink.jpg'},
              {'id': 151203,
               'name': 'Spirit Link Totem',
               'icon': 'spell_shaman_spiritlink.jpg'},
              {'id': 151211,
               'name': 'Spirit Link Totem',
               'icon': 'spell_shaman_spiritlink.jpg'},
              {'id': 158405,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 162762,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 164397,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 167917,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 173312,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 181043,
               'name': 'Avenging Wrath',
               'icon': 'spell_nature_lightningshield.jpg'},
              {'id': 184879, 'name': 'Flourish', 'icon': 'inv_misc_eye_04.jpg'},
              {'id': 185019, 'name': 'Flourish', 'icon': 'inv_misc_eye_04.jpg'},
              {'id': 185413,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 189292,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_crusaderstrike.jpg'},
              {'id': 195272,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 197721, 'name': 'Flourish',
                  'icon': 'spell_druid_wildburst.jpg'},
              {'id': 204756,
               'name': 'Power Word: Barrier',
               'icon': 'spell_holy_powerwordbarrier.jpg'},
              {'id': 204760,
               'name': 'Power Word: Barrier',
               'icon': 'spell_holy_powerwordbarrier.jpg'},
              {'id': 216331,
               'name': 'Avenging Crusader',
               'icon': 'ability_paladin_veneration.jpg'},
              {'id': 216371,
               'name': 'Avenging Crusader',
               'icon': 'spell_holy_restoration.jpg'},
              {'id': 216372,
               'name': 'Avenging Crusader',
               'icon': 'spell_holy_restoration.jpg'},
              {'id': 218346,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 220207, 'name': 'Rewind',
                  'icon': 'spell_mage_altertime_active.jpg'},
              {'id': 220214, 'name': 'Rewind',
                  'icon': 'spell_mage_altertime_active.jpg'},
              {'id': 242743,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 246287,
               'name': 'Evangelism',
               'icon': 'spell_holy_divineillumination.jpg'},
              {'id': 252856,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 254413,
               'name': 'Healing Tide Totem',
               'icon': 'ability_shaman_healingtide.jpg'},
              {'id': 262590, 'name': 'Flourish',
                  'icon': 'ability_rogue_fleetfooted.jpg'},
              {'id': 262785, 'name': 'Flourish',
                  'icon': 'ability_rogue_fleetfooted.jpg'},
              {'id': 265202,
               'name': 'Holy Word: Salvation',
               'icon': 'ability_priest_archangel.jpg'},
              {'id': 267511,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 270497, 'name': 'Healing Tide Totem',
               'icon': 'trade_engineering.jpg'},
              {'id': 281465,
               'name': 'Avenging Crusader',
               'icon': 'spell_holy_restoration.jpg'},
              {'id': 282113,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 282667, 'name': 'Divine Hymn',
                  'icon': 'trade_engineering.jpg'},
              {'id': 282668, 'name': 'Divine Hymn',
                  'icon': 'trade_engineering.jpg'},
              {'id': 292266,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 294027,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 296101, 'name': 'Rewind',
                  'icon': 'spell_azerite_essence13.jpg'},
              {'id': 297850, 'name': 'Revival', 'icon': 'spell_monk_revival.jpg'},
              {'id': 304273,
               'name': 'Spirit Link Totem',
               'icon': 'spell_shaman_spiritlink.jpg'},
              {'id': 304278,
               'name': 'Spirit Link Totem',
               'icon': 'spell_shaman_spiritlink.jpg'},
              {'id': 304281,
               'name': 'Spirit Link Totem',
               'icon': 'spell_shaman_spiritlink.jpg'},
              {'id': 317872,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 322118,
               'name': "Invoke Yu'lon, the Jade Serpent",
               'icon': 'ability_monk_dragonkick.jpg'},
              {'id': 323764,
               'name': 'Convoke the Spirits',
               'icon': 'ability_ardenweald_druid.jpg'},
              {'id': 325174,
               'name': 'Spirit Link Totem',
               'icon': 'spell_shaman_spiritlink.jpg'},
              {'id': 327979,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 331644,
               'name': "Invoke Yu'lon, the Jade Serpent",
               'icon': 'ability_monk_dragonkick.jpg'},
              {'id': 337433,
               'name': 'Convoke the Spirits',
               'icon': 'ability_ardenweald_druid.jpg'},
              {'id': 339044,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 343029,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 343205,
               'name': 'Healing Tide Totem',
               'icon': 'ability_shaman_healingtide.jpg'},
              {'id': 356722, 'name': 'Revival', 'icon': 'spell_monk_revival.jpg'},
              {'id': 358521,
               'name': "Invoke Yu'lon, the Jade Serpent",
               'icon': 'ability_monk_dragonkick.jpg'},
              {'id': 359816,
               'name': 'Dream Flight',
               'icon': 'ability_evoker_dreamflight.jpg'},
              {'id': 362361,
               'name': 'Dream Flight',
               'icon': 'ability_evoker_dreamflight.jpg'},
              {'id': 362362,
               'name': 'Dream Flight',
               'icon': 'ability_evoker_dreamflight.jpg'},
              {'id': 363502,
               'name': 'Dream Flight',
               'icon': 'ability_evoker_dreamflight.jpg'},
              {'id': 363534, 'name': 'Rewind', 'icon': 'ability_evoker_rewind.jpg'},
              {'id': 363558, 'name': 'Rewind', 'icon': 'ability_evoker_rewind.jpg'},
              {'id': 370960,
               'name': 'Emerald Communion',
               'icon': 'ability_evoker_green_01.jpg'},
              {'id': 370984,
               'name': 'Emerald Communion',
               'icon': 'ability_evoker_green_01.jpg'},
              {'id': 373628, 'name': 'Flourish',
                  'icon': 'inv_elemental_mote_fire01.jpg'},
              {'id': 384089, 'name': 'Rewind', 'icon': 'ability_evoker_rewind.jpg'},
              {'id': 384376,
               'name': 'Avenging Wrath',
               'icon': 'spell_holy_avenginewrath.jpg'},
              {'id': 391528,
               'name': 'Convoke the Spirits',
               'icon': 'ability_ardenweald_druid.jpg'},
              {'id': 394088,
               'name': 'Avenging Crusader',
               'icon': 'ability_paladin_veneration.jpg'},
              {'id': 395012, 'name': 'Rewind', 'icon': 'spell_mage_altertime.jpg'},
              {'id': 395013, 'name': 'Rewind', 'icon': 'spell_mage_altertime.jpg'},
              {'id': 407986, 'name': 'Revival', 'icon': 'inv_misc_questionmark.jpg'},
              {'id': 407991,
               'name': "Invoke Yu'lon, the Jade Serpent",
               'icon': 'inv_misc_questionmark.jpg'}]
    
    spell_list = get_names(spells)
    
    return spell_list


def get_names(list):
    """Helper function.
    
    Take the unorganized spell list and filter it so there are no repeats.
    Turn it into organized list with Spell class.
    
    [<id=740, name=Tranquility, icon=spell_nature_tranquility.jpg>,
    <id=15259, name=Darkness, icon=spell_shadow_twilight.jpg>]
    """
    
    spell_list = []
    url = "https://wow.zamimg.com/images/wow/icons/large/"
    for l in list:
        if not any(spell.name == l['name'] for spell in spell_list):
            new_spell = Spell(
            id = l['id'],
            name = l['name'],
            icon = (f"{url}{l['icon']}")
            )
            spell_list.append(new_spell)
            
        
    return spell_list



        