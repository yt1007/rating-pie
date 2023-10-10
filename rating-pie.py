from load_csv import load
import sys
import numpy as np
from matplotlib import pyplot as plt


def main():
    '''Program loads the given csv file, and presents the data in a pie'''
    try:
        assert len(sys.argv) == 2, "Bad CSV"
        data = load(sys.argv[1])
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    except BaseException as e:
        print(e)
    else:
        if data is not None:
            try:
                data = data.set_index('Score')
                pdat = np.array(data.Count)
                plab = np.array(data.index)
                pcol = [ "#ff6666", "#f86d4f", "#ec7638", "#dd8020",
                        "#cb8a00", "#b59300", "#9d9a00", "#82a100",
                        "#62a616", "#33aa33" ]
                pcol = np.array(pcol)
                pcap = 0
                for lab, dat in zip(plab, pdat):
                    if lab >= 8:
                        pcap += dat;
                pcap = pcap * 100 / sum(pdat)
                pcap = f'{pcap:.1f}% rated an 8 or more'
                plt.pie(pdat,
                        wedgeprops=dict(width=0.6),
                        startangle=90, colors=pcol)
                plt.text(0, 0.05, sum(pdat),
                        fontsize=36, weight='bold',
                        horizontalalignment='center',
                        verticalalignment='center')
                plt.text(0, -0.2, "SAMPLES",
                        fontsize=10,
                        horizontalalignment='center',
                        verticalalignment='center')
                plt.text(0, -1.15, pcap,
                        fontsize=10,
                        horizontalalignment='center',
                        verticalalignment='center')
                plt.legend(title='Rating', loc='right', 
                        bbox_to_anchor=(1, 0, 0.15, 1),
                        labels=plab)
                plt.show()
            except Exception as e:
                print(f"{type(e).__name__}: {e}")
            except BaseException as e:
                print(e)


if __name__ == "__main__":
    main()
