# coding: utf-8

from dext.common.utils.app_settings import app_settings

from the_tale.game.balance import constants as c

POWER_HISTORY_WEEKS = 6

places_settings = app_settings('PLACES',
                               POWER_HISTORY_WEEKS=POWER_HISTORY_WEEKS,
                               POWER_HISTORY_LENGTH=int(POWER_HISTORY_WEEKS*7*24*c.TURNS_IN_HOUR),
                               MAX_SIZE=10,
                               MAX_FRONTIER_SIZE=7,
                               MAX_DESCRIPTION_LENGTH=1000,
                               BUILDING_POSITION_RADIUS=2,
                               NEW_PLACE_LIVETIME=2*7*24*60*60,
                               MIN_SAFETY=0.05,
                               MIN_TRANSPORT=0.1,
                               MIN_STABILITY=0,

                               CHRONICLE_RECORDS_NUMBER=10,

                               API_LIST_VERSION='1.0',
                               API_SHOW_VERSION='1.0',

                               SIZE_TO_PERSONS_NUMBER={0: 2,
                                                       1: 2,
                                                       2: 3,
                                                       3: 3,
                                                       4: 3,
                                                       5: 4,
                                                       6: 4,
                                                       7: 4,
                                                       8: 5,
                                                       9: 5,
                                                       10: 6} )
