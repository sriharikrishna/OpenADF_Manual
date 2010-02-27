#!/bin/sh
set -u
set -e
${OPENADROOT}/bin/openad -h | ./fold.py -w 80 > openadScriptOptions.txt
echo "        subroutine head(x)
        end subroutine" > head.f
${OPENADROOT}/bin/openad head.f > openadScriptOutput.txt
${OPENADROOT}/bin/openad -n head.f | ./fold.py -c -w 136 > openadScriptNoAction.txt
