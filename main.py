
import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

sd.resolution = (500, 500)
y_start, y_end = 50, 450

for color in rainbow_colors:
    start_point = sd.get_point(50, y_start)
    end_point = sd.get_point(350, y_end)
    y_start -= 5

    y_end -= 5
    sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
