def help():
    help_msg = """
    Commands may be abbreviated.  Commands are:

    !		    debug		mdir		sendport	site
    $		    dir		    mget		put		    size
    account		disconnect	mkdir		pwd		    status
    append		exit		mls		    quit		struct
    ascii		form		mode		quote		system
    """
    print(help_msg)

while True:
    cmd = input("ftp> ")
    if cmd == "quit":
        break
    elif cmd == "help":
        help()
    elif cmd == "ls":
        pass
    else:
        print('?Invalid command')