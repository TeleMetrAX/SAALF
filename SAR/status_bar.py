import sys


bar_length = 50
fill_character = '█'
empty_character = ' '


def draw_status_bar(progress: float, maximum: float, text: str = ''):
    """
    Draws a status bar that shows progress compared to the maximum value.
    :param progress: The part already done out of the maximum possible.
    :param maximum: Maximum possible score.
    :param text: Text to display next to the status bar.
    :return: No return value.
    """
    percentage = round(100 * progress / maximum, 2)
    block_number = int(round(progress / maximum * bar_length))
    to_print = '\r|{0}| {1}/{2} ({3}%) {4}'.format(block_number * fill_character +
                                                   empty_character * (bar_length - block_number),
                                                   progress, maximum, percentage, text)
    to_print += (100-len(to_print))*' '
    sys.stdout.write(to_print)
    sys.stdout.flush()
    return
