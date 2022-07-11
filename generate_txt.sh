while getopts ":c:f:l:t:" opts;
	do
		case $opts in
			c) csv=$OPTARG;;
			f) input=$OPTARG;;
			l) output=$OPTARG;;
			t) ratio=$OPTARG
			   addRatio=true;;
			?) echo invalid flag;;
esac
done
if [ "$addRatio" = true ]; then
	echo "$csv $input $output $ratio" | python print.py
else 
	echo "$csv $input $output" | python print.py
fi

