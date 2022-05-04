
#!/usr/bin/env python

from pyVim.connect import SmartConnectNoSSL, Disconnect
import ssl
import atexit
#s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#s.verify_mode=ssl.CERT_NONE
si= SmartConnectNoSSL(host="20.13.103.201",
                      user="Administrator@vsphere.local",
                      pwd="Testvxrail123!",
                      port="443")
aboutInfo=si.content.about
#print("Product Name",aboutInfo.fullName)
vc_full=aboutInfo.fullName
#print("Product Build:",aboutInfo.build)
vc_build=aboutInfo.build
#print("Product Unique Id:",aboutInfo.instanceUuid)
vc_uuid=aboutInfo.instanceUuid
#print("Product Version:",aboutInfo.version)
#print("Product Base OS:",aboutInfo.osType)
#print("Product vendor:",aboutInfo.vendor)
#print("Product type:",aboutInfo.apiType)
#print("Datacenter Name:",si.content.rootFolder.childEntity)

for datacenter in si.content.rootFolder.childEntity:
    print("Datacenter name:",datacenter.name)
    print(" ")
    datastores = datacenter.datastore
    print("Datastore(s) name list:")
    for ds in datastores:
        #print(ds.summary)
        print(ds.summary.name)
    #print("Datacenter's datastore:",datacenter.datastore)
    #print(datacenter.hostFolder)
    #print(datacenter.hostFolder.parent)
    print(" ")
#### Convert the cluster name to a list
    cl=[]
    #print(type(cl))
    cluster_object = list(datacenter.hostFolder.childEntity)
    for cln in datacenter.hostFolder.childEntity:
        #print(cln.name)
        cl.append(cln.name)
    print(cl)
####
    print(cluster_object)
    for i in range(len(cluster_object)):
        print("The %s cluster name:%s"%(i+1,cluster_object[i]))
    print("There are(is)",len(cluster_object),"cluster(s) in the",datacenter.name,"Datacenter. The cluster(s)'s list:")
    for cln in datacenter.hostFolder.childEntity:
        print(cln.name)
        
        
