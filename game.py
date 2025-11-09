try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame as pg
    from socket import *
    from pygame.locals import *
except ImportError, err:
    print(f"Failed to load module. {err}")
    sys.exit(2)

