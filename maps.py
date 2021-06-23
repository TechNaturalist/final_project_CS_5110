from player_agent import PlayerAgent
from guard_agent import GuardAgent


class Map1:
    size = 20
    walls = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (14, 4),
             (15, 4), (16, 4), (4, 5), (8, 5), (16, 5), (4, 6), (8, 6), (16, 6), (4, 7), (8, 7), (16, 7), (4, 8),
             (8, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (12, 9), (12, 10), (12, 11), (0, 12), (1, 12),
             (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (12, 12), (13, 12), (14, 12), (15, 12),
             (16, 12), (17, 12), (18, 12), (19, 12), (4, 13), (4, 14), (4, 15), (4, 16), (8, 16), (9, 16), (10, 16),
             (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16), (8, 17), (8, 18), (8, 19)]
    guards = [GuardAgent((1, 6)), GuardAgent((14, 10)), GuardAgent((1, 14))]
    player = PlayerAgent((10, 18))
    door = (0, 1)


class Map2:
    size = 20
    walls = [(16, 0), (16, 1), (16, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3),
             (12, 3), (16, 3), (3, 4), (12, 4), (16, 4), (3, 5), (12, 5), (16, 5), (3, 6), (12, 6), (16, 6), (3, 7),
             (7, 7), (8, 7), (12, 7), (16, 7), (7, 8), (8, 8), (12, 8), (16, 8), (7, 9), (8, 9), (12, 9), (16, 9),
             (7, 10), (8, 10), (12, 10), (16, 10), (3, 11), (7, 11), (8, 11), (12, 11), (16, 11), (3, 12), (7, 12),
             (8, 12), (12, 12), (16, 12), (3, 13), (7, 13), (8, 13), (12, 13), (16, 13), (3, 14), (7, 14), (8, 14),
             (12, 14), (16, 14), (3, 15), (7, 15), (8, 15), (12, 15), (16, 15), (3, 16), (4, 16), (5, 16), (6, 16),
             (7, 16), (8, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16), (3, 17), (3, 18), (3, 19)]
    guards = [GuardAgent((14, 1)), GuardAgent((5, 5)), GuardAgent((1, 17))]
    player = PlayerAgent((18, 1))
    door = (1, 19)


class Map3:
    size = 20
    walls = [(4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3),
             (16, 3), (4, 4), (16, 4), (4, 5), (4, 6), (4, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (4, 8),
             (8, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (4, 9), (8, 9), (16, 9), (4, 10), (8, 10), (16, 10),
             (4, 11), (8, 11), (16, 11), (4, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12), (16, 12), (4, 13),
             (12, 13), (16, 13), (4, 14), (12, 14), (16, 14), (4, 15), (12, 15), (16, 15), (0, 16), (1, 16), (2, 16),
             (3, 16), (4, 16), (5, 16), (6, 16), (7, 16), (8, 16), (12, 16), (16, 16), (16, 17), (16, 18), (16, 19)]
    guards = [GuardAgent((1, 1)), GuardAgent((1, 18)), GuardAgent((18, 18))]
    player = PlayerAgent((10, 8))
    door = (0, 14)


class Map4:
    size = 20
    walls = [(6, 0), (7, 0), (13, 0), (17, 0), (5, 1), (17, 1), (2, 2), (9, 2), (4, 3), (14, 3), (16, 3), (2, 4),
             (6, 4), (12, 4), (2, 5), (7, 5), (8, 5), (0, 6), (10, 6), (11, 6), (14, 6), (18, 6), (3, 7), (4, 7),
             (6, 7), (13, 7), (15, 8), (16, 8), (0, 9), (1, 9), (3, 9), (4, 9), (9, 9), (14, 9), (17, 9), (6, 10),
             (8, 10), (19, 10), (0, 11), (1, 11), (4, 11), (5, 11), (8, 11), (11, 11), (12, 11), (12, 12), (13, 12),
             (17, 12), (19, 12), (5, 13), (10, 13), (16, 13), (3, 14), (7, 14), (11, 14), (14, 14), (15, 14), (2, 15),
             (3, 15), (7, 15), (0, 16), (2, 16), (3, 16), (5, 17), (9, 17), (12, 17), (15, 17), (0, 18), (7, 18),
             (17, 18), (11, 19), (19, 19)]
    guards = [GuardAgent((5, 5)), GuardAgent((17, 7)), GuardAgent((10, 17))]
    player = PlayerAgent((0, 17))
    door = (15, 0)


class Map5:
    size = 20
    walls = [(10, 0), (18, 0), (1, 1), (10, 1), (14, 1), (17, 1), (18, 1), (4, 2), (7, 2), (10, 2), (12, 2), (14, 2),
             (17, 2), (18, 2), (0, 3), (1, 3), (2, 3), (7, 3), (12, 3), (14, 3), (18, 3), (6, 4), (7, 4), (14, 4),
             (16, 4), (1, 5), (3, 5), (7, 5), (9, 5), (18, 5), (19, 5), (1, 6), (2, 6), (3, 6), (7, 6), (8, 6),
             (9, 6), (12, 6), (16, 6), (18, 6), (19, 6), (9, 7), (11, 7), (14, 7), (15, 7), (0, 8), (1, 8), (2, 8),
             (3, 8), (8, 8), (9, 8), (0, 9), (2, 9), (3, 9), (6, 9), (12, 9), (13, 9), (18, 9), (6, 10), (7, 10),
             (8, 10), (10, 10), (11, 10), (12, 10), (13, 10), (16, 10), (2, 11), (5, 11), (13, 11), (0, 12), (2, 12),
             (3, 12), (9, 12), (15, 12), (16, 12), (0, 13), (2, 13), (6, 13), (7, 13), (8, 13), (9, 13), (11, 13),
             (12, 13), (19, 13), (0, 14), (1, 14), (2, 14), (6, 14), (11, 14), (14, 14), (6, 15), (14, 15), (19, 15),
             (1, 16), (2, 16), (3, 16), (5, 16), (6, 16), (8, 16), (10, 16), (11, 16), (12, 16), (13, 16), (14, 16),
             (16, 16), (19, 16), (3, 17), (5, 17), (6, 17), (7, 17), (8, 17), (10, 17), (11, 17), (12, 17), (13, 17),
             (16, 17), (1, 18), (10, 18), (16, 18), (1, 19), (4, 19), (16, 19)]
    guards = [GuardAgent((0, 0)), GuardAgent((10, 9)), GuardAgent((19, 19))]
    player = PlayerAgent((19, 0))
    door = (0, 19)
