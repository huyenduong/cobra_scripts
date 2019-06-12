#!/usr/bin/env python
'''
Autogenerated code using webarya.py
Config to exclude EPG from Preferred Group
Customized by: Huyen Duong
POC Quality

'''

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.naming
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
from cobra.internal.codec.xmlcodec import toXMLStr
from credentials import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
# Confirm the dn below is for your top dn
topDn = cobra.mit.naming.Dn.fromString('uni/tn-HD/ap-AP1/epg-EPG1_1')
topParentDn = topDn.getParent()
topMo = md.lookupByDn(topParentDn)

# build the request using cobra syntax
fvAEPg = cobra.model.fv.AEPg(topMo, isAttrBasedEPg=u'no', matchT=u'AtleastOne', name=u'EPG1_1', prefGrMemb=u'exclude')
#fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, tDn=u'topology/pod-1/paths-101/pathep-[eth1/46]', descr=u'', primaryEncap=u'unknown', instrImedcy=u'immediate', mode=u'regular', encap=u'vlan-551', annotation=u'')
#fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg, numPorts=u'0', portAllocation=u'none', switchingMode=u'native', resImedcy=u'immediate', tDn=u'uni/phys-BM01', bindingType=u'none', epgCos=u'Cos0', classPref=u'encap', netflowPref=u'disabled', secondaryEncapInner=u'unknown', netflowDir=u'both', delimiter=u'', instrImedcy=u'lazy', lagPolicyName=u'', encap=u'unknown', primaryEncapInner=u'unknown', primaryEncap=u'unknown', encapMode=u'auto', annotation=u'', epgCosPref=u'disabled')
#fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, annotation=u'', tnQosCustomPolName=u'')
#fvRsBd = cobra.model.fv.RsBd(fvAEPg, annotation=u'', tnFvBDName=u'BD1')
# commit the generated code to APIC
print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)


# Config EPG1_2
topDn = cobra.mit.naming.Dn.fromString('uni/tn-HD/ap-AP1/epg-EPG1_2')
topParentDn = topDn.getParent()
topMo = md.lookupByDn(topParentDn)

# build the request using cobra syntax
fvAEPg = cobra.model.fv.AEPg(topMo, isAttrBasedEPg=u'no', matchT=u'AtleastOne', name=u'EPG1_2', prefGrMemb=u'exclude')

# commit the generated code to APIC
print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)



# Config EPG1_3
topDn = cobra.mit.naming.Dn.fromString('uni/tn-HD/ap-AP1/epg-EPG1_3')
topParentDn = topDn.getParent()
topMo = md.lookupByDn(topParentDn)

# build the request using cobra syntax
fvAEPg = cobra.model.fv.AEPg(topMo, isAttrBasedEPg=u'no', matchT=u'AtleastOne', name=u'EPG1_3', prefGrMemb=u'exclude')

# commit the generated code to APIC
print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)


# Config EPG2_1
topDn = cobra.mit.naming.Dn.fromString('uni/tn-HD/ap-AP1/epg-EPG2_1')
topParentDn = topDn.getParent()
topMo = md.lookupByDn(topParentDn)

# build the request using cobra syntax
fvAEPg = cobra.model.fv.AEPg(topMo, isAttrBasedEPg=u'no', matchT=u'AtleastOne', name=u'EPG2_1', prefGrMemb=u'exclude')

# commit the generated code to APIC
print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)


# Config EPG2_2
topDn = cobra.mit.naming.Dn.fromString('uni/tn-HD/ap-AP1/epg-EPG2_2')
topParentDn = topDn.getParent()
topMo = md.lookupByDn(topParentDn)

# build the request using cobra syntax
fvAEPg = cobra.model.fv.AEPg(topMo, isAttrBasedEPg=u'no', matchT=u'AtleastOne', name=u'EPG2_2', prefGrMemb=u'exclude')

# commit the generated code to APIC
print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)











