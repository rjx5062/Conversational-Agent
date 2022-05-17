from datasets import load_metric
from pprint import pprint

import torch
import math
import time
import sys
import json
import numpy as np


def make_sgd_datasets(bKnowledge):
    if bKnowledge:
        out_names = ['sgd.train_c.txt', 'sgd.valid_c.txt', 'sgd.test_c.txt']
    else:
        out_names = ['sgd.train_b.txt', 'sgd.valid_a.txt', 'sgd.test_a.txt', 'sgd.valid_b.txt', 'sgd.test_b.txt']
    max_ins = [18, 2, 2, 2, 2]

    count = 0
    counts = []
    for dataset in range(len(out_names)):
        fout = open(out_names[dataset], 'wt')

        # New ---
        if dataset == 0:
            path_prefix = 'train/'
        elif dataset % 2 != 0:
            path_prefix = 'dev/'
        else:
            path_prefix = 'test/'
        # ---

        for dialog in range(1, max_ins[dataset], 1):
                        # New
            file_name = path_prefix + 'dialogues_%03d.json' % dialog
            print(file_name)
            with open(file_name) as f:
                data = json.load(f)
            for dialogue in data:
                if len(dialogue['services']) == 1:
                    if dialogue['services'][0] == 'Restaurants_1' or dialogue['services'][0] == 'Restaurants_2' :
                        prev_speaker = ''
                        prev_utterance = ''
                        for turn in dialogue['turns']:
                            count = count + 1
                            speaker = turn['speaker']
                            utterance = turn['utterance']

                            for frame in turn['frames']:
                                if frame['service'] == 'Restaurants_1' or dialogue['services'][0] == 'Restaurants_2':
                                    knowledge = ''
                                    try:
                                        knowledge = '[KNOWLEDGE] '
                                        for slot in frame['slots']:
                                            temp = '%s [EQUAL] %s [SEP] ' % (slot['slot'], slot['value'])
                                            knowledge = knowledge + temp
                                    except:
                                        nothing = 1
                                    try:
                                        if len(knowledge) == 0:
                                            knowledge = '[KNOWLEDGE] '
                                        try:
                                            intent = frame['state']['active_intent']
                                            temp = '%s [EQUAL] %s [SEP] ' % ('active_intent', intent)
                                            knowledge = knowledge + temp
                                            slot_values = frame['state']['slot_values']
                                            for slot in slot_values:
                                                vals = slot_values[slot]
                                                for val in vals:
                                                    temp = '%s [EQUAL] %s [SEP] ' % (slot, val)
                                                    knowledge = knowledge + temp
                                        except:
                                            nothing = 1
                                    except:
                                        noting = 1

                            if len(prev_speaker) > 0:
                                if not bKnowledge:
                                    knowledge = ''
                                if dataset == 0:
                                    text = '[%s] %s %s [%s] %s [END]' % (prev_speaker,
                                                                         prev_utterance,
                                                                         knowledge,
                                                                         speaker,
                                                                         utterance)
                                else:
                                    text = '[%s] %s %s [%s] | %s [END]' % (prev_speaker,
                                                                           prev_utterance,
                                                                           knowledge,
                                                                           speaker,
                                                                           utterance)
                                fout.write('%s\n' % (text))
                                print(text)
                            prev_speaker = speaker
                            prev_utterance = utterance
        counts.append(count)
        count = 0
    print(counts)


def main():
    make_sgd_datasets(True)
    make_sgd_datasets(False)


if __name__ == "__main__":
    main()
