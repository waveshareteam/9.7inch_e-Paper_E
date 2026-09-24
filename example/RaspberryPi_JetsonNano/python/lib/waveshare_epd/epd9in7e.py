# *****************************************************************************
# * | File        :   epd9in7e.py
# * | Author      :   Waveshare team
# * | Function    :   9.7inch e-Paper (E) driver
# * | Info        :
# *----------------
# * | This version:   V1.0
# * | Date        :   2026-06-25
# * | Info        :   Python demo
# -----------------------------------------------------------------------------
# ******************************************************************************/
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import logging

from PIL import Image

from . import epdconfig

# Display resolution
EPD_WIDTH = 1120
EPD_HEIGHT = 784

logger = logging.getLogger(__name__)


class EPD:
    def __init__(self):
        self.reset_pin = epdconfig.RST_PIN
        self.dc_pin = epdconfig.DC_PIN
        self.busy_pin = epdconfig.BUSY_PIN
        self.cs_pin = epdconfig.CS_PIN
        self.width = EPD_WIDTH
        self.height = EPD_HEIGHT
        self.BLACK = 0x000000
        self.WHITE = 0xFFFFFF
        self.YELLOW = 0x00FFFF
        self.RED = 0x0000FF
        self.BLUE = 0xFF0000
        self.GREEN = 0x00FF00
        if epdconfig.module_init() != 0:
            return -1

    # Hardware reset
    def reset(self):
        epdconfig.digital_write(self.reset_pin, 0)
        epdconfig.delay_ms(20)
        epdconfig.digital_write(self.reset_pin, 1)
        epdconfig.delay_ms(10)
        epdconfig.digital_write(self.reset_pin, 0)
        epdconfig.delay_ms(20)
        epdconfig.digital_write(self.reset_pin, 1)
        epdconfig.delay_ms(10)

    def send_command(self, command):
        epdconfig.digital_write(self.dc_pin, 0)
        epdconfig.digital_write(self.cs_pin, 0)
        epdconfig.spi_writebyte([command])
        epdconfig.digital_write(self.cs_pin, 1)

    def send_data(self, data):
        epdconfig.digital_write(self.dc_pin, 1)
        epdconfig.digital_write(self.cs_pin, 0)
        epdconfig.spi_writebyte([data])
        epdconfig.digital_write(self.cs_pin, 1)

    # Send a block of data
    def send_data2(self, data):
        epdconfig.digital_write(self.dc_pin, 1)
        epdconfig.digital_write(self.cs_pin, 0)
        epdconfig.spi_writebyte2(data)
        epdconfig.digital_write(self.cs_pin, 1)

    def ReadBusyH(self):
        logger.debug("e-Paper busy H")
        while epdconfig.digital_read(self.busy_pin) == 0:
            epdconfig.delay_ms(10)
        epdconfig.delay_ms(20)
        logger.debug("e-Paper busy H release")

    def TurnOnDisplay(self):
        self.send_command(0x12) # Write DRF
        self.send_data(0x00)
        self.ReadBusyH()
        logger.debug("Display Done")

    def init(self):
        self.reset()
        self.ReadBusyH()

        self.send_command(0x74)
        self.send_data(0x00)
        self.send_data(0x0C)
        self.send_data(0x0C)
        self.send_data(0xD9)
        self.send_data(0xDD)
        self.send_data(0xDD)
        self.send_data(0x15)
        self.send_data(0x15)
        self.send_data(0x55)

        self.send_command(0xF0)
        self.send_data(0x49)
        self.send_data(0x55)
        self.send_data(0x13)
        self.send_data(0x5D)
        self.send_data(0x05)
        self.send_data(0x10)

        self.send_command(0xA4)
        self.send_data(0x03)
        self.send_data(0x00)
        self.send_data(0x01)
        self.send_data(0x03)
        self.send_data(0x00)
        self.send_data(0x03)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)

        self.send_command(0x00)
        self.send_data(0xDF)
        self.send_data(0x6B)

        self.send_command(0xA5)
        self.send_data(0x44)
        self.send_data(0x54)
        self.send_data(0x00)

        self.send_command(0x30)
        self.send_data(0x08)

        self.send_command(0x50)
        self.send_data(0x37)

        self.send_command(0x60)
        self.send_data(0x03)
        self.send_data(0x03)

        self.send_command(0x03)
        self.send_data(0x00)
        self.send_data(0xC0)
        self.send_data(0x03)
        self.send_data(0xA8)

        self.send_command(0x86)
        self.send_data(0x00)

        self.send_command(0xE3)
        self.send_data(0x22)

        self.send_command(0xE0)
        self.send_data(0x00)

        self.send_command(0x61)
        self.send_data(0x04)
        self.send_data(0x60)
        self.send_data(0x03)
        self.send_data(0x10)

        self.send_command(0x01)
        self.send_data(0x0F)
        self.send_data(0x02)
        self.send_data(0x28)
        self.send_data(0x30)
        self.send_data(0x28)
        self.send_data(0x42)

        self.send_command(0xE7)
        self.send_data(0x01)

        self.send_command(0xB6)
        self.send_data(0x07)

        self.send_command(0x06)
        self.send_data(0xD0)
        self.send_data(0x18)

        self.send_command(0xB7)
        self.send_data(0x01)

        self.send_command(0x05)
        self.send_data(0xD0)
        self.send_data(0x18)

        self.send_command(0xB0)
        self.send_data(0x01)

        self.send_command(0xB1)
        self.send_data(0x02)

        self.send_command(0x04) # Write PON
        self.ReadBusyH()

        return 0

    def getbuffer(self, image):
        # Palette indices are the color codes required by the panel.
        pal_image = Image.new("P", (1, 1))
        pal_image.putpalette(
            (
                0, 0, 0,          # 0: black
                255, 255, 255,    # 1: white
                255, 255, 0,      # 2: yellow
                255, 0, 0,        # 3: red
                0, 0, 0,          # 4: unused
                0, 0, 255,        # 5: blue
                0, 255, 0,        # 6: green
            )
            + (0, 0, 0) * 249
        )

        imwidth, imheight = image.size
        if imwidth == self.width and imheight == self.height:
            image_temp = image
        elif imwidth == self.height and imheight == self.width:
            image_temp = image.rotate(90, expand=True)
        else:
            raise ValueError(
                "Invalid image dimensions: %d x %d, expected %d x %d"
                % (imwidth, imheight, self.width, self.height)
            )

        image_6color = image_temp.convert("RGB").quantize(palette=pal_image)
        buf_6color = bytearray(image_6color.tobytes("raw"))

        # The panel uses 4 bits per pixel, with two pixels in each byte.
        buf = [0x00] * (self.width * self.height // 2)
        for index in range(0, len(buf_6color), 2):
            buf[index // 2] = (buf_6color[index] << 4) | buf_6color[index + 1]

        return buf

    def display(self, image):
        self.send_command(0x10)
        self.send_data2(image)
        self.TurnOnDisplay()

    def Clear(self, color=0x11):
        self.send_command(0x10)
        self.send_data2([color] * int(self.height) * int(self.width/2))

        self.TurnOnDisplay()

    def sleep(self):
        self.send_command(0x02) # Write POF
        self.send_data(0x01)
        self.ReadBusyH()

    def EPD_END(self):
        epdconfig.delay_ms(2000)
        epdconfig.module_exit()

### END OF FILE ###
