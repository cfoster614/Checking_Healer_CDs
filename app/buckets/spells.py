from app.models.logs_database import Spell, Boss
from app.extensions import db


URL = "https://wow.zamimg.com/images/wow/icons/large/"

def populate_spells():


    EVOKER = [  
        Spell.add_spell(spell_id=370960, name="Emerald Communion",               icon=f"{URL}ability_evoker_green_01.jpg"),
        Spell.add_spell(spell_id=363534, name="Rewind",                          icon=f"{URL}ability_evoker_rewind.jpg"),
        Spell.add_spell(spell_id=359816, name="Dreamflight",                     icon=f"{URL}ability_evoker_dreamflight.jpg"),
        Spell.add_spell(spell_id=370562, name="Stasis",                          icon=f"{URL}ability_evoker_stasis.jpg"),
        Spell.add_spell(spell_id=374227, name="Zephyr",                          icon=f"{URL}ability_evoker_hoverblack.jpg"),
        Spell.add_spell(spell_id=406732, name="Spatial Paradox",                 icon=f"{URL}ability_evoker_stretchtime.jpg")
    ]        

    DRUID = [        
        Spell.add_spell(spell_id=197721, name="Flourish",                        icon=f"{URL}spell_druid_wildburst.jpg"),
        Spell.add_spell(spell_id=740,    name="Tranquility",                     icon=f"{URL}spell_nature_tranquility.jpg"),
        Spell.add_spell(spell_id=33891,  name="Incarnation: Tree of Life",       icon=f"{URL}ability_druid_improvedtreeform.jpg")
    ]        

    DEMONHUNTER = [          
        Spell.add_spell(spell_id=196718, name="Darkness",                        icon=f"{URL}ability_demonhunter_darkness.jpg"),
    ]                
    DEATHKNIGHT = [                      
        Spell.add_spell( spell_id=51052, name="Anti-Magic Zone",                 icon=f"{URL}spell_deathknight_antimagiczone.jpg"),
    ]
    MONK = [  
        Spell.add_spell(spell_id=322118, name="Invoke Yu'lon, the Jade Serpent", icon=f"{URL}ability_monk_dragonkick.jpg"),
        Spell.add_spell(spell_id=115310, name="Revival",                         icon=f"{URL}spell_monk_revival.jpg"),
        Spell.add_spell(spell_id=325197, name="Invoke Chi-Ji, the Red Crane",    icon=f"{URL}inv_pet_cranegod.jpg"),
        Spell.add_spell(spell_id=116680, name="Thunder Focus Tea",               icon=f"{URL}ability_monk_thunderfocustea.jpg"),
        Spell.add_spell(spell_id=399491, name="Sheilun's Gift",                  icon=f"{URL}inv_staff_2h_artifactshaohao_d_01.jpg")
    ]          

    PALADIN = [             
        Spell.add_spell(spell_id=375576, name="Divine Toll",                     icon=f"{URL}ability_bastion_paladin.jpg"),
        Spell.add_spell(spell_id=31884,  name="Avenging Wrath",                  icon=f"{URL}spell_holy_avenginewrath.jpg"),
        Spell.add_spell(spell_id=6940,   name="Blessing of Sacrifice",           icon=f"{URL}spell_holy_sealofsacrifice.jpg"),
        Spell.add_spell(spell_id=200025, name="Beacon of Virtue",                icon=f"{URL}ability_paladin_beaconofinsight.jpg"),
        Spell.add_spell(spell_id=216331, name="Avenging Crusader",               icon=f"{URL}ability_paladin_veneration.jpg"),
        Spell.add_spell(spell_id=114158, name="Light's Hammer",                  icon=f"{URL}spell_paladin_lightshammer.jpg"),
        Spell.add_spell(spell_id=414170, name="Daybreak",                        icon=f"{URL}spell_holy_aspiration.jpg")
    ]

    DISC_PRIEST = [             
        Spell.add_spell(spell_id=47536, name="Rapture",                          icon=f"{URL}spell_holy_rapture.jpg"),
        Spell.add_spell(spell_id=246287,name="Evangelism",                       icon=f"{URL}spell_holy_divineillumination.jpg"),
        Spell.add_spell(spell_id=194509,name="Power Word: Radiance",             icon=f"{URL}spell_priest_power-word.jpg"),
        Spell.add_spell(spell_id=314867,name="Shadow Covenant",                  icon=f"{URL}spell_shadow_summonvoidwalker.jpg"),
        Spell.add_spell(spell_id=373178,name="Light's Wrath",                    icon=f"{URL}inv_staff_2h_artifacttome_d_01.jpg"),
        Spell.add_spell(spell_id=62618, name="Power Word: Barrier",              icon=f"{URL}spell_holy_powerwordbarrier.jpg")
    ]


    HOLY_PRIEST = [             
        Spell.add_spell(spell_id=64843, name="Divine Hymn",                      icon=f"{URL}spell_holy_divinehymn.jpg"),
        Spell.add_spell(spell_id=265202,name="Holy Word: Salvation",             icon=f"{URL}ability_priest_archangel.jpg"),
        Spell.add_spell(spell_id=200183,name="Apotheosis",                       icon=f"{URL}ability_priest_ascension.jpg"),
        Spell.add_spell(spell_id=64901, name="Symbol of Hope",                   icon=f"{URL}spell_holy_symbolofhope.jpg")
    ]

    SHAMAN = [             
        Spell.add_spell(spell_id=108280, name="Healing Tide Totem",               icon=f"{URL}ability_shaman_healingtide.jpg"),
        Spell.add_spell(spell_id=98008,  name="Spirit Link Totem",                icon=f"{URL}spell_shaman_spiritlink.jpg"),
        Spell.add_spell(spell_id=16191,  name="Mana Tide Totem",                  icon=f"{URL}spell_frost_summonwaterelemental.jpg"),
        Spell.add_spell(spell_id=207399, name="Ancestral Protection Totem",       icon=f"{URL}spell_nature_reincarnation.jpg"),
        Spell.add_spell(spell_id=198838, name="Earthen Wall Totem",               icon=f"{URL}spell_nature_stoneskintotem.jpg"),
        Spell.add_spell(spell_id=157153, name="Cloudburst Totem",                 icon=f"{URL}ability_shaman_condensationtotem.jpg")
    ]

    WARRIOR = [             
        Spell.add_spell(spell_id=97462,  name="Rallying Cry",                     icon=f"{URL}ability_warrior_rallyingcry.jpg")
    ]

