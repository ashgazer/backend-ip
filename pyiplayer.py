import subprocess
import sys


class iplayer(object):
    def search(self, query):
        p = subprocess.Popen(["get_iplayer",  str(sys.argv[0])],
                             stdout=subprocess.PIPE)
        output, err = p.communicate()

        try:
            print err
        except:
            print output

        print ("done")
        print type((output))

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
