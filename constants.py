# path constants
PATH_TO_DATA_FOLDER = "data/game_xlsx"
PATH_TO_CSV_FOLDER = "data/game_csv"
PATH_TO_TRASH_FOLDER = "data/game_trash"
PATH_TO_RAW_DATA_CSV = "data/raw_data.csv"
PATH_TO_CLEANED_DATA_CSV = "data/cleaned_data.csv"

# data mapping constants
PLAY_TYPE_MAPPING = { "run": 0, "pass": 1}
HASH_MAPPING = { "r": 0, "l": 1, "m": 2 }
OFF_STR_MAPPING = { "r": 0, "l": 1, "bal": 2, "--": "--" }
PLAY_DIR_MAPPING = { "r": 0, "l": 1, "--": "--" }
RESULT_MAPPING = {
    "rush": 0, "sack": 1, "incomplete": 2, "complete": 3, "timeout": 4,
    "interception": 5, "fumble": 6, "rush, td": 7, "penalty": 8, 
    "scramble": 9, "--": "--", "td": 10
}
OFF_FORM_MAPPING = {
    "twins": {"te": 0, "wr": 4, "rb": 1},  
    "ace twins": {"te": 0, "wr": 4, "rb": 1},  
    "liz": {"te": 1, "wr": 3, "rb": 1},  
    "doubles": {"te": 0, "wr": 4, "rb": 1},  
    "twins split": {"te": 0, "wr": 4, "rb": 1},  
    "pro": {"te": 1, "wr": 2, "rb": 2},  
    "trips": {"te": 0, "wr": 4, "rb": 1},  
    "te trips wing": {"te": 1, "wr": 2, "rb": 2},  
    "trips pinch": {"te": 0, "wr": 4, "rb": 1},  
    "te trips split": {"te": 1, "wr": 3, "rb": 1},  
    "doubles wing": {"te": 0, "wr": 3, "rb": 2},  
    "twins tight wing": {"te": 1, "wr": 3, "rb": 1},  
    "double tight": {"te": 2, "wr": 2, "rb": 1},  
    "unbalanced pro": {"te": 2, "wr": 2, "rb": 1},  
    "empty": {"te": 0, "wr": 5, "rb": 0},  
    "ace": {"te": 1, "wr": 3, "rb": 1},  
    "tight double wing": {"te": 2, "wr": 2, "rb": 1},  
    "double wing split": {"te": 2, "wr": 2, "rb": 1},  
    "split": {"te": 0, "wr": 4, "rb": 1},  
    "tight pro": {"te": 2, "wr": 2, "rb": 1},  
    "empty tight": {"te": 2, "wr": 3, "rb": 0},  
    "trips tight": {"te": 1, "wr": 3, "rb": 1},  
    "double wing": {"te": 2, "wr": 2, "rb": 1},  
    "wing split": {"te": 2, "wr": 2, "rb": 1},  
    "ace wing": {"te": 1, "wr": 3, "rb": 1},  
    "trips nasty": {"te": 2, "wr": 2, "rb": 1},  
    "nasty twins": {"te": 2, "wr": 2, "rb": 1},  
    "tight wing": {"te": 2, "wr": 2, "rb": 1},  
    "doubles pinch": {"te": 0, "wr": 4, "rb": 1},  
    "right": {"te": 1, "wr": 3, "rb": 1},  
    "liz nasty": {"te": 1, "wr": 3, "rb": 1},  
    "empty wing": {"te": 1, "wr": 4, "rb": 0},  
    "empty double tight": {"te": 2, "wr": 3, "rb": 0},  
    "unbalanced wing split": {"te": 2, "wr": 2, "rb": 1},
    "double split": {"te": 0, "wr": 4, "rb": 1},
    "double tight wing": {"te": 2, "wr": 1, "rb": 2},
    "trips bunch": {"te": 0, "wr": 4, "rb": 1},
    "trips bunch wing": {"te": 0, "wr": 3, "rb": 2},
    "trips bunch split": {"te": 1, "wr": 3, "rb": 1},
    "nasty wing": {"te": 2, "wr": 2, "rb": 2},
    "rip nasty": {"te": 2, "wr": 2, "rb": 2},
    "lion": {"te": 0, "wr": 3, "rb": 2},
    "ram": {"te": 0, "wr": 3, "rb": 2},
    "rome": {"te": 0, "wr": 3, "rb": 2},
    "leo": {"te": 0, "wr": 3, "rb": 2},
    "rip": {"te": 1, "wr": 3, "rb": 1},
    "left": {"te": 1, "wr": 3, "rb": 1},
    "right": {"te": 1, "wr": 3, "rb": 1},
    "ray": {"te": 0, "wr": 4, "rb": 2},
    "ray bunch": {"te": 0, "wr": 4, "rb": 2},
    "ray pinch": {"te": 0, "wr": 4, "rb": 2},
    "lou": {"te": 0, "wr": 4, "rb": 2},
    "lou pinch": {"te": 0, "wr": 4, "rb": 2},
    "lou bunch": {"te": 0, "wr": 4, "rb": 2},
    "doubes": {"te": 0, "wr": 4, "rb": 1},
    "east": {"te": 0, "wr": 5, "rb": 0},
    "west": {"te": 0, "wr": 5, "rb": 0},
    "diesel": {"te": 0, "wr": 2, "rb": 3},
    "--": {"te": 0, "wr": 0, "rb": 0}
}
OFF_PLAY_MAPPING = {
    "counter": 0,
    "power": 1,
    "trap": 2,
    "sweep": 3,
    "wr screen": 4,
    "rb screen": 5,
    "trick play": 6,
    "zone": 7,
    "boot": 8,
    "--": "--",
    "sweep/qb run": 10,
    "pass": 11
}


# reverse mapping constants
GET_PLAY_TYPE = {
    0: "run",
    1: "pass"
}
GET_RESULT = {
    0: "rush",
    1: "sack",
    2: "incomplete",
    3: "complete",
    4: "timeout",
    5: "interception",
    6: "fumble",
    7: "rush, td",
    8: "penalty",
    9: "scramble",
    10: "td",
    "--": "--"
}
GET_PLAY_DIR = {
    0: "r",
    1: "l",
    "--": "--"
}
GET_HASH = {
    0: "r",
    1: "l",
    2: "m"
}
GET_OFF_STR = {
    0: "r",
    1: "l",
    2: "bal",
    "--": "--"
}
GET_OFF_FORM = {
    0: "te",
    1: "wr",
    2: "rb",
    "--": "--"
}
GET_OFF_PLAY = {
    0: "counter",
    1: "power",
    2: "trap",
    3: "sweep",
    4: "wr screen",
    5: "rb screen",
    6: "trick play",
    7: "zone",
    8: "boot",
    9: "--",
    10: "sweep/qb run",
    11: "pass"
}