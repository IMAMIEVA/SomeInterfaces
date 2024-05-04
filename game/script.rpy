label start:

    scene bg

    show screen stop_all
    pause


    return

screen stop_all:
    # Так как нет других механик, которые будут ответсвенны за все остальное - мы просто запрещаем пользователю тыкать в другие места
    modal True
    button action NullAction()