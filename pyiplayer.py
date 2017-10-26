import subprocess
import sys

print str(sys.argv[1])


class iplayer(object):
    def search(self):
        p = subprocess.Popen(["get_iplayer",  str(sys.argv[1])],
                             stdout=subprocess.PIPE)
        output, err = p.communicate()

        try:
            print err
        except:
            print output

        print ("done")
        print (output.split("\n"))

    def list(self):
        p = subprocess.Popen(["transmission-remote", "-n", "transmission:transmission", "-l"], stdout=subprocess.PIPE)
        output, err = p.communicate()

        try:
            print err
        except:
            print output

        print ("done")
        print type((output))


status = iplayer()

status.search()
