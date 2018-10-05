from mycroft import MycroftSkill, intent_file_handler


class Count(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('count.intent')
    def handle_count(self, message):
        try: 
            number = int(message.data.get("number"))
            response = {'number': message.data.get("number")}
            self.speak_dialog("count_start", data=response)
            for i in range(1,number+1,+1):
                self.speak(str(i))
            self.speak_dialog("count_stop")
            pass
        except:
            self.speak_dialog("count_error")

    @intent_file_handler('countdown.intent')
    def handle_countdown_intent(self, message):
        try:
            number = int(message.data.get("number"))
            response = {'number': message.data.get("number")}
            self.speak_dialog("countdown_start", data=response)
            for i in range(number,0,-1):
                self.speak(str(i))
            self.speak_dialog("countdown_stop")
            pass
        except:
            self.speak_dialog("count_error")

def create_skill():
    return Count()

