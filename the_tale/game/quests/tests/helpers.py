# coding: utf-8

from game.prototypes import TimePrototype

from game.actions.prototypes import ActionQuestPrototype

class QuestTestsMixin(object):

    def turn_to_quest(self, storage, hero_id):

        current_time = TimePrototype.get_current_time()

        hero = storage.heroes[hero_id]

        while hero.actions.current_action.TYPE != ActionQuestPrototype.TYPE:
            storage.process_turn()
            current_time.increment_turn()

        storage.save_changed_data()

        return hero.actions.current_action.quest
