# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:26:26 2022

@author: Kevin
"""

base_level_types = ['arcane_buffer','berserker','bloodletter','bombardier','bonebreaker','chaosweaver',
                    'consecrator','deadeye','dynamo','echoist','flameweaver','frenzied','frostweaver',
                    'gargantuan','hasted','incendiary','juggernaut','malediction','opulent','overcharged',
                    'permafrost','sentinel','soul_conduit','steel-infused','stormweaver','toxic','vampiric']

def return_components(recipe_name):
    return_list = []
    for i in recipes[recipe_name]:
        if i in base_level_types:
            return_list.append(i)
        else:
            return_list.append(return_components(i))
    return return_list

recipes = {
        "heralding_minions": ['dynamo', 'arcane_buffer'],
        "empowering_minions": ['necromancer', 'executioner', 'gargantuan'],
        "assassin": ['deadeye', 'vampiric'],
        "trickster": False,
        'necromancer': ['bombardier', 'overcharged'],
        'rejuvinating': ['gargantuan', 'vampiric'],
        'executioner': ['frenzied', 'berserker'],
        'hexer': ['chaosweaver', 'echoist'],
        'drought_bringer': ['deadeye', 'malediction'],
        'entangler': ['bloodletter', 'toxic'],
        'temporal_bubble': ['juggernaut', 'hexer', 'arcane_buffer'],
        'treant_horde': ['steel_infused', 'sentinel', 'toxic'],
        'frost_strider': ['frostweaver', 'hasted'],
        'ice_prison': ['permafrost', 'sentinel'],
        'soul_eater': ['soul_conduit', 'necromancer', 'gargantuan'],
        'flame_strider': ['flameweaver', 'hasted'],
        'corpse_detonator': ['necromancer', 'incendiary'],
        'evocationist': ['flameweaver', 'frostweaver', 'stormweaver'],
        'magma_barrier': ['incendiary', 'bonebreaker'],
        'mirror_image': ['echoist', 'soul_conduit'],
        'storm_strider': ['stormweaver', 'hasted'],
        'mana_siphoner': ['consecrator', 'dynamo'],
        'corrupter': ['bloodletter', 'chaosweaver'],
        'invulnerable': ['sentinel', 'juggernaut', 'consecrator'],
        'crystal_skinned': False,
        'empower_elements': False,
        'effigy': ['hexer', 'malediction', 'corrupter'],
        'lunaris_touched': ['invulnerable', 'frost_strider', 'empowering_minions'],
        'solaris_touched': ['invulnerable', 'magma_barrier', 'empowering_minions'],
        'araakali_touched': ['corpse_detonator', 'entangler', 'assassin'],
        'brine_king_touched': ['ice_prison', 'storm_strider', 'heralding_minions'],
        'tukohama_touched': ['bonebreaker', 'executioner', 'magma_barrier'],
        'abberath_touched': ['flame_strider', 'frenzied', 'rejuvinating'],
        'shakari_touched': ['entangler', 'soul_eater', 'drought_bringer'],
        'innocence_touched': ['lunaris_touched', 'solaris_touched', 'mirror_image', 'mana_siphoner'],
        'kitava_touched': ['tukohama_touched', 'abberath_touched', 'corrupter', 'corpse_detonator']
        }

desired_recipes = ['ice_prison']

for i in desired_recipes:
    print(f"{i}'s components :{return_components(i)}")