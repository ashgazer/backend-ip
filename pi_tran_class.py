import subprocess


class transmission(object):

	def add_torrent(self,magnet):
		p = subprocess.Popen(["transmission-remote","-n", "transmission:transmission" ,"-a",magnet], stdout=subprocess.PIPE)
		output, err = p.communicate()
		

		try:
		        print err
		except:
		        print output


		print ("done")
		return (output)

	def list(self):
		p = subprocess.Popen(["transmission-remote","-n", "transmission:transmission" ,"-l"], stdout=subprocess.PIPE)
		output, err = p.communicate()
		

		try:
		        print err
		except:
		        print output


		print ("done")
		print (output)



#status = transmission()

#status.list()

