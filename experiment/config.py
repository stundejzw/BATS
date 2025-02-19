class Config:
    def __init__(self):
        # the orginal data of test case name, test function, associated patch including 'single test case' and 'full' versions.
        self.path_test = '../data/test_case_all.pkl'
        # developers' patches in defects4j
        self.path_patch_root = '../data/defects4j_patch_sliced/'

        #  generated patches of APR tools
        self.path_generated_patch = '/Users/haoye.tian/Documents/University/data/BATS_DataSet/PatchCollectingV1_sliced/'
        # for Naturalness
        # self.path_generated_patch = '/Users/haoye.tian/Documents/ISSTA2022withTextUnique/'

        # choose one type of representations to learn the behaviour of patch
        self.patch_w2v = 'cc2vec'
        # self.patch_w2v = 'bert'
        # self.patch_w2v = 'string'

        self.organized_dataset = '../data/organized_dataset_' + self.patch_w2v + '.pickle'


if __name__ == '__main__':
    Config()