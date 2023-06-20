import sys
import pygame

import match_manager


if __name__ == "__main__":

    # start pygame
    pygame.init()
    pygame.font.init()
    win = pygame.display.set_mode((1200, 650))
    pygame.display.set_caption("Chess GUI")

    # set the engine paths
    engine_1_path = "engine_1/engine.exe"
    engine_2_path = "engine_2/engine.exe"

    # set other variables
    does_log_final_positions = False
    match_terminated = False

    # set the time controls (starting time, increment)
    time_controls = [(10000, 100), (30000, 300)]

    # start a match for each time control
    for time_control in time_controls:
        if not match_terminated:
            sys.stdout.write("<< INFO >> ********************* Starting New Time Control *********************\n")
            starting_time, increment = time_control

            match = match_manager.MatchManager(
                engine_1_path=engine_1_path,
                engine_2_path=engine_2_path,
                starting_time=starting_time,
                increment=increment,
                win=win,
                does_log_final_positions=does_log_final_positions)

            match_terminated = match.start_match()

    # close PyGame before quitting
    pygame.quit()
