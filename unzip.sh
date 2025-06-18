for zipfile in *.zip; do
	    foldername="${zipfile%.zip}"
	        mkdir -p "$foldername"
		    unzip -q "$zipfile" -d "$foldername"
	    done

