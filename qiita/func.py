def func(a:int) -> None:
    """Just Print Function

    Args:
        a (Int): printed number
    """
    import torch

    from . import log

    print("torch.__version__ in qiita.func.func: ",torch.__version__)
    log.printf(f"Printed Number Is {torch.tensor(a)} 😄")

def makeDead() -> None:
    """Terminate Session
    """
    from subprocess import run
    run("pkill --oldest",shell=True)
