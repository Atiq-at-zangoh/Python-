
https_status = 200

match https_status:
    case 200|201:
        print("Success")

    case 404:
        print("Not Found")

    case 500:
        print("Server error")        