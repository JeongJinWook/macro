import pywinmacro as pw
import time

location = (174, 271)


def lunch():
    pw.click(location)
    pw.key_press_once('tab')
    pw.type_in('여의도 점심 맛집')
    time.sleep(0.1)
    pw.key_press_once('enter')
    time.sleep(3)
    pw.alt_f4()


lunch()



