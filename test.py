import ezdxf

# Create new DXF document
doc = ezdxf.new(dxfversion='R2010')
msp = doc.modelspace()

# Board outline (100mm x 80mm)
width, height = 100, 80
msp.add_lwpolyline([(0, 0), (width, 0), (width, height), (0, height), (0, 0)], close=True)

# Output pads (50)
for i in range(50):
    x = 5 + (i % 25) * 3.8
    y = 5 if i < 25 else 10
    msp.add_circle((x, y), radius=0.75)
    msp.add_text(f"O{i+1}", dxfattribs={'height': 1.2, 'insert': (x - 1.5, y + 1.5)})

# DIP Switches (6)
for i in range(6):
    x = 5
    y = height - 5 - i * 4
    msp.add_lwpolyline([(x, y), (x+3, y), (x+3, y+3), (x, y+3), (x, y)], close=True)
    msp.add_text(f"DIP{i}", dxfattribs={'height': 1.2, 'insert': (x + 4, y + 0.5)})

# LED indicators
led_names = ['PWR', 'DMX', 'STATUS']
for i, name in enumerate(led_names):
    x = width - 15
    y = height - 5 - i * 5
    msp.add_circle((x, y), radius=1)
    msp.add_text(name, dxfattribs={'height': 1.5, 'insert': (x + 3, y - 0.5)})

# Save DXF
doc.saveas("dmx_board_layout.dxf")
print("Saved: dmx_board_layout.dxf")
