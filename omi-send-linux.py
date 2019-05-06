#!/usr/bin/env python3
import requests

r = requests.post("http://localhost:8080", data =
"""<omiEnvelope xmlns="http://www.opengroup.org/xsd/omi/1.0/" version="1.0" ttl="0">
  <write msgformat="odf">
    <msg>
      <Objects xmlns="http://www.opengroup.org/xsd/odf/1.0/">
        <Object>
          <id>Linux-Computer</id>	<!-- Change the id name to some unique name (your laptop name) -->
          <InfoItem name="CPUTemperature">
            <value>""" + input() + """</value>
          </InfoItem>
        </Object>
      </Objects>
    </msg>
  </write>
</omiEnvelope>""")
print(r.text)
