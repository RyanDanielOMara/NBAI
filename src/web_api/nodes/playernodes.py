from database.tables.fields import Fields as f
from web_api.nodes.basenode import BaseNode
from web_api.parsers import cast_int, get_height, get_dob



class ShortPlayerBioNode(BaseNode):

    def __init__(self, nba_data):
        self.attrs = {
            f.player_id   : 'PERSON_ID',
            f.player_name : 'DISPLAY_FIRST_LAST',
            f.first_year  : 'FROM_YEAR',
        }

        self.parsers = {
            f.player_id  : cast_int,
            f.first_year : cast_int,
        }

        self.init_attrs(nba_data)
        return



class LongPlayerBioNode(BaseNode):

    def __init__(self, nba_data):
        self.attrs = {
            f.player_id   : 'PERSON_ID',
            f.player_name : 'DISPLAY_FIRST_LAST',
            f.first_year  : 'FROM_YEAR',
            f.last_year   : 'TO_YEAR',
            f.height      : 'HEIGHT',
            f.weight      : 'WEIGHT',
            f.dob         : 'BIRTHDATE',
            f.country     : 'COUNTRY',
            f.exp         : 'SEASON_EXP',
            f.position    : 'POSITION',
            f.jersey      : 'JERSEY',
        }

        self.parsers = {
            f.player_id   : cast_int,
            f.first_year  : cast_int,
            f.last_year   : cast_int,
            f.height      : get_height,
            f.weight      : cast_int,
            f.dob         : get_dob,
            f.exp         : cast_int,
        }

        self.init_attrs(nba_data)
        return
