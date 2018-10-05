from mycroft import MycroftSkill, intent_file_handler


class Count(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('count.intent')
    def handle_count(self, message):
        number = message.data.get('number')

        self.speak_dialog('count', data={
            'number': number
        })


def create_skill():
    return Count()

