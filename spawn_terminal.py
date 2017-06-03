import pty

# Spawn a terminal from the meterpreter shell from metasploit.
# upload this into the /tmp folder of your target machine's storage directory.
# You should see user@box:/$ when you run this.


pty.spawn('bin/bash')
print('Happy Trails o/')
