init python:

    def note_image(name):
        return "gui/notes/slots/characters/%s.png"%name

    def item_image(name):
        return "gui/inventory/items/%s.png"%name

    class Note:
        def __init__(self, name, image, description):
            self.name = name
            self.image = image
            self.description = description

    class Item:
        def __init__(self, name, image, description):
            self.name = name
            self.image = image
            self.description = description


    def remove_item(i):
        def remove_it():
            inventory.pop(i)
            renpy.restart_interaction()
        return remove_it



default money = 0

default navigated_item = None

default notification = False

default notes = [
    Note("Момашка", note_image("momasha"), "Сегодня мне уже ничего не светит. Следует почистить зубы и лечь спать.")
]

default inventory = [
    Item("Бинокль", item_image("bino"), "Вам это не нужно в квартире")
]


