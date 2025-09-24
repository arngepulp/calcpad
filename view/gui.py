import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl


# HTML template with MathJax for rendering math
MATHJAX_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <script>
        window.MathJax = {
            tex: { inlineMath: [['$', '$'], ['\\(', '\\)']] },
            svg: { fontCache: 'global' }
        };
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
    <div id="math" style="font-size: 150%; padding: 10px;">$x^2$</div>
    <script>
        function renderMath(latex) {
            document.getElementById("math").innerHTML = '$' + latex + '$';
            MathJax.typesetPromise();
        }
    </script>
</body>
</html>
"""


class DesmosStyleInput(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desmos-Style Math Input")
        self.setGeometry(100, 100, 600, 150)

        layout = QVBoxLayout(self)

        # Input box for plain math text
        self.input = QLineEdit()
        self.input.setPlaceholderText("Type something like: x^2/2")
        self.input.textChanged.connect(self.update_render)

        # Web view to render formatted math
        self.renderer = QWebEngineView()
        self.renderer.setHtml(MATHJAX_HTML, QUrl("about:blank"))

        layout.addWidget(self.input)
        layout.addWidget(self.renderer)

    def update_render(self, text):
        # Escape backslashes for LaTeX commands
        latex = text.replace("\\", "\\\\")
        script = f'renderMath({repr(latex)});'
        self.renderer.page().runJavaScript(script)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesmosStyleInput()
    window.show()
    sys.exit(app.exec())
