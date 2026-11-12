#!/usr/bin/env bash
# =============================================================================
# Runner script for LEPTONdipole model generation
# =============================================================================

set -e

if [ -x "/Applications/Mathematica.app/Contents/MacOS/MathKernel" ]; then
    MATH="/Applications/Mathematica.app/Contents/MacOS/MathKernel"
elif [ -x "/Applications/Mathematica.app/Contents/MacOS/WolframKernel" ]; then
    MATH="/Applications/Mathematica.app/Contents/MacOS/WolframKernel"
elif command -v math >/dev/null 2>&1; then
    MATH="math"
else
    echo "[ERROR] MathKernel not found. Please ensure Mathematica is installed."
    exit 1
fi

ARG="${1:-all}"

case "$ARG" in
    all)
        TARGETS=("FA_Unitary" "FA_Feynman" "UFO_Unitary" "UFO_Feynman")
        ;;
    UFO)
        TARGETS=("UFO_Unitary" "UFO_Feynman")
        ;;
    FA)
        TARGETS=("FA_Unitary" "FA_Feynman")
        ;;
    FA_Unitary|FA_Feynman|UFO_Unitary|UFO_Feynman)
        TARGETS=("$ARG")
        ;;
    *)
        echo "[ERROR] Unknown option: $ARG"
        echo "Usage: ./run.sh [all | UFO | FA | FA_Unitary | FA_Feynman | UFO_Unitary | UFO_Feynman]"
        exit 1
        ;;
esac

echo "=========================================================="
echo "LEPTONdipole Model Generation"
echo "Kernel:  $MATH"
echo "Targets: ${TARGETS[*]}"
echo "=========================================================="

for T in "${TARGETS[@]}"; do
    echo ""
    echo ">>> Starting target: $T in a clean kernel ..."
    echo ""
    "$MATH" -noprompt -run "target=\"$T\"; << LEPTONdipole.m; Quit[];"
    echo ""
    echo ">>> Completed target: $T"
done

# Post-process generated UFO directories for Python 3 compatibility
for ufo_dir in *_UFO; do
    if [ -d "$ufo_dir" ]; then
        if [ -f "$ufo_dir/object_library.py" ]; then
            python3 -c "
with open('$ufo_dir/object_library.py', 'r') as f:
    s = f.read()
s = s.replace('raise UFOError, \"UFO does not support yet more than one occurence of CTParameters in the couplings values.\"', 'raise UFOError(\"UFO does not support yet more than one occurence of CTParameters in the couplings values.\")')
with open('$ufo_dir/object_library.py', 'w') as f:
    f.write(s)
"
        fi
        if [ -f "$ufo_dir/write_param_card.py" ]; then
            python3 -c "
with open('$ufo_dir/write_param_card.py', 'r') as f:
    s = f.read()
old_code = '''        for parameter in all_parameters:
            exec(\"%s = %s\" % (parameter.name, parameter.value))'''
new_code = '''        p_scope = {'cmath': cmath}
        for parameter in all_parameters:
            try:
                p_scope[parameter.name] = eval(str(parameter.value), p_scope)
            except Exception:
                try:
                    exec(\"%s = %s\" % (parameter.name, parameter.value), p_scope, p_scope)
                except Exception:
                    pass'''
s = s.replace(old_code, new_code)
s = s.replace('complex(eval(param.value)).real', 'complex(eval(param.value, p_scope)).real')
with open('$ufo_dir/write_param_card.py', 'w') as f:
    f.write(s)
"
        fi
    fi
done

echo ""
echo "=========================================================="
echo "All requested targets completed successfully!"
echo "=========================================================="

