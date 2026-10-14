from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "raw" / "stats.csv"
HTML_PATH = ROOT / "outputs" / "tables" / "data.html"
FIGURE_PATH = ROOT / "outputs" / "figures" / "pitch_shape_scatter.png"


def main():
    df = pd.read_csv(INPUT_PATH)
    HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_html(HTML_PATH)
    df = df.fillna(0)
    compare = df.columns[5:]
    df['max_col'] = df[compare].idxmax(axis=1)

    colors = {
        'n_sl_formatted': 'red',
        'n_ch_formatted': 'green',
        'n_cu_formatted': 'blue',
        'n_si_formatted': 'yellow',
        'n_fc_formatted': 'orange',
        'n_fs_formatted': 'purple',
        'n_st_formatted': 'cyan',
        'n_fo_formatted': 'magenta'
    }
    df['color'] = df['max_col'].map(colors)

    plt.scatter(df['ff_avg_break_x'], df['ff_avg_break_z'], c = df['color'])
    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIGURE_PATH, dpi=150, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    main()
