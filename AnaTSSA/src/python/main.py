from headers import *
from cuts import *


def GetMassArray(tree):
    """
    This function returns numpy array extracted from tree

    Args:
        tree (tree): uproot tree

    Returns:
        numpy array: mass array
    """
    return tree.mass.to_numpy()
    

def main():
    """
    This is the main function.
    """
    datafile = "../../ROOTFiles/roadset57_70_R008_2111v42_tmp_noPhys.root:Tree"
    jpsifile = "../../ROOTFiles/mc_jpsi_LH2_M027_S001_messy_occ_pTxFweight_v2.root:Tree"
    psipfile = "../../ROOTFiles/mc_psiprime_LH2_M027_S001_messy_occ_pTxFweight_v2.root:Tree"
    dyfile   = "../../ROOTFiles/mc_drellyan_LH2_M027_S001_messy_occ_pTxFweight_v2.root:Tree"

    with uproot.open(datafile) as data:
        datatree = e906_data_cuts(data, "data")
        
        with uproot.open(jpsifile) as jpsi:
            jpsitree = e906_data_cuts(jpsi, "jpsi")

            with uproot.open(dyfile) as dy:
                dytree = e906_data_cuts(dy, "dy")

                with uproot.open(psipfile) as psip:
                    psiptree = e906_data_cuts(psip, "psip")

                    dataMassArray = GetMassArray(datatree)
                    jpsiMassArray = GetMassArray(jpsitree)
                    psipMassArray = GetMassArray(psiptree)
                    dyMassArray   = GetMassArray(dytree  )

                    print(f"Data Mass: {len(dataMassArray)}")
                    print(f"Jpsi Mass: {len(jpsiMassArray)}")
                    print(f"Psip Mass: {len(psipMassArray)}")
                    print(f"DY   Mass: {len(dyMassArray)}")
                    







    #result_mix = uproot.open("../e906-LH2-data/merged_RS67_3089LH2.root:result_mix")
    #result_flask = uproot.open("../e906-LH2-data/merged_RS67_3089flask.root:result")

    #datatree = e906_data_cuts(data)
    #tree_mix = e906_data_cuts(result_mix)
    #tree_flask = e906_data_cuts(result_flask)

    #save = uproot.open("../e906-LH2-data/e906-messy-mc.root:save")

    #tree_mc = e906_mc_cuts(save)

    #train_tree, test_tree = train_test_split(tree_mc.to_numpy(), test_size=0.5, shuffle=True)

    # len1 = len(tree.mass.to_numpy())
    # len2 = len(tree_mix.mass.to_numpy())
    # len3 = len(tree_flask.mass.to_numpy())
    # len_total = len1 + len2 + len3

    # weight = 1.57319e+17/3.57904e+16

    # train_dic = {
    #     "mass": np.concatenate((tree.mass.to_numpy(), tree_mix.mass.to_numpy(), tree_flask.mass.to_numpy())),
    #     "pT": np.concatenate((tree.pT.to_numpy(), tree_mix.pT.to_numpy(), tree_flask.pT.to_numpy())),
    #     "xB": np.concatenate((tree.xB.to_numpy(), tree_mix.xB.to_numpy(), tree_flask.xB.to_numpy())),
    #     "xT": np.concatenate((tree.xT.to_numpy(), tree_mix.xT.to_numpy(), tree_flask.xT.to_numpy())),
    #     "xF": np.concatenate((tree.xF.to_numpy(), tree_mix.xF.to_numpy(), tree_flask.xF.to_numpy())),
    #     "weight": np.concatenate((np.ones(len1), -1. * np.ones(len2), -weight * np.ones(len3))),
    # }

    # train_dic_mc = {
    #     "mass": test_tree["mass"][:len_total],
    #     "pT": test_tree["pT"][:len_total],
    #     "xB": test_tree["x1"][:len_total],
    #     "xT": test_tree["x2"][:len_total],
    #     "xF": test_tree["xF"][:len_total],
    #     "weight": np.ones(len_total),
    # }

    # test_dic_mc = {
    #     "mass": test_tree["mass"][:len_total],
    #     "pT": test_tree["pT"][:len_total],
    #     "xB": test_tree["x1"][:len_total],
    #     "xT": test_tree["x2"][:len_total],
    #     "xF": test_tree["xF"][:len_total],
    #     "weight": np.ones(len_total),
    # }

    # outputs = h5py.File("../e906-LH2-data/reweight.hdf5", "w")

    # outputs.create_dataset("train_tree/mass", data=train_dic["mass"])
    # outputs.create_dataset("train_tree/pT", data=train_dic["pT"])
    # outputs.create_dataset("train_tree/xB", data=train_dic["xB"])
    # outputs.create_dataset("train_tree/xT", data=train_dic["xT"])
    # outputs.create_dataset("train_tree/xF", data=train_dic["xF"])
    # outputs.create_dataset("train_tree/weight", data=train_dic["weight"])


    # outputs.create_dataset("train_tree_mc/mass", data=train_dic_mc["mass"])
    # outputs.create_dataset("train_tree_mc/pT", data=train_dic_mc["pT"])
    # outputs.create_dataset("train_tree_mc/xB", data=train_dic_mc["xB"])
    # outputs.create_dataset("train_tree_mc/xT", data=train_dic_mc["xT"])
    # outputs.create_dataset("train_tree_mc/xF", data=train_dic_mc["xF"])
    # outputs.create_dataset("train_tree_mc/weight", data=train_dic_mc["weight"])


    # outputs.create_dataset("test_tree_mc/mass", data=test_dic_mc["mass"])
    # outputs.create_dataset("test_tree_mc/pT", data=test_dic_mc["pT"])
    # outputs.create_dataset("test_tree_mc/xB", data=test_dic_mc["xB"])
    # outputs.create_dataset("test_tree_mc/xT", data=test_dic_mc["xT"])
    # outputs.create_dataset("test_tree_mc/xF", data=test_dic_mc["xF"])
    # outputs.create_dataset("test_tree_mc/weight", data=test_dic_mc["weight"])

    # outputs.close()

if __name__ == '__main__':
    main()