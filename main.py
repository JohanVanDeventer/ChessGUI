import pygame

import match_manager


if __name__ == "__main__":

    # start pygame
    pygame.init()
    pygame.font.init()
    win = pygame.display.set_mode((1200, 650))
    pygame.display.set_caption("Chess GUI")

    # start a new match between two engines
    match = match_manager.MatchManager(
        engine_1_path="engine_1/engine.exe",
        engine_2_path="engine_2/engine.exe",
        starting_time=10000,
        increment=100,
        win=win,
        does_log_final_positions=False)

    print("----------------------- Starting Match -------------------------")
    match.start_match()
    print("----------------------- Finished Match -------------------------")

    # close PyGame before quitting
    pygame.quit()
