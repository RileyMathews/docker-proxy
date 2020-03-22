from jinja2 import Template
import os
import pdb
import sys
print(sys.argv)

# read in yaml file as string
file_string = ""
with open("./resources/envoy.yaml", "r") as file:
    file_string_array = file.readlines()
    file_string = "".join(file_string_array)

# get env vars and set defaults
LISTENER_ADDRESS = os.getenv("LISTENER_ADDRESS", "0.0.0.0")
LISTENER_PORT    = os.getenv("LISTENER_PORT", "80")
PROXY_ADDRESS    = os.getenv("PROXY_ADDRESS", "host.docker.internal")
PROXY_PORT       = os.getenv("PROXY_PORT", "8080")

# assign string of rendered template
template = Template(file_string)
new_file_string = template.render(
    LISTENER_ADDRESS = LISTENER_ADDRESS,
    LISTENER_PORT = LISTENER_PORT,
    PROXY_ADDRESS = PROXY_ADDRESS,
    PROXY_PORT = PROXY_PORT
)

# save string as yaml file
with open("/etc/envoy.yaml", "w") as output_file:
    output_file.write(new_file_string)
