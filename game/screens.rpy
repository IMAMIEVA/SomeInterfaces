
screen main_menu:
    textbutton  "Тестовое задание" action Start()




screen game_overlay:

    add "gui/overlay/shadow.png"

    hbox:
        xpos 16
        ypos 5
        imagebutton idle "gui/overlay/buttons/phone%s.png"%("_notify" if notification else "") action ShowMenu("phone")
        imagebutton idle "gui/overlay/buttons/map.png" action NullAction()
        imagebutton idle "gui/overlay/buttons/bag.png" action ShowMenu("inventory")
        imagebutton idle "gui/overlay/buttons/notes.png" action ShowMenu("notes")

    frame:
        xpos 642
        add "gui/overlay/time.png" 
        text "Воскресенье" pos (36, 46) min_width 209 textalign .5 size 31
        text "День" pos (513, 46) min_width 209 textalign .5 size 31

    frame:
        xpos 1579 ypos 11
        add "gui/overlay/money.png" 
        frame:
            ypos 35
            xpos 31
            xsize 189
            
            text "$"+str(money) min_width 189 textalign 1.0 size 31 kerning -0.07

    if navigated_item:
        frame:
            pos (772, 988)
            xysize (494, 76)
            add "gui/overlay/navigated_object.png" 
            text str(navigated_item) align (0.5, 0.5) size 31 kerning -0.07


screen phone:

    tag overlay

    
    button action Return()

    use game_overlay


    timer 0.000001 action SetVariable("notification", False)

    imagebutton idle "gui/phone.png" pos (772, 167) action NullAction()

screen inventory:
    tag overlay



    button action Return()

    use game_overlay

    default current_item = None


    button:
        action NullAction()
        pos (323, 204)
        xysize (1321, 753)
        background "gui/inventory/background.png" 

        hbox:
            xmaximum 1200
            spacing 11
            box_wrap True
            box_wrap_spacing 15
            ypos 133
            xalign .5
            for i, item in enumerate(inventory[:24]):
                button:
                    xysize (124, 124)
                    add "gui/inventory/slot.png"
                    add item.image align (0.5, 0.5)
                    action [remove_item(i), SetScreenVariable("current_item", None)]
                    hovered SetScreenVariable("current_item", item)
                    unhovered SetScreenVariable("current_item", None)

            
            for i in range(24-len(inventory[:24])):
                add "gui/inventory/slot.png"

        if current_item:
            text current_item.description ypos 592 xalign .5 size 31 color "#FFF"

screen notes(note=None):

    tag overlay



    button action Return()

    use game_overlay


    button:
        action NullAction()
        pos (324, 198)
        background "gui/notes/background.png" 
        xysize (1347, 807)

        text (note.name if note else "Заметки"):
            color "000"
            size 60
            pos (599, 34)

        if note:
            imagebutton idle "gui/notes/return.png" action Show("notes") pos (109, 128)
            text note.description xalign 0.5 ypos 308 xmaximum 1032 size 31 line_spacing 6
        else:
            hbox:
                xmaximum 1200
                spacing 32
                box_wrap True
                box_wrap_spacing 47
                ypos 133
                xalign .5
                for n in notes:
                    button:
                        xysize (193, 222)
                        add "gui/notes/slots/active.png"
                        add n.image pos (19, 13)
                        text n.name ypos 161 xalign .5 size 32
                        action Show("notes", note=n)
                
                for i in range(10-len(notes)):
                    add "gui/notes/slots/innactive.png"

screen debug_screen:

    zorder 103

    default debug_on = True


    # Для дебага возможностей
    key "K_t" action SetScreenVariable("debug_on", not debug_on)
    if debug_on:
        frame:
            align (1.0, 0.5)
            background Solid("CCC")
            vbox:
                textbutton "DEBUG (T)" action SetScreenVariable("debug_on", not debug_on)

                null height 10


                vbox:
                    label "Тут типо наводятся предметы:"
                    hbox:
                        spacing 20
                        textbutton "Стул" hovered SetVariable("navigated_item", "Стул") unhovered SetVariable("navigated_item", None) action NullAction()
                        textbutton "Стол" hovered SetVariable("navigated_item", "Стол") unhovered SetVariable("navigated_item", None) action NullAction()
                        textbutton "Милфхантер" hovered SetVariable("navigated_item", "Милфхантер") unhovered SetVariable("navigated_item", None) action NullAction()

                    null height 10

                    label "Деньги:"
                    hbox:
                        spacing 20
                        textbutton "+1223" action SetVariable("money", money+1223)
                        textbutton "-1313" action SetVariable("money", max(money-1313, 0))

                    null height 10


                    textbutton "Переключить уведомление" action SetVariable("notification", not notification)

                    null height 10
                    label "Добавить предмет:"
                    hbox:
                        spacing 20
                        box_wrap True
                        xmaximum 300
                        textbutton "Вино" action Function(inventory.append, Item("Вино", item_image("vine"), "Не грузинское, но вкусное"))
                        textbutton "Трусики" action Function(inventory.append, Item("Трусики", item_image("pants"), "Главное не сорваться и не надеть на голову..."))
                        textbutton "Диск" action Function(inventory.append, Item("Диск", item_image("disk"), "Диск с Лолитой. Но мне интересны лишь сочные мамки"))
                        textbutton "Шпилька" action Function(inventory.append, Item("Шпилька", item_image("forceps"), "Не только для волос..."))
                        textbutton "Отмычка" action Function(inventory.append, Item("Отмычка", item_image("maskey"), "Необходимо для открытия замков"))
                        textbutton "Масло" action Function(inventory.append, Item("Масло", item_image("oil"), "Я люблю когда волосатые мужики обмазываются..."))
                        textbutton "Часы" action Function(inventory.append, Item("Часы", item_image("watch"), "А который час?"))
                        textbutton "Бинокль" action Function(inventory.append, Item("Бинокль", item_image("bino"), "Вам это не нужно в квартире"))


init python:
    config.overlay_screens.append("game_overlay")
    config.overlay_screens.append("debug_screen")