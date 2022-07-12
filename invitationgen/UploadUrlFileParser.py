# location on encrypted drive where upload lcoations of all participants are stored
upload_urls_file_location = "/Volumes/RestifyVolume/upload-locations.txt"

def parse_all_upload_locations():

    # Prepare target map
    upload_locations = {}

    # Open file for interpretation
    upload_urls = open(upload_urls_file_location, 'r')
    lines = upload_urls.readlines()

    # parse every line and fill name-to-email map.
    for line in lines:
        words = line.split()
        pseudonym = words[0]
        url = words[1]
        upload_locations[pseudonym] = url

    # return the map
    return upload_locations