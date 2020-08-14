from phue import Bridge
from ip_address import bridge_ip_address

b = Bridge(bridge_ip_address)
b.connect()

lights = b.lights
# Print light names
for l in lights:
    print(l.name)

# Set brightness of each light to 254
for l in lights:
    l.brightness = 254

def access_lights(bridge_ip_address):
    b = Bridge(bridge_ip_address)
    light_names_list = b.get_light_objects('name')
    return light_names_list

#Specific Light
def Light1():
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 10000
        lights[light].saturation = 200

if __name__ == '__main__':
    Light1()


