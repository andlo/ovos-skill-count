from mycroft import MycroftSkill, intent_file_handler


class Count(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('count.intent')
    def handle_count(self, message):
        number = int(message.data.get("number"))
        response = {'number': message.data.get("number")}
        self.speak_dialog("count_start", data=response)
        for i in range(number-1,0,+1):
            self.speak(str(i))
        self.speak_dialog("count_stop")

    @intent_file_handler('countdown.intent')
    def handle_countdown_intent(self, message):
        number = int(message.data.get("number"))
        response = {'number': message.data.get("number")}
        self.speak_dialog("countdown_start", data=response)
        for i in range(number-1,0,-1):
            self.speak(str(i))
        self.speak_dialog("countdown_stop")

def create_skill():
    return Count()

