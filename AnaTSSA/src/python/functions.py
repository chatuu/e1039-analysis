from headers import *

def GetBeamOffSet(tree, etype):
    """
    This function returns appropriate beam offsets for different event types.

    Args:
        tree (Tree): uproot Tree
        etype (str): event type: {Data, Mix, Jpsi, DY, PsiPrime}

    Returns:
        numpy array: beam offsets
    """

    branch = tree.keys()
    events = tree.arrays(branch)
    runID  = events.runID

    match etype:
        case "data":
            offsets = np.array([0.4 if 8912 <= x <= 10912 else (1.6 if 11075 <= x <= 16076 else 1.6) for x in runID])

        case "jpsi":
            offsets = np.array([1.598 for x in runID])

        case "dy":
            offsets = np.array([1.6 for x in runID])

        case "psip":
            offsets = np.array([1.6 for x in runID])

        case "mix":
            offsets = np.array([1.6 for x in runID])

    return offsets
