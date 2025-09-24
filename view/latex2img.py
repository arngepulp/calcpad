
# https://medium.com/@ealbanez/how-to-easily-convert-latex-to-images-with-python-9062184dc815
# Eduardo Albanez
# thank u for code ed i edit it slightly
from io import BytesIO
from PyQt6.QtGui import QPixmap
import matplotlib.pyplot as plt

def latex2img(expr):
    latex_expression = f"${expr}$"
    fig = plt.figure(figsize=(1, 0.5),dpi = 600)  
    fig.text(
        x=0.5,
        y=0.5,
        s=latex_expression,
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=16
    )
    
    plt.axis('off')  
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)
    plt.close(fig)

    buf.seek(0)
    pixmap = QPixmap()
    pixmap.loadFromData(buf.read(), 'PNG')
    return pixmap

