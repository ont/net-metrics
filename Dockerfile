FROM almir/webhook

RUN apk add --no-cache python3 conntrack-tools

WORKDIR /srv

COPY hooks.json /etc/webhook/hooks.json
COPY conns_histogram.py .

CMD ["-verbose", "-hooks=/etc/webhook/hooks.json", "-hotreload"]
