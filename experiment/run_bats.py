import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '.')))

import dotenv

from experiment.main import Experiment
from experiment.config import Config

dotenv.load_dotenv()

def run_bats_main(predict, cut_off, predict_id, path_to_patch_snippet):
    config = Config()
    path_test = config.path_test
    path_patch_root = config.path_patch_root
    path_generated_patch = config.path_generated_patch
    organized_dataset = config.organized_dataset
    patch_w2v = config.patch_w2v

    e = Experiment(path_test, path_patch_root, path_generated_patch, organized_dataset, patch_w2v)
    e.run(predict, cut_off, predict_id, path_to_patch_snippet)

if __name__ == '__main__':
    run_bats_main(
        'predict',
        0.8,
        'Chart_26',
        '/Users/jzw/workspace/apr/data/datasets/BATS_DataSet/PatchCollectingV1_sliced/PraPR/Correct/Chart/26/patch1'
    )
