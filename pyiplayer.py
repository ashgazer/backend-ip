import subprocess


class iplayer(object):
    def search(self, query):
        p = subprocess.Popen(["get_iplayer", query],
                             stdout=subprocess.PIPE)
        output, err = p.communicate()

        try:
            print err
        except:
            print output

        print ("done")
        print (output)

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

status.search('Strictly')
