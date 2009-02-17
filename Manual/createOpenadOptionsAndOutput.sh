#!/bin/sh
set -u
${OPENADROOT}/bin/openad -h > openadScriptOptions.txt
echo "        subroutine head(x)
        end subroutine" > head.f
${OPENADROOT}/bin/openad head.f > openadScriptOutput.txt
${OPENADROOT}/bin/openad -n head.f | ./fold.py > openadScriptNoAction.txt
