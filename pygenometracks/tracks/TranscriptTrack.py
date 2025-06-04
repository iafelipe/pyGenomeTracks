# -*- coding: utf-8 -*-
from . GenomeTrack import GenomeTrack
from . BedTrack import BedTrack
import matplotlib as mpl
from matplotlib.patches import Rectangle, Polygon

mpl.rcParams['hatch.linewidth'] = 2

class TranscriptTrack(BedTrack):
    SUPPORTED_ENDINGS = []
    TRACK_TYPE = 'transcript'
    OPTIONS_TXT = GenomeTrack.OPTIONS_TXT
    
    def draw_gene_simple(self, ax, bed, ypos, rgb, edgecolor, linewidth):
        """
        draws an interval with direction (if given)
        So either a rectangle if no direction is given
        Or a rectangle with an arrow giving the orientation
        """

        if bed.strand not in ['+', '-']:
            ax.add_patch(Rectangle((bed.start, ypos),
                         bed.end - bed.start, 1,
                         edgecolor='white', facecolor=rgb,
                         linewidth=linewidth, hatch='|'))
        else:
            vertices = self._draw_arrow(bed.start, bed.end, bed.strand, ypos)
            ax.add_patch(Polygon(vertices, closed=True, fill=True,
                                 edgecolor='white',
                                 facecolor=rgb,
                                 linewidth=linewidth, hatch='|'))