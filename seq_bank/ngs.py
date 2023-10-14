""" main entrance of seq bank
"""
import sys
import os
from datetime import datetime
import click
import json
import pandas as pd
from loguru import logger
from seq import SeqManager, Compound
# PARENT_DIR = os.path.dirname(os.getcwd())
# print(os.getcwd())
# sys.path.append(PARENT_DIR)

def run(fpath):
    df = pd.read_excel(fpath, 0)
    # df = df.sort_values('Vol', ascending=False).iloc[:100].copy()
    df = df.drop_duplicates(subset='seqs').copy()
    df_iter = df.copy()
    for idx, seq in df_iter.seqs.iteritems():
        # if len(seq) < 32:
        #     continue
        print(seq)
        # seq += 'CCA'
        seq = T2U(seq)
        df_5p = generate_mass_ladder_5p(seq)
        df_3p = generate_mass_ladder_3p(seq)

        df.loc[idx, 'seq'] = seq
        df.loc[idx, 'MassLadder5p'] = df_5p.to_json()
        df.loc[idx, 'MassLadder3p'] = df_3p.to_json()

    df.to_excel('~/Downloads/a.xlsx')
    # return generate_mass_ladder_5p(seqs[0])

def generate_mass_ladder_5p(seq):
    if not seq:
        return pd.DataFrame()

    anchor = 18.0106 + 79.9663

    sm = SeqManager()
    _, cpds = sm.generate_cpds_5p(seq, anchor)
    df = Compound.cpds2df(cpds)
    # print(df.info())
    return df

def generate_mass_ladder_3p(seq):
    if not seq:
        return pd.DataFrame()

    rev_anchor = -61.9557

    sm = SeqManager()
    _, cpds = sm.generate_cpds_3p(seq, rev_anchor)
    df = Compound.cpds2df(cpds)
    # print(df.info())
    return df

def T2U(seq):
    """Change input sequence from DNA to RNA stype, 'T' to 'U' 
    """
    # print('input', seq)
    if 'N' in seq: # means randomly ACGU
        return ''
    seq = seq.replace('T', 'U').replace('t', 'U')
    return seq

@click.command()
# @click.option("--seqs", "-s", type=str, help="sequences.")
@click.option("--fpath", "-f", type=str, help="path to an Excel file which contains a list of sequences.")
def action(fpath):
    # seqs = seqs.split(',')
    return run(fpath)

if __name__ == "__main__":
    action()
