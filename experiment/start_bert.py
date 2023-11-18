from bert_serving.server import BertServer
from bert_serving.server.helper import get_args_parser


def start_bert_server():
    bert_run_args = get_args_parser().parse_args([
        '-model_dir', '/Users/jzw/workspace/apr/PatchCorrectnessRunner/data/models/wwm_cased_L-24_H-1024_A-16',
        '-num_worker', '2',
        '-max_seq_len', '360'
    ])
    bert_server = BertServer(bert_run_args)
    try:
        bert_server.start()
    except InterruptedError:
        bert_server.close()

if __name__ == '__main__':
    start_bert_server()
