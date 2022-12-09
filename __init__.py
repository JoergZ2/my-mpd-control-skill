from mycroft import MycroftSkill, intent_file_handler


class MyMpdControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.mpd.my.intent')
    def handle_control_mpd_my(self, message):
        self.speak_dialog('control.mpd.my')


def create_skill():
    return MyMpdControl()

