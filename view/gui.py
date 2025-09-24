import os
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu"
os.environ["QT_QUICK_BACKEND"] = "software"

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QScrollArea, QLabel
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from sympy import sympify, latex


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
    <div id="math" style="font-size: 140%; padding: 5px 10px;">$x^2$</div>
    <script>
        function renderMath(latex) {
            document.getElementById("math").innerHTML = '$' + latex + '$';
            MathJax.typesetPromise();
        }
    </script>
</body>
</html>
"""


class ExpressionWidget(QWidget):
    """One expression input + math renderer + value display"""

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.input = QLineEdit()
        self.input.setPlaceholderText("Type expression, e.g. 2/x or sqrt(x^2 + 1)")
        self.input.textChanged.connect(self.update_render)

        self.renderer = QWebEngineView()
        self.renderer.setFixedHeight(50)

        self.value_label = QLabel("Value: ...")
        self.value_label.setStyleSheet("font-weight: bold; padding-left: 10px;")

        self.renderer.setHtml(MATHJAX_HTML, QUrl("about:blank"))

        self.layout.addWidget(self.input)
        self.layout.addWidget(self.renderer)
        self.layout.addWidget(self.value_label)

    def update_render(self, raw_text):
        try:
            parsed_expr = sympify(raw_text)
            latex_expr = latex(parsed_expr)
            # Here you would calculate the value and update self.value_label
            # For now, just show a placeholder
            self.value_label.setText("Value: ...")
        except Exception:
            latex_expr = raw_text
            self.value_label.setText("Value: (invalid expression)")

        latex_expr = latex_expr.replace("\\", "\\\\")
        script = f'renderMath("{latex_expr}");'
        self.renderer.page().runJavaScript(script)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desmos-Style Multiple Expressions")
        self.setGeometry(100, 100, 600, 550)

        self.main_layout = QVBoxLayout(self)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.container = QWidget()
        self.expr_layout = QVBoxLayout(self.container)
        self.expr_layout.setSpacing(15)

        self.scroll.setWidget(self.container)

        self.main_layout.addWidget(self.scroll)

        self.btn_add = QPushButton("Add Expression")
        self.btn_add.clicked.connect(self.add_expression)

        self.main_layout.addWidget(self.btn_add)

        self.add_expression()

    def add_expression(self):
        expr_widget = ExpressionWidget()
        self.expr_layout.addWidget(expr_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
