#!/bin/sh

ops=$(echo $(cat mpo | grep 'if \[ "$1" ==' | cut -d'=' -f3 | cut -d']' -f1 | sed 's/ *//g' | sed 's/"//g'))


# generate header
echo "#"
echo "#  Completion for mpo:"
echo "#"
for operation in $ops; do
	echo "#  mpo $operation"
done
echo ""

# generate completion
cat << EOF
_go2fed()
{
    local cur prev opts
    COMPREPLY=()
    cur="\${COMP_WORDS[COMP_CWORD]}"
    prev="\${COMP_WORDS[COMP_CWORD-1]}"
EOF
echo "    opts=\"$ops\""
echo "    case "\${prev}" in"

for operation in $ops; do
	echo "        $operation)"
	echo "            COMPREPLY=( \$(compgen -f \${cur}) )"
        echo "            return 0"
        echo "            ;;"
done

cat << EOF
        *)
        ;;
    esac

    COMPREPLY=( \$(compgen -W "\${opts}" -- \${cur}) )
}
complete -F _mpo mpo
EOF
