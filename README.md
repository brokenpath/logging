# logging


  

# What needs testing  
Test of crash. What to do when crash occures, server, clients.
Dataloss: shipping files (will be a problem with retention), HA setup?

Upgrading, test 2.0.1 -> 2.1 (Format should)





  
# Promtail  

Correctly formatted docker export.
Correctly formatted python export.






  
#  Usage
export LOKI_ADDR=http://localhost:3100  
loki -config.file=loki.yaml

  

#build haproxy  
buildah bud -f Dockerfile  -t haproxy:2.28