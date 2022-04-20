from gpiozero import Button
import os
import logging

if __name__ == '__main__':
    button = Button(21)
    logger = logging.getLogger('moonboard.reset')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    while True:
        button.wait_for_press()
        logger.info('Reset moonboard')
        os.system("sudo /home/pi/moonboard/scripts/reset.sh")
        button.wait_for_release()
        logger.info("Reset button Released")


