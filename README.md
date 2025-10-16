# colon3board

This is a custom designed mechanical keyboard, created for the the [Hackpad](https://hackpad.hackclub.com/) event. It has a full sized 104 key layout, and a built in OLED display.

![image](/images/pcb_front.png)

![image](/images/pcb_back.png)

![image](/images/pcb_design.png)

![image](/images/pcb_schematic.png)

![image](/images/case.png)

I designed this so I could get more practice with designing PCBs in KiCad and with modeling larger parts in Fusion 360. Also, I get to have a free keyboard in the end thanks to the grant from Hack Club. 

## BOM

### For PCB:
| Part                                  | Count (needed) | Count (purchased) | Price  | Shipping Cost | Link                                                                                          |
|---------------------------------------|----------------|-------------------|--------|---------------|-----------------------------------------------------------------------------------------------|
| Raspberry Pi Pico                     | 1              | 0                 | $0.00  | $0.00         | https://www.amazon.com/Raspberry-RP2040-microcontroller-Dual-core-Processor-1pc/dp/B0BK9CTMSV |
| SSD1306 128x32 OLED                   | 1              | 1                 | $2.32  | $0.00         | https://www.aliexpress.us/item/3256805123611667.html                                          |
| Cherry MX key switches                | 104            | 108               | $32.99 | $0.00         | https://www.amazon.com/Zjmehty-Switches-Mechanical-Pre-Lubed-Pin-Enhanced/dp/B0CF8DWDGF       |
| PBT Keycaps                           | 104            | 139               | $13.99 | $0.00         | https://www.amazon.com/Doubleshot-Mechanical-Keyboard-Compatiability-Keyboads/dp/B0F7H32LKC   |
| PCB Mount Stabilizers Kit             | 1              | 1                 | $9.99  | $0.00         | https://www.amazon.com/GLORIOUS-Stabilizer-Mechanical-Keyboards-Compatible/dp/B09MZKFLXP      |
| 1x4 2.54mm vertical female pin header | 1              | 1                 | $0.25  | $4.99         | https://www.digikey.com/en/products/detail/adam-tech/RS1-04-G/9829303                         |
| 1x4 2.54mm vertical male pin header   | 1              | 1                 | $0.20  | $0.00         | https://www.digikey.com/en/products/detail/metz-connect-usa-inc/PR20204VBNN/12342903          |
| MCP23008 IO expander                  | 1              | 1                 | $1.54  | $0.00         | https://www.digikey.com/en/products/detail/microchip-technology/MCP23008-E-P/735951           |
| 1N4148 diodes                         | 104            | 110               | $3.72  | $0.00         | https://www.digikey.com/en/products/detail/onsemi/1N4148-T50A/978509                          |
| PCB Fabrication from JLCPCB           | 1              | 5                 | $25.80 | $52.08        | https://jlcpcb.com/                                                                           |

### For Case:
- Case is 3d printed in PLA
- 6x M2x5 screw
- 4x M3x12 screw
- 4x M3x4 heat set inserts

## License

This project is licensed under the GNU GPL v3.

```
ading2210/colon3board - A custom mechanical keyboard
Copyright (C) 2025 ading2210

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```