#!/bin/sh

while : ; do
    tc qdisc add dev ens39  root netem delay 100ms 400ms 10% loss 15% duplicate 0.8% corrupt 0.5%
    val=$((RANDOM%540+60))
    echo "[`date +%Y-%m-%d\ %H:%M:%S`]开始网络限制 $val(S)"
    sleep $val
    tc qdisc delete dev ens39 root
    val=$((RANDOM%90+30))
    echo "[`date +%Y-%m-%d\ %H:%M:%S`]解除网络限制 $val(S)"
    sleep $val
done
