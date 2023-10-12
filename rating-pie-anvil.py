from load_csv import load
import numpy as np
from matplotlib import pyplot as plt
import anvil.server
import anvil.mpl_util
import matplotlib


matplotlib.use('agg')
anvil.server.connect("server_B6UIGNOVAFYKZ5AP4NWSMM2G-MWKTDDNSEUFGQRCT")

@anvil.server.callable
def csv_to_pie(media):
    '''Program loads the given csv file, and presents the data in a pie'''
    fig = None
    try:
        with open('data.csv', "wb") as f:
            f.write(media.get_bytes())
            f.close()
        data = load('data.csv')
        print(data)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    except BaseException as e:
        print(e)
    else:
        if data is not None:
            try:
                fig = draw_pie(data)
            except Exception as e:
                print(f"{type(e).__name__}: {e}")
            except BaseException as e:
                print(e)
    return fig


def draw_pie(data):
    '''
    Function takes a data frame containing scores and counts,
    and draws a donut chart using Matplotlib.
    '''
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
        fig, ax = plt.subplots()
        ax.pie(pdat,
                wedgeprops=dict(width=0.6),
                startangle=90, colors=pcol)
        ax.text(0, 0.05, sum(pdat),
                fontsize=36, weight='bold',
                horizontalalignment='center',
                verticalalignment='center')
        ax.text(0, -0.2, "SAMPLES",
                fontsize=10,
                horizontalalignment='center',
                verticalalignment='center')
        ax.text(0, -1.15, pcap,
                fontsize=10,
                horizontalalignment='center',
                verticalalignment='center')
        ax.legend(title='Rating', loc='right', 
                bbox_to_anchor=(1, 0, 0.15, 1),
                labels=plab)
        plt.savefig('data.svg')
        return anvil.mpl_util.plot_image()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    except BaseException as e:
        print(e)


anvil.server.wait_forever()
