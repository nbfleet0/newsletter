#!/bin/bash
PATH="$PATH:/Users/sanghapark/Downloads/DIR/VentureDigest/newsletter"
python2.7 scrape.py && python2.7 send.py #runs scrape.py and when it's finished, runs send.py
echo "newsletter sent"