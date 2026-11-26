import pathlib


def get_root():
    loger_script = pathlib.Path(__file__).resolve()
    project_root = next(p for p in loger_script.parents if p.name == "Flight_tracker")
    return project_root


#     loger_script = pathlib.Path(__file__).resolve()
#     project_root = next(p for p in loger_script.parents if p.name == "Fitness-check")
#     return project_root
