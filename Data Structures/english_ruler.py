def draw_line(tick_length, tick_label=''):
    """Draw one line with the given tick length"""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print (line)

def draw_interval(center_length):
    """Draw tick interval based on a central tick length"""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    """Draw english ruler with given number of inches, major tick length"""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

if __name__ == '__main__':

    draw_ruler(2,5)
