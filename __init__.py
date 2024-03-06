"""
skill count
Copyright (C) 2018  Andreas Lorensen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from lingua_franca.parse import extract_number
from ovos_workshop.decorators import intent_handler
from ovos_workshop.skills import OVOSSkill


class Count(OVOSSkill):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counting = False

    @intent_handler('count.intent')
    def handle_count(self, message):
        self.counting = True
        try:
            number = int(extract_number(message.data.get("number")))
            response = {'number': message.data.get("number")}
            self.speak_dialog("count_start", data=response)
            for i in range(1, number + 1, +1):
                if not self.counting:
                    break
                self.speak(str(i) + " .", wait=True)
            if self.counting:
                self.speak_dialog("count_stop")
        except:
            self.speak_dialog("count_error")

    @intent_handler('countdown.intent')
    def handle_countdown_intent(self, message):
        self.counting = True
        try:
            number = int(extract_number(message.data.get("number")))
            response = {'number': message.data.get("number")}
            self.speak_dialog("countdown_start", data=response)
            for i in range(number, 0, -1):
                if not self.counting:
                    break
                self.speak(str(i) + " .", wait=True)
            if self.counting:
                self.speak_dialog("countdown_stop")
        except:
            self.speak_dialog("count_error")
        self.counting = False

    def stop(self):
        if self.counting:
            self.counting = False
            return True
        return False
