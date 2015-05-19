#!/bin/sh
echo "Content-type: text/html"
echo ""

x=`cat /sys/class/leds/tp-link:blue:relay/brightness`

if [ "$x" -eq 0 ]
then
        echo "Light is ON"
        echo 1 > /sys/class/leds/tp-link:blue:relay/brightness
else
        echo "Light is OFF"
        echo 0 > /sys/class/leds/tp-link:blue:relay/brightness
fi

