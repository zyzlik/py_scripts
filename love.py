# -*- encoding: utf8 -*-

import curses


screen = curses.initscr()
screen.nodelay(1)
screen.immedok(True)
screen.keypad(True)
height, width = screen.getmaxyx()

curses.start_color()
curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.noecho()
curses.cbreak()
curses.curs_set(0)
curses.def_prog_mode()

screen.bkgd(' ', curses.color_pair(1))

wind = curses.newwin(8, 9, height // 2 - 3, width // 2 - 3)
wind.bkgd(' ', curses.color_pair(1))
wind.addstr(0, 1, '@@@ @@@')
wind.addstr(1, 0, '@@@@@@@')
wind.addstr(2, 1, '@@@@@')
wind.addstr(3, 2, '@@@')
wind.addstr(4, 3, '@')
wind.refresh()

key = screen.getch()
if key == curses.KEY_F1:
    curses.endwin()
