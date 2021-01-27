FROM centos:centos7

ENV   HAPROXY_MJR_VERSION=2.2 \
  HAPROXY_VERSION=2.2.8 \
  HAPROXY_CONFIG='/etc/haproxy/haproxy.cfg' \
  OPENSSL_VERSION=1.1.1i

RUN \
  yum install -y epel-release && \
  yum update -y && \
  `# Install build tools. Note: perl needed to compile openssl...` \
  yum install -y \
  inotify-tools \
  wget \
  tar \
  gzip \
  make \
  gcc \
  perl \
  pcre-devel \
  zlib-devel \
  iptables \
  pth-devel && \
  `# Install newest openssl...` \
  wget -O /tmp/openssl.tgz https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz && \
  tar -zxf /tmp/openssl.tgz -C /tmp && \
  cd /tmp/openssl-* && \
  ./config --prefix=/usr \
  --openssldir=/etc/ssl \
  --libdir=lib          \
  no-shared zlib-dynamic && \
  make -j$(getconf _NPROCESSORS_ONLN) V= && make install_sw && \
  cd && rm -rf /tmp/openssl* && \
  `# Install HAProxy...` \
  wget -O /tmp/haproxy.tgz http://www.haproxy.org/download/${HAPROXY_MJR_VERSION}/src/haproxy-${HAPROXY_VERSION}.tar.gz && \
  tar -zxvf /tmp/haproxy.tgz -C /tmp

WORKDIR "/tmp/haproxy-${HAPROXY_VERSION}"
RUN  make -j$(getconf _NPROCESSORS_ONLN) V= \
   TARGET=linux-glibc \
   USE_LINUX_TPROXY=1 \
   USE_ZLIB=1 \
   USE_REGPARM=1 \
   USE_PCRE=1 \
   USE_PCRE_JIT=1 \
   USE_OPENSSL=1 \
   SSL_INC=/usr/include \
   SSL_LIB=/usr/lib \
   ADDLIB=-ldl \
   ADDLIB=-lpthread \
   CFLAGS="-O2 -g -fno-strict-aliasing -DTCP_USER_TIMEOUT=18" && \
   make install && \
   rm -rf /tmp/haproxy* && \
   `# Configure HAProxy...` \
   mkdir -p /var/lib/haproxy && \
   groupadd haproxy && adduser --uid 1001 haproxy -g haproxy && chown -R haproxy:haproxy /var/lib/haproxy && \
   `# Clean up: build tools...` \
   yum remove -y make gcc pcre-devel && \
   yum clean all && rm -rf /var/cache/yum




# Internal params
#HAPROXY_CMD="/usr/local/sbin/haproxy -f ${HAPROXY_CONFIG} -W ${HAPROXY_USER_PARAMS}"


ADD haproxy.cfg ${HAPROXY_CONFIG}

CMD ["/usr/local/sbin/haproxy", "-f", "${HAPROXY_CONFIG}"]