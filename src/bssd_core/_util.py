from typing import Optional


def _to_yesno(b: bool) -> Optional[str]:
    if b is None:
        return b
    return "yes" if b else "no"


def _from_yesno(s: str):
    return s == "yes"
