header=$(head -n1 input.csv)
tail -n +2 input.csv | split -l 6 - tmp_input_

n=1
for f in tmp_input_*; do
    echo "$header" > input${n}.csv
    cat "$f" >> input${n}.csv
    rm "$f"
    n=$((n+1))
done

