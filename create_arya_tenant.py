#!/usr/bin/env python
# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.naming
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.vns
from cobra.internal.codec.xmlcodec import toXMLStr

from credentials import *

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
# Confirm the dn below is for your top dn
topDn = cobra.mit.naming.Dn.fromString('uni/tn-ARYA')
topParentDn = topDn.getParent()
topMo = md.lookupByDn(topParentDn)

# build the request using cobra syntax
fvTenant = cobra.model.fv.Tenant(topMo, ownerKey=u'', name=u'ARYA', descr=u'', nameAlias=u'', ownerTag=u'', annotation=u'')
vnsSvcCont = cobra.model.vns.SvcCont(fvTenant, annotation=u'')
fvRsTenantMonPol = cobra.model.fv.RsTenantMonPol(fvTenant, annotation=u'', tnMonEPGPolName=u'')


# commit the generated code to APIC
print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)