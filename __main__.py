import argparse
import datetime
import logging
import subprocess

from PySide6.QtWidgets import QApplication

from ui.mainwindow import MainWindow

# --- Basic argument parsing ---

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true", default=False)
args = parser.parse_args()


# --- Logging setup ---


class ColoredFormatter(logging.Formatter):
    colors = {
        logging.DEBUG: "\033[92m",
        logging.INFO: "\033[0m",
        logging.WARNING: "\033[93m",
        logging.ERROR: "\033[91m",
    }

    def format(self, record: logging.LogRecord):
        base_format = super().format(record)
        color = self.colors.get(record.levelno, "\033[0m")
        return f"{color}{base_format}\033[0m"


handler = logging.StreamHandler()
handler.setFormatter(
    ColoredFormatter(
        datefmt="%H:%M:%S", fmt="[{asctime}] {levelname:<8} - {message}", style="{"
    )
)


level = logging.DEBUG if args.debug else logging.INFO
logging.basicConfig(level=level, handlers=[handler])

# Display startup information about the software

try:
    version = subprocess.check_output(["git", "describe"], stderr=subprocess.DEVNULL)
except subprocess.CalledProcessError:
    version = subprocess.check_output(["git", "describe", "--always"])

logging.info(datetime.datetime.now().strftime(r"%a %d %B %Y"))
logging.info(f"Git revision {version.decode().strip()}")
if args.debug:
    logging.info("Debug mode active")


# --- UI setup ---


app = QApplication()
mainwindow = MainWindow()

mainwindow.show()
app.exec()
