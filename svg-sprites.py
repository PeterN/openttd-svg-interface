# pip install git+https://github.com/citymania-org/grf-py.git@ae4aeab54638cc206d3c969caae0e473a8636651#egg=grf

import struct
import numpy as np

import grf

THIS_FILE = grf.PythonFile(__file__)


class SVGFile(grf.ResourceFile):
    def get_data(self):
        return open(self.path, 'rb').read()


class SVGSprite(grf.Resource):
    def __init__(self, files, w, h, xofs, yofs):
        for file in files:
            assert(isinstance(file, SVGFile))

        super().__init__()
        self.files = files
        self.w = w
        self.h = h
        self.xofs = xofs
        self.yofs = yofs

    def get_real_data(self, context):
        stack = []
        for file in self.files:
            data = file.get_data()
            stack.append(struct.pack('<i', len(data) + 1) + data + b'\0')
        data = b''.join(stack)
        return struct.pack(
            '<BBBBHHhhB',
            0,  # type = 0
            0xFF,  # zoom 0xFF = extended
            0xFF,  # multiplier 0xFF, and
            0x00,  # divisor 0x00 = svg
            self.h,
            self.w,
            self.xofs,
            self.yofs,
            len(self.files)
        ) + data

    def get_fingerprint(self):
        return dict(
            **{'class': self.__class__.__name__},
            w=self.w,
            h=self.h,
            xofs=self.xofs,
            yofs=self.yofs,
        )

    def get_resource_files(self):
        return (THIS_FILE, self.files[0])


g = grf.NewGRF(
    grfid=b'PNS\xFF',
    name='SVG decorations',
    description='SVG window decorations',
)

g.add(grf.ReplaceOldSprites(((0, 1),)))
g.add(SVGSprite((SVGFile('base/0_mouse_cursor.svg'),), 24, 24, 0, 0))
g.add(grf.ReplaceOldSprites(((143, 1),)))
g.add(SVGSprite((SVGFile('base/143_closebox.svg'),), 8, 9, 1, 0))
g.add(grf.ReplaceOldSprites(((682, 1),)))
g.add(SVGSprite((SVGFile('base/682_large_small_window.svg'),), 12, 12, 0, 0))
g.add(grf.ReplaceOldSprites(((709, 4),)))
g.add(SVGSprite((SVGFile('base/709_skip_to_prev.svg'),), 20, 20, 0, 0))
g.add(SVGSprite((SVGFile('base/710_skip_to_next.svg'),), 20, 20, 0, 0))
g.add(SVGSprite((SVGFile('base/711_stop_music.svg'),), 20, 20, 0, 0))
g.add(SVGSprite((SVGFile('base/712_play_music.svg'),), 20, 20, 0, 0))
g.add(grf.ReplaceOldSprites(((747, 1),)))
g.add(SVGSprite((SVGFile('base/747_company_icon.svg'), SVGFile('base/747_company_icon_mask.svg')), 14, 8, 0, 0))
g.add(grf.ReplaceOldSprites(((874, 1),)))
g.add(SVGSprite((SVGFile('base/874_gradient.svg'), SVGFile('base/874_gradient_mask.svg')), 92, 119, 0, 0))
g.add(grf.ReplaceOldSprites(((4836, 9),)))
g.add(SVGSprite((SVGFile('openttd/blank.svg'),), 1, 1, 0, 0))
g.add(SVGSprite((SVGFile('openttd/blank.svg'),), 1, 1, 0, 0))
g.add(SVGSprite((SVGFile('openttd/blank.svg'),), 1, 1, 0, 0))
g.add(SVGSprite((SVGFile('openttd/logo.svg'),), 128, 128, 0, 0))
g.add(SVGSprite((SVGFile('openttd/blank.svg'),), 1, 1, 0, 0))
g.add(SVGSprite((SVGFile('openttd/blank.svg'),), 1, 1, 0, 0))
g.add(SVGSprite((SVGFile('openttd/blank.svg'),), 1, 1, 0, 0))
g.add(SVGSprite((SVGFile('openttd/blank.svg'),), 1, 1, 0, 0))
g.add(SVGSprite((SVGFile('openttd/blank.svg'),), 1, 1, 0, 0))
g.add(grf.ReplaceNewSprites(21, 2, offset=12))
g.add(SVGSprite((SVGFile('openttd/blank.svg'),), 1, 1, 0, 0))
g.add(SVGSprite((SVGFile('openttd/blank.svg'),), 1, 1, 0, 0))
g.add(grf.ReplaceNewSprites(21, 12, offset=38))
g.add(SVGSprite((SVGFile('openttd/38_square.svg'), SVGFile('openttd/38_square_mask.svg')), 10, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/39_blot.svg'), SVGFile('openttd/39_blot_mask.svg')), 10, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/40_lock.svg'),), 7, 9, 0, 0))
g.add(SVGSprite((SVGFile('openttd/41_square_empty.svg'),), 9, 7, 0, 0))
g.add(SVGSprite((SVGFile('openttd/42_square_checked.svg'),), 9, 7, 0, 0))
g.add(SVGSprite((SVGFile('openttd/43_warning_sign.svg'),), 10, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/44_window_resize_right.svg'),), 7, 7, 0, 0))
g.add(SVGSprite((SVGFile('openttd/45_down_arrow.svg'),), 7, 4, 0, 0))
g.add(SVGSprite((SVGFile('openttd/46_up_arrow.svg'),), 7, 4, 0, 0))
g.add(SVGSprite((SVGFile('openttd/47_left_arrow.svg'),), 4, 7, 0, 0))
g.add(SVGSprite((SVGFile('openttd/48_right_arrow.svg'),), 4, 7, 0, 0))
g.add(SVGSprite((SVGFile('openttd/49_house.svg'),), 8, 8, 0, 0))
g.add(grf.ReplaceNewSprites(21, 2, offset=51))
g.add(SVGSprite((SVGFile('openttd/51_pin_up.svg'),), 8, 8, 0, 0))
g.add(SVGSprite((SVGFile('openttd/52_pin_down.svg'),), 8, 8, 0, 0))
g.add(grf.ReplaceNewSprites(21, 11, offset=147))
g.add(SVGSprite((SVGFile('openttd/147_circle_folded.svg'),), 9, 9, 0, 0))
g.add(SVGSprite((SVGFile('openttd/148_circle_unfolded.svg'),), 9, 9, 0, 0))
g.add(SVGSprite((SVGFile('openttd/149_window_resize_left.svg'),), 7, 7, 0, 0))
g.add(SVGSprite((SVGFile('openttd/150_music_play_rtl.svg'),), 20, 20, 0, 0))
g.add(SVGSprite((SVGFile('openttd/151_window_shade.svg'),), 7, 8, 0, 0))
g.add(SVGSprite((SVGFile('openttd/152_window_unshade.svg'),), 7, 8, 0, 0))
g.add(SVGSprite((SVGFile('openttd/153_window_debug.svg'),), 7, 8, 0, 0))
g.add(SVGSprite((SVGFile('openttd/154_profit_na.svg'),), 8, 8, 0, 0))
g.add(SVGSprite((SVGFile('openttd/155_profit_negative.svg'),), 8, 8, 0, 0))
g.add(SVGSprite((SVGFile('openttd/156_profit_some.svg'),), 8, 8, 0, 0))
g.add(SVGSprite((SVGFile('openttd/157_profit_lot.svg'),), 8, 8, 0, 0))
g.add(grf.ReplaceNewSprites(21, 4, offset=162))
g.add(SVGSprite((SVGFile('openttd/154_profit_na.svg'),), 8, 8, 0, 0))
g.add(SVGSprite((SVGFile('openttd/155_profit_negative.svg'),), 8, 8, 0, 0))
g.add(SVGSprite((SVGFile('openttd/156_profit_some.svg'),), 8, 8, 0, 0))
g.add(SVGSprite((SVGFile('openttd/157_profit_lot.svg'),), 8, 8, 0, 0))
g.add(grf.ReplaceNewSprites(21, 3, offset=166))
g.add(SVGSprite((SVGFile('openttd/166_delete_left.svg'),), 14, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/167_delete_right.svg'),), 14, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/168_window_defsize.svg'),), 8, 8, 0, 0))
g.add(grf.ReplaceNewSprites(21, 7, offset=184))
g.add(SVGSprite((SVGFile('openttd/184_rename.svg'),), 10, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/185_goto_location.svg'),), 11, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/186_chat.svg'),), 12, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/187_admin.svg'),), 12, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/188_join.svg'),), 12, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/189_player_self.svg'),), 10, 10, 0, 0))
g.add(SVGSprite((SVGFile('openttd/190_player_host.svg'),), 10, 10, 0, 0))

# g.add(grf.FileSprite(grf.ImageFile('pause.png'),), 0, 0, 16, 16))

grf.main(g, 'svg_sprites.grf')
