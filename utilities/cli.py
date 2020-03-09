import argparse


def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--browser", default="chrome")
    parser.add_argument("--env", default="dev")
    parser.add_argument("--report", dest="report", action="store_true", default=False)
    parser.add_argument("--scope", dest="scope")
    args = parser.parse_args()
    return args
