import os
import sys

from streamlit.web import cli


def app():
    sys.argv = ["streamlit", "run", "src/stream_lit/main.py"]
    cli.main()