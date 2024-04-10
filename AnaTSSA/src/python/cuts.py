from headers import *
from functions import *

def e906_data_cuts(tree: uproot.models.TTree.Model_TTree_v19, etype) -> uproot.models.TTree.Model_TTree_v19:
    
    beam_offset = GetBeamOffSet(tree, etype)
    branch = tree.keys()
    events = tree.arrays(branch)
    runID  = events.runID

    dimuon_cut_2111_v42 = (
        (np.abs(events.dx) < 0.25) &
        (np.abs(events.dy - beam_offset) < 0.22) &
        (events.dz < -5.) &
        (events.dz > -280.) &
        (np.abs(events.dpx) < 1.8) &
        (np.abs(events.dpy) < 2.0) &
        (np.abs(events.costh) < 0.5) &
        (events.dpz < 116.) &
        (events.dpz > 38.) &
        (events.dpx * events.dpx + events.dpy * events.dpy < 5.) &
        (events.dx * events.dx + (events.dy - beam_offset) * (events.dy - beam_offset) < 0.06) &
        (events.xF < 0.95) &
        (events.xF > -0.1) &
        (events.xT > 0.005) &
        (events.xT < 0.55) &
        (np.abs(events.trackSeparation) < 270.) &
        (events.chisq_dimuon < 18)
    )

    track1_cut_2111_v42 = (
        (events.chisq1_target < 15.) &
        (events.pz1_st1 > 9.) &
        (events.pz1_st1 < 75.) &
        (events.nHits1 > 13) &
        (events.x1_t * events.x1_t + (events.y1_t - beam_offset) * (events.y1_t - beam_offset) < 320.) &
        (events.x1_d * events.x1_d + (events.y1_d - beam_offset) * (events.y1_d -beam_offset) < 1100.) &
        (events.x1_d * events.x1_d + (events.y1_d - beam_offset) * (events.y1_d -beam_offset) > 16.) &
        (events.chisq1_target < 1.5 * events.chisq1_upstream) &
        (events.chisq1_target < 1.5 * events.chisq1_dump) &
        (events.z1_v < -5.) &
        (events.z1_v > -320.) &
        (events.chisq1/(events.nHits1 - 5) < 12) &
        ((events.y1_st1 - beam_offset)/(events.y1_st3 - beam_offset) < 1.) &
        (np.abs(np.abs(events.px1_st1 - events.px1_st3) - 0.416) < 0.008) &
        (np.abs(events.py1_st1 - events.py1_st3) < 0.008) &
        (np.abs(events.pz1_st1 - events.pz1_st3) < 0.08) &
        ((events.y1_st1 - beam_offset) * (events.y1_st3 - beam_offset) > 0.) &
        (np.abs(events.py1_st1) > 0.02)
    )

    track2_cut_2111_v42 = (
            (events.chisq2_target < 15.) &
            (events.pz2_st1 > 9.) &
            (events.pz2_st1 < 75.) &
            (events.nHits2 > 13) &
            (events.x2_t * events.x2_t + (events.y2_t - beam_offset) * (events.y2_t - beam_offset) < 320.) &
            (events.x2_d * events.x2_d + (events.y2_d - beam_offset) * (events.y2_d - beam_offset) < 1100.) &
            (events.x2_d * events.x2_d + (events.y2_d - beam_offset) * (events.y2_d - beam_offset) > 16.) &
            (events.chisq2_target < 1.5 * events.chisq2_upstream) &
            (events.chisq2_target < 1.5 * events.chisq2_dump) &
            (events.z2_v < -5.) &
            (events.z2_v > -320.) &
            (events.chisq2 / (events.nHits2 - 5) < 12) &
            ((events.y2_st1 - beam_offset) / (events.y2_st3 - beam_offset) < 1.) &
            (np.abs(np.abs(events.px2_st1 - events.px2_st3) - 0.416) < 0.008) &
            (np.abs(events.py2_st1 - events.py2_st3) < 0.008) &
            (np.abs(events.pz2_st1 - events.pz2_st3) < 0.08) &
            ((events.y2_st1 - beam_offset) * (events.y2_st3 - beam_offset) > 0.) &
            (np.abs(events.py2_st1) > 0.02)
    )


    tracks_cut_2111_v42 = (
        (np.abs(events.chisq1_target + events.chisq2_target - events.chisq_dimuon) < 2.) &
        ((events.y1_st3 - beam_offset) * (events.y2_st3 - beam_offset) < 0.) &
        (events.nHits1 + events.nHits2 > 29) &
        (events.nHits1St1 + events.nHits2St1 > 8) &
        (np.abs(events.x1_st1 + events.x2_st1) < 42)
    )

    occ_cut_2111_v42 = (
            (events.D1 < 400) &
            (events.D2 < 400) &
            (events.D3 < 400) &
            (events.D1 + events.D2 + events.D3 < 1000)
    )

    events_cut = events[track1_cut_2111_v42 & track2_cut_2111_v42 & dimuon_cut_2111_v42 & tracks_cut_2111_v42 & occ_cut_2111_v42]

    print("---> # of dimuons {}".format(len(events_cut)))

    return events_cut


def e906_mc_cuts(tree: uproot.models.TTree.Model_TTree_v19) -> uproot.models.TTree.Model_TTree_v19:

    branches = tree.keys()
    events = tree.arrays(branches)

    mc_cuts = (
            (events.mass > 4.5) &
            (events.xF > -0.1) &
            (events.xF < 0.95) &
            (events.x2 > 0.05) &
            (events.x2 < 0.55) &
            (np.abs(events.costh) < 0.5)
    )

    tree_cut = events[mc_cuts]

    return tree_cut